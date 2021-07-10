# tondra

A brief example of Kubernetes based Agile-development process with [Skaffold](https://github.com/GoogleContainerTools/skaffold).

With a Zero-downtime and rolling update approach that achieved from Kubernetes features.

###  What is Agile software development?

> In [software development](https://en.wikipedia.org/wiki/Software_development "Software development"), **agile** (sometimes written **Agile**)[[1]](https://en.wikipedia.org/wiki/Agile_software_development#cite_note-1) practices involve discovering requirements and developing solutions through the collaborative effort of [self-organizing](https://en.wikipedia.org/wiki/Self-organizing_communities "Self-organizing communities") and [cross-functional](https://en.wikipedia.org/wiki/Cross-functional_team "Cross-functional team") teams and their [customer(s)](https://en.wikipedia.org/wiki/Customer "Customer")/[end user(s)](https://en.wikipedia.org/wiki/End_user "End user").[[2]](https://en.wikipedia.org/wiki/Agile_software_development#cite_note-Collier_2011-2) It advocates adaptive planning, evolutionary development, early delivery, and [continual improvement](https://en.wikipedia.org/wiki/Continual_improvement_process "Continual improvement process"), and it encourages flexible responses to change. [Wikipedia](https://en.wikipedia.org/wiki/Agile_software_development)

### What is `tondra`?

`tondra` is an example application that used Skaffold to demonstrate agile-development process on Kubernetes based environments. In the environments that using Kubernetes for software deployments and providing services, not only we need a Dev/Prod parity approach for a software development but in most cases of Microservices architecture, developers need to connect to other microservices to develop and test their works. In this situation needs of a development environment with a minimum-trusted access is felt. Skaffold is a right technology to achieve these needs. With the Skaffold, developers do not need to worried about deployments and they should focus just on writing codes. `skaffold dev` command will build the application and deploy it on Kubernetes, code changes are detected automatically and the process of build and deployment is triggered afterward. In addition to this, `tondra` implements all needed health-check endpoints that can makes application highly available.

### Why we should use Skaffold?

Skaffold handles the workflow for building, pushing and deploying your application, allowing you to focus on what matters most: **writing code**. With Skaffold you can write your codes on your local system and deploy them to Kubernetes clusters as easy as drinking a cup of tea.

### How to create a minimum-trusted development environment:

For creating this environment each developer/team that working on a specific microservice needs a Kubernetes `Namespace`. Each of one can connects to other microservices in other namespaces via `Service`. With this approach connectivity is achieved without any unnecessary code disclosure.

## Installation and usage:

To deploy `tondra` you need:

  - Kubernetes v1.20 or later versions.
  - Local Docker v2.10+ installation for building Docker images.
  - Skaffold v1.27+ with v2beta18 api version.
  - Helm v3.4 or newer versions.

### Get started:

```bash
kubectl create ns devel
./start
curl localhost:8080/appinfo
```

![demo](https://raw.githubusercontent.com/ssbostan/tondra/master/demo.gif)

### Available endpoints:

The application goes to unhealthy status after processing a number of requests. After that Kubernetes detects this behavior and restarts the unhealthy pod. The number of requests that application can process before going to unhealthly status is considered randomly at application startup. But with this event - restarting pods - the application works prefectly and responsed to all requests.

| Endpoint | Description |
| -- | -- |
| /appinfo | Shows application info (app_version, git_commit, target_point, num_requests, health_status). |
| /livez | Use this endpoint in Kubernetes livenessProbe property. |
| /readyz | Use this endpoint in Kubernetes readinessProbe property. |
