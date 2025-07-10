class Postman:
    def __init__(self, delivery_data=None):
        self.delivery_data = []

    def add_delivery(self, street, house_number, number_apartment):
        self.delivery_data.append((street, house_number, number_apartment))

    def get_houses_for_street(self, street):
        if len(self.delivery_data) < 1:
            return []
        houses_list = [i[1] for i in self.delivery_data if i[0] == street]
        dict_keys = {}.fromkeys(houses_list)

        new_list = list(dict_keys.keys())
        return new_list

    def get_flats_for_house(self, street, house_number):
        if len(self.delivery_data) < 1:
            return []
        numbers_apartment = [i[2] for i in self.delivery_data if i[0] == street and i[1] == house_number]
        dict_keys = {}.fromkeys(numbers_apartment)

        new_list = list(dict_keys.keys())
        return new_list
