variable "location" {
  description = "The location to host the cluster in"
  default = "us-central1-a"
}

variable "project" {
  description = "The project name"
  default = "vmware-281905"
}

variable "credentials" {
  description = "Credentials file name"
  default = "access.json"
}

variable "cluster_name" {
  description = "The cluster name"
  default = "vmware-cluster"
}

variable "pool_name" {
  description = "The node pool name"
  default = "pool"
}

variable "cluster_suffux" {
  description = "The cluster suffix"
  default = "demo"
}

variable "machine_type" {
  description = "The node pool machine type"
  default = "g1-small"
}

variable "node_count" {
  description = "The node pool machine count"
  default = "1"
}