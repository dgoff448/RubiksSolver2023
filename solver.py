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
        self.cube = simCube

    def solveWhiteCross(self):
        colorFunctionDict = {               # Maps the color string with the actual move to be dynamically called later
            'BCW': self.simCube.blueCW, 
            'RCW': self.simCube.redCW, 
            'GCW': self.simCube.greenCW, 
            'OCW': self.simCube.orangeCW,
            'BCCW': self.simCube.blueCCW, 
            'RCCW': self.simCube.redCCW, 
            'GCCW': self.simCube.greenCCW, 
            'OCCW': self.simCube.orangeCCW,
            'BDub': self.simCube.blueDub, 
            'RDub': self.simCube.redDub, 
            'GDub': self.simCube.greenDub, 
            'ODub': self.simCube.orangeDub
        } 

        # White Cross Cells = 2, 4, 6, 8
        white_cross_cells = []
        for cell in self.simCube.cells:             # Finds the white cross cells
            if cell.actCell in [2, 4, 6, 8]:
                white_cross_cells.append(cell)
            if len(white_cross_cells) == 4:
                break

        white_to_yellow = {6:47, 4:49, 2:51, 8:53}
        for cell in white_cross_cells:
            short_solve1 = {2:11, 4:22, 6:33, 8:44}             # Cell is on 11, 22, 33, 44
            short_solve2 = ['2:29', '4:40', '6:15', '8:26']     # Cell is on 15, 26, 29, 40
            adjColor = cell.connections[0].color                # Color of connected cell
            curColor = cell.curColor                            # Color of current cell's side
            colorOrder = ['B', 'O', 'G', 'R']

            if cell.curCell == cell.actCell:
                pass
            elif int(cell.actCell // 2) * 11 == short_solve1[cell.actCell]:   # Cell is on 11, 22, 33, 44
                if colorOrder[colorOrder.index(curColor)-2] == adjColor:
                    self.simCube.whiteCCW()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CCW']()   # Calls move function corresponding with the given color key
                    self.simCube.whiteCW()
                elif colorOrder[colorOrder.index(curColor)-3] == adjColor:
                    self.simCube.whiteDub()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-1] + 'CCW']()   # Calls move function corresponding with the given color key
                    self.simCube.whiteDub()
                else:
                    self.simCube.whiteCW()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-1] + 'CCW']()   # Calls move function corresponding with the given color key
                    self.simCube.whiteCCW()
                
            elif str(cell.actCell) + ':' + str(cell.curCell) in short_solve2:   # Cell is on 15, 26, 29, 40
                if colorOrder[colorOrder.index(curColor)-2] == adjColor:
                    self.simCube.whiteCW()
                    colorFunctionDict[curColor + 'CW']()    # Calls move function corresponding with the given color key
                    self.simCube.whiteCCW()
                elif colorOrder[colorOrder.index(curColor)-1] == adjColor:
                    self.simCube.whiteDub()
                    colorFunctionDict[curColor + 'CW']()    # Calls move function corresponding with the given color key
                    self.simCube.whiteDub()
                else:
                    self.simCube.whiteCCW()
                    colorFunctionDict[curColor + 'CW']      # Calls move function corresponding with the given color key
                    self.simCube.whiteCW()

            elif cell.curCell in [17, 20, 31, 42]:    # White Cross Side Bottom
                Opps = {'B':'G', 'G':'B', 'R':'O', 'O':'R'}
                if curColor == adjColor:
                    self.simCube.yellowCW()
                elif curColor == Opps[adjColor]:
                    self.simCube.yellowCCW()
                
                if colorOrder[colorOrder.index(curColor)-3] == adjColor:
                    colorFunctionDict[adjColor + 'CW']
                    colorFunctionDict[curColor + 'CW']
                    colorFunctionDict[adjColor + 'CCW']
                    colorFunctionDict[curColor + 'CCW']
                else:
                    colorFunctionDict[adjColor + 'CCW']
                    colorFunctionDict[curColor + 'CCW']
                    colorFunctionDict[adjColor + 'CW']
                    colorFunctionDict[curColor + 'CW']

            elif cell.curCell in [13, 24, 35, 38]: # White Cross Side Top
                Opps = {'B':'G', 'G':'B', 'R':'O', 'O':'R'}
                if adjColor == Opps[curColor]:
                    colorFunctionDict[curColor + 'CCW']
                    self.simCube.whiteCCw()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-1] + 'CCW']
                    self.simCube.whiteCW()
                elif adjColor == colorOrder[colorOrder.index(curColor)-1]:
                    colorFunctionDict[curColor + 'CCW']
                    colorFunctionDict[adjColor + 'CCW']
                elif curColor == colorOrder[colorOrder.index(adjColor)-1]:
                    colorFunctionDict[curColor + 'CW']
                    colorFunctionDict[adjColor + 'CW']
                else:
                    colorFunctionDict[curColor + 'CCW']
                    self.simCube.whiteCW()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-1] + 'CCW']
                    self.simCube.whiteCCW()

            elif cell.curCell > 46:                   # Cell is on the yellow side
                pos = white_to_yellow[cell.actCell] - cell.curCell
                if pos in [-4, 4]:
                    self.simCube.yellowDub()
                elif pos in [-2, 6]:
                    self.simCube.yellowCCW()
                elif pos in [2, -6]:
                    self.simCube.yellowCW()
                else:
                    raise Exception(f"ERROR: Position difference ({pos}) should not exist.")
                
            else:
                raise Exception(f"ERROR: {cell.curCell} is not a valid placement for white edge cell.")
            
    def solveWhiteCorners(self):
        colorFunctionDict = {               # Maps the color string with the actual move to be dynamically called later
            'BCW': self.simCube.blueCW, 
            'RCW': self.simCube.redCW, 
            'GCW': self.simCube.greenCW, 
            'OCW': self.simCube.orangeCW,
            'BCCW': self.simCube.blueCCW, 
            'RCCW': self.simCube.redCCW, 
            'GCCW': self.simCube.greenCCW, 
            'OCCW': self.simCube.orangeCCW,
            'BDub': self.simCube.blueDub, 
            'RDub': self.simCube.redDub, 
            'GDub': self.simCube.greenDub, 
            'ODub': self.simCube.orangeDub
        } 

        # White Corner Cells = 1, 3, 5, 7
        white_corner_cells = []
        for cell in self.simCube.cells:             # Finds the white corner cells
            if cell.actCell in [1, 3, 5, 7]:
                white_corner_cells.append(cell)
            if len(white_corner_cells) == 4:
                break

        for cell in white_corner_cells:
            adjColor = (cell.connections[0].color) if cell.connections[0].color != 'W' else (cell.connections[1].color)         # Color of connected cell that is not on white
            curColor = cell.curColor                            # Color of current cell's side
            colorOrder = ['B', 'O', 'G', 'R']

            if cell.curCell == cell.actCell:
                pass
            elif cell.curCell in [12, 23, 34, 37]:    # White Corners Side Left Top
                if curColor == colorOrder[colorOrder.index(adjColor)-1]:
                    colorFunctionDict[curColor + 'CCW']
                    self.simCube.yellowCCW()
                    colorFunctionDict[curColor + 'Dub']
                    self.simCube.yellowDub()
                    colorFunctionDict[curColor + 'CCW']
                elif curColor == colorOrder[colorOrder.index(adjColor)-2]:
                    colorFunctionDict[curColor + 'CCW']
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-3] + 'CW']
                    self.simCube.yellowDub()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-3] + 'CCW']
                    colorFunctionDict[curColor + 'CW']
                elif curColor == colorOrder[colorOrder.index(adjColor)-3]:
                    colorFunctionDict[curColor + 'CCW']
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CW']
                    self.simCube.yellowCCw()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CCW']
                    colorFunctionDict[curColor + 'CW']
                else:
                    colorFunctionDict[curColor + 'CCW']
                    self.simCube.yellowCCW()
                    colorFunctionDict[curColor + 'CW']
                    self.simCube.yellowCW()
                    colorFunctionDict[curColor + 'CCW']
                    self.simCube.yellowCCW()
                    colorFunctionDict[curColor + 'CW']

            elif cell.curCell in [10, 21, 32, 43]:  # White Corners Side Left Bottom
                if curColor == colorOrder[colorOrder.index(adjColor)-2]:
                    colorFunctionDict[adjColor + 'CW']
                    self.simCube.yellowCCW()
                    colorFunctionDict[adjColor + 'CCW']
                elif curColor == colorOrder[colorOrder.index(adjColor)-3]:
                    colorFunctionDict[adjColor + 'CW']
                    self.simCube.yellowDub()
                    colorFunctionDict[adjColor + 'CCW']
                elif curColor == adjColor:
                    self.simCube.yellowCCW()
                    colorFunctionDict[adjColor + 'CW']
                    self.simCube.yellowDub()
                    colorFunctionDict[adjColor + 'CCW']
                else:
                    self.simCube.yellowCW()
                    colorFunctionDict[adjColor + 'CW']
                    self.simCube.yellowCCW()
                    colorFunctionDict[adjColor + 'CCW']

            elif cell.curCell in [16, 19, 30, 41]:  # White Corners Side Right Bottom
                if curColor == colorOrder[colorOrder.index(adjColor)-2]:
                    colorFunctionDict[adjColor + 'CCW']
                    self.simCube.yellowCW()
                    colorFunctionDict[adjColor + 'CW']
                elif curColor == colorOrder[colorOrder.index(adjColor)-3]:
                    colorFunctionDict[adjColor + 'CCW']
                    self.simCube.yellowDub()
                    colorFunctionDict[adjColor + 'CW']
                elif curColor == adjColor:
                    self.simCube.yellowCW()
                    colorFunctionDict[adjColor + 'CCW']
                    self.simCube.yellowDub()
                    colorFunctionDict[adjColor + 'CW']
                else:
                    self.simCube.yellowCCW()
                    colorFunctionDict[adjColor + 'CCW']
                    self.simCube.yellowCW()
                    colorFunctionDict[adjColor + 'CW']
            
            elif cell.curCell in [14, 25, 28, 39]:  # White Corners Side Right Top
                if curColor == colorOrder[colorOrder.index(adjColor)-1]:
                    colorFunctionDict[curColor + 'CW']
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CCW']
                    self.simCube.yellowCW()
                    colorFunctionDict[colorOrder[colorOrder.index(curColor)-2] + 'CW']
                    colorFunctionDict[curColor + 'CCW']
                elif curColor == colorOrder[colorOrder.index(adjColor)-2]:
                    colorFunctionDict[curColor + 'CW']
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CCW']
                    self.simCube.yellowDub()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CW']
                    colorFunctionDict[curColor + 'CCW']
                elif curColor == colorOrder[colorOrder.index(adjColor)-3]:
                    colorFunctionDict[curColor + 'Dub']
                    self.simCube.yellowCW()
                    colorFunctionDict[adjColor + 'CW']
                    self.simCube.yellowCCW()
                    colorFunctionDict[adjColor + 'Dub']
                    colorFunctionDict[curColor + 'Dub']
                    colorFunctionDict[adjColor + 'CW']
                else:
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CCW']
                    self.simCube.yellowCW()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CW']
                    self.simCube.yellowCCW()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CCW']
                    self.simCube.yellowCW()
                    colorFunctionDict[colorOrder[colorOrder.index(adjColor)-3] + 'CW']

            elif cell.curCell in [46, 48, 50, 52]:      # White Corners on Yellow
                curToAct = {52:1, 50:3, 48:5, 46:7}
                acts = [1, 3, 5, 7]

                # Priming Position of Cell
                if curToAct[cell.curCell] != cell.actCell:
                    if acts[acts.index(cell.actCell)-1] == acts.index(curToAct[cell.curCell]):
                        self.simCube.yellowCCW()
                    elif acts[acts.index(cell.actCell)-2] == acts.index(curToAct[cell.curCell]):
                        self.simCube.yellowDub()
                    else:   # -3
                        self.simCube.yellowCW()

                # Distinguishing between left or right connections
                if colorOrder[colorOrder.index(cell.connections[0].curColor)-1] == colorOrder[colorOrder.index(cell.connections[1].curColor)]:
                    left, right = cell.connections[0], cell.connections[1]
                else:
                    left, right = cell.connections[1], cell.connections[0]

                # Moves to put cell in place
                colorFunctionDict[right.curColor + 'CCW']
                self.simCube.yellowDub()
                colorFunctionDict[right.curColor + 'CW']
                self.simCube.yellowDub()
                colorFunctionDict[left.curColor + 'CW']
                self.simCube.yellowCW()
                colorFunctionDict[left.curColor + 'CCW']

            elif cell.curCell in [1, 3, 5, 7]:          # White Corners on Wrong White
                acts = [1, 3, 5, 7]

                # Distinguishing between left or right connections
                if colorOrder[colorOrder.index(cell.connections[0].curColor)-1] == colorOrder[colorOrder.index(cell.connections[1].curColor)]:
                    left, right= cell.connections[0], cell.connections[1]
                else:
                    left, right = cell.connections[1], cell.connections[0]
                leftleftColor = colorOrder[colorOrder.index(left.curColor)-3]
                rightrightColor = colorOrder[colorOrder.index(right.curColor)-1]

                # Moves to put cell in place
                if acts.index(cell.actCell)-1 == acts.index(cell.curCell):
                    colorFunctionDict[left.curColor + 'CW']
                    colorFunctionDict[leftleftColor + 'CW']
                    self.simCube.yellowCCW()
                    colorFunctionDict[leftleftColor + 'Dub']
                    colorFunctionDict[left.curColor + 'CCW']
                    colorFunctionDict[leftleftColor + 'CW']
                elif acts.index(cell.actCell)-2 == acts.index(cell.curCell):
                    colorFunctionDict[left.curColor + 'CW']
                    colorFunctionDict[rightrightColor + 'CW']
                    self.simCube.yellowDub()
                    colorFunctionDict[rightrightColor + 'CCW']
                    colorFunctionDict[left.curColor + 'CCW']
                else: # -3
                    colorFunctionDict[right.curColor + 'CCW']
                    colorFunctionDict[rightrightColor + 'CCW']
                    self.simCube.yellowCW()
                    colorFunctionDict[rightrightColor + 'Dub']
                    colorFunctionDict[right.curColor + 'CW']
                    colorFunctionDict[rightrightColor + 'CCW']

            else:
                raise Exception(f"ERROR: {cell.curCell} is not a valid placement for white corner cell.")
