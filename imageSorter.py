import os
import shutil

source_folder = r"D:\\"

destination_folder = r"D:\\Images"

os.makedirs(destination_folder, exist_ok=True)

image_extensions = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".bmp"
)

for file_name in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file_name)

    # Skip the Images folder itself
    if file_name == "Images":
        continue

    if file_name.lower().endswith(image_extensions):

        destination_path = os.path.join(destination_folder, file_name)

        # Prevent duplicate overwrite
        if os.path.exists(destination_path):

            name, ext = os.path.splitext(file_name)

            counter = 1

            while os.path.exists(destination_path):
                new_name = f"{name}_{counter}{ext}"
                destination_path = os.path.join(destination_folder, new_name)
                counter += 1

        shutil.move(file_path, destination_path)

        print(f"Moved: {file_name}")

print("Done sorting images.")