import datetime
import configparser
from base64 import b64decode
import webbrowser
import openai
from openai.error import InvalidRequestError
import requests
import cv2
from PIL import Image
import io
import generimg
from fastapi import APIRouter, UploadFile, File
from addobj import add_obj
import uvicorn

router = APIRouter()



config=configparser.ConfigParser()
config.read('credential.ini')
API_KEY=config['openai']['APIKEY']
openai.api_key=API_KEY

SIZES=('1024x1024','512x512','256,256')


def makebackground():
    

    response = generimg.generate_image(" A stage under the ocean. The stage should be in the 510x312 coordinates of the picture.", num_image=1, size=SIZES[0])
    print(response)

    myurl=response['images'][0]
    
    response = requests.get(myurl)

    image = Image.open(io.BytesIO(response.content))

    image.save("resim.jpg")

    


"Create an image where a perfume bottle is placed on an ocean-stage background. The perfume bottle should be visually appealing and well-integrated with the background. The ocean-stage should have a serene and captivating atmosphere, with gentle waves and a beautiful horizon. The colors and lighting should be harmonious and evoke a sense of tranquility. Be creative and imaginative in bringing together these elements to produce a visually stunning image."
