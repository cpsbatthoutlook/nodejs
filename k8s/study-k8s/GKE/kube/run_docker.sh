n=gcp-sdk
i=google/cloud-sdk:284.0.0
mnt=/kube

## Login
docker run -ti --name $n -v ${mnt}:${mnt}  $i gcloud auth login




