from pathlib import Path
import subprocess
import zipfile
from sklearn.model_selection import train_test_split
import pandas as pd
import yaml
import sys



api = "kaggle competitions download -c nyc-taxi-trip-duration"
curr_path = Path.cwd()

def download_data():
    Path("data/kaggle_data").mkdir(parents=True,exist_ok=True)
    
    download_command = api
    subprocess.run(download_command,shell=True,check=True,cwd=Path("data/kaggle_data"))
    print("Dataset Downloaded Successfully")

def unzip_data(pathdata,path_to_zip_file):
    
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
       zip_ref.extractall(Path(pathdata))
    
def load_data(data_path):
    # Load your dataset from a given path
    df = pd.read_csv(data_path)
    return df
    
def main():
    
    curr_dir = Path(__file__)
    print(curr_dir)
    home_dir = Path.cwd()
    print(home_dir)
    if Path("data/kaggle_data/nyc-taxi-trip-duration.zip").exists==False:
       download_data()
       unzip_data("data/raw",Path('data/kaggle_data/nyc-taxi-trip-duration.zip'))
       unzip_data("data/processed",Path('data/raw/train.zip'))
       unzip_data("data/processed",Path('data/raw/test.zip'))
    else:
       print("data already downloaded")
    # params_file = home_dir.as_posix() + '/params.yaml'
    # params = yaml.safe_load(open(params_file))['make_dataset']
   

if __name__ == "__main__":
    main()

