from collections import Counter

def analyze_flights(flights):
    """
    Process a list of flight dictionaries (from /flights API endpoint)
    and compute key insights:
      - top routes by count
      - top airlines by number of flights
      - top departure & arrival airports (with full names and countries)

    Returns:
        dict: Aggregated insights ready for display/charting.
    """
    if not flights:
        return {'error': 'No flight data available'}

    route_counter = Counter()
    airline_counter = Counter()
    dep_airport_counter = Counter()
    arr_airport_counter = Counter()

    # New: mapping IATA → full name - country
    dep_airport_names = {}
    arr_airport_names = {}

    for flight in flights:
        departure = flight.get('departure', {})
        arrival = flight.get('arrival', {})
        airline = flight.get('airline', {})

        dep_iata = departure.get('iata')
        arr_iata = arrival.get('iata')
        dep_name = departure.get('airport')
        arr_name = arrival.get('airport')
        dep_country = departure.get('country')
        arr_country = arrival.get('country')

        airline_name = airline.get('name')

        # Build route
        if dep_iata and arr_iata:
            route = f"{dep_iata}→{arr_iata}"
            route_counter[route] += 1

        if airline_name:
            airline_counter[airline_name] += 1

        if dep_iata:
            dep_airport_counter[dep_iata] += 1
            if dep_iata not in dep_airport_names:
                full_name = f"{dep_name} - {dep_country}" if dep_name and dep_country else dep_name or dep_country or ""
                dep_airport_names[dep_iata] = full_name

        if arr_iata:
            arr_airport_counter[arr_iata] += 1
            if arr_iata not in arr_airport_names:
                full_name = f"{arr_name} - {arr_country}" if arr_name and arr_country else arr_name or arr_country or ""
                arr_airport_names[arr_iata] = full_name

    # Format results with IATA + readable info
    return {
        'top_routes': [{'route': r, 'count': c} for r, c in route_counter.most_common(10)],
        'top_airlines': [{'airline': a, 'count': c} for a, c in airline_counter.most_common(10)],
        'top_departures': [
            {'airport': f"{iata} ({dep_airport_names.get(iata, '')})", 'count': count}
            for iata, count in dep_airport_counter.most_common(10)
        ],
        'top_arrivals': [
            {'airport': f"{iata} ({arr_airport_names.get(iata, '')})", 'count': count}
            for iata, count in arr_airport_counter.most_common(10)
        ],
    }
