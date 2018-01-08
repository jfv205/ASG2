# Name: geogdist.py
# Version: 0.0.2

import math

def distance(latlngA, latlngB):

    '''

    mydist( (latA,lngA), (latB,lngB) ) -> float (mydist in km)

    Returns the approximate straight line mydist between two nearby points
    on the surface of the Earth assuming that the earth is a sphere.

    The default radius value (R) of 6371.009
    The default unit of measure for mydist is kilometers.

    For further reference see the link below:
    https://en.wikipedia.org/wiki/Geographical_distance

    '''

    R = 6371.009  # Approximate radius of Earth's surface (radius from center of the sphere in km).
    latA, lngA = latlngA    
    lngA = math.radians(lngA)
    latA = math.radians(latA)
    latB, lngB = latlngB
    lngB = math.radians(lngB)
    latB = math.radians(latB)
    x = (lngB - lngA) * math.cos((latA + latB) / 2)
    y = latB - latA
    d = math.sqrt(x * x + y * y) * R
    conversion_factor = 0.62137119
    d = d * conversion_factor # Converts kilometre output to it's value in miles.
    return d  # Returns the converted value.
    

if __name__ == "__main__":
    print("testing geodist")
    assert round(distance((50.413905, -3.976364), (50.448022, -3.812943))) == 8
    assert round((distance((50.2095615, -4.5627776), (50.2309890, -4.0639060)))) == 22
    assert round((distance((50.410723, -3.780584), (50.414926, -3.802085)))) == 1
