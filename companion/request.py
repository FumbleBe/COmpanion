import requests


def main():
    # response = requests.get("https://api.frankfurter.app/latest?from=USD&to=GBP")

    payload = {"actor_id": 2}
    response = requests.get("http://158.220.103.9:8000/api/equipments/", params=payload)

    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("There was an error!")

    data = response.json()
    print("JSON data: ", data)


if __name__ == "__main__":
    main()
