import requests

URL = "https://api.thingspeak.com/update"


def send_to_thingspeak(
        api_key,
        voltage,
        current,
        power,
        energy):

    payload = {
        "api_key": api_key,
        "field1": voltage,
        "field2": current,
        "field3": power,
        "field4": energy
    }

    try:

        requests.post(
            URL,
            data=payload,
            timeout=10
        )

    except Exception as e:

        print(
            "ThingSpeak Error:",
            e
        )