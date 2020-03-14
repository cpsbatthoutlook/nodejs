https://kubernetes.github.io/ingress-nginx/deploy/#prerequisite-generic-deployment-command


n=ingress-nginx
wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.30.0/deploy/static/mandatory.yaml
wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.30.0/deploy/static/provider/baremetal/service-nodeport.yaml
kc apply -f mandatory.yaml
kc apply -f service-nodeport.yaml

kubectl exec -it  pod/nginx-ingress-controller-7f74f657bd-kxmng  -n $n -- /nginx-ingress-controller --version




## To test
#https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-ingress-guide-nginx-example.html

curl -k  https://localhost:30243/apple ##Works
curl -k  https://localhost:30243/banana ##Works
curl -k  https://localhost:30243/nginx ##don't work


Error:
         /apple    apple-service:5678 (10.44.0.5:5678)
        /banana   banana-service:5678 (10.44.0.6:5678)
        /nginx    web-ingress:80 (<none>)





##Other references
# https://kubernetes.io/docs/concepts/services-networking/ingress/
# https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/
# Configure deployment & Services
kubectl run web --image=gcr.io/google-samples/hello-app:1.0 --port=8080