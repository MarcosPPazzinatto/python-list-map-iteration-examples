# map_examples.py

def create_map():
    """Initialize an empty dictionary to act as a map."""
    return {}


def populate_map(my_map):
    """Populate the map with some key-value pairs."""
    my_map["apple"] = 3
    my_map["banana"] = 5
    my_map["orange"] = 2
    my_map["grape"] = 10


def print_map(my_map):
    """Print all items in the map."""
    for key, value in my_map.items():
        print(f"{key}: {value}")


def main():
    # Step 1: create the map
    fruit_map = create_map()

    # Step 2: populate the map
    populate_map(fruit_map)

    # Step 3: print the map
    print("Map content:")
    print_map(fruit_map)


if __name__ == "__main__":
    main()

