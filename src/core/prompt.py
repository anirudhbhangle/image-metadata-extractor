import logging
from pathlib import Path
from util.utilities import copy_img_without_metadata, set_custom_timestamp, get_metadata

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff")

logging.basicConfig(filename='./logs/app.log', level=logging.DEBUG, format='LOG.%(levelname)s: %(message)s')

def no_prompt():    
    # go to ROOT directory 
    # i.e. src folder
    base_dir = Path(__file__).resolve().parent.parent
    input_dir = base_dir / "input"
    output_dir = base_dir / "output"

    # mandatory input folder
    if not input_dir.is_dir():
        logging.error(f"Input folder not found: {input_dir}")
        return
    # if output folder not present, create one
    output_dir.mkdir(exist_ok=True)
    
    #successful counter
    processed = 0
    for img in input_dir.iterdir():
        if img.suffix.lower() not in SUPPORTED_EXTENSIONS:
            logging.warning(f'Image with non supported extension ignored: {img}')
            continue
        imgcpy = output_dir / img.name

        try:
            # create new copy of image without original metadata
            copy_img_without_metadata(img,imgcpy)

            # TODO : add code for custom time here
            set_custom_timestamp(imgcpy)

            # save metadata of the copied image
            get_metadata(img,imgcpy)

            processed += 1
            logging.debug(f'Clean Image generated for {img.name}')
        except Exception as e:
            logging.error(f'Error occurred while processing file: {img}')

    logging.info(f'Successful Image counter: {processed}')

    print(f'{processed} number of cleaned images have been created in folder: {output_dir.name}')

    return