# Criação Automática de Pastas e Subpastas com DevOps

Este é um script Python que cria pastas e subpastas automaticamente em um diretório definido, incluindo pastas e subpastas relacionadas a DevOps. O script utiliza a biblioteca `os` para manipulação de diretórios e a biblioteca `argparse` para processamento de argumentos de linha de comando.

## Como usar

O script pode ser executado com os seguintes argumentos opcionais:

- `--root` ou `-r`: especifica o diretório raiz em que as pastas e subpastas serão criadas. Se não for especificado, o diretório atual será usado.
- `--dry-run` ou `-d`: executa o script em modo "dry-run", ou seja, apenas exibe as ações que seriam executadas, sem realmente criá-las.

Por exemplo, para criar as pastas e subpastas no diretório atual em modo "dry-run", você pode executar o seguinte comando:

```shell
python3 create-devops-dirs.py --dry-run
```

## Pastas e Subpastas

O script cria as seguintes pastas:

- `_archive`
- `dev`
- `prd`
- `stg`

E as seguintes subpastas dentro de cada pasta:

- `devops/ansible`
- `devops/packer`
- `devops/terraform`
- `devops/scripts`
- `devops/docker/compose`
- `devops/ansible/playbooks`
- `devops/ansible/roles`
- `devops/ansible/inventories`
- `devops/ansible/templates`
- `devops/ansible/files`
- `apps/utils`
- `apps/_libs`
- `env/host.example.com`
- `env/host.example.com/app_data`
- `env/host.example.com/bkp`
- `env/host.example.com/etc`

O script verifica se as pastas e subpastas já existem e, se existirem, apenas exibe uma mensagem sem tentar criá-las novamente. 

Ao final, o script exibe um resumo dos diretórios criados e dos diretórios já existentes. A contagem total de pastas criadas e pastas já existentes, bem como uma lista com os caminhos de cada pasta, também são exibidos.

## Requisitos

O script requer Python 3.x e as bibliotecas `os` e `argparse`.