# basic_lists.py

def create_list():
    """Create a basic list of fruits."""
    fruits = ["apple", "banana", "orange"]
    return fruits


def modify_list(fruits):
    """Add and remove elements from the list."""
    fruits.append("grape")     # add element
    fruits.remove("banana")    # remove element
    fruits.pop(0)              # remove element at index 0
    return fruits


def access_elements(fruits):
    """Access elements by index and slicing."""
    print("First element:", fruits[0])
    print("Last element:", fruits[-1])
    print("Slice [0:2]:", fruits[0:2])


def list_comprehension():
    """Create a list using list comprehension."""
    numbers = [x * 2 for x in range(5)]
    print("List comprehension (x*2 for range 0-4):", numbers)


def main():
    fruits = create_list()
    print("Initial list:", fruits)

    fruits = modify_list(fruits)
    print("Modified list:", fruits)

    access_elements(fruits)
    list_comprehension()


if __name__ == "__main__":
    main()

