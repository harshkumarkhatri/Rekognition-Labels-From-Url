import boto3
from PIL import Image
import io
import requests
from io import BytesIO


rek=boto3.client('rekognition')

url='https://res.cloudinary.com/harshkumarkhatri/image/upload/v1585238691/demo_images/download_1_y7osxe.jpg'


response = requests.get(url, stream=True)
response.raw.decode_content = True
image = Image.open(response.raw)
print(image)
buf=io.BytesIO()
image.save(buf,format='JPEG')
byte_in=buf.getvalue()
print(buf)
print(byte_in)


if byte_in:
    reponses=rek.detect_labels(
        Image={'Bytes':byte_in}
    )
    print(reponses)
    all_labels=[label['Name'] for label in reponses['Labels']]
    print(all_labels)