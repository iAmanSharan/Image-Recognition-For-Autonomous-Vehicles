import os
from pathlib import Path
import logging

project_name = "Image Recognition"

list_of_files = [
  ".github/workflow/.gitkeep",
  "requirements.txt",
  "setup.py",
  "research/trails.ipynb",
  "params.yaml",
  "dvc.yaml",
  'config/config.yaml'
  f"src/{project_name}/__init__.py",
  f"src/{project_name}/components/__init__.py",
  f"src/{project_name}/uitls/__init__.py",
  f"src/{project_name}/config/__init.py",
  f"src/{project_name}/config/config.py",
  f"src/{project_name}/pipeline/__init__.py",
  f"src/{project_name}/entity/__init__.py",
  f"src/{project_name}/constant/__init__.py"
]

for file in list_of_files:
  file = Path(file)
  filedir,filename = os.path.split(file)
  if filedir != "":
    os.makedirs(filedir , exist_ok = True)
    logging.info("file directory created ")

  if (not os.path.exists(file)) or (os.path.getsize(file)==0):
    with open(file ,'w') as f:
      pass
      logging.info('file created')
  else:
    logging.info('file already exists')
  