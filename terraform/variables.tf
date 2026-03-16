variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
}

variable "client_id" {
  description = "Service Principal App ID"
  type        = string
}

variable "client_secret" {
  description = "Service Principal Password"
  type        = string
  sensitive   = true
}

variable "tenant_id" {
  description = "Azure Tenant ID"
  type        = string
}

variable "location" {
  description = "Region Azure"
  type        = string
  default     = "West Europe"
}

variable "project_name" {
  description = "Nom du projet"
  type        = string
  default     = "devsecops-arsel"
}

variable "admin_username" {
  description = "Nom utilisateur admin VM"
  type        = string
  default     = "azureadmin"
}

variable "ssh_public_key_path" {
  description = "Chemin vers la clé SSH publique"
  type        = string
  default     = "~/.ssh/id_ed25519.pub"
}
