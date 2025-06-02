import os

# ✅ Use correct string formatting
src_folder = r"W:\PraiseHim\static\songs"

for filename in os.listdir(src_folder):
    if filename.endswith("_page.jpg"):
        number = filename.split("_")[0]
        if number.isdigit() and len(number) == 2:  # e.g., 01
            new_name = f"{int(number):03d}_page.jpg"
            old_path = os.path.join(src_folder, filename)
            new_path = os.path.join(src_folder, new_name)
            print(f"Renaming: {filename} -> {new_name}")
            os.rename(old_path, new_path)
