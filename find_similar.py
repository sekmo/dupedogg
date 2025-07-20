#!/usr/bin/env python3

import os
import argparse
from PIL import Image
import imagehash
import shutil
from tqdm import tqdm

def find_similar_images(image_path, threshold, search_dir):
    output_folder = os.path.join(search_dir, "similar_images_found")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not os.path.isabs(image_path):
        source_image_full_path = os.path.join(search_dir, image_path)
    else:
        source_image_full_path = image_path

    try:
        source_hash = imagehash.phash(Image.open(source_image_full_path))
    except FileNotFoundError:
        print(f"Error: The file {source_image_full_path} does not exist.")
        return

    moved_files = []
    image_files = [
        filename for filename in os.listdir(search_dir)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))
    ]

    for filename in tqdm(image_files, desc="Finding similar images", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [ETA: {remaining}{postfix}]", mininterval=1.0):
            current_file_path = os.path.join(search_dir, filename)
            if os.path.abspath(current_file_path) == os.path.abspath(source_image_full_path):
                continue
            try:
                other_hash = imagehash.phash(Image.open(current_file_path))
                if source_hash - other_hash <= threshold:
                    shutil.move(current_file_path, os.path.join(output_folder, filename))
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
    parser.add_argument("--search-dir", required=True, help="The directory to search for images in.")
    args = parser.parse_args()
    find_similar_images(args.image, args.threshold, args.search_dir)
