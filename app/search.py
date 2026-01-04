
def search_flights(origin: str, destination: str, date: str):
    """
    Searches for flights between two airports on a specific date.
    
    Args:
        origin: The three-letter airport code for the starting location (e.g., 'JFK').
        destination: The three-letter airport code for the destination (e.g., 'LHR').
        date: The date of travel in YYYY-MM-DD format.
    """
    print(f"\n[System] Searching flights from {origin} to {destination} on {date}...")
    
    # Mock return data - simulating what a real API would return
    if destination == "CDG": # Paris
        return {
            "flights": [
                {"airline": "Air France", "price": "$650", "time": "10:00 AM"},
                {"airline": "Delta", "price": "$720", "time": "2:00 PM"}
            ]
        }
    elif destination == "HND": # Tokyo
        return {
            "flights": [
                {"airline": "JAL", "price": "$1200", "time": "11:00 AM"},
                {"airline": "ANA", "price": "$1250", "time": "4:00 PM"}
            ]
        }
    else:
        return {"error": "No flights found for this route."}

def search_hotels(location: str, check_in: str, price_range: str = "medium"):
    """
    Searches for hotels in a specific location.
    
    Args:
        location: The city or area to search in (e.g., 'Tokyo', 'Downtown NY').
        check_in: The check-in date in YYYY-MM-DD.
        price_range: Preference for price ('budget', 'medium', 'luxury').
    """
    print(f"\n[System] Searching {price_range} hotels in {location} for {check_in}...")
    
    # Mock Data
    if location == "Tokyo":
        return {
            "hotels": [
                {"name": "Capsule Inn", "price": "$50/night", "rating": "3.5 stars"},
                {"name": "Grand Hyatt Tokyo", "price": "$400/night", "rating": "5 stars"}
            ]
        }
    elif location == "Paris":
        return {
            "hotels": [
                {"name": "Le Petit Hotel", "price": "$150/night", "rating": "4 stars"}
            ]
        }
    else:
        return {"error": "No hotels found."}

# Create the tool dictionary
tools_list = [search_flights, search_hotels]

