"""
File: createCells.py
Author: David Goff
Date: 6/19/24
Description: Creates the list of "cells" for the rubik's cube.
"""

import cell

cornerConnections = [
    [1, 12, 25],
    [3, 23, 28],
    [5, 34, 39],
    [7, 37, 14],
    [46, 43, 16],
    [48, 41, 32],
    [50, 30, 21],
    [52, 10, 19],
]

edgeConnections = [
    [2, 24],
    [4, 35],
    [6, 38],
    [8, 13],
    [47, 42],
    [49, 31],
    [51, 20],
    [53, 17],
    [15, 44],
    [11, 26],
    [22, 29],
    [33, 40],
]

def createCells(filename: str) -> list[cell.Cell]:
    rawCells = [""] * 55
    cells = [""] * 55
    # cells = []

    with open(f'./testInput/{filename}', 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            rawCells[i+1] = lines[i].strip()
    f.close()


    for i in range(1, len(rawCells)):
        if i <= 9:
            faceColor = 'W'
        elif i <= 18:
            faceColor = 'B'
        elif i <= 27:
            faceColor = 'R'
        elif i <= 36:
            faceColor = 'G'
        elif i <= 45:
            faceColor = 'O'
        else:
            faceColor = 'Y'
        
        cells[i] = cell.Cell(i, rawCells[i], faceColor)
        # cells.append(cell.Cell(i, rawCells[i], faceColor))



    for ec in edgeConnections:
        cells[ec[0]].setConnections([cells[ec[1]]])
        cells[ec[1]].setConnections([cells[ec[0]]])

    for cc in cornerConnections:
        for i in range(0, 3):
            tempCC = cc.pop(i)
            cell0 = cells[tempCC]
            cell0.setConnections([cells[cc[0]], cells[cc[1]]])
            cc.insert(i, tempCC)    

    # cells.pop(0)
    # print(cells)
    return cells