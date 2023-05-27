import os
import boto3
import logging

try:
    BUCKET_DESTINATION = os.environ['BUCKET_DESTINATION']
    SIZE = os.environ['SIZE']
except KeyError as erro:
    logging.error('Não foi possível encontrar variável... {}'.format(erro))
    exit(1)
else:
    logging.info('Variavéis encontradas...')

s3 = boto3.client('s3')

def lambda_handler(event, context):

    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        thumb = 'thum-' + key
        with tempfile.TemporaryDirectory() as tmpdir:
            download_apth = os.path.join(tmpdir, key)
            upload_path = os.path.join(tmpdir, key)
            generate_thumbnail(download_path, upload_path)
            s3.upload_file(upload_path, DEST_BUCKET, thumb)
        logging.info('Imagem salva {}/{}'.format(BUCKET_DESTINATION, thumb))

def generate_thumnail(source_path, des_path):
    logging.infor('Thumnail gerado com secusso:', source_path)
    with Image.open(source_path) as image:
        image.thumbnail(SIZE)
        image.save(dest_path)
