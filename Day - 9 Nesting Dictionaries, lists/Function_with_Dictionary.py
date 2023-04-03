travel_log = [
    {
    "Country" : "Nepal",
    "Number_of_visits" : 10000,
    "Cities_Visited" : ["Kathmandu","Bhaktapur","Dhulikhel","Lalitpur","Biratnagar"]
    },
    {
    "Country" : "India",
    "Number_of_Visits" : 1,
    "Cities_Visited" : ["Delhi","Ghaziabad"]
    }
]

def add_country(country,times_visited,cities_visited):
    travel_log.append({
        "Country" : country,
        "Number_of_Visits" : times_visited,
        "Cities_Visited" : cities_visited
    })

add_country(country="China",times_visited=2,cities_visited=["Beijing","Guangzhou"])
print()
print(travel_log)

print(f"\nYou have visited {travel_log[-1]['Country']} {travel_log[-1]['Number_of_Visits']} times. ")
print(f"You have visited {travel_log[-1]['Cities_Visited'][0]} and {travel_log[-1]['Cities_Visited'][1]}")