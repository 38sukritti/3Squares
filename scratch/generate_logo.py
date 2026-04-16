from PIL import Image, ImageDraw

def generate_logo(output_path, foreground_color='#ffffff', background_color=None, scale=4, size_px=120):
    # Base size from SVG
    base_size = size_px
    size = base_size * scale
    
    # Create image
    if background_color:
        img = Image.new('RGB', (size, size), color=background_color)
    else:
        # Transparent background
        img = Image.new('RGBA', (size, size), color=(0, 0, 0, 0))
        
    draw = ImageDraw.Draw(img)
    
    # SVG coordinates and stroke widths
    # Outer Rect: x=10, y=10, w=100, h=100, stroke=12
    # Middle Rect: x=35, y=35, w=50, h=50, stroke=12
    # Inner Dot: x=60, y=60, w=1, h=1, stroke=16
    
    def draw_rect_path(draw, x, y, w, h, stroke_width, color):
        half = (stroke_width / 2)
        # Offset to match SVG layout
        draw.rectangle(
            [ (x - half) * scale, (y - half) * scale, (x + w + half) * scale, (y + h + half) * scale ],
            outline=color,
            width=int(stroke_width * scale)
        )

    # Outer Square
    draw_rect_path(draw, 10, 10, 100, 100, 12, foreground_color)
    
    # Middle Square
    draw_rect_path(draw, 35, 35, 50, 50, 12, foreground_color)
    
    # Inner Dot (Square)
    dot_size = 16
    cx, cy = 60.5, 60.5
    draw.rectangle(
        [ (cx - dot_size/2) * scale, (cy - dot_size/2) * scale, (cx + dot_size/2) * scale, (cy + dot_size/2) * scale ],
        fill=foreground_color
    )
    
    img.save(output_path)
    print(f"Logo saved to {output_path}")

if __name__ == "__main__":
    import os
    # 1. Regenerate Email Logo (White on Green, fixed thickness)
    email_logo = os.path.join('main', 'static', 'main', 'images', 'logo.png')
    generate_logo(email_logo, foreground_color='#ffffff', background_color='#0a2c1c', scale=4)
    
    # 2. Generate Favicon (Dark Green on Transparent)
    favicon_png = os.path.join('main', 'static', 'main', 'images', 'favicon.png')
    generate_logo(favicon_png, foreground_color='#0a2c1c', background_color=None, scale=8) # Higher res for favicon
