import connections

class Cell:

    def __init__(self, placeNum: int, color: str, faceColor: str):
        self.isCenter = (placeNum % 9 == 0)
        self.isEdge = (placeNum in [2,4,6,8,11,13,15,17,20,22,24,26,29,31,33,35,38,40,42,44,47,49,51,53])
        self.isCorner = (placeNum in [1,3,5,7,10,12,14,16,19,21,23,25,28,30,32,34,37,39,41,43,46,48,50,52])

        self.color = color
        self.curCell = placeNum    # the current place the cell is
        self.actCell = (self.curCell if self.isCenter else "")         # the actual cell it is (actual needs to find the currentPlace that matches)
        self.connections = []

    def findActCell(self):
        if self.isEdge:
            c1 = self.connections[0]
            self.actCell = connections.edgeConnectionDict[self.color + c1.color]
        elif self.isCorner:
            c1 = self.connections[0]
            c2 = self.connections[1]
            self.actCell = connections.cornerConnectionDict[self.color + c1.color + c2.color]

    def setConnections(self, cells: list):
        for c in cells:
            self.connections.append(c)
        self.findActCell()

    def __str__(self):
        # return f"curCell: {self.curCell}, actCell: {self.actCell}"
        return str(self.curCell)
    
        
