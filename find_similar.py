
import os
import argparse
from PIL import Image
import imagehash
import shutil

def find_similar_images(image_path, threshold):
    output_folder = "similar_images_found"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        source_hash = imagehash.phash(Image.open(image_path))
    except FileNotFoundError:
        print(f"Error: The file {image_path} does not exist.")
        return

    moved_files = []
    for filename in os.listdir("."):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            if os.path.abspath(filename) == os.path.abspath(image_path):
                continue
            try:
                other_hash = imagehash.phash(Image.open(filename))
                if source_hash - other_hash <= threshold:
                    shutil.move(filename, os.path.join(output_folder, filename))
                    moved_files.append(filename)
            except Exception as e:
                print(f"Could not process {filename}: {e}")

    if moved_files:
        print("Moved the following similar images:")
        for f in moved_files:
            print(f)
    else:
        print("No similar images found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and move similar images.")
    parser.add_argument("--image", required=True, help="The source image to compare against.")
    parser.add_argument("--threshold", type=int, default=5, help="Similarity threshold (lower is more similar).")
    args = parser.parse_args()
    find_similar_images(args.image, args.threshold)
