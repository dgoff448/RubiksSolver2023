"""
File: cube.py
Author: David Goff
Date: 6/19/24
Description: A class reprenting the rubik's cube and how it moves.
"""

colorMap = {
    1:'white',
    2:'white', 
    3:'white', 
    4:'white', 
    5:'white', 
    6:'white', 
    7:'white', 
    8:'white', 
    9:'white', 
    10:'blue', 
    11:'blue', 
    12:'blue', 
    13:'blue', 
    14:'blue', 
    15:'blue', 
    16:'blue', 
    17:'blue', 
    18:'blue', 
    19:'red',  
    20:'red',  
    21:'red',  
    22:'red',  
    23:'red',  
    24:'red',  
    25:'red',  
    26:'red',  
    27:'red',  
    28:'green',
    29:'green',
    30:'green',
    31:'green',
    32:'green',
    33:'green',
    34:'green',
    35:'green',
    36:'green',
    37:'orange',
    38:'orange',
    39:'orange',
    40:'orange',
    41:'orange',
    42:'orange',
    43:'orange',
    44:'orange',
    45:'orange',
    46:'yellow',
    47:'yellow',
    48:'yellow',
    49:'yellow',
    50:'yellow',
    51:'yellow',
    52:'yellow',
    53:'yellow',
    54:'yellow'
}


class Cube:
    def __init__(self, cells: list):
        self.cells = cells
        self.instructions = []
    
    # trades slice a to b with slice c to d
    def trade(self, a: int, b: int, c: int, d: int):
        if a < c and b < d:
            arr = self.cells
            s1 = arr[:a]
            s2 = arr[a:b]
            s3 = arr[b:c]
            s4 = arr[c:d]
            s5 = arr[d:]
        else:
            s1 = arr[:c]
            s2 = arr[c:d]
            s3 = arr[d:a]
            s4 = arr[a:b]
            s5 = arr[b:]
        
        # print(s1, s2, s3, s4, s5)
        self.cells = s1 + s4 + s3 + s2 + s5
    
    def swop(self, a:int, b:int, c:int, d:int, cellSlice=[]):
        arr = self.cells
        if cellSlice == []:
            # Take a slice of the array from a to b,
            # swap it with slice c to d,
            # pop the slice c to d.
            if a < c and b < d:
                s1 = arr[:a]
                s2 = arr[a:b]
                s3 = arr[b:c]
                s4 = arr[c:d]
                s5 = arr[d:]

                # print(s1, s2, s3, s4, s5)
                self.cells = s1 + [-1]*len(s2) + s3 + s2 + s5
                return s4
            else:
                s1 = arr[:c]
                s2 = arr[c:d]
                s3 = arr[d:a]
                s4 = arr[a:b]
                s5 = arr[b:]

                # print(s1, s2, s3, s4, s5)
                self.cells = s1 + s4 + s3 + [-1]*len(s4) + s5
                return s2
        else:
            # swap cellSlice with slice a to b,
            # pop slice a to b
            s1 = arr[:a]
            s2 = arr[a:b]
            s3 = arr[b:]
            self.cells = s1 + cellSlice + s3
            return s2

    def breakTrade(self, a:int, b:int, c:int, d:int, cellSlice:list):
        slice0, slice1 = cellSlice[:2], cellSlice[2:]
        arr = self.cells
        s1 = arr[:a]
        s2 =  arr[a:b]
        s3 = arr[b:c]
        s4 = arr[c:d]
        s5 = arr[d:]

        self.cells = s1 + slice1 + s3 + slice0 + s5
        return s4 + s2

    def checkMove(self, moveType:str, arr:list):
        if arr != [-1, -1, -1]:
            print(self)
            raise(Exception(f"Error: {moveType} didn't end with [-1, -1, -1]!"))

    def updateCellData(self):
        colorMap = {1:'W', 2:'W', 3:'W', 4:'W', 5:'W', 6:'W', 7:'W', 8:'W', 9:'W',
                10:'B', 11:'B', 12:'B', 13:'B', 14:'B', 15:'B', 16:'B', 17:'B', 18:'B',
                19:'R', 20:'R', 21:'R', 22:'R', 23:'R', 24:'R', 25:'R', 26:'R', 27:'R',
                28:'G', 29:'G', 30:'G', 31:'G', 32:'G', 33:'G', 34:'G', 35:'G', 36:'G',
                37:'O', 38:'O', 39:'O', 40:'O', 41:'O', 42:'O', 43:'O', 44:'O', 45:'O',
                46:'Y', 47:'Y', 48:'Y', 49:'Y', 50:'Y', 51:'Y', 52:'Y', 53:'Y', 54:'Y'
        }
        for i in range(1, len(self.cells)):
            self.cells[i].updatePosition(i)
            self.cells[i].updateColor(colorMap[i])

    def white_CW(self):
        self.trade(1, 7, 7, 9) # rotating white cells CW
        
        blue = [self.cells[12], self.cells[13], self.cells[14]]
        self.cells[12], self.cells[13], self.cells[14] = -1, -1, -1

        red = [self.cells[23], self.cells[24], self.cells[25]]
        self.cells[23], self.cells[24], self.cells[25] = blue[0], blue[1], blue[2]

        green = [self.cells[28], self.cells[34], self.cells[35]]
        self.cells[28], self.cells[34], self.cells[35] = red[2], red[0], red[1]

        orange = [self.cells[37], self.cells[38], self.cells[39]]
        self.cells[37], self.cells[38], self.cells[39] = green[1], green[2], green[0]

        self.cells[12], self.cells[13], self.cells[14] = orange[0], orange[1], orange[2]

        self.updateCellData()
        self.instructions.append('W-CW')

    def white_CCW(self):
        self.trade(1, 3, 3, 9) # rotating white cells CCW
        
        blue = [self.cells[12], self.cells[13], self.cells[14]]
        self.cells[12], self.cells[13], self.cells[14] = -1, -1, -1

        orange = [self.cells[37], self.cells[38], self.cells[39]]
        self.cells[37], self.cells[38], self.cells[39] = blue[0], blue[1], blue[2]

        green = [self.cells[28], self.cells[34], self.cells[35]]
        self.cells[28], self.cells[34], self.cells[35] = orange[2], orange[0], orange[1]

        red = [self.cells[23], self.cells[24], self.cells[25]]
        self.cells[23], self.cells[24], self.cells[25] = green[1], green[2], green[0]

        self.cells[12], self.cells[13], self.cells[14] = red[0], red[1], red[2]

        self.updateCellData()
        self.instructions.append('W-CCW')
        
    def white_Dub(self):
        self.trade(1, 5, 5, 9) # rotating white cells Double

        blue = [self.cells[12], self.cells[13], self.cells[14]]
        green = [self.cells[28], self.cells[34], self.cells[35]]
        self.cells[12], self.cells[13], self.cells[14] = green[1], green[2], green[0]
        self.cells[28], self.cells[34], self.cells[35] = blue[2], blue[0], blue[1]

        red = [self.cells[23], self.cells[24], self.cells[25]]
        orange = [self.cells[37], self.cells[38], self.cells[39]]
        self.cells[23], self.cells[24], self.cells[25] = orange[0], orange[1], orange[2]
        self.cells[37], self.cells[38], self.cells[39] = red[0], red[1], red[2]

        self.updateCellData()
        self.instructions.append('W-Dub')

    def blue_CW(self):
        self.trade(10, 16, 16, 18) # rotating blue cells CW

        white = [self.cells[1], self.cells[7], self.cells[8]]
        self.cells[1], self.cells[7], self.cells[8] = -1, -1, -1
        
        orange = [self.cells[37], self.cells[43], self.cells[44]]
        self.cells[37], self.cells[43], self.cells[44] = white[0], white[1], white[2]

        yellow = [self.cells[46], self.cells[52], self.cells[53]]
        self.cells[46], self.cells[52], self.cells[53] = orange[0], orange[1], orange[2]

        red = [self.cells[19], self.cells[25], self.cells[26]]
        self.cells[19], self.cells[25], self.cells[26] = yellow[0], yellow[1], yellow[2]

        self.cells[1], self.cells[7], self.cells[8] = red[0], red[1], red[2]

        self.updateCellData()
        self.instructions.append('B-CW')

    def blue_CCW(self):
        self.trade(10, 12, 12, 18) # rotating blue cells CCW

        white = [self.cells[1], self.cells[7], self.cells[8]]
        self.cells[1], self.cells[7], self.cells[8] = -1, -1, -1

        red = [self.cells[19], self.cells[25], self.cells[26]]
        self.cells[19], self.cells[25], self.cells[26] = white[0], white[1], white[2]

        yellow = [self.cells[46], self.cells[52], self.cells[53]]
        self.cells[46], self.cells[52], self.cells[53] = red[0], red[1], red[2]

        orange = [self.cells[37], self.cells[43], self.cells[44]]
        self.cells[37], self.cells[43], self.cells[44] = yellow[0], yellow[1], yellow[2]

        self.cells[1], self.cells[7], self.cells[8] = orange[0], orange[1], orange[2]

        self.updateCellData()
        self.instructions.append('B-CCW')

    def blue_Dub(self):
        self.trade(10, 14, 14, 18) # rotating blue cells Dub

        white = [self.cells[1], self.cells[7], self.cells[8]]
        yellow = [self.cells[46], self.cells[52], self.cells[53]]
        self.cells[46], self.cells[52], self.cells[53] = white[0], white[1], white[2]
        self.cells[1], self.cells[7], self.cells[8] = yellow[0], yellow[1], yellow[2] 

        red = [self.cells[19], self.cells[25], self.cells[26]]
        orange = [self.cells[37], self.cells[43], self.cells[44]]
        self.cells[19], self.cells[25], self.cells[26] = orange[0], orange[1], orange[2]
        self.cells[37], self.cells[43], self.cells[44] = red[0], red[1], red[2]

        self.updateCellData()
        self.instructions.append('B-Dub')

    def red_CW(self):
        self.trade(19, 25, 25, 27)

        white = [self.cells[1], self.cells[2], self.cells[3]]
        self.cells[1], self.cells[2], self.cells[3] = -1, -1, -1

        blue = [self.cells[10], self.cells[11], self.cells[12]]
        self.cells[10], self.cells[11], self.cells[12] = white[0], white[1], white[2]

        yellow = [self.cells[50], self.cells[51], self.cells[52]]
        self.cells[50], self.cells[51], self.cells[52] = blue[0], blue[1], blue[2]

        green = [self.cells[28], self.cells[29], self.cells[30]]
        self.cells[28], self.cells[29], self.cells[30] = yellow[0], yellow[1], yellow[2]

        self.cells[1], self.cells[2], self.cells[3] = green[0], green[1], green[2]

        self.updateCellData()
        self.instructions.append('R-CW')
        
    def red_CCW(self):
        self.trade(19, 21, 21, 27)

        white = [self.cells[1], self.cells[2], self.cells[3]]
        self.cells[1], self.cells[2], self.cells[3] = -1, -1, -1

        green = [self.cells[28], self.cells[29], self.cells[30]]
        self.cells[28], self.cells[29], self.cells[30] = white[0], white[1], white[2]

        yellow = [self.cells[50], self.cells[51], self.cells[52]]
        self.cells[50], self.cells[51], self.cells[52] = green[0], green[1], green[2]

        blue = [self.cells[10], self.cells[11], self.cells[12]]
        self.cells[10], self.cells[11], self.cells[12] = yellow[0], yellow[1], yellow[2]

        self.cells[1], self.cells[2], self.cells[3] = blue[0], blue[1], blue[2]

        self.updateCellData()
        self.instructions.append('R-CCW')

    def red_Dub(self):
        self.trade(19, 23, 23, 27)

        white = [self.cells[1], self.cells[2], self.cells[3]]
        yellow = [self.cells[50], self.cells[51], self.cells[52]]
        self.cells[1], self.cells[2], self.cells[3] = yellow[0], yellow[1], yellow[2]
        self.cells[50], self.cells[51], self.cells[52] = white[0], white[1], white[2]

        blue = [self.cells[10], self.cells[11], self.cells[12]]
        green = [self.cells[28], self.cells[29], self.cells[30]]
        self.cells[10], self.cells[11], self.cells[12] = green[0], green[1], green[2]
        self.cells[28], self.cells[29], self.cells[30] = blue[0], blue[1], blue[2]

        self.updateCellData()
        self.instructions.append('R-Dub')

    def green_CW(self):
        self.trade(28, 34, 34, 36)

        white = [self.cells[3], self.cells[4], self.cells[5]]
        self.cells[3], self.cells[4], self.cells[5] = -1, -1, -1

        red = [self.cells[21], self.cells[22], self.cells[23]]
        self.cells[21], self.cells[22], self.cells[23] = white[0], white[1], white[2]

        yellow = [self.cells[48], self.cells[49], self.cells[50]]
        self.cells[48], self.cells[49], self.cells[50] = red[0], red[1], red[2]

        orange = [self.cells[39], self.cells[40], self.cells[41]]
        self.cells[39], self.cells[40], self.cells[41] = yellow[0], yellow[1], yellow[2]

        self.cells[3], self.cells[4], self.cells[5] = orange[0], orange[1], orange[2]

        self.updateCellData()
        self.instructions.append('G-CW')
        
    def green_CCW(self):
        self.trade(28, 30, 30, 36)

        white = [self.cells[3], self.cells[4], self.cells[5]]
        self.cells[3], self.cells[4], self.cells[5] = -1, -1, -1

        orange = [self.cells[39], self.cells[40], self.cells[41]]
        self.cells[39], self.cells[40], self.cells[41] = white[0], white[1], white[2]

        yellow = [self.cells[48], self.cells[49], self.cells[50]]
        self.cells[48], self.cells[49], self.cells[50] = orange[0], orange[1], orange[2]

        red = [self.cells[21], self.cells[22], self.cells[23]]
        self.cells[21], self.cells[22], self.cells[23] = yellow[0], yellow[1], yellow[2]

        self.cells[3], self.cells[4], self.cells[5] = red[0], red[1], red[2]

        self.updateCellData()
        self.instructions.append('G-CCW')

    def green_Dub(self):
        self.trade(28, 32, 32, 36)

        white = [self.cells[3], self.cells[4], self.cells[5]]
        yellow = [self.cells[48], self.cells[49], self.cells[50]]
        self.cells[3], self.cells[4], self.cells[5] = yellow[0], yellow[1], yellow[2]
        self.cells[48], self.cells[49], self.cells[50] = white[0], white[1], white[2]

        red = [self.cells[21], self.cells[22], self.cells[23]]
        orange = [self.cells[39], self.cells[40], self.cells[41]]
        self.cells[21], self.cells[22], self.cells[23] = orange[0], orange[1], orange[2]
        self.cells[39], self.cells[40], self.cells[41] = red[0], red[1], red[2]

        self.updateCellData()
        self.instructions.append('G-Dub')

    def orange_CW(self):
        self.trade(37, 43, 43, 45)

        white = [self.cells[5], self.cells[6], self.cells[7]]
        self.cells[5], self.cells[6], self.cells[7] = -1, -1, -1

        green = [self.cells[32], self.cells[33], self.cells[34]]
        self.cells[32], self.cells[33], self.cells[34] = white[0], white[1], white[2]

        yellow = [self.cells[46], self.cells[47], self.cells[48]]
        self.cells[46], self.cells[47], self.cells[48] = green[0], green[1], green[2]

        blue = [self.cells[14], self.cells[15], self.cells[16]]
        self.cells[14], self.cells[15], self.cells[16] = yellow[0], yellow[1], yellow[2]

        self.cells[5], self.cells[6], self.cells[7] = blue[0], blue[1], blue[2]

        self.updateCellData()
        self.instructions.append('O-CW')

    def orange_CCW(self):
        self.trade(37, 39, 39, 45)

        white = [self.cells[5], self.cells[6], self.cells[7]]
        self.cells[5], self.cells[6], self.cells[7] = -1, -1, -1

        blue = [self.cells[14], self.cells[15], self.cells[16]]
        self.cells[14], self.cells[15], self.cells[16] = white[0], white[1], white[2]

        yellow = [self.cells[46], self.cells[47], self.cells[48]]
        self.cells[46], self.cells[47], self.cells[48] = blue[0], blue[1], blue[2]

        green = [self.cells[32], self.cells[33], self.cells[34]]
        self.cells[32], self.cells[33], self.cells[34] = yellow[0], yellow[1], yellow[2]

        self.cells[5], self.cells[6], self.cells[7] = green[0], green[1], green[2]

        self.updateCellData()
        self.instructions.append('O-CCW')

    def orange_Dub(self):
        self.trade(37, 41, 41, 45)

        white = [self.cells[5], self.cells[6], self.cells[7]]
        yellow = [self.cells[46], self.cells[47], self.cells[48]]
        self.cells[5], self.cells[6], self.cells[7] = yellow[0], yellow[1], yellow[2]
        self.cells[46], self.cells[47], self.cells[48] = white[0], white[1], white[2]

        blue = [self.cells[14], self.cells[15], self.cells[16]]
        green = [self.cells[32], self.cells[33], self.cells[34]]
        self.cells[14], self.cells[15], self.cells[16] = green[0], green[1], green[2]
        self.cells[32], self.cells[33], self.cells[34] = blue[0], blue[1], blue[2]

        self.updateCellData()
        self.instructions.append('O-Dub')

    def yellow_CW(self):
        self.trade(46, 52, 52, 54)

        blue = [self.cells[10], self.cells[16], self.cells[17]]
        self.cells[10], self.cells[16], self.cells[17] = -1, -1, -1

        orange = [self.cells[41], self.cells[42], self.cells[43]]
        self.cells[41], self.cells[42], self.cells[43] = blue[1], blue[2], blue[0]

        green = [self.cells[30], self.cells[31], self.cells[32]]
        self.cells[30], self.cells[31], self.cells[32] = orange[0], orange[1], orange[2]

        red = [self.cells[19], self.cells[20], self.cells[21]]
        self.cells[19], self.cells[20], self.cells[21] = green[0], green[1], green[2]

        self.cells[10], self.cells[16], self.cells[17] = red[2], red[0], red[1]

        self.updateCellData()
        self.instructions.append('Y-CW')

    def yellow_CCW(self):
        self.trade(46, 48, 48, 54)

        blue = [self.cells[10], self.cells[16], self.cells[17]]
        self.cells[10], self.cells[16], self.cells[17] = -1, -1, -1

        red = [self.cells[19], self.cells[20], self.cells[21]]
        self.cells[19], self.cells[20], self.cells[21] = blue[1], blue[2], blue[0]

        green = [self.cells[30], self.cells[31], self.cells[32]]
        self.cells[30], self.cells[31], self.cells[32] = red[0], red[1], red[2]

        orange = [self.cells[41], self.cells[42], self.cells[43]]
        self.cells[41], self.cells[42], self.cells[43] = green[0], green[1], green[2]

        self.cells[10], self.cells[16], self.cells[17] = orange[2], orange[0], orange[1]

        self.updateCellData()
        self.instructions.append('Y-CCW')

    def yellow_Dub(self):
        self.trade(46, 50, 50, 54)

        blue = [self.cells[10], self.cells[16], self.cells[17]]  
        green = [self.cells[30], self.cells[31], self.cells[32]]
        self.cells[10], self.cells[16], self.cells[17] = green[2], green[0], green[1]
        self.cells[30], self.cells[31], self.cells[32] = blue[1], blue[2], blue[0]

        red = [self.cells[19], self.cells[20], self.cells[21]]
        orange = [self.cells[41], self.cells[42], self.cells[43]]
        self.cells[19], self.cells[20], self.cells[21] = orange[0], orange[1], orange[2]
        self.cells[41], self.cells[42], self.cells[43] = red[0], red[1], red[2]

        self.updateCellData()
        self.instructions.append('Y-Dub')

    def __str__(self):
        return " ".join([str(cell) for cell in self.cells])[1:]