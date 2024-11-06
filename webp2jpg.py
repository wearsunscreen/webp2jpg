
import os
import argparse
from PIL import Image

def convert_webp_to_jpg(webp_path, jpg_path, quality):
    with Image.open(webp_path) as img:
        img.convert("RGB").save(jpg_path, "JPEG", quality=quality)

def main():
    parser = argparse.ArgumentParser(description="Convert WEBP files to JPG with specified compression level.")
    parser.add_argument("input_file", help="Path to the input file containing list of WEBP files.")
    parser.add_argument("--quality", type=int, default=80, help="Compression level for JPG (default: 80).")
    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        webp_files = file.read().splitlines()

    for webp_file in webp_files:
        if os.path.exists(webp_file):
            jpg_file = os.path.splitext(webp_file)[0] + ".jpg"
            convert_webp_to_jpg(webp_file, jpg_file, args.quality)
            print(f"Converted {webp_file} to {jpg_file} with quality {args.quality}.")
        else:
            print(f"File {webp_file} does not exist.")

if __name__ == "__main__":
    main()