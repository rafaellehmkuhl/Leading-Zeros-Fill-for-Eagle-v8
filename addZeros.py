import sys
import re

def zeroFill(matchobj):

    coord = matchobj.group(0)

    if len(coord) == 2:
        return coord[:1] + '000000' + coord[1:]
    elif len(coord) == 3:
        return coord[:1] + '00000' + coord[1:]
    elif len(coord) == 4:
        return coord[:1] + '0000' + coord[1:]
    elif len(coord) == 5:
        return coord[:1] + '000' + coord[1:]
    elif len(coord) == 6:
        return coord[:1] + '00' + coord[1:]
    elif len(coord) == 7:
        return coord[:1] + '0' + coord[1:]
    elif len(coord) == 8:
        return coord


filename = sys.argv[1]

with open(filename, 'r') as f:
    read_data = f.read()

pattern = '[XY]{1}[0-9]{2,7}'
new_data = re.sub(pattern, zeroFill, read_data)

with open(filename, 'w') as f:
    f.write(new_data)


