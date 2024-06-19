"""
File: connections.py
Author: David Goff
Date: 6/19/24
Description: Dictionaries and lists categorizing the cells and what they are connected to.
"""

cellKey = {
    1 : 'W1', 2 : 'W2', 3 : 'W3', 4 : 'W4', 5 : 'W5', 6 : 'W6', 7 : 'W7', 8 : 'W8', 9 : 'W9',
    10: 'B1', 11: 'B2', 12: 'B3', 13: 'B4', 14: 'B5', 15: 'B6', 16: 'B7', 17: 'B8', 18: 'B9',
    19: 'R1', 20: 'R2', 21: 'R3', 22: 'R4', 23: 'R5', 24: 'R6', 25: 'R7', 26: 'R8', 27: 'R9',
    28: 'G1', 29: 'G2', 30: 'G3', 31: 'G4', 32: 'G5', 33: 'G6', 34: 'G7', 35: 'G8', 36: 'G9',
    37: 'O1', 38: 'O2', 39: 'O3', 40: 'O4', 41: 'O5', 42: 'O6', 43: 'O7', 44: 'O8', 45: 'O9',
    46: 'Y1', 47: 'Y2', 48: 'Y3', 49: 'Y4', 50: 'Y5', 51: 'Y6', 52: 'Y7', 53: 'Y8', 54: 'Y9',
}

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

edgeConnectionDict = {
    'WR' : 2,
    'RW' : 24,
    'WG' : 4,
    'GW' : 35,
    'WO' : 6,
    'OW' : 38,
    'WB' : 8,
    'BW' : 13,
    'YO' : 47,
    'OY' : 42,
    'YG' : 49,
    'GY' : 31,
    'YR' : 51,
    'RY' : 20,
    'YB' : 53,
    'BY' : 17,
    'BR' : 11,
    'RB' : 26,
    'RG' : 22,
    'GR' : 29,
    'GO' : 33,
    'OG' : 40,
    'OB' : 44,
    'BO' : 15
}

cornerConnectionDict = {
    'WBR' : 1,
    'WRB' : 1,
    'BWR' : 12,
    'BRW' : 12,
    'RBW' : 25,
    'RWB' : 25,
    'WRG' : 3,
    'WGR' : 3,
    'RWG' : 23,
    'RGW' : 23,
    'GRW' : 28,
    'GWR' : 28,
    'WGO' : 5,
    'WOG' : 5,
    'GWO' : 34,
    'GOW' : 34,
    'OGW' : 39,
    'OWG' : 39,
    'WOB' : 7,
    'WBO' : 7,
    'OWB' : 37,
    'OBW' : 37,
    'BOW' : 14,
    'BWO' : 14,
    'YBO' : 46,
    'YOB' : 46,
    'BYO' : 16,
    'BOY' : 16,
    'OBY' : 43,
    'OYB' : 43,
    'YOG' : 48,
    'YGO' : 48,
    'OYG' : 41,
    'OGY' : 41,
    'GOY' : 32,
    'GYO' : 32,
    'YRG' : 50,
    'YGR' : 50,
    'RYG' : 21,
    'RGY' : 21,
    'GRY' : 30,
    'GYR' : 30,
    'YBR' : 52,
    'YRB' : 52,
    'BYR' : 10,
    'BRY' : 10,
    'RBY' : 19,
    'RYB' : 19
}

edgeConnectionCells = [
    ['W2', 'R6'],
    ['W4', 'G8'],
    ['W6', 'O2'],
    ['W8', 'B4'],
    ['Y2', 'O6'],
    ['Y4', 'G4'],
    ['Y6', 'R2'],
    ['Y8', 'B8'],
    ['B2', 'R8'],
    ['R4', 'G2'],
    ['G6', 'O4'],
    ['O8', 'B6'],
]

cornerConnectionColors = [
    ['W', 'B', 'R'],
    ['W', 'R', 'G'],
    ['W', 'G', 'O'],
    ['W', 'O', 'B'],
    ['Y', 'B', 'O'],
    ['Y', 'O', 'G'],
    ['Y', 'R', 'G'],
    ['Y', 'B', 'R'],
]

edgeConnectionColors = [
    ['W', 'R'],
    ['W', 'G'],
    ['W', 'O'],
    ['W', 'B'],
    ['Y', 'O'],
    ['Y', 'G'],
    ['Y', 'R'],
    ['Y', 'B'],
    ['B', 'R'],
    ['R', 'G'],
    ['G', 'O'],
    ['O', 'B'],
]

