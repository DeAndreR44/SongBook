import os
import json
import re

# Load songs.json
with open("songs.json", "r", encoding="utf-8") as f:
    songs = json.load(f)

# Normalize titles to safe filenames
def title_to_filename(title):
    safe = re.sub(r'[^a-zA-Z0-9_]', '', title.replace(' ', '_').lower())
    return f"{safe}.jpg"

src_folder = r"W:\PraiseHim\static\songs"

for song in songs:
    old_path = os.path.join(src_folder, song["filename"])
    new_path = os.path.join(src_folder, title_to_filename(song["title"]))
    if os.path.exists(old_path):
        print(f"Renaming: {song['filename']} -> {os.path.basename(new_path)}")
        os.rename(old_path, new_path)
    else:
        print(f"Missing: {old_path}")
