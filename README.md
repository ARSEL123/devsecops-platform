# Plateforme DevSecOps — Azure Kubernetes Service

<div align="center">

**Stayer Arsel DIFFO SOUOP**  
*Master of Engineering — Systèmes, Réseaux & Cloud — SUPINFO Paris 2025/2026*

[![CI/CD Pipeline](https://github.com/ARSEL123/devsecops-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/ARSEL123/devsecops-platform/actions/workflows/ci.yml)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)

### 🌐 Application live → [http://4.253.10.14](http://4.253.10.14)

</div>

---

## Présentation

Plateforme **DevSecOps complète** déployée sur Microsoft Azure, réalisée dans le cadre du Master 2 Systèmes, Réseaux & Cloud à SUPINFO Paris.

Ce projet couvre l'intégralité du cycle de vie d'une infrastructure cloud moderne : provisionnement automatisé, conteneurisation, orchestration Kubernetes, pipeline CI/CD avec sécurité intégrée, et supervision.

---

## Stack technique

| Catégorie | Technologies |
|---|---|
| Infrastructure as Code | Terraform, Ansible |
| Cloud | Microsoft Azure — South Africa North |
| Conteneurs | Docker (multi-stage build) |
| Orchestration | Kubernetes AKS |
| Registre | Azure Container Registry |
| Application | Python Flask + Gunicorn |
| CI/CD | GitHub Actions (4 jobs automatisés) |
| Sécurité | Trivy (scan vulnérabilités) |
| Supervision | Prometheus + Grafana + ELK *(Phase 3)* |

---

## Pipeline CI/CD

Chaque `git push` sur `main` déclenche automatiquement 4 jobs :

| Job | Description | Durée |
|---|---|---|
| **Build & Test** | Tests Python (pytest) + Build Docker | ~30s |
| **Security Scan** | Scan Trivy CRITICAL/HIGH | ~45s |
| **Push to ACR** | Push image sur Azure Container Registry | ~1min |
| **Deploy to AKS** | Rolling update Kubernetes sans downtime | ~2min |

---

## Infrastructure Azure

| Ressource | Nom | Statut |
|---|---|---|
| Resource Group | rg-devsecops-arsel | ✅ |
| Virtual Network | vnet-devsecops-arsel | ✅ |
| VM Ubuntu 22.04 | vm-devsecops-arsel | ✅ |
| Container Registry | acrdevsecopsarsel | ✅ |
| Kubernetes Cluster | aks-devsecops-arsel | ✅ |
| Storage Account | stdevsecopsarsel001 | ✅ |
| IP Publique | 4.253.10.14 | ✅ |

---

## Structure du projet
devsecops-platform/
├── app/                    # Application Flask
│   ├── app.py              # Code source
│   ├── Dockerfile          # Multi-stage build
│   ├── requirements.txt    # Dépendances Python
│   └── tests/              # Tests unitaires
├── terraform/              # Infrastructure as Code
│   ├── main.tf             # Ressources Azure
│   ├── variables.tf        # Variables
│   └── outputs.tf          # Outputs
├── ansible/                # Configuration serveurs
│   ├── inventory/          # Inventaire hôtes
│   ├── playbooks/          # Playbooks
│   └── roles/              # Rôles (base, security, docker)
├── kubernetes/             # Manifests Kubernetes
│   ├── deployments/        # Deployment 2 replicas
│   └── services/           # Service LoadBalancer
├── .github/workflows/      # Pipeline CI/CD
│   └── ci.yml              # GitHub Actions
└── monitoring/             # Supervision Phase 3

---

## Déploiement rapide
```bash
# Cloner le projet
git clone git@github.com:ARSEL123/devsecops-platform.git
cd devsecops-platform

# Déployer l'infrastructure Azure
cd terraform && terraform init
terraform apply -parallelism=1 -auto-approve

# Configurer les serveurs
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/site.yml

# Déployer sur Kubernetes
kubectl apply -f kubernetes/deployments/app-deployment.yml
kubectl apply -f kubernetes/services/app-service.yml
```

---

## Phases du projet

| Phase | Description | Statut |
|---|---|---|
| Phase 1 | Infrastructure as Code — Terraform + Ansible | ✅ Terminée |
| Phase 2 | CI/CD + Docker + Kubernetes | ✅ Terminée |
| Phase 3 | Supervision — Prometheus + Grafana + ELK | 🔄 En cours |
| Phase 4 | Haute disponibilité + Documentation finale | ⏳ À venir |

---

## Contact

**Stayer Arsel DIFFO SOUOP**  
📧 diffoarsel123@gmail.com | 📱 07 59 38 19 27  
🔗 [LinkedIn](https://www.linkedin.com/in/arsel-diffo-42a579338/) | 📍 Île-de-France

---

*SUPINFO Paris — Master of Engineering Systèmes, Réseaux & Cloud — 2025/2026*