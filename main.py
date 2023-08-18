# importing necessary libraries
from io import BytesIO
import typer 
from datetime import datetime 
import requests
from config import API_URL, IMAGE_DIR
from PIL import Image
import os

# initializing app instance
app = typer.Typer()

default_date = typer.Argument(
    datetime.now().strftime('%Y-%m-%d'),
    formats = ['%Y-%m-%d']

)
# setting Typer command with command decorator
@app.command()
def fetch_image(date:datetime = default_date, save: bool=False):
    print("Sending API request ...")
    dt = str(date.date())
    url_for_date = f"{API_URL}&date={dt}"
    # getting the response from the url using request model
    response = requests.get(url_for_date)

    # converting the result of the response into json and assigning to data
    data = response.json()
    
    # grabbing value for url key from that json object
    url = data['url']
    title = data['title']
    print('Fetching image')

    # getting the result
    image_response = requests.get(url)
    # converting it to the BytesIO and opening with Pillows method
    image = Image.open(BytesIO(image_response.content))

    # showing the image to the user
    image.show()

    # it is checking if such directory exist in the current location
    # and if not creating the new one with that name
    if save:
        if not IMAGE_DIR.exists():
            os.mkdir(IMAGE_DIR)
        image_name = f'{title}.{image.format}'
        image.save(IMAGE_DIR / image_name, image.format)

    image.close()


# calling the Typer instance
if __name__ == '__main__':
    app()

