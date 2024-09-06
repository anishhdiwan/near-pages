from PIL import Image, ImageDraw, ImageFont

# Load the PNG image
image_path = 'image.png'  # Replace with your image path
image = Image.open(image_path)

# Load font (specify the path to a .ttf file if needed)
font = ImageFont.load_default()  # You can load a custom font by specifying the path

# Create a drawing object
draw = ImageDraw.Draw(image)

# Label to add
label = "Sample Label"
font_color = "black"

# Get the width and height of the image
img_width, img_height = image.size

# Calculate text size
text_width, text_height = draw.textsize(label, font=font)

# Calculate position to place label at bottom right
x_offset = img_width - text_width - 10  # 10 pixels padding from right edge
y_offset = img_height - text_height - 10  # 10 pixels padding from bottom edge

# Calculate the bounding box of the label for the background rectangle
left, top, right, bottom = draw.textbbox((x_offset, y_offset), label, font=font)

# Draw a white rectangle behind the text for better visibility
draw.rectangle((left - 5, top - 5, right + 5, bottom + 5), fill="white")

# Draw the text label on the image at the bottom right
draw.text((x_offset, y_offset), label, font=font, fill=font_color)

# Save or display the image
image.show()  # Display the image
image.save('image_with_label.png')  # Save the modified image
