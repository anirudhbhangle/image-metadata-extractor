import logging
from pathlib import Path
from util.utilities import create_new_img, set_custom_timestamp, get_metadata
from constants.pythonConstants import SUPPORTED_EXTENSIONS

logger = logging.getLogger(__name__)

def clean_images():    
    # go to ROOT directory 
    # i.e. src folder
    base_dir = Path(__file__).resolve().parent.parent
    input_dir = base_dir / "input"
    output_dir = base_dir / "output"

    # mandatory input folder
    if not input_dir.is_dir():
        logger.error(f"Input folder not found in: {base_dir}")
        return
    # if output folder not present, create one
    output_dir.mkdir(exist_ok=True)
    
    #successful counter
    processed = 0
    for img in input_dir.iterdir():
        if img.suffix.lower() not in SUPPORTED_EXTENSIONS:
            logger.warning(f'File with non supported extension ignored: {img}')
            continue
        imgcpy = output_dir / img.name

        try:
            # create new copy of image without original metadata
            create_new_img(img,imgcpy)

            # TODO : add code for custom time here
            set_custom_timestamp(imgcpy)

            # save metadata of the copied image
            get_metadata(img,imgcpy)

            processed += 1
            logger.debug(f'Clean Image generated for {img.name}')
        except Exception as e:
            logger.error(f'Error occurred while processing file: {img}')

    logger.info(f'Successful Image counter: {processed}')
    logger.info(f'{processed} number of clean images have been generated in folder: {output_dir.name}')
    return;