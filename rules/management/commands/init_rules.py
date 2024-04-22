from django.core.management.base import BaseCommand
from django.apps import apps

import os
import json
from rules.models import *


class Command(BaseCommand):

    help = "Initialize rules for Chroniques Oubliées"

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))
        Capacity.objects.all().delete()
        Path.objects.all().delete()
        Profile.objects.all().delete()
        Species.objects.all().delete()

        if Capacity.objects.all():
            self.stdout.write(self.style.WARNING("Capacities already exists in DB !"))

        else:
            _Capacity_created = 0
            _Capacity_total = 0
            _enc_Capacity_created = 0
            _enc_Capacity_total = 0
            _Profile_created = 0
            _Profile_total = 0
            _Path_created = 0
            _Path_total = 0
            _enc_Path_created = 0
            _enc_Path_total = 0
            _Species_total = 0
            _Species_created = 0
            module_dir = apps.get_app_config("rules").path
            profiles_json = os.path.join(module_dir, "fixtures/profiles.json")
            paths_json = os.path.join(module_dir, "fixtures/paths.json")
            enc_paths_json = os.path.join(module_dir, "fixtures/encounters-paths.json")

            capacities_json = os.path.join(module_dir, "fixtures/capacities.json")
            enc_capacities_json = os.path.join(
                module_dir, "fixtures/encounters-capacities.json"
            )
            species_json = os.path.join(module_dir, "fixtures/species.json")

            f_profiles = open(profiles_json)
            f_paths = open(paths_json)
            f_enc_paths = open(enc_paths_json)
            f_capacities = open(capacities_json)
            f_enc_capacities = open(enc_capacities_json)
            f_species = open(species_json)

            profiles = json.load(f_profiles)
            paths = json.load(f_paths)
            enc_paths = json.load(f_enc_paths)
            capacities = json.load(f_capacities)
            enc_capacities = json.load(f_enc_capacities)
            species = json.load(f_species)

            _drs = Source.objects.get(name="CO DRS")
            _compagnon = Source.objects.get(name="CO Compagnon")
            _vengeance = Source.objects.get(name="Vengeance")
            _autre = Source.objects.get(name="Autre")

            self.stdout.write(self.style.NOTICE("Importing Rules..."))

            for profile in profiles:
                _Profile_total += 1
            for path in paths:
                _Path_total += 1
            for path in enc_paths:
                _enc_Path_total += 1
            for capacity in capacities:
                _Capacity_total += 1
            for capacity in enc_capacities:
                _enc_Capacity_total += 1
            for race in species:
                _Species_total += 1

            for profile in profiles:
                name = profile["name"]
                slug = profile["data"]["key"]
                description = profile["data"]["description"]
                source = profile["data"]["source"]
                if "Chroniques Oubliées DRS" in source:
                    source = _drs
                elif "Chroniques Oubliées Compagnon" in source:
                    source = _compagnon
                elif "Vengeance" in source:
                    source = _vengeance
                else:
                    source = _autre

                dv = profile["data"]["dv"]
                spellcasting = profile["data"]["spellcasting"].upper()
                mpfactor = profile["data"]["mpfactor"]

                _Profile = Profile.objects.create(
                    name=name,
                    slug=slug,
                    description=description,
                    source=source,
                    dv=dv,
                    spellcasting=spellcasting,
                    mpfactor=mpfactor,
                )
                _Profile_created += 1

                for _path in profile["data"]["paths"]:
                    _id = _path["_id"]
                    rank = 1
                    for path in paths:
                        if path["_id"] == _id:
                            name = path["name"]
                            slug = path["data"]["key"]
                            description = path["data"]["description"]
                            source = path["data"]["source"]

                            if "Chroniques Oubliées DRS" in source:
                                source = _drs
                            elif "Chroniques Oubliées Compagnon" in source:
                                source = _compagnon
                            elif "Vengeance" in source:
                                source = _vengeance
                            else:
                                source = _autre

                            _Path, created = Path.objects.get_or_create(
                                name=name,
                                slug=slug,
                                defaults={"description": description, "source": source},
                            )
                            if created:
                                _Path_created += 1

                            _Profile.paths.add(_Path)
                            _Profile.save()

                            for _capacity in path["data"]["capacities"]:
                                _id_cap = _capacity["_id"]
                                for capacity in capacities:
                                    if capacity["_id"] == _id_cap:
                                        name = capacity["name"]
                                        slug = capacity["data"]["key"]
                                        description = capacity["data"]["description"]
                                        source = capacity["data"]["source"]
                                        if "Chroniques Oubliées DRS" in source:
                                            source = _drs
                                        elif "Chroniques Oubliées Compagnon" in source:
                                            source = _compagnon
                                        elif "Vengeance" in source:
                                            source = _vengeance
                                        else:
                                            source = _autre

                                        spell = capacity["data"]["spell"]
                                        limited = capacity["data"]["limited"]

                                        _Capacity, created = (
                                            Capacity.objects.get_or_create(
                                                name=name,
                                                slug=slug,
                                                defaults={
                                                    "description": description,
                                                    "source": source,
                                                    "spell": spell,
                                                    "limited": limited,
                                                },
                                            )
                                        )
                                        if created:
                                            _Capacity_created += 1

                                        _Path.capacities.add(_Capacity, through_defaults={'rank': rank})
                                        _Path.save()
                                        print(_Capacity)
                                        print(rank)
                                        rank += 1

            for path in enc_paths:
                name = path["name"]
                slug = path["data"]["key"]
                description = path["data"]["description"]
                source = path["data"]["source"]

                if "Chroniques Oubliées DRS" in source:
                    source = _drs
                elif "Chroniques Oubliées Compagnon" in source:
                    source = _compagnon
                elif "Vengeance" in source:
                    source = _vengeance
                else:
                    source = _autre

                _Path, created = Path.objects.get_or_create(
                    name=name,
                    slug=slug,
                    defaults={
                        "description": description,
                        "source": source,
                        "encounter": True,
                    },
                )
                if created:
                    _enc_Path_created += 1

                for _capacity in path["data"]["capacities"]:
                    _id_cap = _capacity["_id"]
                    rank = 1
                    for capacity in capacities:
                        if capacity["_id"] == _id_cap:
                            name = capacity["name"]
                            slug = capacity["data"]["key"]
                            description = capacity["data"]["description"]
                            source = capacity["data"]["source"]
                            if "Chroniques Oubliées DRS" in source:
                                source = _drs
                            elif "Chroniques Oubliées Compagnon" in source:
                                source = _compagnon
                            elif "Vengeance" in source:
                                source = _vengeance
                            else:
                                source = _autre

                            spell = capacity["data"]["spell"]
                            limited = capacity["data"]["limited"]

                            _Capacity, created = Capacity.objects.get_or_create(
                                name=name,
                                slug=slug,
                                defaults={
                                    "description": description,
                                    "source": source,
                                    "spell": spell,
                                    "limited": limited,
                                },
                            )
                            if created:
                                _Capacity_created += 1

                            _Path.capacities.add(
                                _Capacity, through_defaults={"rank": rank}
                            )
                            _Path.save()
                            rank += 1

                    for capacity in enc_capacities:
                        if capacity["_id"] == _id_cap:
                            name = capacity["name"]
                            slug = capacity["data"]["key"]
                            description = capacity["data"]["description"]
                            source = capacity["data"]["source"]
                            if "Chroniques Oubliées DRS" in source:
                                source = _drs
                            elif "Chroniques Oubliées Compagnon" in source:
                                source = _compagnon
                            elif "Vengeance" in source:
                                source = _vengeance
                            else:
                                source = _autre

                            spell = capacity["data"]["spell"]
                            limited = capacity["data"]["limited"]

                            _Capacity, created = Capacity.objects.get_or_create(
                                name=name,
                                slug=slug,
                                description=description,
                                source=source,
                                spell=spell,
                                limited=limited,
                                encounter=True,
                            )
                            if created:
                                _enc_Capacity_created += 1

                            _Path.capacities.add(
                                _Capacity, through_defaults={"rank": 0}
                            )
                            _Path.save()

            for race in species:
                name = race["name"]
                slug = race["data"]["key"]
                description = race["data"]["description"]
                source = race["data"]["source"]
                if "Chroniques Oubliées DRS" in source:
                    source = _drs
                elif "Chroniques Oubliées Compagnon" in source:
                    source = _compagnon
                elif "Vengeance" in source:
                    source = _vengeance
                else:
                    source = _autre

                STR = race["data"]["bonuses"]["str"]
                DEX = race["data"]["bonuses"]["dex"]
                CON = race["data"]["bonuses"]["con"]
                INT = race["data"]["bonuses"]["int"]
                WIS = race["data"]["bonuses"]["wis"]
                CHA = race["data"]["bonuses"]["cha"]

                _Species = Species.objects.create(
                    name=name,
                    slug=slug,
                    description=description,
                    source=source,
                    STR = STR,
                    DEX = DEX,
                    CON = CON,
                    INT = INT,
                    WIS = WIS,
                    CHA = CHA,
                )
                _Species_created += 1

                for _path in race["data"]["paths"]:
                    _id = _path["_id"]
                    rank = 1
                    for path in paths:
                        if path["_id"] == _id:
                            name = path["name"]
                            slug = path["data"]["key"]
                            description = path["data"]["description"]
                            source = path["data"]["source"]

                            if "Chroniques Oubliées DRS" in source:
                                source = _drs
                            elif "Chroniques Oubliées Compagnon" in source:
                                source = _compagnon
                            elif "Vengeance" in source:
                                source = _vengeance
                            else:
                                source = _autre

                            _Path, created = Path.objects.get_or_create(
                                name=name,
                                slug=slug,
                                defaults={"description": description, "source": source},
                            )
                            if created:
                                _Path_created += 1

                            _Species.paths.add(_Path)
                            _Species.save()

                            for _capacity in path["data"]["capacities"]:
                                _id_cap = _capacity["_id"]
                                for capacity in capacities:
                                    if capacity["_id"] == _id_cap:
                                        name = capacity["name"]
                                        slug = capacity["data"]["key"]
                                        description = capacity["data"]["description"]
                                        source = capacity["data"]["source"]
                                        if "Chroniques Oubliées DRS" in source:
                                            source = _drs
                                        elif "Chroniques Oubliées Compagnon" in source:
                                            source = _compagnon
                                        elif "Vengeance" in source:
                                            source = _vengeance
                                        else:
                                            source = _autre

                                        spell = capacity["data"]["spell"]
                                        limited = capacity["data"]["limited"]

                                        _Capacity, created = (
                                            Capacity.objects.get_or_create(
                                                name=name,
                                                slug=slug,
                                                defaults={
                                                    "description": description,
                                                    "source": source,
                                                    "spell": spell,
                                                    "limited": limited,
                                                },
                                            )
                                        )
                                        if created:
                                            _Capacity_created += 1

                                        _Path.capacities.add(
                                            _Capacity, through_defaults={"rank": rank}
                                        )
                                        _Path.save()
                                        rank += 1

                for _capacity in race["data"]["capacities"]:
                    _id_cap = _capacity["_id"]
                    for capacity in capacities:
                        if capacity["_id"] == _id_cap:
                            name = capacity["name"]
                            slug = capacity["data"]["key"]
                            description = capacity["data"]["description"]
                            source = capacity["data"]["source"]
                            if "Chroniques Oubliées DRS" in source:
                                source = _drs
                            elif "Chroniques Oubliées Compagnon" in source:
                                source = _compagnon
                            elif "Vengeance" in source:
                                source = _vengeance
                            else:
                                source = _autre

                            spell = capacity["data"]["spell"]
                            limited = capacity["data"]["limited"]

                            _Capacity, created = Capacity.objects.get_or_create(
                                name=name,
                                slug=slug,
                                defaults={
                                    "description": description,
                                    "source": source,
                                    "spell": spell,
                                    "limited": limited,
                                },
                            )
                            if created:
                                _Capacity_created += 1

                            _Species.capacities.add(
                                _Capacity, through_defaults={"rank": 0}
                            )
                            _Species.save()

            for capacity in enc_capacities:
                name = capacity["name"]
                slug = capacity["data"]["key"]
                description = capacity["data"]["description"]
                source = capacity["data"]["source"]
                if "Chroniques Oubliées DRS" in source:
                    source = _drs
                elif "Chroniques Oubliées Compagnon" in source:
                    source = _compagnon
                elif "Vengeance" in source:
                    source = _vengeance
                else:
                    source = _autre

                spell = capacity["data"]["spell"]
                limited = capacity["data"]["limited"]

                _Capacity, created = Capacity.objects.get_or_create(
                    name=name,
                    slug=slug,
                    description=description,
                    source=source,
                    spell=spell,
                    limited=limited,
                    encounter=True,
                )
                if created:
                    _enc_Capacity_created += 1

            for capacity in capacities:
                name = capacity["name"]
                slug = capacity["data"]["key"]
                description = capacity["data"]["description"]
                source = capacity["data"]["source"]
                if "Chroniques Oubliées DRS" in source:
                    source = _drs
                elif "Chroniques Oubliées Compagnon" in source:
                    source = _compagnon
                elif "Vengeance" in source:
                    source = _vengeance
                else:
                    source = _autre

                spell = capacity["data"]["spell"]
                limited = capacity["data"]["limited"]

                _Capacity, created = Capacity.objects.get_or_create(
                    name=name,
                    slug=slug,
                    defaults={
                        "description": description,
                        "source": source,
                        "spell": spell,
                        "limited": limited,
                    },
                )
                if created:
                    _Capacity_created += 1

            self.stdout.write(
                self.style.NOTICE(
                    "{} Profiles in files...".format(_Profile_total)
                )
            )
            self.stdout.write(
                self.style.SUCCESS("{} profiles created !".format(_Profile_created))
            )
            self.stdout.write(
                self.style.NOTICE(
                    "{} Paths in files...".format(_Path_total)
                )
            )
            self.stdout.write(
                self.style.SUCCESS("{} paths created !".format(_Path_created))
            )
            self.stdout.write(
                self.style.NOTICE(
                    "{} Encounters Paths in files...".format(_enc_Path_total)
                )
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "{} encounter paths created !".format(_enc_Path_created)
                )
            )
            self.stdout.write(
                self.style.NOTICE(
                    "{} Capacities in files...".format(_Capacity_total)
                )
            )
            self.stdout.write(
                self.style.SUCCESS("{} capacities created !".format(_Capacity_created))
            )
            self.stdout.write(
                self.style.NOTICE(
                    "{} Encounters Capacities in files...".format(_enc_Capacity_total)
                )
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "{} encounter capacities created !".format(_enc_Capacity_created)
                )
            )
            self.stdout.write(
                self.style.NOTICE(
                    "{} Species in files...".format(_Species_total)
                )
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "{} species created !".format(_Species_created)
                )
            )
            # for capacity in capacities:
            #     name = capacity["name"]
            #     slug = capacity["data"]["key"]
            #     description = capacity["data"]["description"]
            #     source = capacity["data"]["source"]
            #     if "Chroniques Oubliées DRS" in source:
            #         source = "drs"
            #     elif "Chroniques Oubliées Compagnon" in source:
            #         source = "compagnon"

            #     else:
            #         source = ""

            #     spell = capacity["data"]["spell"]
            #     limited = capacity["data"]["limited"]

            #     Capacity.objects.create(
            #         name=name,
            #         slug=slug,
            #         description=description,
            #         source=source,
            #         spell=spell,
            #         limited=limited,
            #     )
            #     self.stdout.write(self.style.SUCCESS("{} created !".format(name)))


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
