
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

