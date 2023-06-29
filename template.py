import sys
import os
from pathlib import Path
import logging
project_name="project_name"

list_of_files = [
    ".gitub/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src:{project_name}/components/__init__.py",
    f"src:{project_name}/utils/__init__.py",
    f"src:{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trial;ipynb"
]

for file in list_of_files:
    file==Path(file)
    filedir,filename=os.path.split(file)
    if filedir:
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created {filedir}")
    if (not os.path.exists(file) or os.path.getsize(file)==0):
        with open(file,"w") as f:
            pass
        logging.info(f"Created {file}")
        
    else:
        logging.info(f"{file} already exists")
