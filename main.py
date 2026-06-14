import os
import time

from dotenv import load_dotenv
from datetime import datetime

from python_simulation.smart_home_simulator import simulate_home
from python_simulation.virtual_sensor import generate_sensor_data
from python_simulation.logger import save_row
from python_simulation.thingspeak_client import send_to_thingspeak
from python_simulation.dashboard_generator import create_dashboard

load_dotenv()

API_KEY = os.getenv(
    "THINGSPEAK_API_KEY"
)

TARIFF = float(
    os.getenv(
        "TARIFF_RATE",
        8
    )
)

energy_kwh = 0

print("\nSMART HOME ENERGY MONITOR\n")

for cycle in range(20):

    appliances, total_power = simulate_home()

    voltage, current = generate_sensor_data(
        total_power
    )

    power = total_power

    energy_increment = (
        power / 1000
    ) * (15 / 3600)

    energy_kwh += energy_increment

    cost = energy_kwh * TARIFF

    alert = (
        "HIGH USAGE"
        if power > 1000
        else "NORMAL"
    )

    print("\n---------------------")

    print(
        f"Cycle {cycle+1}"
    )

    for name, state in appliances.items():

        print(
            f"{name}: "
            f"{'ON' if state else 'OFF'}"
        )

    print(
        f"Power: {power:.2f} W"
    )

    print(
        f"Energy: {energy_kwh:.4f} kWh"
    )

    print(
        f"Cost: ₹{cost:.2f}"
    )

    print(
        f"Alert: {alert}"
    )

    row = {

        "timestamp":
        datetime.now(),

        "voltage":
        voltage,

        "current":
        current,

        "power":
        power,

        "energy_kwh":
        round(
            energy_kwh,
            5
        ),

        "cost":
        round(
            cost,
            2
        ),

        "alert":
        alert
    }

    save_row(row)

    send_to_thingspeak(
        API_KEY,
        voltage,
        current,
        power,
        energy_kwh
    )

    create_dashboard(
        appliances,
        voltage,
        current,
        power,
        energy_kwh,
        alert
    )

    time.sleep(15)

print(
    "\nSimulation Complete"
)