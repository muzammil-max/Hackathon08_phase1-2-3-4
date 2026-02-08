# Deployment Guide: MyTodoApp on Local Kubernetes

This guide explains how to deploy the MyTodoApp (Frontend, Backend, and Database) onto a local Minikube cluster using Helm.

## Prerequisites

1.  **Docker Desktop**: Installed and running.
2.  **Minikube**: Installed (`winget install Kubernetes.minikube`).
3.  **Helm**: Installed (`winget install Helm.Helm`).
4.  **kubectl**: Installed (usually comes with Docker or Minikube).

## 1. Prepare Local Cluster

Start Minikube using the docker driver:

```powershell
minikube start --driver=docker
```

Enable the Ingress addon (optional but recommended):

```powershell
minikube addons enable ingress
```

## 2. Build Container Images

Configure your shell to use Minikube's Docker daemon so the images are built directly into the cluster:

**PowerShell:**
```powershell
minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

Build the images:

```powershell
# Backend
cd backend
docker build -t todo-backend:v1 .

# Frontend
cd frontend
docker build -t todo-frontend:v1 .
```

## 3. Deploy with Helm

From the project root, install the Helm chart:

```powershell
helm upgrade --install todo-app ./deploy/helm/todo-app
```

## 4. Access the Application

The frontend is exposed via a **NodePort** (30080).

1.  Get the Minikube IP:
    ```powershell
    minikube ip
    ```
2.  Access in your browser: `http://<MINIKUBE_IP>:30080`

*Note: On some Windows environments, you may need to run `minikube service todo-app-frontend` to open a tunnel.*

## 5. Operations

- **Check Status**: `kubectl get pods`
- **View Logs**: `kubectl logs -l app=todo-app-backend`
- **Uninstall**: `helm uninstall todo-app`
- **Update**: Make changes to `values.yaml` and run `helm upgrade todo-app ./deploy/helm/todo-app`

## Configuration

You can customize the deployment by editing `deploy/helm/todo-app/values.yaml`:

- `replicaCount`: Number of frontend/backend instances.
- `database.password`: Database credentials.
- `resources`: CPU and memory limits for each service.