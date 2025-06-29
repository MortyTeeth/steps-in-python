def checksum(pickle_name, num):
    with open(pickle_name, 'rb') as pickle_file:
        obj = pickle.load(pickle_file)
    vr_list = []
    for var in obj:
        if isinstance(var, int):
            vr_list.append(var)

    if isinstance(obj, list) and len(vr_list) == num:
        print('Контрольные суммы совпадают')
    elif isinstance(obj, list) and len(vr_list) != num:
        if any(isinstance(x, int) for x in vr_list):
            if isinstance(obj, list):
                min_int = min(vr_list)
                max_int = max(vr_list)
                if max_int * min_int == num:
                    print('Контрольные суммы совпадают')
                else:
                    print('Контрольные суммы не совпадают')
        else:
            print('Контрольные суммы не совпадают')

    elif isinstance(obj, dict):
        counter = 0
        for key, value in obj.items():
            if isinstance(key, int):
                counter += key
        if counter == num:
            print('Контрольные суммы совпадают')
        else:
            print('Контрольные суммы не совпадают')


pickle_name = input()
number = int(input())

checksum(pickle_name, number)
