import requests
import time
import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from images.models import Image


# Get private data fron .env variable
load_dotenv()
SHOPER_LOGIN = os.environ.get("SHOPER_LOGIN")
SHOPER_PASSWORD = os.environ.get("SHOPER_PASSWORD")
SHOPER_STORE = os.environ.get("SHOPER_STORE")


# Get a token by login to your store.
def get_token():
    """Generates fresh token from SHOPER API."""

    url_login = f"https://{SHOPER_STORE}/webapi/rest/auth"
    response = requests.post(url_login, auth=(SHOPER_LOGIN, SHOPER_PASSWORD))
    access_token = response.json().get("access_token")
    return access_token


# Get instance of TOKEN.
TOKEN = get_token()


# Get number of pages from image list API.
def get_number_of_image_pages():
    """Get number of all image pages from SHOPER api"""

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    pages = res.get("pages")

    return pages


def copy_all_product_images_from_shoper_api():
    """Copy all images from SHOPER Api and saves them as Image objects in DB."""

    for x in range(1, get_number_of_image_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        for i in items:
            # print(i) # for debuging!
            image = Image.objects.create(
                shoper_id=i.get("gfx_id"),
                shoper_product_id=i.get("product_id"),
                shoper_main=i.get("main"),
                order=i.get("order"),
                shoper_link=f'https://{SHOPER_STORE}/userdata/public/gfx/{i.get("gfx_id")}/{i.get("name")}.jpg',
                shoper_unic=i.get("unic_name"),
                hidden=i.get("hidden"),
                extension=f'{i.get("extension")}',
            )
            image.save()
            time.sleep(1)
            print(f"Object with ID:{image.id} Created")

    return


def clear_data():
    Image.objects.all().delete()


class Command(BaseCommand):
    """Main class for command object that imports images from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        clear_data()
        self.stdout.write(
            self.style.SUCCESS(
                f"Database cleared Image objects count: {Image.objects.all().count()}"
            )
        )
        copy_all_product_images_from_shoper_api()
        self.stdout.write(self.style.SUCCESS("Database available!"))
