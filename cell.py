import connections

class Cell:

    def __init__(self, placeNum: int, color: str, faceColor: str):
        self.isCenter = (placeNum == 9)
        self.isEdge = (placeNum % 2 == 0)
        self.isCorner = (placeNum % 2 == 1 and placeNum != 9)

        self.color = color
        self.curCell = faceColor + str(placeNum)    # the current place the cell is
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
        return f"curCell: {self.curCell}, actCell: {self.actCell}"
        
