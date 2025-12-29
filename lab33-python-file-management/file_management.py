import os
import shutil

# Define source and destination directories
source_dir = "source_folder"
backup_dir = "backup_folder"

# Create backup directory if it does not exist
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# List files in source directory
files = os.listdir(source_dir)
print("Files found:", files)

# Copy and rename files
for file in files:
    source_path = os.path.join(source_dir, file)
    name, ext = os.path.splitext(file)
    new_name = f"{name}_backup{ext}"
    dest_path = os.path.join(backup_dir, new_name)

    shutil.copy(source_path, dest_path)

print("Files copied and renamed successfully.")
