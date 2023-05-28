from datetime import datetime
import boto3

def lambda_handler(event, context):
    # Lista regioes
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]
    
    for region in regions:

        print('Instancias EC2 na regiao {}:'.format(region))
        ec2 = boto3.resource('ec2', region_name=region)

        isnstances = ec2.instances.filter(
            Filters=[{
                'Name': 'tag:backup', 
                'Values': ['true']
            }]
        )

        # Adiciona timestamp
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

        for i in isnstances.all():
            for v in i.volumes.all():

                desc = 'Backup da {}, volume {}'.format(i.id, v.id, timestamp)

                snapshot = v.create_snapshot(Description=desc)

                print("Snapshot creado:", snapshot.id)