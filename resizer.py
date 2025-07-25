import os
from PIL import Image

input_folder = 'input_images'
output_folder = 'output_images'

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        try:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img = img.resize((400, 400))  # Resize

            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
            img.save(output_path)

            print(f" Saved: {output_path}")
        except Exception as e:
            print(f" Error with {filename}: {e}")
