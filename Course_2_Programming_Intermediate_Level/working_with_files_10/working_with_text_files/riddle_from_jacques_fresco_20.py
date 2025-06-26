with open('goats.txt', 'r', encoding='utf-8') as goats, open('answer.txt', 'w', encoding='utf-8') as answer:
    first_list = set(i.rstrip() for i in goats.readlines() if len(i.split()) > 1)
    goats.seek(0)
    second_list = [i.rstrip() for i in goats.readlines()]
    index_goats = second_list.index('GOATS')
    second_list_after_change = [i for i in second_list][index_goats + 1:]
    num_goats_ = len(second_list_after_change)
    count_goats = {}
    goats_for_filter = []


    def num_goats(first_list, second_list_after_change):
        for color in second_list_after_change:
            if color in first_list:
                if color not in count_goats:
                    count_goats.update({color: 1})
                else:
                    count_goats[color] += 1


    num_goats(first_list, second_list_after_change)


    def goats_that_fit_the_condition(count_goats):
        for key, value in count_goats.items():
            if int(value / num_goats_ * 100) > 7:
                goats_for_filter.append(key)
        return goats_for_filter


    goats_that_fit_the_condition(count_goats)

    print(*sorted(goats_for_filter), sep='\n', file=answer)
