# Here will go the logic for the conversions.

def length_conversions(value, from_unit, to_unit):
    
    to_meters = {
        'km': 1000.0,      # 1 kilometer = 1000 meters
        'm': 1.0,          # 1 meter = 1 meter (base unit)
        'cm': 0.01,        # 1 centimeter = 0.01 meters
        'mm': 0.001,       # 1 millimeter = 0.001 meters
        'mi': 1609.344,    # 1 mile = 1609.344 meters (exact)
        'yd': 0.9144,      # 1 yard = 0.9144 meters (exact)
        'ft': 0.3048,      # 1 foot = 0.3048 meters (exact)
        'in': 0.0254       # 1 inch = 0.0254 meters (exact)
    }

    # If units are equal
    if from_unit == to_unit:
        return value
    
    # Convert to meters and then to the target unit
    try:
        # First convert the value to meters
        value_in_meters = value * to_meters[from_unit]
        
        # Then convert from meters to the target unit
        result = value_in_meters / to_meters[to_unit]
        
        return result
    
    except KeyError:
        return None
    
def weight_conversions(value, from_unit, to_unit):
    to_grams = {
        'kg': 1000.0,      # 1 kilogram = 1000 gram
        'g': 1.0,          # 1 gram = 1 gram (base unit)
        'mg': 0.001 ,      # 1 milligram = 0.001 gram
        'oz': 28.3495,     # 1 ounce = 28.3495 gram (exact)
        'lb': 453.592      # 1 pound = 453.592 gram (exact)
    }
    
    if from_unit == to_unit:
        return value
    
    try:
        value_in_grams = value * to_grams[from_unit]
        
        result = value_in_grams / to_grams[to_unit]
        
        return result
    
    except KeyError:
        return None