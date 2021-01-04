def findElement(seq, elem, finder):
    for item in seq:
        if finder(item) == elem:
            return item
    raise RuntimeError("Could not find element in list")

d = [
    {"name": "John Hopkins", "age": 24},
    {"name": "Rolf Smith", "age": 24},
    {"name": "Kenny Cartman", "age": 24}
    ]

def finder(item):
    return item["name"]

print(findElement(d, "Rolf Smith", finder))
