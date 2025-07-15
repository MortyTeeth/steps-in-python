def limited_hash(left, right, hash_function=hash):
    def decorator(*args, **kwargs):
        hashh = hash_function(*args, **kwargs)
        if hashh in range(left, right + 1):
            return hashh

        elif hashh > right:
            while hashh > right:
                hashh = hashh - (right - left + 1)
            return hashh

        elif hashh < left:
            while hashh < left:
                hashh = hashh + (right - left + 1)
            return hashh

    return decorator
