
import os

# Define the folder where the files are located
folder_path =r"C:\Users\MY GURUKUL\Desktop\Image"

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file has a valid extension
    if filename.endswith(('.png', '.jpg')):
        # Extract the student ID and add ".png"
        student_id = filename.split('_')[-1].split('.')[0] + ".png"

        # Old and new file paths
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, student_id)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {student_id}")
