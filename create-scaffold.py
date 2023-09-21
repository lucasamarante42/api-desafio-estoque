from pathlib import Path
import os
import sys

"""
Script: create-scaffold

Objetivo: criação da estrutura inicial do App

Parâmetros:
	1 => path do diretório

Utilização: python create-scaffold.py 'modulo'
"""

path = sys.argv[1]
print('Entrando no diretorio: {}'.format(path))
os.chdir(path)

Path('serializers.py').touch()
Path('filters.py').touch()
Path('repositories.py').touch()
Path('business.py').touch()
Path('urls.py').touch()
