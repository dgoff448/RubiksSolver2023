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
            curColor = cell.color                               # Color of current cell
            colorOrder = ['B', 'O', 'G', 'R']

            if int(cell.actCell // 2) * 11 == short_solve1[cell.actCell]:   # Cell is on 11, 22, 33, 44
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
                
            elif cell.curCell in [17, 20, 31, 42]:  # Cell is on bottom of sides
                if adjColor == 'B':
                    ...
                elif adjColor == 'R':
                    ...
                elif adjColor == 'G':
                    ...
                elif adjColor == 'O':
                    ...
                else:
                    raise Exception(f"ERROR: {adjColor} is not a valid adjacent color.")

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
            
    
