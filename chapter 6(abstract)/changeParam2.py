#__author__ = 'SinnerA'
#coding=utf-8

def init(data):
    data['first'] = {}
    data["middle"] = {}
    data["last"] = {}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

data = {}
init(data)
store(data, "SinnerA Jiang", "Sheldon Jiang")
print lookup(data, "last", "Jiang")