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
        # White Cross Cells = 2, 4, 6, 8

        white_cross_cells = []
        for cell in self.simCube.cells:             # Finds the white cross cells
            if cell.actCell in [2, 4, 6, 8]:
                white_cross_cells.append(cell)
            if len(white_cross_cells) == 4:
                break

        white_to_yellow = {6:47, 4:49, 2:51, 8:53}
        for cell in white_cross_cells:
            short_solve1 = {2:11, 4:22, 6:33, 8:44}
            short_solve2 = ['2:29', '4:40', '6:15', '8:26']
            color = cell.connections[0].color                   # Color of connected cell

            if int(cell.actCell // 2) * 11 == short_solve1[cell.actCell]:   # Cell is on 11, 22, 33, 44
                colorFunctionDict = {
                    'B': self.simCube.blueCW, 
                    'R': self.simCube.redCW, 
                    'G': self.simCube.greenCW, 
                    'O': self.simCube.orangeCW
                    }
                colorFunctionDict[color]()
                
            elif str(cell.actCell) + ':' + str(cell.curCell) in short_solve2:   # Cell is on 29, 40, 15, 26
                colorFunctionDict = {
                    'B': self.simCube.blueCCW, 
                    'R': self.simCube.redCCW, 
                    'G': self.simCube.greenCCW, 
                    'O': self.simCube.orangeCCW
                }
                colorFunctionDict[color]()
                
            elif cell.curCell in [17, 20, 31, 42]:  # Cell is on bottom of sides
                pass

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
