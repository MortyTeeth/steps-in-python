import pickle


def filter_dump(filename, objects, typename):
    list_with_objects = [obj for obj in objects if isinstance(obj, typename)]
    with open(filename, mode='wb') as pickle_file:
        pickle.dump(list_with_objects, pickle_file)

        return list_with_objects
