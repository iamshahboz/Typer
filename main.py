# importing necessary libraries
import typer 
from datetime import datetime 
import requests
from config import API_URL
from helpers import url_query_params, get_image, save_image_to_filesystem


# initializing app instance
app = typer.Typer()

default_date = typer.Argument(
    datetime.now().strftime('%Y-%m-%d'),
    formats = ['%Y-%m-%d']

)
# setting Typer command with command decorator
@app.command()
def fetch_image(
    date:datetime = default_date, 
    save: bool=False,
    start: datetime = typer.Option(None),
    end: datetime = typer.Option(None)
    ):

    print("Sending API request ...")

    query_params = url_query_params(date, start, end)
    # dt = str(date.date())
    # url_for_date = f"{API_URL}&date={dt}"

    # getting the response from the url using request model
    # response = requests.get(url_for_date)
    response = requests.get(API_URL, params=query_params)

    # converting the result of the response into json and assigning to data
    data = response.json()

    if isinstance(data, dict):
        data = [data]
    
    for resp in data:

    
    # grabbing value for url key from that json object
        url = resp['url']
        title = resp['title']
        print('Fetching image')

    # getting the result
    # image_response = requests.get(url)
    # converting it to the BytesIO and opening with Pillows method
    # image = Image.open(BytesIO(image_response.content))

    # showing the image to the user
    # image.show()
        image = get_image(url)
        image.show()

    # it is checking if such directory exist in the current location
    # and if not creating the new one with that name
    # if save:
    #     if not IMAGE_DIR.exists():
    #         os.mkdir(IMAGE_DIR)
    #     image_name = f'{title}.{image.format}'
    #     image.save(IMAGE_DIR / image_name, image.format)

    # image.close()

        if save:
            save_image_to_filesystem(image, title)
        
        image.close


# calling the Typer instance
if __name__ == '__main__':
    app()

