# image-metadata-extractor
Mini code which reconstructs an image without its initial metadata

### Usage

Pre-requisite:
- Install Python and the python modules included in requirements.txt
- Create a folder named "input" in src folder

Input:
- Add all images to be cleaned in input folder in root directory
    e.g. "src/input/image.jpg"

Input Image Formats Supported:
    .jpg, .jpeg, .png, .webp, .bmp, .tiff

Output:
- All new images will be saved in output folder in root directory.
    e.g. "src/output/image.jpg"
- If no output folder is present, a new one will be created.
- All metadata fetched from source image will be saved to a text file with same name.
    e.g. "src/output/image.txt"
