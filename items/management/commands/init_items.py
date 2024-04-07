from django.core.management.base import BaseCommand
from django.apps import apps
from django.utils.text import slugify

import os
import json
from items.models import Item
from rules.choices import ItemTrait, Source


class Command(BaseCommand):

    help = "Initialize items for Chroniques Oubliées"

    def if_null(self, value, default):
        if value is None:
            return default
        elif value != "":
            return value
        else:
            return default

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))
        Item.objects.all().delete()

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

            # Get trait object
            _weapon = ItemTrait.objects.get(name="Arme")
            _equipment = ItemTrait.objects.get(name="Équipement")
            _protection = ItemTrait.objects.get(name="Protection")
            _ranged = ItemTrait.objects.get(name="À distance")
            _effects = ItemTrait.objects.get(name="Effet magique")

            _drs = Source.objects.get(name="CO DRS")
            _compagnon = Source.objects.get(name="CO Compagnon")
            _vengeance = Source.objects.get(name="Vengeance")
            _autre = Source.objects.get(name="Autre")

            for item in items:
                _Item_total += 1

            for item in items:
                name = item["name"]
                slug = slugify(name)
                img_name = item["img"].split("/")[-1]
                img = "icons/items/" + img_name

                source = item["data"]["source"]
                if "Chroniques Oubliées DRS" in source:
                    source = _drs
                elif "Chroniques Oubliées Compagnon" in source:
                    source = _compagnon
                elif "Vengeance" in source:
                    source = _vengeance
                else:
                    source = _autre

                subtype = item["data"]["subtype"]
                if subtype == "trapping":
                    subtype = "equipment"

                traits = []
                if item["data"]["properties"]["weapon"]:
                    traits.append(_weapon)

                if item["data"]["properties"]["equipment"]:
                    traits.append(_equipment)

                if item["data"]["properties"]["protection"]:
                    traits.append(_protection)

                if item["data"]["properties"]["ranged"]:
                    traits.append(_ranged)

                if item["data"]["properties"]["effects"]:
                    traits.append(_effects)

                rarity = item["data"]["rarity"]
                unique = item["data"]["properties"]["unique"]
                price = item["data"]["price"]
                value = item["data"]["value"]

                equipment = item["data"]["properties"]["equipment"]
                stackable = item["data"]["properties"]["stackable"]
                qty = item["data"]["qty"]
                stacksize = self.if_null(item["data"]["stacksize"], 1)
                deleteWhen0 = item["data"]["deleteWhen0"]
                tailored = item["data"]["properties"]["tailored"]
                two_handed = item["data"]["properties"]["2h"]
                consumable = item["data"]["properties"]["consumable"]
                description = item["data"]["description"]

                protection = item["data"]["properties"]["protection"]
                def_tot = item["data"]["def"]
                def_base = item["data"]["defBase"]
                def_bonus = item["data"]["defBonus"]
                dr = item["data"]["properties"]["dr"]
                dr_value = item["data"]["def"]

                weapon = item["data"]["properties"]["weapon"]

                dmg_tot = self.if_null(item["data"]["dmg"], 0)
                dmg_base = self.if_null(item["data"]["dmgBase"], 0)
                try:
                    dmg_stat = item["data"]["dmgStat"].split(".")[1]
                except IndexError:
                    dmg_stat = ""
                dmg_bonus = item["data"]["dmgBonus"]
                mod = item["data"]["mod"]
                try:
                    skill = item["data"]["skill"].split(".")[1]
                except IndexError:
                    skill = ""
                skillBonus = item["data"]["skillBonus"]
                critrange = item["data"]["critrange"]

                ranged = item["data"]["properties"]["ranged"]
                range = item["data"]["range"]
                reloadable = item["data"]["properties"]["reloadable"]
                reload = item["data"]["reload"]
                bow = item["data"]["properties"]["bow"]
                crossbow = item["data"]["properties"]["crossbow"]
                powder = item["data"]["properties"]["powder"]
                throwing = item["data"]["properties"]["throwing"]
                sling = item["data"]["properties"]["sling"]
                spell = item["data"]["properties"]["spell"]

                equipable = item["data"]["properties"]["equipable"]
                worn = item["data"]["worn"]
                slot = item["data"]["slot"]

                _Item = Item.objects.create(
                    name = name,
                    slug = slug,
                    img = img,
                    source = source,
                    subtype = subtype,
                    rarity = rarity,
                    unique = unique,
                    price = price,
                    value = value,
                    equipment = equipment,
                    stackable = stackable,
                    qty = qty,
                    stacksize = stacksize,
                    deleteWhen0 = deleteWhen0,
                    tailored = tailored,
                    two_handed = two_handed,
                    consumable = consumable,
                    description = description,
                    protection = protection,
                    def_tot = def_tot,
                    def_base = def_base,
                    def_bonus = def_bonus,
                    dr = dr,
                    dr_value = dr_value,
                    weapon = weapon,
                    dmg_tot = dmg_tot,
                    dmg_base = dmg_base,
                    dmg_stat = dmg_stat,
                    dmg_bonus = dmg_bonus,
                    mod = mod,
                    skill = skill,
                    skillBonus = skillBonus,
                    critrange = critrange,
                    ranged = ranged,
                    range = range,
                    reloadable = reloadable,
                    reload = reload,
                    bow = bow,
                    crossbow = crossbow,
                    powder = powder,
                    throwing = throwing,
                    sling = sling,
                    spell = spell,
                    equipable = equipable,
                    worn = worn,
                    slot = slot
                )

                for t in traits:
                    _Item.trait.add(t)
                    _Item.save()

                _Item_created += 1

            self.stdout.write(
                self.style.NOTICE("{} Items in files...".format(_Item_total))
            )
            self.stdout.write(
                self.style.SUCCESS("{} items created !".format(_Item_created))
            )
