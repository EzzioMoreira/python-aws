import os
import boto3
import logging

try:
    AMI = os.environ['AMI']
    INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
    SUBNET_ID = os.environ['SUBNET_ID']

except KeyError as error:
    logging.error('Não foi possível encontrar variável {}'.format(error))
    exit(1)

ec2 = boto3.resource('ec2')

try:
    def lambda_handler(event, context):
        instance = ec2.create_instance(
            Image=AMI,
            InstanceType=INSTANCE_TYPE,
            SubnetId=SUBNET_ID,
            MaxCount=1,
            MixCount=1
        )

        print('Nova instancia criada', instance[0].id, instance[0].name)

except Exception as error:
    logging.error('Nao foi possível criar instancia{}',format(error))
    exit(1)
