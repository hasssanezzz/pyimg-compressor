# Image Compressor

Image Compressor is a simple command-line tool for resizing and compressing images. It allows you to resize images to different dimensions while maintaining their aspect ratio. Whether you need to prepare images for a website, reduce file sizes for faster loading, or create thumbnails, Image Compressor has you covered.

## Features

- Resize images to specific widths while preserving aspect ratio.
- Automatically compress images to reduce file size.
- Supports multiple input image formats (JPEG, PNG, etc.).
- CLI (Command-Line Interface) for easy and quick image compression.

## Getting Started

### Prerequisites

Before you start, make sure you have Python 3 and the following libraries installed:

- Pillow (PIL Fork)
- argparse (usually included in Python standard library)

You can install Pillow with pip:

```bash
pip install pillow
```

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/image-compressor.git
```

2. Change your working directory to the project folder:

```bash
cd image-compressor
```

### Usage

Image Compressor is a command-line tool. To compress an image, run the following command:

```bash
python3 src/main.py -i input_image.jpg -o output_filename -s "size1 size2 size3 ..."
```
replace `input_imgae.jpg` and `output_filename` to the desired file names.

### Command-line options

* `-i` or `--input`: Input image file path.
* `-o` or `--output`: Output filename prefix for resized images.
* `-s`  or `--sizes`: Sizes separated by spaces (e.g., "1000 750 500"). Default is "1000 750 500".

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
