cornerConnectionCells = [
    ['W1', 'B3', 'R7'],
    ['W3', 'R5', 'G1'],
    ['W5', 'G7', 'O3'],
    ['W7', 'O1', 'B5'],
    ['Y1', 'B7', 'O7'],
    ['Y3', 'O5', 'G5'],
    ['Y5', 'R3', 'G3'],
    ['Y7', 'B1', 'R1'],
]

for cc in cornerConnectionCells:
    print("'" + cc[0][0] + cc[1][0] + cc[2][0] + "'", ":", "'" + cc[0] + "',")
    print("'" + cc[0][0] + cc[2][0] + cc[1][0] + "'", ":", "'" + cc[0] + "',")

    print("'" + cc[1][0] + cc[0][0] + cc[2][0] + "'", ":", "'" + cc[1] + "',")
    print("'" + cc[1][0] + cc[2][0] + cc[0][0] + "'", ":", "'" + cc[1] + "',")

    print("'" + cc[2][0] + cc[1][0] + cc[0][0] + "'", ":", "'" + cc[2] + "',")
    print("'" + cc[2][0] + cc[0][0] + cc[1][0] + "'", ":", "'" + cc[2] + "',")