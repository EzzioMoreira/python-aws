## Cria EC2

Lambda para criar instância EC2.

Configure variavéis de ambiente

Exemplo

```shell
AMI=ami-0715c1897453cabd1
INSTANCE_TYPE=t2.nano
SUBNET_ID=subnet-08b73d2ba25dc8a97
```

### Terraform

Execute o terraform em container.

```shell
run -it --rm -v $PWD:/app -w /app/ -e AWS_ACCESS_KEY_ID=$$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$$AWS_SECRET_ACCESS_KEY --entrypoint "" hashicorp/terraform:latest sh
```
