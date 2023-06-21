import datetime
import configparser
from base64 import b64decode
import webbrowser
import openai
from openai.error import InvalidRequestError
from fastapi import APIRouter

def generate_image(prompt, num_image=1, size='1024x1024', output_format='url'):
   
    try:
        images = []
        response = openai.Image.create(
            prompt=prompt,
            n=num_image,
            size=size,
            response_format=output_format
        )
        if output_format == 'url':
            for image in response['data']:
                images.append(image.url)
        elif output_format == 'b64_json':
            for image in response['data']:
                images.append(image.b64_json)
        return {'created': datetime.datetime.fromtimestamp(response['created']), 'images': images}
    except InvalidRequestError as e:
        print(e)