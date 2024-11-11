from PIL import Image
import os

def convert_png_to_jpg(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            # Construct the full file path
            input_path = os.path.join(input_folder, filename)
            
            # Open the PNG image
            with Image.open(input_path) as img:
                # Convert the image to RGB, which removes the alpha channel if present
                rgb_img = img.convert("RGB")
                
                # Construct the output file path with .jpg extension
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")
                
                # Save the image as a JPG file
                rgb_img.save(output_path, "JPEG")
                print(f"Converted {filename} to {os.path.basename(output_path)}")

if __name__ == "__main__":
    input_folder = "C:\\Users\\cbgno\\OneDrive\\Desktop\\SURP\\test_nn\\data\\in_out_dataset\\train\\move_out"  # Replace with your PNG folder path
    output_folder = "C:\\Users\\cbgno\\OneDrive\\Desktop\\SURP\\test_nn\\data\\in_out_dataset\\train\\move_out_jpg"  # Replace with the folder where you want to save JPGs
    convert_png_to_jpg(input_folder, output_folder)
