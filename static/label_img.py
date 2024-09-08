from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm

# Function to add a label to the top-right of the image
def add_label_to_image(image, label, font_color="black", font_size=60, bold=True):
    # Load the standard font from matplotlib
    try:
        font_path = fm.findfont(fm.FontProperties(family="DejaVu Sans", weight="bold" if bold else "normal"))
        font = ImageFont.truetype(font_path, size=font_size)
    except IOError:
        # Fallback to default font if DejaVu Sans is not found
        print("DejaVu Sans font not found, using default font.")
        font = ImageFont.load_default()

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Get the width and height of the image
    img_width, img_height = image.size

    # Calculate text size using the textbbox method
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate position to place label at top right
    x_offset = img_width - text_width - 10  # 10 pixels padding from right edge
    y_offset = 10  # 10 pixels padding from top edge

    # Calculate the bounding box for the background rectangle
    left, top, right, bottom = draw.textbbox((x_offset, y_offset), label, font=font)

    # Draw a white rectangle behind the text for better visibility
    draw.rectangle((left - 5, top - 5, right + 5, bottom + 5), fill="white")

    # Draw the text label on the image at the top right
    draw.text((x_offset, y_offset), label, font=font, fill=font_color)

    return image

# Load the PNG image
image_path = 'strike.png'  # Replace with your image path
image = Image.open(image_path)

# Label to add
label = "Walk + Punch"

# Call the function to add the label to the image
image_with_label = add_label_to_image(image, label, font_color="black", font_size=140, bold=True)

# Save or display the image
image_with_label.show()  # Display the image
image_with_label.save('strike.png')  # Save the modified image
