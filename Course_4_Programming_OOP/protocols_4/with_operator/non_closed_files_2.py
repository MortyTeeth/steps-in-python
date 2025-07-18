def non_closed_files(files):
    list_with_open_file = []
    for file in files:
        if file.closed:
            pass
        else:
            list_with_open_file.append(file)
    return list_with_open_file
