import os
from PIL import Image

# Function to crop the image while maintaining the aspect ratio
# def crop_image(image, crop_percentage):
#     width, height = image.size
#     crop_width = int(width * crop_percentage)
#     crop_height = int(height * crop_percentage)
    
#     left = crop_width // 2
#     upper = crop_height // 2
#     right = width - (crop_width // 2)
#     lower = height - (crop_height // 2)
    
#     # Crop the image
#     cropped_image = image.crop((left, upper, right, lower))
#     return cropped_image

def crop_image(image, crop_percentage):
    width, height = image.size
    crop_width = int(width * crop_percentage)
    
    # Keep the full height, no cropping
    left = 0  # Start from the left
    upper = 0  # No change in vertical position
    right = crop_width  # Keep the percentage of the width starting from the left
    lower = height  # Full height
    
    # Crop the image
    cropped_image = image.crop((left, upper, right, lower))
    return cropped_image


# Function to process all PNG images in a directory
def crop_images_in_directory(directory, crop_percentage):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            file_path = os.path.join(directory, filename)
            
            with Image.open(file_path) as img:
                # Crop the image
                cropped_img = crop_image(img, crop_percentage)
                
                # Save the cropped image
                cropped_img.save(os.path.join(directory, f"cropped_{filename}"))
                print(f"Cropped image saved as: cropped_{filename}")

# Main function to get user input and run the script
if __name__ == "__main__":
    directory = input("Enter the directory path containing PNG images: ")
    crop_percentage = float(input("Enter the crop percentage (e.g., 0.1 for 10% crop): "))
    
    crop_images_in_directory(directory, crop_percentage)
    print("All images cropped successfully!")
