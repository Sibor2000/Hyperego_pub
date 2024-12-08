from g4f.client import Client
from g4f import Provider, models
import requests

class ImageCaptioner:
    def __init__(self):
        self.client = Client()

    def label(self, image) -> str:
        # If the image is a URL, we need to create a request object that's readable
        try:
            response = requests.get(image, stream=True)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return "Could not retrieve image"

        response = self.client.chat.completions.create(
            model=models.gemini_pro,
            provider=Provider.Blackbox,
            messages=[
                {
                    "role": "system",
                    "content": "You are an image analyzer. Provide a description of the image in one sentence (single line response and nothing else)."
                }
            ],
            image=response.raw
        )
        return response.choices[0].message.content