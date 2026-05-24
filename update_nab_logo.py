from PIL import Image, ImageOps
import os

input_path = r'C:\Users\ALMANPY\Desktop\al-rawasi-site-main\static-site\images\clients\nab-bank.png'
# The new image provided by user is media__1779647008281.jpg
# But I'll first try to make a better version using the provided JPG
new_img_path = r'C:\Users\ALMANPY\.gemini\antigravity\brain\e7919463-4cf8-454f-95fb-64a06af9abb2\media__1779647008281.jpg'
output_path = r'C:\Users\ALMANPY\Desktop\al-rawasi-site-main\static-site\images\clients\nab-bank.png'

def process_logo(src, dst):
    img = Image.open(src).convert("RGBA")
    
    # Remove white background
    datas = img.getdata()
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

process_logo(new_img_path, output_path)
