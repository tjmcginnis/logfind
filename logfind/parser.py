def parse(s, k):
    """returns True if all words in k are in s. False otherwise."""
    k = k.split()
    for word in k:
        if word not in s:
            return False
    return True


def parse_or(s, k):
    """returns True if any word in k is in s. False otherwise."""
    k = k.split()
    for word in k:
        if word in s:
            return True
    return False
