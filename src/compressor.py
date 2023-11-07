from PIL import Image


class ImgCompressor:
    """
    A class for compressing and resizing images.

    This class provides methods for resizing an image to multiple sizes while maintaining the aspect ratio
    and saving the resized images with specific filenames.

    Methods:
        compress(img_src, sizes):
            Resize an image to multiple sizes while maintaining the aspect ratio.

        write_imgs(imgs, sizes, output_name):
            Save resized images to files with specific names.
    """

    @staticmethod
    def compress(img_src: str, sizes: list[int]) -> list[Image.Image]:
        """
        Resize an image to multiple sizes while maintaining the aspect ratio.

        Args:
            img_src (str): The path to the input image file.
            sizes (list[int]): A list of target widths for the resized images.

        Returns:
            list[Image.Image]: A list of resized image objects.

        Example:
            To resize 'img.jpg' to multiple sizes:
            - sizes = [1000, 750, 500]
            - results = ImgCompressor.compress('img.jpg', sizes)
            The results will be a list of resized image objects.
        """
        results = []
        img = Image.open(img_src)
        for size in sizes:
            aspect_ratio = float(img.height) / float(img.width)
            new_height = int(size * aspect_ratio)

            resized_img = img.resize((size, new_height), Image.LANCZOS)
            results.append(resized_img)

        return results

    @staticmethod
    def write_imgs(imgs: list[Image.Image], sizes: list[int], output_name: str) -> None:
        """
        Save resized images to files with specific names.

        Args:
            imgs (list[Image.Image]): A list of resized image objects.
            sizes (list[int]): A list of target widths corresponding to the resized images.
            output_name (str): The prefix for the output file names.

        Returns:
            None

        Example:
            To save the resized images with filenames like 'output_name_1000.jpg', 'output_name_750.jpg', etc.:
            - ImgCompressor.write_imgs(results, sizes, 'output_name')
        """
        for i, size in enumerate(sizes):
            imgs[i].save(f'{output_name}_{size}.jpg')
