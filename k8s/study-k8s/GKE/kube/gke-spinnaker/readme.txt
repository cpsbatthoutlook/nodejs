https://docs.armory.io/spinnaker-install-admin-guides/install-on-gke/

alias kc="kubectl $*"
WKG_DIR=/kube/gke-spinnaker
gke=spinnaker-cluster
r=us-west3
z=us-west3-b

gcloud container clusters create ${gke}  --num-nodes 1 
#gcloud container cluster resize ${gke} --num-nodes 1 

export KUBECONFIG=kubeconfig-gke
export KK=${KUBECONFIG}
gcloud container clusters get-credentials ${gke}

alias kc="kubectl --kubeconfig ${KK} $*"
#kc --kubeconfig ${KK} get ns  ## to check
kc get ns



## Create kubeconfig file for Halyard/spinnaker

##Grant permissions to the Google IAM users for this cluster
xx=$(gcloud config get-value account) ##cp***outlo***
kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user $(gcloud config get-value account)


##Get the spinnaker tools
cd ${WKG_DIR}
# If you're on Linux instead of OSX, use this URL instead:
curl -L https://github.com/armory/spinnaker-tools/releases/download/0.0.6/spinnaker-tools-linux -o spinnaker-tools
chmod +x spinnaker-tools

##Run this tools
# The 'gcloud container clusters get-credentials' command from above will create/update this file
SOURCE_KUBECONFIG=${KK}
CONTEXT=$(kubectl --kubeconfig ${SOURCE_KUBECONFIG} config current-context)
DEST_KUBECONFIG=kubeconfig-spinnaker-system-sa
SPINNAKER_NAMESPACE=spinnaker-system
SPINNAKER_SERVICE_ACCOUNT_NAME=spinnaker-service-account

./spinnaker-tools create-service-account \
  --kubeconfig ${SOURCE_KUBECONFIG} \
  --context ${CONTEXT} \
  --output ${DEST_KUBECONFIG} \
  --namespace ${SPINNAKER_NAMESPACE} \
  --service-account-name ${SPINNAKER_SERVICE_ACCOUNT_NAME}


##Create a GCS service account for Spinnaker
export SERVICE_ACCOUNT_NAME=spinnaker-gcs-account-trial
export SERVICE_ACCOUNT_FILE=spinnaker-gcs-account.json
export PROJECT=$(gcloud info --format='value(config.project)')

gcloud --project ${PROJECT} iam service-accounts create \
    ${SERVICE_ACCOUNT_NAME} \
    --display-name ${SERVICE_ACCOUNT_NAME}
SA_EMAIL=$(gcloud --project ${PROJECT} iam service-accounts list \
    --filter="displayName:${SERVICE_ACCOUNT_NAME}" \
    --format='value(email)')
gcloud --project ${PROJECT} projects add-iam-policy-binding ${PROJECT} \
    --role roles/storage.admin --member serviceAccount:${SA_EMAIL}
mkdir -p $(dirname ${SERVICE_ACCOUNT_FILE})
gcloud --project ${PROJECT} iam service-accounts keys create ${SERVICE_ACCOUNT_FILE} \
    --iam-account ${SA_EMAIL}


##Stage files on the Halyard machine
# Feel free to use some other directory for this; make sure it is a persistent directory.
# Also, make sure this directory doesn't live on an NFS mount, as that can cause issues
#WORKING_DIRECTORY=~/gke-spinnaker/
WORKING_DIRECTORY=${WKG_DIR}
mkdir -p ${WORKING_DIRECTORY}/.hal
mkdir -p ${WORKING_DIRECTORY}/.secret
mkdir -p ${WORKING_DIRECTORY}/resources

#
cp kubeconfig-spinnaker-system-sa ${WORKING_DIRECTORY}/.secret
cp spinnaker-gcs-account.json ${WORKING_DIRECTORY}/.secret



## ARMORY phase [ from outside the Vagrant status]

export WKG_DIR=/kube/gke-spinnaker
export WORKING_DIRECTORY=${WKG_DIR}
ls -la ${WKG_DIR}
an=armory-halyard
ai=armory/halyard-armory:1.8.2
docker run --name ${an} -it --rm \
  -v ${WORKING_DIRECTORY}/.hal:/home/spinnaker/.hal \
  -v ${WORKING_DIRECTORY}/.secret:/home/spinnaker/.secret \
  -v ${WORKING_DIRECTORY}/resources:/home/spinnaker/resources \
  ${ai}


## Run in Halyand containers {as root to make it easier}
docker exec -it ${an}   bash

export NAMESPACE="spinnaker-system"
# Enter the name you want Spinnaker to use to identify the cloud provider account
export ACCOUNT_NAME="cpsbatth@outlook.com"
# Update this with the full path to your kubeconfig inside the container)
export KUBECONFIG_FULL=/home/spinnaker/.secret/kubeconfig-spinnaker-system-sa

## Enable a version {to supress warning of chosing the version}
hal config version edit --version 2.17.5


# Enable the Kubernetes cloud provider {"/home/spinnaker/.hal/config": /home/spinnaker/.hal/config: Text file busy }
hal config provider kubernetes 
        enable
        account list



# Add account {Issue:  check the file if it already setup}
hal config provider kubernetes account add ${ACCOUNT_NAME} --provider-version v2 \
  --kubeconfig-file ${KUBECONFIG_FULL} --only-spinnaker-managed true --namespaces ${NAMESPACE}
#hal config provider kubernetes account add cpsbatth@outlook.com --provider-version v2 --kubeconfig-file /home/spinnaker/.secret/kubeconfig-spinnaker-system-sa --only-spinnaker-managed true --namespaces spinnaker-system


#Configure to install in K8s  {  "/home/spinnaker/.hal/config": /home/spinnaker/.hal/config: Text file busy }
hal config deploy edit  --type distributed \
  --account-name ${ACCOUNT_NAME}   --location ${NAMESPACE}
#hal config deploy edit --type distributed --account-name cpsbatth@outlook.com --location spinnaker-system

hal config features edit --artifacts true
hal config artifact http enable


#--- use Google storage bucket 
####### Inside container
PROJECT=GOOGLE_CLOUD_PROJECT_NAME
BUCKET_LOCATION=us
SERVICE_ACCOUNT_FILE=~/.secret/spinnaker-gcs-account.json
ROOT_FOLDER=front-50

hal config storage gcs edit --project ${PROJECT} --bucket-location ${BUCKET_LOCATION} \
    --root-folder ${ROOT_FOLDER} --json-path ${SERVICE_ACCOUNT_FILE}
  hal config storage edit --type gcs


