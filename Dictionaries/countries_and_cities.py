''' Given a list of countries and cities of each country. 
    Then given the names of the cities. For each city specify the country in which it is located. '''

# Initialize the dictionary to store countries and their cities
countries_cities = {}

# Read the number of countries
n = int(input("Enter the number of countries: "))
for _ in range(n):
    country, *cities = input("Enter the country followed by its cities: ").split()
    for city in cities:
        countries_cities[city] = country

# Read the number of queries for cities
q = int(input("Enter the number of city queries: "))
for _ in range(q):
    city = input("Enter the city name: ")
    print(countries_cities.get(city, "City not found"))
