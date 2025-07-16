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

## Making the Script a Global Command (for zsh)

To make the script available as a command from anywhere in your terminal, follow these steps:

1.  **Make the script executable:**
    ```bash
    chmod +x find_similar.py
    ```

2.  **Add the script's directory to your `PATH`:**
    ```bash
    echo 'export PATH="/Users/francescomari/similar_images_gemini:$PATH"' >> ~/.zshrc
    ```

3.  **Refresh your shell session:**

    Open a new terminal window or run `source ~/.zshrc`.

Now you can run the command from any directory like this:

```bash
find_similar.py --image YOUR_IMAGE.JPG --threshold 5
```



To use the script, run the following command from the project's root directory:

```bash
python3 find_similar.py --image YOUR_IMAGE.JPG --threshold 5
```

### Arguments

*   `--image`: The path to the source image to compare against.
*   `--threshold`: The similarity threshold, which represents the maximum allowed Hamming distance between two image hashes. A lower number means the images must be *more* similar. The default is 5.
    *   A threshold of `0` means the images must be absolutely identical.
    *   A threshold of `1` to `10` is good for finding near-identical images (e.g., minor edits, watermarks, or format changes).
    *   Values above `10` may start to identify images that are only loosely related. There is no theoretical maximum, but a very high value (e.g., `100`) would likely treat all images as similar.

The script will create a `similar_images_found` directory and move any similar images into it.
