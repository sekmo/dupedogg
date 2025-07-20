# Similar Image Finder

A Python script to find and move images that are visually similar to a source image.

## How it works

This script uses a perceptual hashing algorithm to find images that are visually similar to a source image. It then moves the similar images to a `similar_images_found` directory.

## Installation

1.  **Clone this repository:**
    ```bash
    git clone <repository-url> similar_images_gemini
    cd similar_images_gemini
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Make the script executable:**
    ```bash
    chmod +x find_similar.py
    ```

## Making the Script a Global Command

To make the script available as a command from anywhere in your terminal, you can create a launcher script.

1.  **Ensure `~/bin` is in your PATH.** Add the following line to your `~/.zshrc` or `~/.bash_profile` if it's not already there:
    ```bash
    export PATH="$HOME/bin:$PATH"
    ```

2.  **Create a launcher script** at `~/bin/find_similar` with the following content:
    ```bash
    #!/bin/zsh

    # The absolute path to the directory where the script is located
    SCRIPT_DIR="/Users/francescomari/similar_images_gemini"

    # Activate the virtual environment, run the python script with all passed arguments
    (cd "$SCRIPT_DIR" && source venv/bin/activate && python3 find_similar.py "$@")
    ```

3.  **Make the launcher script executable:**
    ```bash
    chmod +x ~/bin/find_similar
    ```

4.  **Refresh your shell session:**

    Open a new terminal window or run `source ~/.zshrc`.

## Usage

Now you can run the command from any directory like this:

```bash
find_similar --image YOUR_IMAGE.JPG --threshold 5
```

### Arguments

*   `--image`: (Optional) The path to the source image to compare against. If not provided, the script will look for `reference.jpg` or `reference.png` in the `--search-dir` directory.
*   `--search-dir`: The directory to search for images in. This is also where the `similar_images_found` directory will be created.
*   `--threshold`: The similarity threshold, which represents the maximum allowed Hamming distance between two image hashes. A lower number means the images must be *more* similar. The default is 5.
    *   A threshold of `0` means the images must be absolutely identical.
    *   A threshold of `1` to `10` is good for finding near-identical images (e.g., minor edits, watermarks, or format changes).
    *   Values above `10` may start to identify images that are only loosely related. There is no theoretical maximum, but a very high value (e.g., `100`) would likely treat all images as similar.

The script will create a `similar_images_found` directory in the current working directory and move any similar images into it.

## Releasing a New Version

To release a new version of `dupedogg`, follow these steps:

1.  **Update the Application (`dupedogg` repo)**
    *   Make your code changes in the `dupedogg` directory.
    *   Update the version number in `setup.py`.
    *   Commit your changes (`git commit -m "Your detailed commit message"`).
    *   Create a new version tag (e.g., `git tag v0.2.0`).
    *   Push your commits and the new tag to GitHub (`git push && git push origin v0.2.0`).

2.  **Update the Homebrew Tap (`homebrew-dupedogg` repo)**
    *   Calculate the `sha256` checksum for the new release asset (e.g., `curl -sL https://github.com/sekmo/dupedogg/archive/refs/tags/v0.2.0.tar.gz | shasum -a 256`).
    *   Edit the `dupedogg.rb` file in the `homebrew-dupedogg` repository.
    *   Change the `url` to point to the new version tag.
    *   Replace the old `sha256` with the new one.
    *   Commit and push these changes to the `homebrew-dupedogg` repository.