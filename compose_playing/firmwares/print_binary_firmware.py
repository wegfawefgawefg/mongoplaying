import os
starting_firmwares = os.listdir(".")
print(starting_firmwares)
first_firm = starting_firmwares[0]
print(first_firm)
with open(first_firm, "rb") as f:
    data = f.read(8)
print(data)
print(type(data))