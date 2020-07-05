import sys
import os.path
from PIL import Image

try:
    origin_folder = sys.argv[1]
    destination_folder = sys.argv[2]

    # check whether the directory to hold the PNG files exists otherwise create it
    if not os.path.exists(destination_folder):
        os.mkdir(f'{destination_folder}')

    os.chdir(origin_folder)
    cwd = os.listdir(os.getcwd())
    for file in cwd:
        os.chdir(os.path.dirname(os.getcwd()))
        os.chdir(origin_folder)
        # check for jpg files in the directory
        if file.endswith('.jpg'):
            img = Image.open(file)
            png_img = img
            os.chdir(os.path.dirname(os.getcwd()))
            os.chdir(destination_folder)
            png_img.save(f'{file.replace("jpg", "png")}', 'png')

# Let the user know that the origin directory does not exist
except FileNotFoundError:
    print(f'{sys.argv[1]} is not a directory that exists. Try again later.')
    exit(1)

