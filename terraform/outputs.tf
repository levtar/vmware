output "cluster_name" {
  value = google_container_cluster.gke-cluster.name
}

output "location" {
  value = google_container_cluster.gke-cluster.location
}

output "project" {
  value = google_container_cluster.gke-cluster.project
}