from django.core.management.base import BaseCommand
from django.apps import apps
from django.utils.text import slugify

import os
import json
from items.models import Item


class Command(BaseCommand):

    help = "Initialize items for Chroniques Oubliées"

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        if Item.objects.all():
            self.stdout.write(self.style.WARNING("Some items already exists in DB !"))

        else:
            _Item_created = 0
            _Item_total = 0

            module_dir = apps.get_app_config("items").path
            items_json = os.path.join(module_dir, "fixtures/items.json")

            f_items = open(items_json)

            items = json.load(f_items)

            self.stdout.write(self.style.NOTICE("Importing Items..."))

            for item in items:
                _Item_total += 1

            for item in items:
                pass
                name = item["name"]
                slug = slugify('name')
                
                img_path = item[img]
                img = img_path.split("/")[-1]
                
                source = item["data"]["source"]
                if "Chroniques Oubliées DRS" in source:
                    source = "drs"
                elif "Chroniques Oubliées Compagnon" in source:
                    source = "compagnon"
                else:
                    source = ""
                
                subtype = 
                trait = 
                rarity = 
                unique = 
                price = 
                value = 

                equipment = 
                stackable = 
                qty = 
                stacksize = 
                deleteWhen0 = 
                tailored = 
                two_handed = 
                consumable = 

                description = 
                protection = 
                def_tot = 
                def_base = 
                def_bonus = 
                dr = 
                dr_value = 

                weapon = 
                dmg_tot = 
                dmg_base = 
                dmg_stat = 
                dmg_bonus = 
                mod = 
                skill = 
                skillBonus = 
                critrange = 

                ranged = 
                range = 
                reloadable = 
                reload = 
                bow = 
                crossbow = 
                powder = 
                throwing = 
                sling = 
                spell = 

                equipable = 
                worn = 
                slot = 
                access =
                # slug = profile["data"]["key"]
                # description = profile["data"]["description"]
                # source = profile["data"]["source"]
                # if "Chroniques Oubliées DRS" in source:
                #     source = "drs"
                # elif "Chroniques Oubliées Compagnon" in source:
                #     source = "compagnon"

                # else:
                #     source = ""

                # dv = profile["data"]["dv"]
                # spellcasting = profile["data"]["spellcasting"].upper()
                # mpfactor = profile["data"]["mpfactor"]

                # _Profile = Profile.objects.create(
                #     name=name,
                #     slug=slug,
                #     description=description,
                #     source=source,
                #     dv=dv,
                #     spellcasting=spellcasting,
                #     mpfactor=mpfactor,
                # )
                # _Item_created += 1

            self.stdout.write(
                self.style.NOTICE("{} Items in files...".format(_Item_total))
            )
            self.stdout.write(
                self.style.SUCCESS("{} items created !".format(_Item_created))
            )
