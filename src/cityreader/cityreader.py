# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv

# Create city class with name, lat, lon attributes
class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon


# Create cities list
cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list

    # open the csv file
    with open('src/cityreader/cities.csv') as csvfile:
        # Turn the csvfile into indiviudal lists split with ','
        readcsv = csv.reader(csvfile, delimiter=',')
        # enumerate and iterate through the csvreader object
        # to take out the lists
        for i, row in enumerate(readcsv):
            # We don't want the first row since that contains
            # the headers of the csv file
            if i != 0:
                cities.append(City(row[0], float(row[3]), float(row[4])))
            # if it is the header or i == 0, don't do anything
            else:
                pass
    # returns the list of cities
    return cities


# Runs the function and creates the list of cities using the
# city class
cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    # Makes sure that lat1 will always be the lower number
    if lat1 < lat2:
        pass
    else:
        lat1, lat2 = lat2, lat1

    # makes sure that lon1 will always be the lower number
    if lon1 < lon2:
        pass

    else:
        lon1, lon2 = lon2, lon1

    # iterates through the cities list and checks if the lat on is within
    # the boundrys of a specific city. If it is, append it to the within
    # list
    for city in cities:
        if city.lat >= lat1 and city.lat <= lat2 and city.lon >= lon1 and city.lon <= lon2:
            within.append(city)

    # returns the within list
    return within


# Uncomment everything below if you want to test the user input yourself

# # asks for user input for lat1 and lon1
# latlon1 = input("Enter lat1,lon1: ")
# latlon1 = latlon1.split(', ')

# # asks for user input for lat2 and lon2
# latlon2 = input("Enter lat2,lon2: ")
# latlon2 = latlon2.split(', ')

# # runs the cityreader_stretch function and sets it to a variable that holds the list
# within = cityreader_stretch(float(latlon1[0]), float(latlon1[1]), float(latlon2[0]), float(latlon2[1]), cities)

# # print out the list of cities within the boundrys
# for city in within:
#   print(f"{city.name}: {(city.lat, city.lon)}")
