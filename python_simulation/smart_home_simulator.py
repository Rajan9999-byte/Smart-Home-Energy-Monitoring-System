import random

APPLIANCES = {
    "Fan": 80,
    "TV": 120,
    "Laptop": 90,
    "Refrigerator": 250,
    "Air Conditioner": 1500
}


def simulate_home():

    appliance_states = {}

    total_power = 0

    for appliance, wattage in APPLIANCES.items():

        status = random.choice([True, False])

        appliance_states[appliance] = status

        if status:
            total_power += wattage

    return appliance_states, total_power