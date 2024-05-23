#Nesting Dictionary in Dictionary

travel_log = {
    "France": {"cities_visited": ["paris", "Lille", "Dijon"], "total-visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgard"], "total-visits": 5},
}

#Nesting Dictionary in List

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["paris", "Lille", "Dijon"], 
        "total-visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgard"], 
        "total-visits": 5
    },
]

print(travel_log)