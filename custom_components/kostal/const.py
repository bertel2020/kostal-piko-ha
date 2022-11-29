"""Constants for the Kostal piko integration."""
from datetime import timedelta

from homeassistant.const import (
    POWER_WATT,
    ENERGY_KILO_WATT_HOUR,
    ELECTRIC_POTENTIAL_VOLT,
    ELECTRIC_CURRENT_AMPERE,
)

DOMAIN = "kostal"

DEFAULT_NAME = "Kostal piko"

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=30)

SENSOR_TYPES = {
    "solar_generator_power": ["Solar generator power", POWER_WATT, "mdi:solar-power", "measurement", "power"],
    "consumption_phase_1": ["Consumption phase 1", POWER_WATT, "mdi:power-socket-eu", "measurement", "power"],
    "consumption_phase_2": ["Consumption phase 2", POWER_WATT, "mdi:power-socket-eu", "measurement", "power"],
    "consumption_phase_3": ["Consumption phase 3", POWER_WATT, "mdi:power-socket-eu", "measurement", "power"],
    "current_power": ["Current power", POWER_WATT, "mdi:solar-power", "measurement", "power"],
    "total_energy": ["Total energy", ENERGY_KILO_WATT_HOUR, "mdi:solar-power", "total_increasing", "energy"],
    "daily_energy": ["Daily energy", ENERGY_KILO_WATT_HOUR, "mdi:solar-power", "total_increasing", "energy"],
    "string1_voltage": ["String 1 voltage", ELECTRIC_POTENTIAL_VOLT, "mdi:current-ac", "measurement", "voltage"],
    "string1_current": ["String 1 current", ELECTRIC_CURRENT_AMPERE, "mdi:flash", "measurement", "current"],
    "string2_voltage": ["String 2 voltage", ELECTRIC_POTENTIAL_VOLT, "mdi:current-ac", "measurement", "voltage"],
    "string2_current": ["String 2 current", ELECTRIC_CURRENT_AMPERE, "mdi:flash", "measurement", "current"],
    "string3_voltage": ["String 3 voltage", ELECTRIC_POTENTIAL_VOLT, "mdi:current-ac", "measurement", "voltage"],
    "string3_current": ["String 3 current", ELECTRIC_CURRENT_AMPERE, "mdi:flash", "measurement", "current"],
    "l1_voltage": ["L1 voltage", ELECTRIC_POTENTIAL_VOLT, "mdi:current-ac", "measurement", "voltage"],
    "l1_power": ["L1 power", POWER_WATT, "mdi:power-plug", "measurement", "power"],
    "l2_voltage": ["L2 voltage", ELECTRIC_POTENTIAL_VOLT, "mdi:current-ac", "measurement", "voltage"],
    "l2_power": ["L2 power", POWER_WATT, "mdi:power-plug", "measurement", "power"],
    "l3_voltage": ["L3 voltage", ELECTRIC_POTENTIAL_VOLT, "mdi:current-ac", "measurement", "voltage"],
    "l3_power": ["L3 power", POWER_WATT, "mdi:power-plug", "measurement", "power"],
    "status": ["Status", None, "mdi:solar-power", None, None],
}
