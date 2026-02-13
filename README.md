# 🚀 Crypto Tracker: DevOps End-to-End Project

Una plataforma de monitoreo de criptomonedas construida con arquitectura de microservicios, infraestructura como código (IaC) y orquestación en Kubernetes.



## 🏗️ Arquitectura
* **Backend:** FastAPI (Python) expone los datos.
* **Worker:** Servicio en segundo plano (Python) que consulta CoinGecko y escribe en DB.
* **Datos:** PostgreSQL (Persistencia) & Redis (Cache).
* **Visualización:** Grafana (Dashboards en tiempo real).
* **Infraestructura:** Terraform (LocalStack para S3/DynamoDB) & Kubernetes (Minikube).
* **CI/CD:** GitHub Actions (Build Multi-Arch ARM/AMD) -> Docker Hub.
* **Orquestación:** Helm Charts customizados.

## 🛠️ Tecnologías
`Python` `Docker` `Kubernetes` `Terraform` `GitHub Actions` `Helm` `Postgres` `Redis` `Grafana`

---

## 🚀 Cómo correrlo localmente

### Opción A: Modo Docker Compose (Rápido)
Ideal para desarrollo local sin Kubernetes.
1. Clonar el repo.
2. Levantar todo:
   ```bash
   docker-compose up --build -d
   ```

3. Acceder a la API: `http://localhost:8080/prices`

### Opción B: Modo Kubernetes (Full DevOps)

La experiencia completa con orquestación.

**Prerequisitos:** Minikube, Kubectl, Helm.

1. **Iniciar Cluster:**
```bash
minikube start --driver=docker

```


2. **Desplegar con Helm:**
```bash
helm install v1 ./k8s/crypto-app

```


3. **Acceder a la API:**
Como usamos `ClusterIP` (seguridad), necesitamos un túnel:
```bash
kubectl port-forward svc/v1-api 8080:80
# Ver en: http://localhost:8080/prices

```


4. **Acceder a Grafana (Dashboard):**
En otra terminal:
```bash
kubectl port-forward svc/v1-grafana 3000:80

```


* **URL:** `http://localhost:3000`
* **User/Pass:** `admin` / `admin`
* **Setup:** Conectar Data Source (Postgres) -> Host: `v1-postgres:5432`



---

## 📂 Estructura del Proyecto

* `/app`: Código fuente Python (API + Worker).
* `/k8s`: Helm Chart para despliegue en Kubernetes.
* `/terraform`: Infraestructura como Código (LocalStack).
* `.github/workflows`: Pipelines de CI/CD.

---
