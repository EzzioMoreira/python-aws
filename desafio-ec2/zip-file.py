import zipapp
import os

def create_lambda_zip(source, destination):
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source):
            for file in files:
                files_path = os.path.join(root, file)
                zipf.write(files_path, os.path.realpath(files_path, source))

source = 'main.py' # Pasta contendo o código Python
destination = 'create_lambda.zip' # Caminho e nome do arquivo ZIP de saída

create_lambda_zip(source, destination)
