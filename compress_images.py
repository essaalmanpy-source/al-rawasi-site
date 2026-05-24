"""
Compress all images in static-site/images/ without changing filenames or formats.
This keeps the website looking exactly the same but reduces file sizes significantly.
"""
import os
import sys
from PIL import Image

IMAGE_DIR = os.path.join("static-site", "images")
JPEG_QUALITY = 75  # Good balance of quality vs size
PNG_OPTIMIZE = True
MAX_DIMENSION = 1200  # Max width/height for large photos (not logos)

# Directories containing small logos/icons - don't resize these, just compress
LOGO_DIRS = {"clients", "partners", "certificates"}

stats = {"processed": 0, "skipped": 0, "original_bytes": 0, "new_bytes": 0}


def compress_jpeg(filepath):
    """Compress a JPEG file in-place."""
    original_size = os.path.getsize(filepath)
    stats["original_bytes"] += original_size

    try:
        img = Image.open(filepath)
        
        # Convert RGBA to RGB if needed
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')

        # Resize if it's a large photo (not a logo)
        parent_dir = os.path.basename(os.path.dirname(filepath))
        if parent_dir not in LOGO_DIRS:
            w, h = img.size
            if max(w, h) > MAX_DIMENSION:
                ratio = MAX_DIMENSION / max(w, h)
                new_w = int(w * ratio)
                new_h = int(h * ratio)
                img = img.resize((new_w, new_h), Image.LANCZOS)

        # Save with optimization
        tmp_path = filepath + ".tmp"
        img.save(tmp_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
        if os.path.getsize(tmp_path) < original_size:
            os.replace(tmp_path, filepath)
        else:
            os.remove(tmp_path)
            
        new_size = os.path.getsize(filepath)
        stats["new_bytes"] += new_size
        stats["processed"] += 1

        saved = original_size - new_size
        pct = (saved / original_size * 100) if original_size > 0 else 0
        print(f"  OK {os.path.basename(filepath)}: {original_size//1024}KB -> {new_size//1024}KB (saved {pct:.0f}%)")
    except Exception as e:
        stats["new_bytes"] += original_size
        stats["skipped"] += 1
        print(f"  ERR {os.path.basename(filepath)}: ERROR - {e}")


def compress_png(filepath):
    """Compress a PNG file in-place."""
    original_size = os.path.getsize(filepath)
    stats["original_bytes"] += original_size

    try:
        img = Image.open(filepath)

        # Resize if it's a large photo (not a logo)
        parent_dir = os.path.basename(os.path.dirname(filepath))
        if parent_dir not in LOGO_DIRS:
            w, h = img.size
            if max(w, h) > MAX_DIMENSION:
                ratio = MAX_DIMENSION / max(w, h)
                new_w = int(w * ratio)
                new_h = int(h * ratio)
                img = img.resize((new_w, new_h), Image.LANCZOS)

        # For PNGs with transparency, keep RGBA; otherwise convert
        if img.mode == 'RGBA':
            # Use a valid quantization method for RGBA
            quantized = img.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
            # Temporary save to check size
            tmp_path = filepath + ".tmp"
            quantized.save(tmp_path, "PNG", optimize=True)
            if os.path.getsize(tmp_path) < original_size:
                os.replace(tmp_path, filepath)
            else:
                os.remove(tmp_path)
        elif img.mode == 'P':
            img.save(filepath, "PNG", optimize=True)
        else:
            img = img.convert('RGB')
            img.save(filepath, "PNG", optimize=True)

        new_size = os.path.getsize(filepath)
        stats["new_bytes"] += new_size
        stats["processed"] += 1

        saved = original_size - new_size
        pct = (saved / original_size * 100) if original_size > 0 else 0
        print(f"  OK {os.path.basename(filepath)}: {original_size//1024}KB -> {new_size//1024}KB (saved {pct:.0f}%)")
    except Exception as e:
        stats["new_bytes"] += original_size
        stats["skipped"] += 1
        print(f"  ERR {os.path.basename(filepath)}: ERROR - {e}")


def main():
    print("=" * 60)
    print("  Al-Rawasi Image Compression Tool")
    print("=" * 60)

    if not os.path.isdir(IMAGE_DIR):
        print(f"ERROR: Directory {IMAGE_DIR} not found!")
        sys.exit(1)

    for root, dirs, files in os.walk(IMAGE_DIR):
        rel_dir = os.path.relpath(root, IMAGE_DIR)
        if rel_dir == ".":
            print(f"\n[DIR] images/")
        else:
            print(f"\n[DIR] images/{rel_dir}/")

    for root, dirs, files in os.walk(IMAGE_DIR):
        for filename in sorted(files):
            filepath = os.path.join(root, filename)
            ext = filename.lower().rsplit(".", 1)[-1] if "." in filename else ""

            if ext in ("jpg", "jpeg"):
                compress_jpeg(filepath)
            elif ext == "png":
                compress_png(filepath)
            else:
                print(f"  - {filename}: skipped (not an image)")

    print("\n" + "=" * 60)
    print("  Results:")
    print(f"  Processed: {stats['processed']} files")
    print(f"  Skipped:   {stats['skipped']} files")
    orig_mb = stats['original_bytes'] / (1024 * 1024)
    new_mb = stats['new_bytes'] / (1024 * 1024)
    saved_mb = orig_mb - new_mb
    pct = (saved_mb / orig_mb * 100) if orig_mb > 0 else 0
    print(f"  Original:  {orig_mb:.2f} MB")
    print(f"  New:       {new_mb:.2f} MB")
    print(f"  Saved:     {saved_mb:.2f} MB ({pct:.0f}%)")
    print("=" * 60)


if __name__ == "__main__":
    main()
