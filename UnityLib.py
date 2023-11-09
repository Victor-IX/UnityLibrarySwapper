import os
import shutil

# Define the paths
new_branch_name = ".Release"
old_branch_name = ".Develop"

unity_project_path = "C:/Users/Number/Documents/Git/UnityProject/Library"
library_repo_path_temp = "C:/Users/Number/Documents/Git/UnityLibraryRepo/Temp/Library"
library_repo_path_backup = "C:/Users/Number/Documents/Git/UnityLibraryRepo/Backup/Library"

old_library_temp_path = library_repo_path_temp + old_branch_name
old_library_backup_path = library_repo_path_backup + old_branch_name
new_library_backup_path = library_repo_path_backup + new_branch_name

if os.path.exists(old_library_temp_path):
    shutil.rmtree(old_library_temp_path)

shutil.copytree(unity_project_path, old_library_temp_path) # copy past old
shutil.rmtree(unity_project_path) # delet

if os.path.exists(unity_project_path):
    shutil.rmtree(unity_project_path)

shutil.copytree(new_library_backup_path, unity_project_path) # copy past new

if os.path.exists(old_library_backup_path):
    shutil.rmtree(old_library_backup_path)

shutil.copytree(old_library_temp_path, old_library_backup_path)
shutil.rmtree(old_library_temp_path)

print("Library folders updated.")