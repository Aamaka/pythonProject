import json


class A(list):

    def __getitem__(self, item):
        if item <= 0:
            raise IndexError("index out of bounds")
        return super().__getitem__(item - 1)

    def __setitem__(self, key, value):
        if key <= 0:
            raise IndexError("index out of bounds")
        return super().__setitem__(key - 1, value)


p = A()
p.append(4)
p.append(55)
p[1] = 89
print(p[1] == 89)

b_file = open("B.txt", "w")


class B(dict):

    def __init__(self, *args, **kwargs):
        super(B, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("key already exist")
        else:
            super().__setitem__(key, value)
            with(open("temp.txt", "w")) as fil_obj:
                json.dump(a, fil_obj)


a = B()
a["key"] = "value"
a["name"] = "Amaka"
a["age"] = 99
