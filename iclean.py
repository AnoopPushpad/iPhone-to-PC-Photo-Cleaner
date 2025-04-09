import os

# Get all files in current directory
files = os.listdir()

# Separate IMG_ and IMG_E files by number part (ignoring extensions)
originals = {}
edited = set()

for f in files:
    filename = f.upper()  # Normalize for case-insensitivity (e.g., .jpg vs .JPG)

    if filename.startswith("IMG_E"):
        name_part = filename[6:].split('.')[0]
        edited.add(name_part)

    elif filename.startswith("IMG_") and not filename.startswith("IMG_E"):
        name_part = filename[4:].split('.')[0]
        originals[name_part] = f  # Keep original filename case for deletion

# Delete originals that have a matching edited version
for num, original_file in originals.items():
    if num in edited:
        try:
            os.remove(original_file)
            print(f"🗑️ Deleted original: {original_file}")
        except Exception as e:
            print(f"❌ Failed to delete {original_file}: {e}")
    else:
        print(f"✅ Keeping original (no edited found): {original_file}")
