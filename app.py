import argparse

from config import get_env_variable

API_KEY = get_env_variable("API_KEY")
LANG = get_env_variable("LANG")
BASE_URL = get_env_variable("BASE_URL")


def get_args() -> tuple:
    parser = argparse.ArgumentParser(
        description="A CLI weather information from http://weatherapi.com",
        epilog="python weatherapp -l Rufisque",
    )
    parser.add_argument(
        "-l",
        "--location",
        required=True,
        help="The location name(name of a city)",
    )

    args = parser.parse_args()
    return args.location


def print_weather_data(data: dict) -> None:
    print("š " * 21, "\n")
    print("\tš :", data["location"]["name"])
    print("\tš :", data["current"]["last_updated"])
    print("\tš„ :", data["current"]["temp_c"], " Ā°C")
    print("\tš :", data["current"]["condition"]["text"], "\n")
    print("š " * 21)


def main():
    import requests

    location_name = get_args()

    endpoint = f"{BASE_URL}?key={API_KEY}&q={location_name}&lang={LANG}"

    response = requests.get(endpoint)
    data = response.json()
    print_weather_data(data)


if __name__ == "__main__":
    main()
