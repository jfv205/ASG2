from filter.geodist import distance
from filter.bounding_box import bounding_box

def crimes_in_box(post_lat, post_lon, radius):
    """
    Returns list of crimes within radius.

    Goes through compiled CSV file and checks whether the latlong is the bounding box,
    and then calculates distance from the postcode geoposition. This is added to a new
    nested list [[row], [row], [row]] of crimes within the list with the heading row.
    """
    crime_loc = []

    file = open(r'compile_csv/crimes_in_sw.csv', 'r')
    crime_loc = list(file)  # turns into list to use indices

    headings = crime_loc[0]  # takes first row which is a single element in the file list
    headings = headings.split(",")  # splits into list

    crimes_list = []
    crimes_list.append(headings)  # adds headings to top of list

    lat_min, lat_max, lon_min, lon_max = bounding_box((post_lat, post_lon), radius)

    for row in crime_loc[1:]:
        row = row.split(',')  # turns into a list of strings

        if row[3] != '':
            lat, lon = float(row[3]), float(row[2])
            if lat != '':  # checks for no location
                if (lat >= lat_min) and (lat <= lat_max):
                    if (lon >= lon_min) and (lon <= lon_max):
                        difference = distance((post_lat, post_lon), (lat, lon))
                        if difference <= radius:
                            crimes_list.append(row)

    return crimes_list

if __name__ == "__main__":
    print("testing crimes in box")
    assert empty_list(crimes_in_box(50.4127679, -4.085751, 1))
    assert empty_list(crimes_in_box(50.71413737, -2.43711588, 2))
    assert empty_list(crimes_in_box(50.71461595, -3.54978917, 5))
