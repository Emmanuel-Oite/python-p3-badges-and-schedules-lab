def badge_maker(name):
    """
    Create a badge with the given name.
    
    Args:
        name (str): The name to be included in the badge.
    
    Returns:
        str: The badge message including the given name.
    """
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    """
    Create badges for a list of names.

    Args:
        names (list): A list of names for which badges need to be created.

    Returns:
        list: A list of badges created for each name.
    """
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    """
    Create a list of room assignments for the given names and return it.
    """
    rooms = list(range(1, len(names) + 1))
    return [f"Hello, {name}! You'll be assigned to room {room}!" for name, room in zip(names, rooms)]

def printer(names):
    """
    This function takes a list of names as input and performs the following actions:
    1. Calls batch_badge_creator to generate badges for each name in the input list.
    2. Iterates through the generated badges and prints each badge.
    3. Calls assign_rooms to allocate rooms for each name in the input list.
    4. Iterates through the allocated rooms and prints each room.
    """
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)