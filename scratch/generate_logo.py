from PIL import Image, ImageDraw

def generate_logo(output_path, background_color='#0a2c1c', scale=4):
    # Base size from SVG
    base_size = 120
    size = base_size * scale
    
    # Create image
    img = Image.new('RGB', (size, size), color=background_color)
    draw = ImageDraw.Draw(img)
    
    white = (255, 255, 255)
    
    # SVG coordinates and stroke widths
    # Outer Rect: x=10, y=10, w=100, h=100, stroke=12
    # Middle Rect: x=35, y=35, w=50, h=50, stroke=12
    # Inner Dot: x=60, y=60, w=1, h=1, stroke=16 (Center x=60.5, y=60.5?)
    
    def draw_rect_path(draw, x, y, w, h, stroke_width, color):
        # Draw stroke aligned to center of path
        # x, y = top-left of path
        # Pillow draws 'outline' inside or outside?
        # Standard draw.rectangle with width draws inside.
        # To match SVG center-aligned stroke:
        half = stroke_width / 2
        draw.rectangle(
            [ (x - half) * scale, (y - half) * scale, (x + w + half) * scale, (y + h + half) * scale ],
            outline=color,
            width=int(stroke_width * scale)
        )

    # Outer Square
    draw_rect_path(draw, 10, 10, 100, 100, 12, white)
    
    # Middle Square
    draw_rect_path(draw, 35, 35, 50, 50, 12, white)
    
    # Inner Dot (Square)
    # The SVG used: <rect x="60" y="60" width="1" height="1" stroke-width="16"/>
    # This is effectively a 16x16 square centered at 60.5, 60.5
    dot_size = 16
    cx, cy = 60.5, 60.5
    draw.rectangle(
        [ (cx - dot_size/2) * scale, (cy - dot_size/2) * scale, (cx + dot_size/2) * scale, (cy + dot_size/2) * scale ],
        fill=white
    )
    
    img.save(output_path, "PNG")
    print(f"Logo saved to {output_path}")

if __name__ == "__main__":
    import os
    target = os.path.join('main', 'static', 'main', 'images', 'logo.png')
    generate_logo(target)
