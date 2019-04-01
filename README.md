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

kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended/kubernetes-dashboard.yaml
 

kubectl apply -f dashboard-adminuser.yaml

```
#### Now we need to find token we can use to log in. Execute following command:

```kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin-user | awk '{print $1}')```

Now copy the token and paste it into Enter token field on log in screen. 
 
```http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/```

### 3. Deploy  
Move to directory kubernates/access/

run
```
kubectl create -f web-pod.yml &&
kubectl create -f web-svc.yml &&
kubectl create -f web-rc.yml

```
