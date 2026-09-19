import math

def calculate_moment_magnitude(length_km, width_km, slip_m, shear_mod_gpa):
    """
    Calculate moment magnitude from fault rupture parameters.
    
    Args:
        length_km (float): Fault rupture length in kilometers
        width_km (float): Fault width in kilometers
        slip_m (float): Average slip in meters
        shear_mod_gpa (float): Crustal shear modulus in gigapascals
    
    Returns:
        tuple: (moment_n_m, moment_dyne_cm, magnitude)
            - moment_n_m: Seismic moment in newton-meters
            - moment_dyne_cm: Seismic moment in dyne-centimeters
            - magnitude: Moment magnitude (Mw)
    """
    # Convert dimensions to meters
    length_m = length_km * 1000.0
    width_m = width_km * 1000.0
    
    # Calculate rupture area in square meters
    rupture_area = length_m * width_m
    
    # Convert shear modulus to pascals (1 GPa = 1e9 Pa)
    shear_mod_pa = shear_mod_gpa * 1e9
    
    # Calculate seismic moment: M0 = shear_modulus * rupture_area * average_slip
    moment_n_m = shear_mod_pa * rupture_area * slip_m
    
    # Convert to dyne-cm (1 N·m = 1e7 dyne·cm)
    moment_dyne_cm = moment_n_m * 1e7
    
    # Calculate moment magnitude: Mw = (2/3) * log10(M0) - 6.03
    # where M0 is in N·m
    if moment_n_m <= 0:
        raise ValueError("Calculated seismic moment is non-positive, check input values")
    
    magnitude = (2.0 / 3.0) * math.log10(moment_n_m) - 6.03
    
    return moment_n_m, moment_dyne_cm, magnitude
