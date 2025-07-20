# DupeDog

A command-line tool to find and move images that are visually similar to a source image.

## How it works

This tool uses a perceptual hashing algorithm to find images that are visually similar to a source image. It then moves the similar images to a `similar_images_found` directory.

## Installation

### Using Homebrew (Recommended)

```bash
brew install sekmo/dupedogg/dupedogg
```

### Manual Installation

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/sekmo/dupedogg.git
    cd dupedogg
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Install the package:**
    ```bash
    pip install .
    ```

## Usage

```bash
dupedogg [--search-dir <directory>] [--image <image_file>] [--threshold <number>]
```

### Arguments

*   `--search-dir`: (Optional) The directory to search for images in. Defaults to the current directory. This is also where the `similar_images_found` directory will be created.
*   `--image`: (Optional) The path to the source image to compare against. If not provided, dupedogg will look for `reference.jpg` or `reference.png` in the search directory.
*   `--threshold`: The similarity threshold, which represents the maximum allowed Hamming distance between two image hashes. A lower number means the images must be *more* similar. The default is 5.
    *   A threshold of `0` means the images must be absolutely identical.
    *   A threshold of `1` to `10` is good for finding near-identical images (e.g., minor edits, watermarks, or format changes).
    *   Values above `10` may start to identify images that are only loosely related. There is no theoretical maximum, but a very high value (e.g., `100`) would likely treat all images as similar.

Dupedogg will create a `similar_images_found` directory in the search directory and move any similar images into it.

### Examples

Run dupedogg in the current directory (looks for `reference.jpg` or `reference.png`):
```bash
dupedogg
```

Find images similar to a specific reference image:
```bash
dupedogg --search-dir ./photos --image reference.jpg --threshold 5
```

Find images similar to `reference.jpg` or `reference.png` in a specific directory:
```bash
dupedogg --search-dir ./photos --threshold 3
```

Check version:
```bash
dupedogg --version
```

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