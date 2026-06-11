from PIL import Image
import os

new_img_path = r'C:\Users\ALMANPY\.gemini\antigravity\brain\be6bada8-007e-4a1a-92de-43706eda91c3\media__1781183528357.jpg'
output_path = r'C:\Users\ALMANPY\Desktop\al-rawasi-site-main\static-site\images\clients\man-made-river.png'

def process_logo(src, dst):
    img = Image.open(src).convert("RGBA")
    
    # Remove white background
    datas = list(img.getdata())
    newData = []
    for item in datas:
        # If it's very close to white, make it transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    
    # Crop the logo (remove empty transparency)
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    # Resize to a reasonable height (e.g. 200px) while maintaining aspect ratio
    target_height = 200
    w, h = img.size
    new_w = int(w * (target_height / h))
    img = img.resize((new_w, target_height), Image.LANCZOS)
    
    img.save(dst, "PNG")
    print(f"Processed {src} -> {dst}")
    print(f"Size: {img.size}")

process_logo(new_img_path, output_path)
