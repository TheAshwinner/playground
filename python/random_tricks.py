
def find_longest_name(name_list: list[str]):
    """Find longest name in a list of names.

    This tip demonstrates item 8 in Effective Python to process
    iterators in parallel.

    Args:
        name_list (list[str]): A list of names.

    Returns:
        str: the name with the longest length.
    """
    count_list = [len(name) for name in name_list]
    max_length = 0
    max_name = None
    for name, count in zip(name_list, count_list):
        if count > max_length:
            max_length = count
            max_name = name
    return max_name


def walrus_tester():
    """Test out walrus operator functionality."""
    fresh_fruit = {
        'orange': 11,
        'apple': 4,
        'mango': 7
    }

    if mango_count := fresh_fruit.get('mango', 0):
        print(f'Make mango lassi with {mango_count} mangoes.')
    
    def pick_fruit(count: int):
        if count > 3:
            return None
        else:
            return 'mango'
    
    count = 0
    while fruit := pick_fruit(count):
        print(f'There are {fresh_fruit.get(fruit)} fruits of type {fruit}')
        count += 1