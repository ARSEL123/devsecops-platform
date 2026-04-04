# 🚀 Plateforme DevSecOps — Azure Kubernetes Service

<div align="center">

**Stayer Arsel DIFFO SOUOP**  
*Master of Engineering — Systèmes, Réseaux & Cloud*  
*SUPINFO Paris — 2025/2026*

[![CI/CD Pipeline](https://github.com/ARSEL123/devsecops-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/ARSEL123/devsecops-platform/actions/workflows/ci.yml)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

**🌐 Application live → http://4.253.10.14**

</div>

---

## 📋 Présentation

Ce projet est une **plateforme DevSecOps complète** déployée sur Microsoft Azure, réalisée dans le cadre du Master 2 Systèmes, Réseaux & Cloud à SUPINFO Paris.

L'objectif est de démontrer la maîtrise de l'ensemble du cycle de vie d'une infrastructure cloud moderne :
- **Infrastructure as Code** avec Terraform et Ansible
- **Conteneurisation** avec Docker (multi-stage build)
- **Orchestration** avec Kubernetes (AKS)
- **CI/CD automatisé** avec GitHub Actions
- **Sécurité intégrée** avec Trivy
- **Supervision** avec Prometheus, Grafana et ELK *(Phase 3)*

---

## 🏗️ Architecture globale

┌─────────────────────────────────────────────────────────┐
│                    Développeur                          │
│                   git push main                         │
└──────────────────────┬──────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────┐
│                 GitHub Actions CI/CD                    │
│  ┌──────────┐  ┌──────────┐  ┌─────────┐  ┌────────┐  │
│  │ Build +  │→ │  Trivy   │→ │  Push   │→ │Deploy  │  │
│  │  Tests   │  │  Scan    │  │  ACR    │  │  AKS   │  │
│  └──────────┘  └──────────┘  └─────────┘  └────────┘  │
└─────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────┐
│              Microsoft Azure                            │
│  ┌─────────────────────────────────────────────────┐   │
│  │  AKS Cluster (South Africa North)               │   │
│  │  ┌─────────────────┐  ┌─────────────────┐      │   │
│  │  │   Pod 1 Flask   │  │   Pod 2 Flask   │      │   │
│  │  │   (Running ✅)  │  │   (Running ✅)  │      │   │
│  │  └─────────────────┘  └─────────────────┘      │   │
│  │              Load Balancer                      │   │
│  │         http://4.253.10.14                      │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐  │
│  │     ACR      │  │     VM       │  │   Storage   │  │
│  │  (Registry)  │  │  (Ubuntu)    │  │   Account   │  │
│  └──────────────┘  └──────────────┘  └─────────────┘  │
└─────────────────────────────────────────────────────────┘

---

## 🛠️ Stack technique

| Catégorie | Technologies |
|---|---|
| **Infrastructure as Code** | Terraform 1.x, Ansible |
| **Cloud** | Microsoft Azure (South Africa North) |
| **Conteneurs** | Docker (multi-stage build) |
| **Orchestration** | Kubernetes AKS (Free tier) |
| **Registre** | Azure Container Registry (ACR) |
| **Application** | Python Flask + Gunicorn |
| **CI/CD** | GitHub Actions (4 jobs) |
| **Sécurité** | Trivy (scan vulnérabilités) |
| **Supervision** | Prometheus + Grafana + ELK *(Phase 3)* |
| **Versioning** | Git + GitHub |

---

## 📁 Structure du projet

devsecops-platform/
│
├── 📱 app/                        # Application Flask
│   ├── app.py                     # Code source (routes HTML + API)
│   ├── Dockerfile                 # Build multi-stage (builder + production)
│   ├── requirements.txt           # Dépendances Python
│   └── tests/
│       └── test_app.py            # Tests unitaires (pytest)
│
├── 🏗️ terraform/                  # Infrastructure as Code
│   ├── main.tf                    # Ressources Azure (VM, VNet, AKS, ACR...)
│   ├── variables.tf               # Déclaration des variables
│   ├── outputs.tf                 # Outputs (IPs, noms, credentials)
│   └── providers.tf               # Provider Azure (azurerm)
│
├── ⚙️ ansible/                    # Configuration automatisée
│   ├── inventory/hosts.yml        # Inventaire des serveurs
│   ├── playbooks/site.yml         # Playbook principal
│   └── roles/
│       ├── base/                  # Paquets essentiels + user deploy
│       ├── security/              # UFW + hardening SSH
│       └── docker/                # Installation Docker CE
│
├── ☸️ kubernetes/                  # Manifests Kubernetes
│   ├── deployments/               # Deployment (2 replicas, probes)
│   └── services/                  # Service LoadBalancer
│
├── 🔄 .github/workflows/          # Pipeline CI/CD
│   └── ci.yml                     # 4 jobs: build, scan, push, deploy
│
├── 📊 monitoring/                 # Supervision (Phase 3)
└── 📚 docs/                       # Documentation technique

---

## 🔄 Pipeline CI/CD

Chaque `git push` sur la branche `main` déclenche automatiquement :
git push
│
▼
┌─────────────────────────────────────────────┐
│  Job 1 — Build & Test (~30s)               │
│  ✅ Installation dépendances Python          │
│  ✅ Tests unitaires pytest (3 tests)         │
│  ✅ Build image Docker multi-stage           │
└─────────────────────┬───────────────────────┘
│
▼
┌─────────────────────────────────────────────┐
│  Job 2 — Security Scan Trivy (~45s)        │
│  ✅ Scan vulnérabilités CRITICAL/HIGH        │
│  ✅ Rapport de sécurité généré              │
└─────────────────────┬───────────────────────┘
│
▼
┌─────────────────────────────────────────────┐
│  Job 3 — Push to ACR                       │
│  ✅ Login Azure Container Registry          │
│  ✅ Tag image avec SHA du commit            │
│  ✅ Push image (SHA + latest)               │
└─────────────────────┬───────────────────────┘
│
▼
┌─────────────────────────────────────────────┐
│  Job 4 — Deploy to AKS                     │
│  ✅ Rolling update Kubernetes               │
│  ✅ Vérification rollout status             │
│  ✅ App mise à jour sans downtime           │
└─────────────────────────────────────────────┘

---

## ☁️ Infrastructure Azure

| Ressource | Nom | Région | Statut |
|---|---|---|---|
| Resource Group | rg-devsecops-arsel | South Africa North | ✅ |
| Virtual Network | vnet-devsecops-arsel | South Africa North | ✅ |
| VM Ubuntu 22.04 | vm-devsecops-arsel | South Africa North | ✅ |
| Container Registry | acrdevsecopsarsel | South Africa North | ✅ |
| Kubernetes Cluster | aks-devsecops-arsel | South Africa North | ✅ |
| Storage Account | stdevsecopsarsel001 | South Africa North | ✅ |
| Public IP | 4.253.10.14 | South Africa North | ✅ |

---

## 🚀 Déploiement rapide

### Prérequis
- Azure CLI + compte Azure actif
- Terraform >= 1.0
- Ansible >= 2.16
- Docker
- kubectl

### Installation
```bash
# 1. Cloner le projet
git clone git@github.com:ARSEL123/devsecops-platform.git
cd devsecops-platform

# 2. Déployer l'infrastructure Azure
cd terraform
terraform init
terraform apply -parallelism=1 -auto-approve

# 3. Configurer kubectl
az aks get-credentials \
  --name aks-devsecops-arsel \
  --resource-group rg-devsecops-arsel

# 4. Configurer les serveurs via Ansible
ansible-playbook \
  -i ansible/inventory/hosts.yml \
  ansible/playbooks/site.yml

# 5. Déployer l'application sur Kubernetes
kubectl apply -f kubernetes/deployments/app-deployment.yml
kubectl apply -f kubernetes/services/app-service.yml

# 6. Vérifier le déploiement
kubectl get pods
kubectl get service devsecops-app-service
```

---

## 📊 Phases du projet

| Phase | Description | Durée | Statut |
|---|---|---|---|
| **Phase 1** | Infrastructure as Code (Terraform + Ansible) | 1 mois | ✅ Terminée |
| **Phase 2** | CI/CD + Docker + Kubernetes | 1 mois | ✅ Terminée |
| **Phase 3** | Supervision (Prometheus + Grafana + ELK) | 1 mois | 🔄 En cours |
| **Phase 4** | Haute dispo + Documentation finale | 1 mois | ⏳ À venir |

---

## 📞 Contact

**Stayer Arsel DIFFO SOUOP**  
📧 diffoarsel123@gmail.com  
📱 07 59 38 19 27  
🔗 [LinkedIn](https://www.linkedin.com/in/arsel-diffo-42a579338/)  
📍 Île-de-France, France

---

<div align="center">
<i>SUPINFO Paris — Master of Engineering Systèmes, Réseaux & Cloud — 2025/2026</i>
</div>
