import random

# List of possible damaged systems
damaged_systems = [
    "navigation",
    "communications",
    "life_support",
    "engines",
    "deflector_shield"
]

# Mapping of repair codes
repair_codes = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# saturation data (pressure in MPa) ---
saturation_table = {
    1.0:  (0.00104, 1.694),   # example at 1 MPa
    3.0:  (0.0015, 0.5),      # example at 3 MPa
    5.0:  (0.0022, 0.1),      # example at 5 MPa
    10.0: (0.0035, 0.0035),   # critical point: both equal vc
}


# Randomly pick a damaged system on startup
damaged_system = random.choice(damaged_systems)