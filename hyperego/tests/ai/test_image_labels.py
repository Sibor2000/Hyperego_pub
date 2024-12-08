import logging
from hyperego.ai.image_captioner import ImageCaptioner
from os import path

Logger = logging.getLogger(__name__)

def test_local_image():
    return
    image_path = path.join(path.dirname(__file__), "data", "rave.jpg")
    img = open(image_path, "rb").read()
    Logger.info(f"Captioning image: {image_path}")

    captioner = ImageCaptioner()
    try:
        caption = captioner.label(img)
        Logger.info(f"Caption: {caption}")
    except Exception as e:
        Logger.error(f"Error captioning image: {e}")
        assert False, f"Error captioning image: {e}"

    assert caption, f"Expected a caption, got {caption}"
    
    caption = caption.strip().lower()
    assert "man" in caption or "person" in caption, f"Expected label describing a person, got {caption}"