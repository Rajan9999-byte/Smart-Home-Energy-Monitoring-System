import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


APPLIANCE_WATTAGES = {
    "Fan": 80,
    "TV": 120,
    "Laptop": 90,
    "Refrigerator": 250,
    "Air Conditioner": 1500
}


def draw_appliance(ax, x, y, name, status):

    color = "#2ecc71" if status else "#e74c3c"

    wattage = APPLIANCE_WATTAGES[name] if status else 0

    ax.scatter(x, y, s=220, c=color)

    ax.text(
        x + 2,
        y,
        f"{name}",
        fontsize=9,
        va="center"
    )

    ax.text(
        x + 2,
        y - 3,
        f"{'ON' if status else 'OFF'} | {wattage}W",
        fontsize=8,
        va="center"
    )


def create_dashboard(
        appliances,
        voltage,
        current,
        power,
        energy,
        alert):

    os.makedirs(
        "images",
        exist_ok=True
    )

    fig, ax = plt.subplots(
        figsize=(14, 9)
    )

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.axis("off")

    fig.patch.set_facecolor("#eef5fb")

    # ==================================
    # HEADER
    # ==================================

    ax.add_patch(
        Rectangle(
            (0, 92),
            100,
            8,
            color="#1f77b4"
        )
    )

    ax.text(
        50,
        96,
        "SMART HOME ENERGY MONITORING SYSTEM",
        ha="center",
        va="center",
        fontsize=20,
        color="white",
        weight="bold"
    )

    # ==================================
    # HOUSE OUTER WALL
    # ==================================

    ax.add_patch(
        Rectangle(
            (10, 20),
            80,
            60,
            fill=False,
            linewidth=4
        )
    )

    # Vertical wall

    ax.plot(
        [50, 50],
        [20, 80],
        linewidth=3
    )

    # Horizontal wall

    ax.plot(
        [10, 90],
        [50, 50],
        linewidth=3
    )

    # Room Labels

    ax.text(
        30,
        75,
        "LIVING ROOM",
        fontsize=14,
        weight="bold",
        ha="center"
    )

    ax.text(
        70,
        75,
        "BEDROOM",
        fontsize=14,
        weight="bold",
        ha="center"
    )

    ax.text(
        30,
        45,
        "KITCHEN",
        fontsize=14,
        weight="bold",
        ha="center"
    )

    ax.text(
        70,
        45,
        "UTILITY ROOM",
        fontsize=14,
        weight="bold",
        ha="center"
    )

    # ==================================
    # APPLIANCES
    # ==================================

    draw_appliance(
        ax,
        18,
        68,
        "Fan",
        appliances["Fan"]
    )

    draw_appliance(
        ax,
        18,
        60,
        "TV",
        appliances["TV"]
    )

    draw_appliance(
        ax,
        58,
        64,
        "Laptop",
        appliances["Laptop"]
    )

    draw_appliance(
        ax,
        18,
        34,
        "Refrigerator",
        appliances["Refrigerator"]
    )

    draw_appliance(
        ax,
        58,
        34,
        "Air Conditioner",
        appliances["Air Conditioner"]
    )

    # ==================================
    # SYSTEM METRICS
    # ==================================

    active_devices = sum(
        appliances.values()
    )

    top_consumer = "None"

    max_power = 0

    for appliance, status in appliances.items():

        if status:

            watt = APPLIANCE_WATTAGES[
                appliance
            ]

            if watt > max_power:

                max_power = watt

                top_consumer = appliance

    ax.add_patch(
        Rectangle(
            (5, 5),
            90,
            10,
            fill=False,
            linewidth=2
        )
    )

    metrics_text = (
        f"Voltage: {voltage:.1f} V    "
        f"Current: {current:.2f} A    "
        f"Power: {power:.0f} W    "
        f"Energy: {energy:.3f} kWh    "
        f"Devices ON: {active_devices}/5"
    )

    ax.text(
        50,
        11,
        metrics_text,
        ha="center",
        fontsize=10,
        weight="bold"
    )

    ax.text(
        50,
        7,
        f"Top Consumer: {top_consumer}",
        ha="center",
        fontsize=10
    )

    # ==================================
    # ALERT BANNER
    # ==================================

    banner_color = (
        "#e74c3c"
        if alert == "HIGH USAGE"
        else "#2ecc71"
    )

    ax.add_patch(
        Rectangle(
            (30, 84),
            40,
            5,
            color=banner_color
        )
    )

    ax.text(
        50,
        86.5,
        alert,
        color="white",
        weight="bold",
        fontsize=12,
        ha="center"
    )

    plt.tight_layout()

    plt.savefig(
        "images/virtual_home_status.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()