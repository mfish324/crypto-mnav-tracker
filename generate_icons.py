"""
Generate PWA icons for the Crypto mNAV Tracker
Creates simple colored icons with text
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("PIL not available. Install with: pip install Pillow")

def create_icon(size, filename):
    """Create a simple icon with the app name"""
    # Create image with dark background and cyan border
    img = Image.new('RGB', (size, size), color='#0a0a0a')
    draw = ImageDraw.Draw(img)

    # Draw cyan border
    border_width = max(5, size // 20)
    draw.rectangle(
        [(0, 0), (size-1, size-1)],
        outline='#00ffff',
        width=border_width
    )

    # Draw centered text
    try:
        # Try to use a nice font
        font_size = size // 6
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageDraw.ImageFont.load_default()

    text = "mNAV\nTracker"

    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center the text
    position = ((size - text_width) // 2, (size - text_height) // 2)

    # Draw text in cyan
    draw.text(position, text, fill='#00ffff', font=font, align='center')

    # Save
    img.save(filename)
    print(f"Created {filename}")

if __name__ == "__main__":
    if PIL_AVAILABLE:
        import os

        # Create static directory if it doesn't exist
        os.makedirs('static', exist_ok=True)

        # Generate icons
        create_icon(192, 'static/icon-192.png')
        create_icon(512, 'static/icon-512.png')

        print("\nIcons generated successfully!")
        print("Your PWA is ready to deploy!")
    else:
        print("\nTo generate icons, install Pillow:")
        print("pip install Pillow")
        print("\nThen run: python generate_icons.py")
