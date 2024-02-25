from django.core.management.base import BaseCommand
from django.apps import apps

import os
import json
from rules.models import *


class Command(BaseCommand):

    help = "Initialize rules for Chroniques Oubliées"

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        if Capacity.objects.all():
            self.stdout.write(self.style.WARNING("Capacities already exists in DB !"))

        else:
            module_dir = apps.get_app_config("rules").path
            capacities_json_path = os.path.join(module_dir, "fixtures/capacities.json")

            f = open(capacities_json_path)
            capacities = json.load(f)

            self.stdout.write(self.style.SUCCESS("Creating Capacities"))

            for capacity in capacities:
                name = capacity["name"]
                slug = capacity["data"]["key"]
                description = capacity["data"]["description"]
                source = capacity["data"]["source"]
                if "Chroniques Oubliées DRS" in source:
                    source = "drs"
                elif "Chroniques Oubliées Compagnon" in source:
                    source = "compagnon"

                else:
                    source = ""

                spell = capacity["data"]["spell"]
                limited = capacity["data"]["limited"]
                

                Capacity.objects.create(
                    name=name,
                    slug=slug,
                    description=description,
                    source=source,
                    spell=spell,
                    limited=limited,
                )
                self.stdout.write(self.style.SUCCESS("{} created !".format(name)))


# for data_category in CATEGORIES:
#     category = Category.objects.create(
#         name=data_category["name"], active=data_category["active"]
#     )
#     for data_product in data_category["products"]:
#         product = category.products.create(
#             name=data_product["name"], active=data_product["active"]
#         )
#         for data_article in data_product["articles"]:
#             product.articles.create(
#                 name=data_article["name"],
#                 active=data_article["active"],
#                 price=data_article["price"],
#             )

# UserModel.objects.create_superuser(ADMIN_ID, "admin@oc.drf", ADMIN_PASSWORD)

# self.stdout.write(self.style.SUCCESS("All Done !"))
