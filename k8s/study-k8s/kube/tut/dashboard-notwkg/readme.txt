#Shutdown 1 of the nodes
curl -o dashboard.yaml  https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-rc3/aio/deploy/recommended.yaml
##change dashboard namespace to chander
kc apply -f dashboard.yaml
kc  edit svc kubernetes-dashboard -n chander

====  ISSUES .. retried below ==== https://github.com/kubernetes/dashboard/issues/4088
wget https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml


## https://medium.com/@lyokowarrior14/troubleshooting-kubernetes-the-beginners-guide-2440ec400155?source=email-360682594c0d-1582717539924-digest.reader------3-59------------------41c56d29_0a2d_4099_912a_8293c4190083-1-----
