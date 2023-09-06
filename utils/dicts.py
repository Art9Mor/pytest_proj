def get_val(collection, key, default='git'):
    print_key = key
    if len(collection) == 0:
        return default

    elif collection.get(print_key) is not None:
        return collection.get(print_key)

    return default

