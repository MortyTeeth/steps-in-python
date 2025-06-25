is_non_negative_num = lambda x: x.count('.') < 2 and all([i not in 'qwertyuiopasdfghjklzxcvbnm-' for i in x]) == True
