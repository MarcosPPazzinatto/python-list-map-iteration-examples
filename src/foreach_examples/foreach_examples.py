# foreach_examples.py

def list_foreach_example():
    """Iterate over a list using foreach style (for-in)."""
    fruits = ["apple", "banana", "orange", "grape"]
    print("List iteration:")
    for fruit in fruits:
        print(fruit)


def list_with_index_example():
    """Iterate over a list with index using enumerate()."""
    fruits = ["apple", "banana", "orange", "grape"]
    print("\nList iteration with index:")
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")


def dict_foreach_example():
    """Iterate over a dictionary using foreach style."""
    fruit_map = {"apple": 3, "banana": 5, "orange": 2, "grape": 10}
    print("\nDictionary iteration:")
    for key, value in fruit_map.items():
        print(f"{key}: {value}")


def main():
    list_foreach_example()
    list_with_index_example()
    dict_foreach_example()


if __name__ == "__main__":
    main()

