provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "data_lake" {
  bucket = "threat-intel-data"
}
