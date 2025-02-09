hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    for char in hexNum:
            if char.upper() not in hexNumbers:
                return None
    decimal = 0
    length = len(hexNum)
    for i, char in enumerate(hexNum):
        if length <= 3:
            value = hexNumbers[char.upper()]
            power = length - i -1 
            decimal += value * (16 ** power)
        else:
            return None
    print(decimal)
    return decimal
   
hexToDec("34a")