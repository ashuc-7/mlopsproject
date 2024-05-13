import os
from pathlib import Path
list_of_file=[           #src folder wil take the source code
    ".github/workflows/.gitkeep", # Workflow for For CI/CD
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipleine/__init__.py",
    "src/pipleine/training_pipeline.py",
    "src/pipleine/prediction_pipeline.py",   #Component will take the pipeline like training pipeline etc
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.config",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
    
]

for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        #logging.info(f"Creating directory:{filedir} for file :{filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass #Create an empty file