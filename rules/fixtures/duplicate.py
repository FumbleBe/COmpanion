import json


def check_duplicates(json_file, key):
    with open(json_file, "r") as file:
        data = json.load(file)

    values_seen = set()
    duplicates = set()

    def check_value(value):
        if value in values_seen:
            duplicates.add(value)
        else:
            values_seen.add(value)

    def traverse(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    check_value(v)
                traverse(v)
        elif isinstance(obj, list):
            for item in obj:
                traverse(item)

    traverse(data)

    return duplicates


# Usage example
json_file_path = "/home/fumble/Auberge/rules/fixtures/spells.json"
specific_key = "key"  # Specify the specific key here
duplicate_values = check_duplicates(json_file_path, specific_key)
print("Duplicate values for key '{}': {}".format(specific_key, duplicate_values))
