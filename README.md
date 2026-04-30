# 🚀 Plateforme DevSecOps — Azure

<div align="center">

[![CI/CD](https://github.com/ARSEL123/devsecops-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/ARSEL123/devsecops-platform/actions/workflows/ci.yml)
&nbsp;
![Azure](https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?logo=ansible&logoColor=white)

<br/>

> **Stayer Arsel DIFFO SOUOP**  
> Conception et déploiement d'une infrastructure DevSecOps complète sur Microsoft Azure 


<br/>

### 🌐 [Voir l'application en live → http://20.87.90.91](http://20.87.90.91)

</div>

---

## 📌 À propos

Ce projet est une **plateforme DevSecOps complète** déployée sur Microsoft Azure.  
Il démontre la maîtrise de l'ensemble du cycle de vie d'une infrastructure cloud moderne :

- 🏗️ **Infrastructure as Code** — Terraform provisionne Azure, Ansible configure les serveurs
- 🐳 **Conteneurisation** — Docker avec multi-stage build et tests automatiques
- ☸️ **Orchestration** — Kubernetes AKS avec haute disponibilité (2 pods)
- 🔄 **CI/CD automatisé** — GitHub Actions déploie à chaque `git push`
- 🔒 **Sécurité intégrée** — Scan Trivy sur chaque image avant déploiement

---

## ⚡ Pipeline CI/CD

> Chaque `git push` sur `main` déclenche automatiquement :

| # | Job | Ce qui se passe | Durée |
|---|---|---|---|
| 1 | 🔨 **Build & Test** | Tests Python (pytest) + Build Docker | ~30s |
| 2 | 🔒 **Security Scan** | Scan Trivy CRITICAL/HIGH | ~45s |
| 3 | 📦 **Push to ACR** | Image pushée sur Azure Container Registry | ~1min |
| 4 | 🚀 **Deploy to AKS** | Rolling update Kubernetes sans interruption | ~2min |

---

## ☁️ Infrastructure Azure déployée

| Ressource | Nom | Statut |
|---|---|---|
| Resource Group | rg-devsecops-arsel | ✅ Actif |
| Virtual Machine Ubuntu 22.04 | vm-devsecops-arsel | ✅ Running |
| Kubernetes Cluster (AKS) | aks-devsecops-arsel | ✅ Running |
| Container Registry (ACR) | acrdevsecopsarsel | ✅ Actif |
| Virtual Network | vnet-devsecops-arsel | ✅ Actif |
| Storage Account | stdevsecopsarsel001 | ✅ Actif |
| IP Publique | 20.87.90.91 | ✅ Live |

---

## 🛠️ Stack technique

| Catégorie | Technologies utilisées |
|---|---|
| ☁️ Cloud | Microsoft Azure (South Africa North) |
| 🏗️ Infrastructure as Code | Terraform + Ansible |
| 🐳 Conteneurs | Docker multi-stage build |
| ☸️ Orchestration | Kubernetes AKS (Free tier) |
| 📦 Registre | Azure Container Registry |
| 💻 Application | Python Flask + Gunicorn |
| 🔄 CI/CD | GitHub Actions (4 jobs) |
| 🔒 Sécurité | Trivy (scan vulnérabilités) |
| 📊 Supervision | Prometheus + Grafana + ELK *(Phase 3)* |

---

## 📁 Organisation du projet

| Dossier | Contenu |
|---|---|
| `app/` | Application Flask — code source, Dockerfile, tests |
| `terraform/` | Provisionnement infrastructure Azure |
| `ansible/` | Configuration automatisée des serveurs |
| `kubernetes/` | Manifests de déploiement Kubernetes |
| `.github/workflows/` | Pipeline CI/CD GitHub Actions |
| `monitoring/` | Supervision Prometheus + Grafana + ELK |
| `docs/` | Documentation technique |

---

## 🗺️ Phases du projet

| Phase | Description | Statut |
|---|---|---|
| **Phase 1** | Infrastructure as Code — Terraform + Ansible | ✅ **Terminée** |
| **Phase 2** | CI/CD + Docker + Kubernetes | ✅ **Terminée** |
| **Phase 3** | Supervision — Prometheus + Grafana + ELK | ✅ **Terminée** |
| **Phase 4** | Haute disponibilité + Documentation finale | ⏳ À venir |

---

## 🚀 Lancer le projet
```bash
# 1. Cloner le dépôt
git clone git@github.com:ARSEL123/devsecops-platform.git
cd devsecops-platform

# 2. Provisionner Azure
cd terraform
terraform init
terraform apply -parallelism=1 -auto-approve

# 3. Configurer les serveurs
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/site.yml

# 4. Déployer sur Kubernetes
kubectl apply -f kubernetes/deployments/app-deployment.yml
kubectl apply -f kubernetes/services/app-service.yml

# 5. Vérifier
kubectl get pods
curl http://20.87.90.91
```

---

## 📬 Contact

| | |
|---|---|
| 👤 **Nom** | Stayer Arsel DIFFO SOUOP |
| 📧 **Email** | diffoarsel123@gmail.com |
| 📱 **Téléphone** | 07 59 38 19 27 |
| 🔗 **LinkedIn** | [arsel-diffo](https://www.linkedin.com/in/arsel-diffo-42a579338/) |
| 📍 **Localisation** | Île-de-France, France |

---

<div align="center">
<sub>SUPINFO Paris · Master of Engineering Systèmes, Réseaux & Cloud · 2025/2026</sub>
</div>