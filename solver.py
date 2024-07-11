"""
File: solver.py
Author: David Goff
Date: 6/19/24
Description: A class for solving the current cube configuration.

    Order of Operations:
        1. White Cross
        2. White Corners
        3. Middle Layer
        4. Yellow Cross
        5. Yellow Corners

"""
import cube
import cell

class Solver:
    
    def __init__(self, simCube):
        self.simCube = simCube

    def solveWhiteCross(self):
        colorFunctionDict = {               # Maps the color string with the actual move to be dynamically called later
            'BCW': self.simCube.blue_CW, 
            'RCW': self.simCube.red_CW, 
            'GCW': self.simCube.green_CW, 
            'OCW': self.simCube.orange_CW,
            'BCCW': self.simCube.blue_CCW, 
            'RCCW': self.simCube.red_CCW, 
            'GCCW': self.simCube.green_CCW, 
            'OCCW': self.simCube.orange_CCW,
            'BDub': self.simCube.blue_Dub, 
            'RDub': self.simCube.red_Dub, 
            'GDub': self.simCube.green_Dub, 
            'ODub': self.simCube.orange_Dub
        } 

        # White Cross Cells = 2, 4, 6, 8
        white_cross_cells = []
        for i in range(1, len(self.simCube.cells)):            # Finds the white cross cells
            cell = self.simCube.cells[i]
            if cell.actCell in [2, 4, 6, 8]:
                white_cross_cells.append(cell)
            if len(white_cross_cells) == 4:
                break

        white_to_yellow = {6:47, 4:49, 2:51, 8:53}
        for cell in white_cross_cells:
            print([cell.curCell for cell in white_cross_cells]) # TESTING
            print(f"Solving {cell.actCell} at {cell}")

            short_solve1 = {2:11, 4:22, 6:33, 8:44}             # Cell is on 11, 22, 33, 44
            short_solve2 = ['2:29', '4:40', '6:15', '8:26']     # Cell is on 15, 26, 29, 40
            adjColor = cell.connections[0].color                # Color of connected cell
            adjCurColor = cell.connections[0].curColor
            curColor = cell.curColor                            # Color of current cell's side
            colorOrder = ['B', 'O', 'G', 'R']

            if cell.curCell == cell.actCell:
                pass
            elif cell.curCell in [2, 4, 6, 8]:
                if colorOrder[colorOrder.index(adjColor)-3] == adjCurColor:
                    colorFunctionDict[adjCurColor + 'Dub']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[adjColor + 'Dub']()
                elif colorOrder[colorOrder.index(adjCurColor)-2] == adjColor:
                    colorFunctionDict[adjCurColor + 'Dub']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[adjColor + 'Dub']()
                else:
                    colorFunctionDict[adjCurColor + 'Dub']()
                    self.simCube.yellow_CW()
                    colorFunctionDict[adjColor + 'Dub']()

            elif cell.curCell > 46:                   # Cell is on the yellow side
                pos = white_to_yellow[cell.actCell] - cell.curCell

                # Priming cell for move
                if pos in [-4, 4]:
                    self.simCube.yellow_Dub()
                elif pos in [-2, 6]:
                    self.simCube.yellow_CCW()
                elif pos in [2, -6]:
                    self.simCube.yellow_CW()
                
                colorFunctionDict[adjColor + 'Dub']()
                
            # elif int(cell.actCell // 2) * 11 == short_solve1[cell.actCell]:   # Cell is on 11, 22, 33, 44
            elif cell.curCell in [11, 22, 33, 44]:      # Cell is on 11, 22, 33, 44
                if adjColor == adjCurColor:
                    colorFunctionDict[adjColor + 'CCW']()
                elif colorOrder[colorOrder.index(curColor)-2] == adjColor:
                    self.simCube.white_CCW()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CCW']()   # Calls move function corresponding with the given color key
                    self.simCube.white_CW()
                elif colorOrder[colorOrder.index(curColor)-3] == adjColor:
                    self.simCube.white_Dub()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-1] + 'CCW']()   # Calls move function corresponding with the given color key
                    self.simCube.white_Dub()
                else:
                    self.simCube.white_CW()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-1] + 'CCW']()   # Calls move function corresponding with the given color key
                    self.simCube.white_CCW()
                
            # elif str(cell.actCell) + ':' + str(cell.curCell) in short_solve2:   # Cell is on 15, 26, 29, 40
            elif cell.curCell in [15, 26, 29, 40]:   # Cell is on 15, 26, 29, 40
                if adjColor == adjCurColor:
                    colorFunctionDict[adjColor + 'CW']()
                elif colorOrder[colorOrder.index(curColor)-2] == adjColor:
                    self.simCube.white_CW()
                    colorFunctionDict[adjCurColor + 'CW']()    # Calls move function corresponding with the given color key
                    self.simCube.white_CCW()
                elif colorOrder[colorOrder.index(curColor)-1] == adjColor:
                    self.simCube.white_Dub()
                    colorFunctionDict[adjCurColor + 'CW']()    # Calls move function corresponding with the given color key
                    self.simCube.white_Dub()
                else:
                    self.simCube.white_CCW()
                    colorFunctionDict[adjCurColor + 'CW']()      # Calls move function corresponding with the given color key
                    self.simCube.white_CW()

            elif cell.curCell in [17, 20, 31, 42]:    # White Cross Side Bottom
                Opps = {'B':'G', 'G':'B', 'R':'O', 'O':'R'}
                if curColor == adjColor:
                    self.simCube.yellow_CW()
                elif curColor == Opps[adjColor]:
                    self.simCube.yellow_CCW()
                elif colorOrder[colorOrder.index(curColor)-3] == adjColor:
                    self.simCube.yellow_Dub()
                
                colorFunctionDict[adjColor + 'CW']()
                colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CW']()
                colorFunctionDict[adjColor + 'CCW']()
                colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CCW']()

            elif cell.curCell in [13, 24, 35, 38]: # White Cross Side Top
                Opps = {'B':'G', 'G':'B', 'R':'O', 'O':'R'}
                if adjColor == Opps[curColor]:
                    colorFunctionDict[curColor + 'CCW']()
                    self.simCube.white_CCW()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-1] + 'CCW']()
                    self.simCube.white_CW()
                elif adjColor == colorOrder[colorOrder.index(curColor)-1]:
                    colorFunctionDict[curColor + 'CCW']()
                    colorFunctionDict[adjColor + 'CCW']()
                elif curColor == colorOrder[colorOrder.index(adjColor)-1]:
                    colorFunctionDict[curColor + 'CW']()
                    colorFunctionDict[adjColor + 'CW']()
                else:
                    colorFunctionDict[curColor + 'CCW']()
                    self.simCube.white_CW()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-1] + 'CCW']()
                    self.simCube.white_CCW()
                
            else:
                raise Exception(f"ERROR: {cell.curCell} is not a valid placement for white edge cell.")
            print(self.simCube.instructions)    # TESTING
            print()
            self.simCube.instructions.clear()   # TESTING
        
    def solveWhiteCorners(self):
        colorFunctionDict = {               # Maps the color string with the actual move to be dynamically called later
            'BCW': self.simCube.blue_CW, 
            'RCW': self.simCube.red_CW, 
            'GCW': self.simCube.green_CW, 
            'OCW': self.simCube.orange_CW,
            'BCCW': self.simCube.blue_CCW, 
            'RCCW': self.simCube.red_CCW, 
            'GCCW': self.simCube.green_CCW, 
            'OCCW': self.simCube.orange_CCW,
            'BDub': self.simCube.blue_Dub, 
            'RDub': self.simCube.red_Dub, 
            'GDub': self.simCube.green_Dub, 
            'ODub': self.simCube.orange_Dub
        } 

        # White Corner Cells = 1, 3, 5, 7
        white_corner_cells = []
        for i in range(1, len(self.simCube.cells)):            # Finds the white corner cells
            cell = self.simCube.cells[i]
            if cell.actCell in [1, 3, 5, 7]:
                white_corner_cells.append(cell)
            if len(white_corner_cells) == 4:
                break

        for cell in white_corner_cells:
            print([cell.curCell for cell in white_corner_cells]) # TESTING
            print(f"Solving {cell.actCell} at {cell}")

            adjColor = (cell.connections[0].color) if cell.connections[0].curColor != 'W' else (cell.connections[1].color)         # Color of connected cell that is not on white
            curColor = cell.curColor                            # Color of current cell's side
            colorOrder = ['B', 'O', 'G', 'R']

            if cell.curCell == cell.actCell:
                pass
            elif cell.curCell in [12, 23, 34, 37]:    # White Corners Side Left Top
                if curColor == colorOrder[colorOrder.index(adjColor)-1]:                        
                    colorFunctionDict[curColor + 'CCW']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[curColor + 'Dub']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[curColor + 'CCW']()
                elif curColor == colorOrder[colorOrder.index(adjColor)-2]:                      
                    colorFunctionDict[curColor + 'CCW']()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-3] + 'CW']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-3] + 'CCW']()
                    colorFunctionDict[curColor + 'CW']()
                elif curColor == colorOrder[colorOrder.index(adjColor)-3]:                       
                    colorFunctionDict[curColor + 'CCW']()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CW']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CCW']()
                    colorFunctionDict[curColor + 'CW']()
                else:                                                                           
                    colorFunctionDict[curColor + 'CCW']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[curColor + 'CW']()
                    self.simCube.yellow_CW()
                    colorFunctionDict[curColor + 'CCW']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[curColor + 'CW']()

            elif cell.curCell in [10, 21, 32, 43]:  # White Corners Side Left Bottom
                adjColor = (cell.connections[0].color) if cell.connections[0].curColor != 'Y' else (cell.connections[1].color)         # Color of connected cell that is not on white
                
                if curColor == colorOrder[colorOrder.index(adjColor)-2]:    # 
                    colorFunctionDict[adjColor + 'CW']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[adjColor + 'CCW']()
                elif curColor == colorOrder[colorOrder.index(adjColor)-1]:  # Opposite Corner
                    colorFunctionDict[adjColor + 'CW']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[adjColor + 'CCW']()
                elif curColor == colorOrder[colorOrder.index(adjColor)-3]:  # 
                    self.simCube.yellow_CW()
                    colorFunctionDict[adjColor + 'CW']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[adjColor + 'CCW']()
                else: # curColor == adjColor:
                    self.simCube.yellow_CCW()
                    colorFunctionDict[adjColor + 'CW']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[adjColor + 'CCW']()
                    

            elif cell.curCell in [16, 19, 30, 41]:  # White Corners Side Right Bottom
                adjColor = (cell.connections[0].color) if cell.connections[0].curColor != 'Y' else (cell.connections[1].color)         # Color of connected cell that is not on white

                if curColor == colorOrder[colorOrder.index(adjColor)-2]:
                    colorFunctionDict[adjColor + 'CCW']()
                    self.simCube.yellow_CW()
                    colorFunctionDict[adjColor + 'CW']()
                elif curColor == colorOrder[colorOrder.index(adjColor)-3]:
                    colorFunctionDict[adjColor + 'CCW']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[adjColor + 'CW']()
                elif curColor == adjColor:
                    self.simCube.yellow_CW()
                    colorFunctionDict[adjColor + 'CCW']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[adjColor + 'CW']()
                else:
                    self.simCube.yellow_CCW()
                    colorFunctionDict[adjColor + 'CCW']()
                    self.simCube.yellow_CW()
                    colorFunctionDict[adjColor + 'CW']()
            
            elif cell.curCell in [14, 25, 28, 39]:  # White Corners Side Right Top
                if curColor == colorOrder[colorOrder.index(adjColor)-1]:
                    colorFunctionDict[curColor + 'CW']()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CCW']()
                    self.simCube.yellow_CW()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CW']()
                    colorFunctionDict[curColor + 'CCW']()
                elif curColor == colorOrder[colorOrder.index(adjColor)-2]:
                    colorFunctionDict[curColor + 'CW']()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CCW']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CW']()
                    colorFunctionDict[curColor + 'CCW']()
                elif curColor == colorOrder[colorOrder.index(adjColor)-3]:
                    colorFunctionDict[curColor + 'Dub']()
                    self.simCube.yellow_CW()
                    colorFunctionDict[adjColor + 'CW']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[adjColor + 'Dub']()
                    colorFunctionDict[curColor + 'Dub']()
                    colorFunctionDict[adjColor + 'CW']()
                else:
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CCW']()
                    self.simCube.yellow_CW()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CW']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CCW']()
                    self.simCube.yellow_CW()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CW']()

            elif cell.curCell in [46, 48, 50, 52]:      # White Corners on Yellow
                curToAct = {52:1, 50:3, 48:5, 46:7}
                acts = [1, 3, 5, 7]

                # Priming Position of Cell
                if curToAct[cell.curCell] != cell.actCell:
                    if acts[acts.index(cell.actCell)-1] == acts[acts.index(curToAct[cell.curCell])]:
                        self.simCube.yellow_CCW()
                    elif acts[acts.index(cell.actCell)-2] == acts[acts.index(curToAct[cell.curCell])]:
                        self.simCube.yellow_Dub()
                    else:   # -3
                        self.simCube.yellow_CW()

                # Distinguishing between left or right connections
                if colorOrder[colorOrder.index(cell.connections[0].curColor)-1] == colorOrder[colorOrder.index(cell.connections[1].curColor)]:
                    left, right = cell.connections[0], cell.connections[1]
                else:
                    left, right = cell.connections[1], cell.connections[0]
                rightColor = right.curColor
                leftColor = left.curColor

                # Moves to put cell in place
                colorFunctionDict[rightColor + 'CW']()
                self.simCube.yellow_Dub()
                colorFunctionDict[rightColor + 'CCW']()
                self.simCube.yellow_Dub()
                colorFunctionDict[leftColor + 'CCW']()
                self.simCube.yellow_CW()
                colorFunctionDict[leftColor + 'CW']()

            elif cell.curCell in [1, 3, 5, 7]:          # White Corners on Wrong White
                acts = [1, 3, 5, 7]

                # Distinguishing between left or right connections
                if colorOrder[colorOrder.index(cell.connections[0].curColor)-1] == colorOrder[colorOrder.index(cell.connections[1].curColor)]:
                    right, left = cell.connections[0], cell.connections[1]
                else:
                    right, left = cell.connections[1], cell.connections[0]
                leftleftColor = colorOrder[colorOrder.index(left.curColor)-1]
                leftColor = left.curColor
                rightrightColor = colorOrder[colorOrder.index(right.curColor)-3]
                rightColor = right.curColor

                print(f"right: {right}, {right.curColor}, {right.curColor + 'CW'}")
                print(f"cell.actCell: {cell.actCell}, cell.curCell: {cell.curCell}")
                # Moves to put cell in place
                if acts[acts.index(cell.actCell)-1] == acts[acts.index(cell.curCell)]:      # If cell is CCW one space from where it should be
                    # colorFunctionDict[left.curColor + 'CW']()
                    # colorFunctionDict[leftleftColor + 'CW']()
                    # self.simCube.yellow_CCW()
                    # colorFunctionDict[leftleftColor + 'Dub']()
                    # colorFunctionDict[left.curColor + 'CCW']()  
                    # colorFunctionDict[leftleftColor + 'CW']()
                    colorFunctionDict[leftColor + 'CW']()
                    self.simCube.yellow_CW()
                    colorFunctionDict[leftColor + 'CCW']()
                    colorFunctionDict[leftleftColor + 'CW']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[leftleftColor + 'CCW']()
                elif acts[acts.index(cell.actCell)-2] == acts[acts.index(cell.curCell)]:    # If cell is opposite corner from where it should be
                    colorFunctionDict[left.curColor + 'CW']()
                    colorFunctionDict[rightrightColor + 'CW']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[rightrightColor + 'CCW']()
                    colorFunctionDict[leftColor + 'CCW']()
                else:                                                                       # If cell is CW one space from where it should be
                    colorFunctionDict[rightColor + 'CCW']()
                    self.simCube.yellow_CCW()
                    colorFunctionDict[rightColor + 'CW']()
                    colorFunctionDict[rightrightColor + 'CCW']()
                    self.simCube.yellow_Dub()
                    colorFunctionDict[rightrightColor + 'CW']()

            else:
                raise Exception(f"ERROR: {cell.curCell} is not a valid placement for white corner cell.")
            print(self.simCube.instructions)    # TESTING
            print()
            self.simCube.instructions.clear()   # TESTING
