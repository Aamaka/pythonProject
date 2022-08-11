travel_log = [
    {
        "Country": "france",
        "Cities_visited": ["paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "Country": "Germany",
        "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 20}
]

new_country = {}


def add_new_country(name, number_of_times_visited, cities):
    new_country["Country"] = name
    new_country["Cities_visited"] = number_of_times_visited
    new_country["total_visit"] = cities
    travel_log.append(new_country)
    print(travel_log)


add_new_country("Japan", ["bla", "blah", "blah"], 5)
