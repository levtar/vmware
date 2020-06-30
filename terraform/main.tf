provider "google" {
  version = "~> 3.3.0"
  region  = var.location
  credentials = file(var.credentials)
  project     = var.project
}

resource "google_container_cluster" "gke-cluster" {
  name     = "${var.cluster_name}-${var.cluster_suffux}"
  location = var.location

  # We can't create a cluster with no node pool defined, but we want to only use
  # separately managed node pools. So we create the smallest possible default
  # node pool and immediately delete it.
  remove_default_node_pool = true
  initial_node_count       = 1

  master_auth {
    username = ""
    password = ""

    client_certificate_config {
      issue_client_certificate = false
    }
  }
  logging_service = "none"
  monitoring_service = "none"
  # create cluster connection context
  provisioner "local-exec" {
    command = "gcloud container clusters get-credentials ${google_container_cluster.gke-cluster.name} --zone  ${google_container_cluster.gke-cluster.location} --project ${google_container_cluster.gke-cluster.project}"
  }
}

resource "google_container_node_pool" "gke-cluster_preemptible_nodes" {
  name       = "${var.pool_name}-${var.cluster_suffux}"
  location   = var.location
  cluster    = google_container_cluster.gke-cluster.name
  node_count = var.node_count

  node_config {
    preemptible  = true
    machine_type = var.machine_type

    metadata = {
      disable-legacy-endpoints = "true"
    }

    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }
}

data "google_client_config" "default" {
}

provider "kubernetes" {
    // Due to bug in resent provider version 11.1 I had to pin the provider version to 1.10
    // https://github.com/terraform-providers/terraform-provider-kubernetes/issues/759
    version = "1.10"

  load_config_file = false
  host             = google_container_cluster.gke-cluster.endpoint
  token            = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(google_container_cluster.gke-cluster.master_auth[0].cluster_ca_certificate)
}

# Create production namespace
resource "kubernetes_namespace" "production" {
  metadata {
    labels = {
      mylabel = "production"
    }
    name = "production"
  }
}

