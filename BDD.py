import psycopg2
import networkx as nx
import itertools

# Database connection
def get_db_connection():
    return psycopg2.connect(
        dbname="tourism",
        user="user",
        password="your_password",
        host="localhost",
        port="5432"
    )

# Fetch travel times between cities
def get_travel_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
    SELECT from_city_id, to_city_id, duration FROM transport_costs;
    """
    cursor.execute(query)
    travel_data = cursor.fetchall()
    
    conn.close()
    return travel_data

# Build the travel graph
def build_travel_graph(travel_data):
    G = nx.Graph()
    for from_city, to_city, duration in travel_data:
        G.add_edge(from_city, to_city, weight=duration.total_seconds())  # Convert time to seconds
    return G

# Instead of the nearest-neighbor approach, use brute-force to compute the optimal route
def find_optimal_route(city_list):
    travel_data = get_travel_data()
    G = build_travel_graph(travel_data)

    # Convert city names to IDs
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT id, name FROM cities WHERE name IN %s;"
    cursor.execute(query, (tuple(city_list),))
    city_id_map = {name: city_id for city_id, name in cursor.fetchall()}
    city_name_map = {city_id: name for name, city_id in city_id_map.items()}
    conn.close()

    city_ids = []
    for city in city_list:
        city_id = city_id_map.get(city)
        if city_id:
            city_ids.append(city_id) 
    if not city_ids:
        return "No valid cities found in database"

    start_city = city_ids[0]  # Fix the starting city
    end_city = city_ids[-1]  # Fix the ending city
    best_route = None
    best_cost = float("inf")

    # Evaluate all permutations of the remaining cities
    perm_ids = city_ids[1:-1]
    for perm in itertools.permutations([city for city in perm_ids ]):
        route = [start_city] + list(perm) + [end_city]
        cost = 0
        valid = True
        # Compute the total travel cost for this route
        for i in range(len(route) - 1):
            try:
                cost += G[route[i]][route[i+1]]["weight"]
            except KeyError:
                # If there is no direct connection between two cities, mark as invalid
                valid = False
                break
        if valid and cost < best_cost:
            best_cost = cost
            best_route = route

    if best_route is None:
        return "No complete path found"

    # Convert back to city names in the optimal order
    ordered_cities = [city_name_map[city_id] for city_id in best_route]
    return ordered_cities

# Example usage
cities_to_visit = []
next = True
while next:
    next_city = input("Enter the next city to visit (or press Enter to finish): ")
    if next_city != "":
        cities_to_visit.append(next_city)
    else:
        next = False
optimal_order = find_optimal_route(cities_to_visit)
print("Optimal Route:", optimal_order)

