import pandas as pd
from django.core.management.base import BaseCommand
from external.get_products import (
    get_list_of_all_shoper_product_sku,
)
from products.models import Product


CSV_PATH = "Images.csv"
df = pd.read_csv(CSV_PATH, sep=";")


def generate_missing_sku_to_copy(df, from_lang):
    """
    Compares Shoper's DB for number of SKU code with language_tag extension.
    SKU123PL
    """
    # outcome_list = []
    # This creates a list of all SKU that we should have in Shoper's DB with desired language tag at the end of SKU Code.
    sku_parrents = [f"{row.product_code}{from_lang[3:]}" for row in df.itertuples()]
    # This creates a list of all SKU codes with specified language tag that we have on Shoper's DB.
    # This method actually returns list, Do I double loop here to create same output?
    sku_api_response = get_list_of_all_shoper_product_sku(from_lang[3:])
    # outcome_list = [sku[:-2] for sku in sku_parrents if sku not in sku_api_response]
    return (sku[:-2] for sku in sku_parrents if sku not in sku_api_response)


def validate_databases(from_lang):
    """
    Validates that products number in SHOPER DB for specified language tag is equal to product number from CSV file.
    CSV serves here as a indicator of state of DB before dupliaction process.
    With this method I want to check if copying process happend for all products from file.
    """

    sku_parrents = [
        row.shoper_sku
        for row in Product.objects.filter(shoper_sku__endswith=f"{from_lang[3:]}")
    ]
    sku_api_response = get_list_of_all_shoper_product_sku(from_lang[3:])
    outcome_list = [sku[:-2] for sku in sku_parrents if sku not in sku_api_response]

    if len(sku_parrents) == len(sku_api_response):
        print("Databases are equal")
        print(f"PARENT:{len(sku_parrents)} | FROM API:{len(sku_api_response)}")
    elif len(sku_parrents) > len(sku_api_response):
        print(
            "Parrent file is bigger then Shoper's DB state. Some products weren't copied."
        )
        print(f"PARENT:{len(sku_parrents)} | FROM API:{len(sku_api_response)}")
    elif len(sku_parrents) < len(sku_api_response):
        print("Error! API response from DB inidicates that there are duplicated SKUs")
        print(f"PARENT:{len(sku_parrents)} | FROM API:{len(sku_api_response)}")

    return outcome_list


class Command(BaseCommand):
    """Main class for command object that imports images from shoper."""

    def add_arguments(self, parser):
        parser.add_argument(
            "from_language",
            type=str,
            help="From ",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""

        from_lang = kwargs["from_language"]

        print(validate_databases(from_lang))
