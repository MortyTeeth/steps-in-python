def log_for(logfile, date_str):
    with open(logfile, 'r', encoding='UTF-8') as file_for_read, open(f"log_for_{date_str}.txt", 'w',
                                                                     encoding='UTF-8') as file_for_write:
        read = file_for_read.readlines()
        for line in read:
            if date_str in line:
                new_line = line.replace(date_str + ' ', '')
                file_for_write.write(new_line)
