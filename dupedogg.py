#!/usr/bin/env python3

import os
import argparse
from PIL import Image
import imagehash
import shutil
from tqdm import tqdm
import multiprocessing
import functools

def process_image(source_hash, threshold, output_folder, search_dir, filename):
    current_file_path = os.path.join(search_dir, filename)
    try:
        other_hash = imagehash.phash(Image.open(current_file_path))
        if source_hash - other_hash <= threshold:
            shutil.move(current_file_path, os.path.join(output_folder, filename))
            return filename
    except Exception as e:
        print(f"Could not process {filename}: {e}")
    return None

def find_similar_images(image_path, threshold, search_dir):
    output_folder = os.path.join(search_dir, "similar_images_found")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    source_image_full_path = image_path
    if not source_image_full_path:
        # If --image is not provided, try to find reference.jpg or reference.png
        ref_jpg = os.path.join(search_dir, "reference.jpg")
        ref_png = os.path.join(search_dir, "reference.png")
        if os.path.exists(ref_jpg):
            source_image_full_path = ref_jpg
        elif os.path.exists(ref_png):
            source_image_full_path = ref_png
        else:
            print("Error: No source image provided and no 'reference.jpg' or 'reference.png' found in the search directory.")
            return
    else:
        # Only join with search_dir if user provided --image and it's not an absolute path
        if not os.path.isabs(source_image_full_path):
            source_image_full_path = os.path.join(search_dir, source_image_full_path)

    try:
        source_hash = imagehash.phash(Image.open(source_image_full_path))
    except FileNotFoundError:
        print(f"Error: The file {source_image_full_path} does not exist.")
        return

    image_files = [
        filename for filename in os.listdir(search_dir)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')) and
           os.path.abspath(os.path.join(search_dir, filename)) != os.path.abspath(source_image_full_path)
    ]

    moved_files = []
    # Use multiprocessing to speed up image processing
    with multiprocessing.Pool() as pool:
        func = functools.partial(process_image, source_hash, threshold, output_folder, search_dir)
        for result in tqdm(pool.imap_unordered(func, image_files), total=len(image_files),
                           desc="Finding similar images", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [ETA: {remaining}{postfix}]", mininterval=1.0):
            if result:
                moved_files.append(result)

    if moved_files:
        print("Moved the following similar images:")
        for f in moved_files:
            print(f)
    else:
        print("No similar images found.")

def main():
    parser = argparse.ArgumentParser(description="Find and move similar images.")
    parser.add_argument("--image", help="The source image to compare against. If not provided, will look for 'reference.jpg' or 'reference.png' in the search directory.")
    parser.add_argument("--threshold", type=int, default=5, help="Similarity threshold (lower is more similar).")
    parser.add_argument("--search-dir", default="./", help="The directory to search for images in. Defaults to current directory.")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.3")
    args = parser.parse_args()
    find_similar_images(args.image, args.threshold, args.search_dir)

if __name__ == "__main__":
    main()
