# 1. Definimos el Provider (Le decimos que use LocalStack, no AWS real)
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test" # Claves falsas
  secret_key                  = "test"
  
  # ACÁ ESTÁ EL TRUCO: Redirigimos todo a localhost
  s3_use_path_style           = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3       = "http://localhost:4566"
    dynamodb = "http://localhost:4566"
  }
}

# 2. Recurso: Bucket S3 (Para guardar el estado de Terraform en el futuro)
resource "aws_s3_bucket" "terraform_state" {
  bucket = "crypto-terraform-state"
}

# 3. Recurso: Tabla DynamoDB (Para bloquear el estado y evitar conflictos)
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}