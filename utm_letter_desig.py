def _UTMLetterDesignator(Lat):
    """
    This routine determines the correct UTM letter designator for the given latitude.
    Returns 'Z' if latitude is outside the UTM limits of 84N to 80S.
    
    Written by Chuck Gantz - chuck.gantz@globalstar.com
    Refactored for clarity and maintainability.
    """
    
    # Return 'Z' if latitude is outside UTM limits
    if Lat > 84 or Lat < -80:
        return 'Z'
    
    # UTM latitude bands (lower_bound, letter)
    # Most bands are 8 degrees wide, except X (72N to 84N) which is 12 degrees
    latitude_bands = [
        (72, 'X'),
        (64, 'W'),
        (56, 'V'),
        (48, 'U'),
        (40, 'T'),
        (32, 'S'),
        (24, 'R'),
        (16, 'Q'),
        (8, 'P'),
        (0, 'N'),
        (-8, 'M'),
        (-16, 'L'),
        (-24, 'K'),
        (-32, 'J'),
        (-40, 'H'),
        (-48, 'G'),
        (-56, 'F'),
        (-64, 'E'),
        (-72, 'D'),
        (-80, 'C')
    ]
    
    # Find and return the appropriate letter designator
    for lower_bound, letter in latitude_bands:
        if Lat >= lower_bound:
            return letter
    
    return 'Z'


# Test the function
if __name__ == "__main__":
    # Test with Lat = 8
    print(f"Lat = 8: {_UTMLetterDesignator(8)}")
    
    # Additional tests
    test_values = [0, -8, 45, 72, 84, 90, -80, -85]
    for lat in test_values:
        print(f"Lat = {lat}: {_UTMLetterDesignator(lat)}")
