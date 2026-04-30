# 🚀 Plateforme DevSecOps — Azure — Stayer Arsel DIFFO SOUOP

<div align="center">

[![CI/CD Pipeline](https://github.com/ARSEL123/devsecops-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/ARSEL123/devsecops-platform/actions/workflows/ci.yml)
![Azure](https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)


<br/>

> **Stayer Arsel DIFFO SOUOP**  
> Conception et déploiement d'une infrastructure DevSecOps complète sur Microsoft Azure 


<br/>
### 🌐 Portfolio live → [http://20.87.59.67](http://20.87.59.67)
### 🚀 App DevSecOps → [http://20.87.90.91](http://20.87.90.91)

</div>

---

## Présentation

Plateforme **DevSecOps complète** déployée sur Microsoft Azure,

Ce dépôt contient :
- Un **portfolio React** déployé sur Kubernetes avec CI/CD automatisé
- Une **plateforme DevSecOps** complète avec supervision Prometheus + Grafana + ELK
- L'intégralité de l'infrastructure as Code (Terraform + Ansible)

## 📌 À propos

Ce projet est une **plateforme DevSecOps complète** déployée sur Microsoft Azure.  
Il démontre la maîtrise de l'ensemble du cycle de vie d'une infrastructure cloud moderne :

- 🏗️ **Infrastructure as Code** — Terraform provisionne Azure, Ansible configure les serveurs
- 🐳 **Conteneurisation** — Docker avec multi-stage build et tests automatiques
- ☸️ **Orchestration** — Kubernetes AKS avec haute disponibilité (2 pods)
- 🔄 **CI/CD automatisé** — GitHub Actions déploie à chaque `git push`
- 🔒 **Sécurité intégrée** — Scan Trivy sur chaque image avant déploiement

---

## Applications déployées

| Application | URL | Technologie | Statut |
|---|---|---|---|
| Portfolio React | http://20.87.59.67 | React + Nginx + Kubernetes | ✅ Live |
| Plateforme DevSecOps | http://20.87.90.91 | Python Flask + Kubernetes | ✅ Live |

---

## Stack technique

| Catégorie | Technologies |
|---|---|
| Infrastructure as Code | Terraform, Ansible |
| Cloud | Microsoft Azure — South Africa North |
| Conteneurs | Docker (multi-stage build) |
| Orchestration | Kubernetes AKS |
| Registre | Azure Container Registry |
| Applications | React + Nginx, Python Flask + Gunicorn |
| CI/CD | GitHub Actions (4 jobs automatisés) |
| Sécurité | Trivy (scan vulnérabilités) |
| Supervision | Prometheus + Grafana + ELK Stack |

---

## Pipeline CI/CD

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
| Virtual Machine Ubuntu 22.04 | vm-devsecops-arsel | ✅ Running |
| Kubernetes Cluster (AKS) | aks-devsecops-arsel | ✅ Running |
| Container Registry (ACR) | acrdevsecopsarsel | ✅ |
| Virtual Network | vnet-devsecops-arsel | ✅ |
| Storage Account | stdevsecopsarsel001 | ✅ |
| Portfolio IP | 20.87.59.67 | ✅ Live |
| App DevSecOps IP | 20.87.90.91 | ✅ Live |

---

## Structure du projet

| Dossier | Contenu |
|---|---|
| `app/` | Application Flask — code source, Dockerfile, tests |
| `portfolio/` | Portfolio React — composants, build, Dockerfile |
| `terraform/` | Provisionnement infrastructure Azure |
| `ansible/` | Configuration automatisée des serveurs |
| `kubernetes/` | Manifests de déploiement (Flask + Portfolio) |
| `.github/workflows/` | Pipeline CI/CD GitHub Actions |
| `monitoring/` | Supervision Prometheus + Grafana + ELK |
| `docs/` | Tests de charge k6 + documentation |

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

# Déployer les applications sur Kubernetes
kubectl apply -f kubernetes/deployments/
kubectl apply -f kubernetes/services/

# Vérifier
kubectl get pods
curl http://4.253.10.14 
Portfolio  http://20.87.59.67
Plateforme  http://20.87.90.91
```

---

## Phases du projet

| Phase | Description | Statut |
|---|---|---|
| Phase 1 | Infrastructure as Code — Terraform + Ansible | ✅ Terminée |
| Phase 2 | CI/CD + Docker + Kubernetes | ✅ Terminée |
| Phase 3 | Supervision — Prometheus + Grafana + ELK | ✅ Terminée |
| Phase 4 | Haute disponibilité + Tests de charge + Portfolio | ✅ Terminée |

---

## Résultats clés

| Indicateur | Valeur |
|---|---|
| Ressources Azure déployées | 12 actives |
| Tests de charge k6 | 50 VUs, 0% erreurs, p95=395ms |
| Tâches Ansible | 21 tâches, 0 erreur |
| Pipeline CI/CD | 4 jobs 100% verts |
| Applications live | 2 (Portfolio + DevSecOps) |

---

## Contact

| | |
|---|---|
| **Nom** | Stayer Arsel DIFFO SOUOP |
| **Email** | diffoarsel123@gmail.com |
| **Téléphone** | 07 59 38 19 27 |
| **LinkedIn** | [arsel-diffo](https://www.linkedin.com/in/arsel-diffo-42a579338/) |
| **Localisation** | Île-de-France, France |

---

