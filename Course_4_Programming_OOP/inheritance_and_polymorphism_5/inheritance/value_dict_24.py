class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        else:
            return None

    def keys_of(self, value):
        time_list = []
        for k, v in self.items():
            if v == value:
                time_list.append(k)

        return time_list
