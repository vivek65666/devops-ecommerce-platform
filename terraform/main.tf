module "network" {source="./modules/network" project_name=var.project_name vpc_cidr=var.vpc_cidr az_count=var.az_count}
resource "aws_ecr_repository" "services" {
  for_each=toset(["frontend","api-gateway","user-service","product-service","cart-service","order-service","payment-service","notification-service"])
  name="${var.project_name}/${each.key}"
  image_tag_mutability="IMMUTABLE"
  image_scanning_configuration {scan_on_push=true}
  encryption_configuration {encryption_type="AES256"}
}
