import os
import shutil
import kagglehub

# Download latest version
data_path = "mayurdalvi/sonar-mine-dataset"

def download_dataset():
    path = kagglehub.dataset_download(data_path)
    print(path)
    for filename in os.listdir(path):
        print("Copying ",filename)
        shutil.copyfile(os.path.join(path,filename),os.path.join(os.getcwd(),filename))
# print("Path to dataset files:", dataset())

download_dataset()