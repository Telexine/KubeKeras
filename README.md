# KubeKeras

description 

## Setup Kubernates

### 1. Install kubectl

```
brew install  kubectl
```

### 2. create dashboard
```
kubectl config current-context docker-for-desktop

kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml

kubectl get pod --namespace=kube-system

* from get pod
kubectl port-forward *${kubernetes-dashboard-xxxxxxxx-rtsvm} 8334:8443 --namespace=kube-system

```

Wait untill It's ready then go to https://localhost:8443

### 3. Deploy  
Move to directory kubernates/access/

run
```
kubectl create -f web-pod.yml &&
kubectl create -f web-svc.yml &&
kubectl create -f web-rc.yml

```
