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
    fresh_fruit = {"orange": 11, "apple": 4, "mango": 7}

    if mango_count := fresh_fruit.get("mango", 0):
        print(f"Make mango lassi with {mango_count} mangoes.")

    def pick_fruit(count: int):
        if count > 3:
            return None
        else:
            return "mango"

    count = 0
    while fruit := pick_fruit(count):
        print(f"There are {fresh_fruit.get(fruit)} fruits of type {fruit}")
        count += 1


def list_comprehension():
    """Test list, set, dict comprehensions.

    This corresponds to tip 27, 28 in Effective Python.
    """
    num_list = [x for x in range(10)]
    even_square_list = [x**2 for x in num_list if x % 2 == 0]
    print(even_square_list)
    even_square_dict = {x: x**2 for x in num_list if x % 2 == 0}
    print(even_square_dict)
    three_cube_set = {x**3 for x in num_list if x % 3 == 0}
    print(three_cube_set)

    # List comprehensions support multiple if statements.
    a = [x for x in num_list if x > 4 and x % 2 == 0]
    b = [x for x in num_list if x > 4 if x % 2 == 0]
    assert a == b


def sort_priority_tester():
    """ """

    def sort_priority(values, group):
        """Sort a list based on which members are in `group`.

        Args:
            values (list): employees at a company
            group (list): software engineers at the company
        """

        def helper(x):
            if x in group:
                return (0, x)
            return (1, x)

        values.sort(key=helper)

    name_list = ["Bill", "Joe", "Cathy", "Ed", "Anna"]
    swe_group = ["Joe", "Cathy"]
    sort_priority(name_list, swe_group)
    print(name_list)

    def sort_priority2(values, group):
        """Sort members if they are in `group` and track group members.

        Because of scopes, the `found` in inner helper function will not
        affect the outer helper function.

        Args:
            values (list): employees at a company
            group (list): software engineers at the company
        """
        found = False

        def helper(x):
            if x in group:
                found = True
                return (0, x)
            return (1, x)

        values.sort(key=helper)
        return found

    name_list2 = ["Bill", "Joe", "Cathy", "Ed", "Anna"]
    swe_group2 = ["Joe", "Cathy"]
    found2 = sort_priority2(name_list2, swe_group2)
    print(name_list2)
    # We expect found to be true, since there are members of the swe_group2 present.
    # Yet it turns out that `found` is None.
    print("Found2:", found2)

    def sort_priority3(values, group):
        """Sort members if they are in `group` and track group members.

        This uses nonlocal to make sure that inner scope `found` affects
        outer scope `found`.

        Args:
            values (list): employees at a company
            group (list): software engineers at the company
        """
        found = False

        def helper(x):
            nonlocal found
            if x in group:
                found = True
                return (0, x)
            return (1, x)

        values.sort(key=helper)
        return found

    name_list3 = ["Bill", "Joe", "Cathy", "Ed", "Anna"]
    swe_group3 = ["Joe", "Cathy"]
    found3 = sort_priority3(name_list3, swe_group3)
    print(name_list3)
    # We expect found to be true, since there are members of the swe_group2 present.
    # Yet it turns out that `found` is None.
    print("Found3:", found3)


def v_arg_tester():
    """Testing variable positional arguments (Effective Python tip 22)."""

    def log1(message, values):
        if not values:
            print(message)
        else:
            values_str = ", ".join(str(v) for v in values)
            print(f"{message}: {values_str}")

    log1("Hi there", [4, 3, 6])
    # log1("sup") # This will throw errors because `values` is expecting a variable.

    def log2(message, *values):
        if not values:
            print(message)
        else:
            values_str = ", ".join(str(v) for v in values)
            print(f"{message}: {values_str}")

    log2("Hi there", [4, 3, 6])
    log2("sup")  # This works as expected
    log2("Favorite colors", ["red", "blue", "green"])

    # Problems with using the star operator in functions:
    # Problem 1: optional arguments are turned into a tuple before being
    # passed into a function. You should only use variable arguments
    # if you know the number of arguments is small.

    def generator(num: int):
        for i in range(num):
            yield i

    log2("Favorite numbers", *generator(7))

    # Problem 2: you can't add new positional arguments without
    # needing to migrate callers.
    def log3(sequence, message, *values):
        if not values:
            print(f"seq: {sequence}: message {message}")
        else:
            values_str = ", ".join(str(v) for v in values)
            print(f"seq: {sequence}: message {message}: {values_str}")

    log3("sequence1", "test message", [4, 9, 7])
    log3("Hi there", [4, 3, 6])  # This silently breaks.
    # log3("sup")  # This breaks as expected.
    log3("Favorite colors", ["red", "blue", "green"])  # This silently breaks.
