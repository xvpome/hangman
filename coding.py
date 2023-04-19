travelLog = [
    {
        "contry": "France",
        "cities": ["Lile, Dijon"],
        "visits": 12,
    }
    
]

def addNewCountry(country:str, visited:int, city:list, travelLog:list):
    travelLog.append({"coutry": country, "visits": visited, "city": city})
    print(f"You've been to {country} {visited} times.")
    if len(city) == 1:
        print(f"You've been to {city}")
    elif len(city) == 2:
        print(f"You've been to {city[0]} and {city[1]}")
    else:
        print(f"You've been to {city[0: len(city)]} and {city[-1]}")

addNewCountry("Russia", 2, ["Moscow, St. Peterburg"], travelLog)
    
          
