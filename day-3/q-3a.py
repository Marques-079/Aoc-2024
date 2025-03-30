#Completed 31/03/2025 - 0(1) time complexity :D

with open("day-3/INPUT3.txt") as f:
    lines = f.read()

def muls_present(sub): 
    i = 4 
    num1 = ""
    while i < len(sub) and sub[i].isdigit():
        num1 += sub[i]
        i += 1
        if len(num1) > 3:
            return 0

    if i >= len(sub) or sub[i] != ',' or num1 == "":
        return 0

    i += 1 
    num2 = ""
    while i < len(sub) and sub[i].isdigit():
        num2 += sub[i]
        i += 1
        if len(num2) > 3:
            return 0

    if i >= len(sub) or sub[i] != ')' or num2 == "":
        return 0

    return int(num1) * int(num2)

def find_muls(text):
    collection = 0
    for i in range(len(text)):
        if text[i:i+4] == 'mul(':
            result = muls_present(text[i:i+15])
            collection += result
    return collection

print(find_muls(lines))
