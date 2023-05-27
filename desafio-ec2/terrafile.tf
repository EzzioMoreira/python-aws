provider "aws" {
  region = "us-east-1"  # Defina a região desejada
}

resource "aws_lambda_function" "thin" {
  filename      = "create_instance.zip"  # Nome do arquivo ZIP contendo o código do Lambda
  function_name = "create_instance_ec2"  # Nome da função do Lambda
  role          = aws_iam_role.thin.arn  # ARN da role do IAM para a função do Lambda
  handler       = "lambda_function.lambda_handler"  # Nome da função de manipulador (handler)
  runtime       = "python3.8"  # Versão do Python a ser usada

  environment {
    variables = {
      AMI           = var.ami
      INSTANCE_TYPE = var.instance_type
      SUBNET_ID     = var.subnet_id
    }
  }
}

resource "aws_iam_role" "thin" {
  name = "create_instance_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
            "ec2:RunInstances",
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
        ]
        Effect = "Allow"
        Sid    = ""
        }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "thin" {
  role       = aws_iam_role.thin.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

variable "ami" {
  default = "ami-0715c1897453cabd1"
  description = "AMI ID"
}

variable "instance_type" {
  default = "t2.nano"
  description = "Instance Type"
}

variable "subnet_id" {
  default = "subnet-08b73d2ba25dc8a97"
  description = "Subnet ID"
}

# Compare this snippet from desafio-ec2/zip-file.py: