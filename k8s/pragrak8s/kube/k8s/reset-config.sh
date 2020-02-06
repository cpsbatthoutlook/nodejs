kubeadm reset -f
rm -rf /var/lib/cni /etc/cni
rm -rf /var/lib/kubelet ~/.kube
systemctl stop kubelet
systemctl stop docker
ifconfig cni0 down
ifconfig flannel.1 down
ifconfig docker0 down
ip link delete cni0
ip link delete flannel.1
echo Reboot `hostname`
