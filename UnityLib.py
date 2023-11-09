import os
import shutil
import subprocess

# Define the paths
unity__project_path = "C:/Users/Number/Documents/Git/UnityProject"
unity_library_path = "C:/Users/Number/Documents/Git/UnityProject/Library"
library_repo_path_temp = "C:/Users/Number/Documents/Git/UnityLibraryRepo/Temp/Library"
library_repo_path_backup = "C:/Users/Number/Documents/Git/UnityLibraryRepo/Backup/Library"

try:
    # Get Cutent and previous git branch name
    current_branch_result = subprocess.run(['git', 'rev-parse', '--symbolic-full-name', 'HEAD'], cwd=unity__project_path, stdout=subprocess.PIPE, text=True, check=True)
    current_branch_path = current_branch_result.stdout.strip()
    current_branch_name = current_branch_path.split("/")[-1]
    
    previous_branch_result = subprocess.run(['git', 'rev-parse', '--symbolic-full-name', '@{-1}'], cwd=unity__project_path, stdout=subprocess.PIPE, text=True, check=True)
    previous_branch_path = previous_branch_result.stdout.strip()
    previous_branch_name = previous_branch_path.split("/")[-1]

    print(previous_branch_name)
    print(current_branch_name)

except subprocess.CalledProcessError as e:
    print(f'Error running the Git command: {e.stderr}')
except FileNotFoundError:
    print('Git executable not found. Please make sure Git is installed and available in your system PATH.')

new_branch_name = "." + current_branch_name
old_branch_name = "." + previous_branch_name

old_library_temp_path = library_repo_path_temp + old_branch_name
old_library_backup_path = library_repo_path_backup + old_branch_name
new_library_backup_path = library_repo_path_backup + new_branch_name

if os.path.exists(old_library_temp_path):
    shutil.rmtree(old_library_temp_path)

shutil.copytree(unity_library_path, old_library_temp_path) # copy past old
shutil.rmtree(unity_library_path) # delet

if os.path.exists(unity_library_path):
    shutil.rmtree(unity_library_path)

shutil.copytree(new_library_backup_path, unity_library_path) # copy past new

if os.path.exists(old_library_backup_path):
    shutil.rmtree(old_library_backup_path)

shutil.copytree(old_library_temp_path, old_library_backup_path)
shutil.rmtree(old_library_temp_path)

print("Library folders updated.")