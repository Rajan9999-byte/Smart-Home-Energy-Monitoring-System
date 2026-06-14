import random


def generate_sensor_data(total_power):

    voltage = round(
        random.uniform(225, 235),
        2
    )

    current = round(
        total_power / voltage,
        2
    )

    return voltage, current