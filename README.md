# KubeKeras [![Build Status](https://travis-ci.org/Telexine/KubeKeras.svg?branch=master)](https://travis-ci.org/Telexine/KubeKeras)

Hosted preview here 
http://35.240.243.117/


![Screenshot](https://github.com/Telexine/KubeKeras/blob/master/s1.png)
![Screenshot](https://github.com/Telexine/KubeKeras/blob/master/s2.png)
![Screenshot](https://github.com/Telexine/KubeKeras/blob/master/s3.png)
## Setup Kubernates

### 1. Install kubectl

```
brew install  kubectl
```

### 2. create dashboard

< Must Enable kube in docker before this >
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
