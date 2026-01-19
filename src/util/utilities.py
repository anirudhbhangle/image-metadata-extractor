import os
import time
import random
import logging
from datetime import datetime, timedelta
from PIL import Image


def remove_metadata(input_path, output_path):
    """
        Removes metadata and generates a completely new image
    """
    if not os.path.isfile(input_path):
        logging.error("Invalid filepath")
        raise FileNotFoundError("Input image not found")

    img = Image.open(input_path)

    # Convert to safe mode (drops profiles)
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGB")

    # Rebuild image from raw pixels (no metadata)
    clean_img = Image.new(img.mode, img.size)
    clean_img.putdata(list(img.getdata()))

    # quality=95 --> best quality , JPEG, WEBP
    # optimize=True --> image optimized for file size
    clean_img.save(
        output_path,
        quality=95,
        optimize=True
    )

    logging.info("High quality image generated")
    return ;

def set_custom_timestamp(file_path, dt = None):
    """
    Set accessed & modified timestamps (cross-platform) for the file.
    
    :param dt: Timestamp to be set (local time)
    """
    if dt:
        dt_ip = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
        ts = time.mktime(dt_ip.timetuple())
        os.utime(file_path, (ts, ts))
    else:
        logging.info("No date-time specified. Generating random timestamp")
        now = datetime.now()
        random_past_time = now - timedelta(
                                            days=random.randint(30, 900),
                                            seconds=random.randint(0, 86400)
                                        )
        ts = time.mktime(random_past_time.timetuple())
        os.utime(file_path, (ts, ts))

    return ;