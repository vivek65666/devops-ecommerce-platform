data "aws_availability_zones" "available" {state="available"}
resource "aws_vpc" "this" {cidr_block=var.vpc_cidr enable_dns_hostnames=true enable_dns_support=true tags={Name="${var.project_name}-vpc"}}
resource "aws_subnet" "public" {count=var.az_count vpc_id=aws_vpc.this.id cidr_block=cidrsubnet(var.vpc_cidr,8,count.index) availability_zone=data.aws_availability_zones.available.names[count.index] map_public_ip_on_launch=true tags={Name="${var.project_name}-public-${count.index+1}",Tier="public"}}
resource "aws_subnet" "private" {count=var.az_count vpc_id=aws_vpc.this.id cidr_block=cidrsubnet(var.vpc_cidr,8,count.index+10) availability_zone=data.aws_availability_zones.available.names[count.index] tags={Name="${var.project_name}-private-${count.index+1}",Tier="private"}}
