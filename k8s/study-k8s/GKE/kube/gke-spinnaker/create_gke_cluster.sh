r=us-west3
z=us-west3-b
gke=gke-cluster-1
gke=spinnaker-cluster  ## https://docs.armory.io/spinnaker-install-admin-guides/install-on-gke/
KUBECONFIG=kubeconfig-gke
gk_project_id=gke-project-94570
# login into GCP
gcloud auth login
# login to kubectl
gcloud auth application-default login
# set project id that your cluster belongs to
gcloud config set project ${gk_project_id}
#Create cluster
gcloud container clusters create $gke --zone $z  --num-nodes 1
# download kubeconfig to local computer from a cluster by name
gcloud container clusters get-credentials ${gke}  --zone  ${z}
# get kubeconfig context
CONTEXT=$(kubectl config current-context)
echo ${CONTEXT}

## this service account uses the ClusterAdmin role -- this is not necessary, more restrictive roles can by applied.
#wget -o service-account.yml https://spinnaker.io/downloads/kubernetes/service-account.yml
#kubectl apply --context $CONTEXT -f service-account.yml
#Added from https://docs.armory.io/spinnaker-install-admin-guides/install-on-gke/

cd ~/workarea #cd ~/gke-spinnaker
kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user $(gcloud config get-value account)
curl -L https://github.com/armory/spinnaker-tools/releases/download/0.0.6/spinnaker-tools-linux -o spinnaker-tools
chmod +x spinnaker-tools
KUBECONFIG=kubeconfig-gke
gcloud container clusters get-credentials ${gke}  --zone  ${z}
alias kc="kubectl --kubeconfig ${KUBECONFIG=kubeconfig-gke} $*"
CONTEXT=$(kubectl --kubeconfig ${KUBECONFIG} config current-context)
DEST_KUBECONFIG=kubeconfig-spinnaker-system-sa
SPINNAKER_NAMESPACE=spinnaker-system
SPINNAKER_SERVICE_ACCOUNT_NAME=spinnaker-service-account

./spinnaker-tools create-service-account --kubeconfig ${KUBECONFIG} --context ${CONTEXT} \
 --output ${DEST_KUBECONFIG} --namespace ${SPINNAKER_NAMESPACE} --service-account-name ${SPINNAKER_SERVICE_ACCOUNT_NAME}
#./spinnaker-tools create-service-account --kubeconfig kubeconfig-gke --context gke_gke-project-94570_us-west3-b_spinnaker-cluster --output kubeconfig-spinnaker-system-sa --namespace spinnaker-system --service-account-name spinnaker-service-account


# get service token
TOKEN=$(kubectl get secret --context $CONTEXT  \
	   $(kubectl get serviceaccount spinnaker-service-account --context $CONTEXT -n ${SPINNAKER_NAMESPACE} -o jsonpath='{.secrets[0].name}') \
		   -n ${SPINNAKER_NAMESPACE} -o jsonpath='{.data.token}' | base64 --decode)

TOKEN=$(kubectl get secret --context $CONTEXT spinnaker-service-account-token-n5g8t -n ${SPINNAKER_NAMESPACE} -o jsonpath='{.data.token}'|base64 --decode)
# set credentials
kubectl config set-credentials ${CONTEXT}-token-user --token $TOKEN
# set context
kubectl config set-context $CONTEXT --user ${CONTEXT}-token-user
##
## Install Halyard https://www.spinnaker.io/setup/install/halyard/
## curl -O https://raw.githubusercontent.com/spinnaker/halyard/master/install/debian/InstallHalyard.sh
## sudo bash InstallHalyard.sh
##
##
# enable kubernetes
hal config provider kubernetes enable
# add in provider account
hal config provider kubernetes account add spinnaker-account --provider-version v2 --context ${CONTEXT}
# finally enable artifacts
hal config features edit --artifacts true
##
##
## Look at ~/.hal/config -- most important file
##
##
##
# set the account to install spinnaker into
ACCOUNT=spinnaker-account
# install spinnaker
hal config deploy edit --type distributed --account-name $ACCOUNT
##
##
## Enable Google storage for Persistence
##
##
## https://medium.com/google-cloud/spinnaker-on-gcp-with-gke-edfa994652f7
SERVICE_ACCOUNT_NAME=spinnaker-gcs-account
SERVICE_ACCOUNT_DEST=~/.gcp/gcs-account.json
# create service account
gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME --display-name $SERVICE_ACCOUNT_NAME
# set service account email  ##spinnaker-gcs-account-trial@gke-project-94570.iam.gserviceaccount.com
#     ##spinnaker-gcs-account@gke-project-94570.iam.gserviceaccount.com
SA_EMAIL=$(gcloud iam service-accounts list --filter="displayName:$SERVICE_ACCOUNT_NAME" --format='value(email)')
# set project # gke-project-94570
PROJECT=$(gcloud info --format='value(config.project)')
# bind iam policy
gcloud projects add-iam-policy-binding $PROJECT --role roles/storage.admin --member serviceAccount:$SA_EMAIL
mkdir -p $(dirname $SERVICE_ACCOUNT_DEST)
# create service account keys
gcloud iam service-accounts keys create $SERVICE_ACCOUNT_DEST --iam-account $SA_EMAIL
# see https://cloud.google.com/storage/docs/bucket-locations
BUCKET_LOCATION=us
# set configuration
hal config storage gcs edit --project $PROJECT --bucket-location $BUCKET_LOCATION --json-path $SERVICE_ACCOUNT_DEST
# enable gcs
hal config storage edit --type gcs
# deploy all your changes
hal deploy apply ##Failed ##
##
##
## Add GCS Artifact support 
##
##
## https://medium.com/google-cloud/spinnaker-on-gcp-with-gke-edfa994652f7
# service account from earlier
SERVICE_ACCOUNT_DEST=~/.gcp/gcs-artifacts-account.json
# artifact account name
ARTIFACT_ACCOUNT_NAME=my-gcs-artifact-account
# enable artifact support if you didn't already
hal config features edit --artifacts true
# enable gcs artifact support
hal config artifact gcs account add $ARTIFACT_ACCOUNT_NAME --json-path $SERVICE_ACCOUNT_DEST
hal config artifact gcs enable
# deploy your changes
hal deploy apply
