# advanced_lists.py

def sort_list():
    """Sort a list in ascending and descending order."""
    numbers = [5, 2, 9, 1, 7]
    print("Original list:", numbers)
    print("Sorted ascending:", sorted(numbers))
    print("Sorted descending:", sorted(numbers, reverse=True))


def check_membership():
    """Check if an element exists in a list."""
    fruits = ["apple", "banana", "orange"]
    print("\nIs 'apple' in fruits?", "apple" in fruits)
    print("Is 'grape' in fruits?", "grape" in fruits)


def extend_list():
    """Extend a list with another list."""
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    list_a.extend(list_b)
    print("\nExtended list:", list_a)


def zip_lists():
    """Combine two lists into pairs using zip()."""
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    combined = list(zip(names, scores))
    print("\nZipped lists:", combined)


def list_length():
    """Get the length of a list."""
    numbers = [10, 20, 30, 40]
    print("\nList length:", len(numbers))


def main():
    sort_list()
    check_membership()
    extend_list()
    zip_lists()
    list_length()


if __name__ == "__main__":
    main()

