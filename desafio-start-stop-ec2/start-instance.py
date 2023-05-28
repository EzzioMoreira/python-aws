import boto3
import logging

try:
    def lambda_handler(event, context):
        ec2 = boto3.client('ec2')
        regions = [region['RegionName']
                   for region in ec2.describe_regions()['Regions']]
          
        # Busca em todas as regions
        for region in regions:
            ec2 = boto3.resource('ec2', region_name=region)
    
            print('AWS_Region: ', region)

            # Filtra instancias desligadas
            instances = ec2.instances.filter(
                Filters=[{
                    'Name': 'instance-state-name',
                    'Values': ['stopped']
                }]
            )

            # Para instancias
            for i in instances:
                i.start()
                print('Instancia desligada: ', instance.id)

except KeyError as error:
    logging.error('não foi possivel ligar instancia {}'.format(error))
    exit(1)
