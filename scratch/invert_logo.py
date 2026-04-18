from PIL import Image, ImageOps
import os

def invert_logo(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    r, g, b, a = img.split()
    
    # Invert RGB channels
    rgb = Image.merge("RGB", (r, g, b))
    inverted_rgb = ImageOps.invert(rgb)
    
    # Merge back with original alpha
    wr, wg, wb = inverted_rgb.split()
    final_img = Image.merge("RGBA", (wr, wg, wb, a))
    
    final_img.save(output_path)
    print(f"Saved inverted logo to {output_path}")

if __name__ == "__main__":
    logo_path = r"c:\Users\ASUS\Desktop\Dubai\main\static\main\images\logo.png"
    output_path = r"c:\Users\ASUS\Desktop\Dubai\main\static\main\images\logo_white.png"
    if os.path.exists(logo_path):
        invert_logo(logo_path, output_path)
    else:
        print(f"Logo not found at {logo_path}")
