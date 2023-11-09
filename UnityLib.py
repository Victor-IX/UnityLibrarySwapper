import os
import shutil
import subprocess
import subprocess
import psutil
from colorama import Fore, Style, init

# Define the paths
unity__project_path = "C:/Users/Number/Documents/Git/UnityProject"
unity_library_path = "C:/Users/Number/Documents/Git/UnityProject/Library"
library_repo_path_temp = "C:/Users/Number/Documents/Git/UnityLibraryRepo/Temp/Library"
library_repo_path_backup = "C:/Users/Number/Documents/Git/UnityLibraryRepo/Backup/Library"

saved_branchs = ["Develop", "Release"]

# Check if unity is runing
def is_process_running(process_name):
    return any(process.info['name'] == process_name for process in psutil.process_iter(attrs=['pid', 'name']))

if is_process_running("Unity.exe"):
    print(Fore.RED + "Error: Unity is running. Please close it before continuing." + Style.RESET_ALL)
    exit(1)


# Get Cutent and previous git branch name
try:
    current_branch_result = subprocess.run(['git', 'rev-parse', '--symbolic-full-name', 'HEAD'], cwd=unity__project_path, stdout=subprocess.PIPE, text=True, check=True)
    current_branch_path = current_branch_result.stdout.strip()
    current_branch_name = current_branch_path.split("/")[-1]
    
    previous_branch_result = subprocess.run(['git', 'rev-parse', '--symbolic-full-name', '@{-1}'], cwd=unity__project_path, stdout=subprocess.PIPE, text=True, check=True)
    previous_branch_path = previous_branch_result.stdout.strip()
    previous_branch_name = previous_branch_path.split("/")[-1]

except subprocess.CalledProcessError as e:
    print(f'Error running the Git command: {e.stderr}')
except FileNotFoundError:
    print('Git executable not found. Please make sure Git is installed and available in your system PATH.')

for branch in saved_branchs:
    if current_branch_name == branch:
        current_saved_branch = True
    if previous_branch_name == branch:
        previous_saved_branch = True
    else:
        continue

new_branch_name = "." + current_branch_name
old_branch_name = "." + previous_branch_name

old_library_temp_path = library_repo_path_temp + old_branch_name
old_library_backup_path = library_repo_path_backup + old_branch_name
new_library_backup_path = library_repo_path_backup + new_branch_name

# copy old lib to the temp folder
if previous_saved_branch == True:

    if os.path.exists(old_library_temp_path):
        shutil.rmtree(old_library_temp_path)

    shutil.copytree(unity_library_path, old_library_temp_path) # copy past old

# copy new lib to the unity folder
if current_saved_branch == True:
    
    if os.path.exists(unity_library_path):
        shutil.rmtree(unity_library_path)

    shutil.copytree(new_library_backup_path, unity_library_path) # copy past new

# copy old lib to the backup folder
if previous_saved_branch == True:
    if os.path.exists(old_library_backup_path):
        shutil.rmtree(old_library_backup_path)

    shutil.copytree(old_library_temp_path, old_library_backup_path)
    shutil.rmtree(old_library_temp_path)

print("Library folders updated.")