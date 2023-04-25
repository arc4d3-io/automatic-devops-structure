import os
import argparse

# Define os argumentos de linha de comando
parser = argparse.ArgumentParser(description='Cria pastas e subpastas automaticamente em um diretório definido.')
parser.add_argument('--root', '-r', type=str, default='', help='O diretório raiz em que as pastas e subpastas serão criadas. Se não for especificado, o diretório atual será usado.')
parser.add_argument('--dry-run', '-d', action='store_true', help='Executa o script em modo "dry-run", ou seja, apenas exibe as ações que seriam executadas, sem realmente criá-las.')
args = parser.parse_args()

# Define o caminho do diretório atual ou do diretório raiz especificado pelos argumentos
current_directory = args.root if args.root else os.getcwd()

# Define o nome das pastas que você deseja criar
folders = ['_archive', 'dev', 'prd', 'stg']

# Define o nome das subpastas que você deseja criar dentro de cada pasta
subfolders = ['devops/ansible', 'devops/packer', 'devops/terraform', 'devops/scripts','devops/docker/compose','devops', 'devops/ansible/playbooks','devops/ansible/roles','devops/ansible/inventories','devops/ansible/templates','devops/ansible/files','apps/utils','apps/_libs','env/host.example.com', 'env/host.example.com/app_data',"env/host.example.com/bkp","env/host.example.com/etc"]

# Define variáveis para contar as pastas criadas e as pastas que já existem
created_folders = 0
existing_folders = 0

# Define listas para armazenar os caminhos das pastas criadas e das pastas que já existem
created_folders_list = []
existing_folders_list = []

# Loop para criar as pastas e subpastas
for folder in folders:
    # Define o caminho completo da pasta
    folder_path = os.path.join(current_directory, folder)
    try:
        # Tenta criar a pasta
        if not args.dry_run:
            os.makedirs(folder_path)
        created_folders += 1
        created_folders_list.append(folder_path)
    except FileExistsError:
        # Caso a pasta já exista, apenas exibe uma mensagem
        existing_folders += 1
        existing_folders_list.append(folder_path)
        continue # pula para a próxima iteração       
    # Loop para criar as subpastas dentro de cada pasta
    for subfolder in subfolders:
        # Define o caminho completo da subpasta
        subfolder_path = os.path.join(folder_path, subfolder)
        try:
            # Tenta criar a subpasta
            if not args.dry_run:
                os.makedirs(subfolder_path)
        except FileExistsError:
            # Caso a subpasta já exista, apenas exibe uma mensagem
            pass

# Exibe o resumo dos diretórios criados e dos diretórios já existentes
print(f"Resumo dos diretórios criados e dos diretórios já existentes:")
print(f"")
print(f"Diretórios criados: {created_folders}")
for path in created_folders_list:
    print(f" - {path}")
print(f"")
print(f"Diretórios já existentes: {existing_folders}")
for path in existing_folders_list:
    print(f" - {path}")
