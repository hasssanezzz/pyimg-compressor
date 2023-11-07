import argparse
from compressor import ImgCompressor

def main():
    """
    Main function to compress an image to multiple sizes and save the resized images.

    This script takes an input image, resizes it to specified sizes while maintaining the aspect ratio,
    and saves the resized images with the provided output filename.

    Command-line Arguments:
        -i, --input: Input image file path.
        -o, --output: Output filename prefix for resized images.
        -s, --sizes: Sizes separated by spaces. Default is '1000 750 500'.

    Returns:
        None
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input_img', type=str, help='Input image to compress', required=True)
    parser.add_argument('-o', '--output', dest='output_filename', type=str, help='Output files name', required=True)
    parser.add_argument('-s', '--sizes', dest='sizes', type=str, help='Sizes separated by spaces', default='1000 750 500')

    args = parser.parse_args()

    sizes = [int(size_str) for size_str in args.sizes.split(' ')]

    results = ImgCompressor.compress(args.input_img, sizes)
    ImgCompressor.write_imgs(results, sizes, args.output_filename)

if __name__ == '__main__':
    main()
