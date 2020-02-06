== RUN container directly as sergice ===

https://kubernetes.io/docs/tutorials/services/source-ip/#source-ip-for-services-with-type-nodeport

s=my-svc
#Run deployment
kubectl run ${s} --image=k8s.gcr.io/echoserver:1.4 -n chander
#Run Service as ClusterIP (default)
kubectl expose deploy $s -n chander --name=clusterip --port=80 --target-port=8080  


#Run same service as nodeport
kc expose deploy $s -n chander --name=nodeport --port=80 --target-port=8080 --type=NodePort
## patch  (to see the client ip is th elocal server not local Node)
 patch -p '{"spec":{"externalTrafficPolicy":"Local"}}'  service/nodeport -n chander


#Run same service as LoadBalancer
kc expose deploy $s -n chander --name=lb --port=80 --target-port=8080 --type=LoadBalancer
## patch  (to see the client ip is th elocal server not local Node)
 patch -p '{"spec":{"externalTrafficPolicy":"Local"}}'  service/nodeport -n chander

??? inGRESS Controller ??
