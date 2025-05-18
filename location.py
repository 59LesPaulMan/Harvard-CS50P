#tuples or combining values
import sys

def main():
    coordinates = (42.376, -71.115)
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    print(f"{sys.getsizeof(coordinates)} bytes")
    
    

main()