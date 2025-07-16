# Similar Image Finder

A Python script to find and move images that are visually similar to a source image.

## How it works

This script uses a perceptual hashing algorithm to find images that are visually similar to a source image. It then moves the similar images to a `similar_images_found` directory.

## Installation

1.  Clone this repository.
2.  Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
3.  Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
4.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the script, run the following command from the project's root directory:

```bash
python3 find_similar.py --image YOUR_IMAGE.JPG --threshold 5
```

### Arguments

*   `--image`: The path to the source image to compare against.
*   `--threshold`: The similarity threshold. A lower number means more similar. The default is 5.

The script will create a `similar_images_found` directory and move any similar images into it.
