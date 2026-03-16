output "resource_group_name" {
  value = azurerm_resource_group.main.name
}

output "vm_public_ip" {
  description = "IP publique de la VM — utilise-la pour Ansible"
  value       = azurerm_public_ip.main.ip_address
}

output "vm_name" {
  value = azurerm_linux_virtual_machine.main.name
}

output "storage_account_name" {
  value = azurerm_storage_account.main.name
}
