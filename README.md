# tondra

##### Continuous Development on Kubernetes environments.

##### With application healthchecks and Zero-downtime deployment model.

##### Using Kubernetes, Helm, Skaffold

###### Copyright 2021, Saeid Bostandoust <ssbostan@linuxmail.org>

### Step 1: Requirements

1- Install docker(20.10.2+), helm(3.4.2+) and skaffold(1.17.2+).

2- Setup and configure kubeconfig to access to your kubernetes cluster.

3- Login docker to Docker Hub or your private registry.

4- To setup development environment, create new namespace with name **devel** on kubernetes.

```sh
kubectl create namespace devel
```

5- Edit **skaffold.yaml** and change **ssbostan/tondra** to your own image repository.

### Step 2: Development

```sh
source initdev
skaffold dev --port-forward=true
curl localhost:8080/appinfo

{"appVersion":"v1.0.0","gitCommit":"5d21d166d930791c6a3907fee18852d0799d674b"}
```

### Step 3: Production

This model creates image tags based on your git tags.

Everything you need to deploy to production environment is changing image tag in helm chart.

This model can be used to automate CD process with ArgoCD or etc...

Join and Enjoy, Saeid Bostandoust.
