# 📸 iPhone to PC Photo Cleaner

Automatically clean up duplicate iPhone photos after transferring them to your Windows PC.

---

## 🔍 What Problem Does This Solve?

When you take a photo on your iPhone using a **filter** (e.g. Vivid, Mono, Dramatic), the Camera app saves:

- `IMG_1234.JPG` → the **original** (unfiltered)
- `IMG_E1234.JPG` → the **filtered/edited** version

On your iPhone, you only see one image.  
But when you transfer photos to a **Windows PC**, both versions appear — cluttering your folder with duplicates.

---

## ✅ What This Tool Does

This script helps you clean up that mess by:

- Scanning all files in a folder
- Identifying duplicate pairs:
  - `IMG_1234.JPG` (original)
  - `IMG_E1234.JPG` (filtered/edited)
- 🗑️ Deleting the original if both exist
- ✅ Keeping:
  - Only the filtered version when both exist
  - The original if no filtered version exists
  - The filtered one if no original is present

---

## 💡 How It Works

| Scenario                                      | Action                      |
|----------------------------------------------|-----------------------------|
| Both `IMG_1234.JPG` and `IMG_E1234.JPG` exist | ✅ Keep `IMG_E`, 🗑️ Delete `IMG_` |
| Only `IMG_1234.JPG` exists                    | ✅ Keep original             |
| Only `IMG_E1234.JPG` exists                   | ✅ Keep edited               |

---

## 🚀 How to Use

1. Place `iclean.py` into the folder with your iPhone-transferred photos
2. Open a terminal or command prompt in that folder
3. Run the script:

```bash
python iclean.py
