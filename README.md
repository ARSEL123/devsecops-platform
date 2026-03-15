# Plateforme DevSecOps — Azure

Projet d'étude Master 2 — SUPINFO Paris  
**Stayer Arsel DIFFO SOUOP**

## Stack technique
- Infrastructure as Code : Terraform + Ansible
- Cloud : Microsoft Azure
- Conteneurs : Docker + Kubernetes (AKS)
- CI/CD : GitHub Actions
- Supervision : Prometheus + Grafana + ELK
- Sécurité : Trivy + VPN IPsec + NSG

## Structure du projet
```
devsecops-platform/
├── terraform/        # Provisionnement Azure
├── ansible/          # Configuration serveurs
├── kubernetes/       # Manifests K8s
├── .github/workflows # Pipelines CI/CD
├── monitoring/       # Prometheus, Grafana, ELK
├── security/         # Règles sécurité
└── docs/             # Documentation
```

## Statut
![CI](https://github.com/TON_USERNAME/devsecops-platform/actions/workflows/ci.yml/badge.svg)

**Phase actuelle : Phase 1 — Infrastructure as Code**
