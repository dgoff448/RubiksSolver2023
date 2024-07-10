#Import PySimpleGUI
import PySimpleGUI as sg
import tkinter as tk

sg.theme("Dark Blue 3")
color = [("black", "white"), ("white", "blue"), ("white", "red"), ("white", "green"), ("white", "orange"), ("black", "yellow")]
rawColor = ["white", "blue", "red", "green", "orange", "yellow"]
order = [[3,3],[3,4],[3,5],[4,5],[5,5],[5,4],[5,3],[4,3],[4,4],         # White
         [3,0],[3,1],[3,2],[4,2],[5,2],[5,1],[5,0],[4,0],[4,1],         # Blue
         [0,3],[0,4],[0,5],[1,5],[2,5],[2,4],[2,3],[1,3],[1,4],         # Red
         [3,6],[3,7],[3,8],[4,8],[5,8],[5,7],[5,6],[4,6],[4,7],         # Green
         [6,3],[6,4],[6,5],[7,5],[8,5],[8,4],[8,3],[7,3],[7,4],         # Orange
         [9,3],[9,4],[9,5],[10,5],[11,5],[11,4],[11,3],[10,3],[10,4],   # Yellow
         ]

#Draw the button
# layout = [[sg.Button('', size=(2,1), button_color=("white", "black"))]]

check = [[False, False, False, True, True, True, False, False, False],
         [False, False, False, True, True, True, False, False, False],
         [False, False, False, True, True, True, False, False, False],
         [True, True, True, True, True, True, True, True, True],
         [True, True, True, True, True, True, True, True, True],
         [True, True, True, True, True, True, True, True, True],
         [False, False, False, True, True, True, False, False, False],
         [False, False, False, True, True, True, False, False, False],
         [False, False, False, True, True, True, False, False, False],
         [False, False, False, True, True, True, False, False, False],
         [False, False, False, True, True, True, False, False, False],
         [False, False, False, True, True, True, False, False, False],
         ]

def findColor(values):
    for v in values:
        if values[v]:
            return v

layout = []
cores = [[4, 4], [4, 1], [1, 4], [4, 7], [7, 4], [10, 4]]
for i in range(0, 12):
    layout.append([])
    for j in range(0, 9):
        good = False
        for c in cores:
            if [i,j] == c:
                layout[i].append(sg.Button('', metadata=rawColor.index(rawColor[cores.index([i,j])]), key=f"{i}-{j}", size=(6,3), button_color=rawColor[cores.index([i,j])]))
                good = True
        if good:
            pass
        elif check[i][j]:
            layout[i].append(sg.Button('', metadata="-1", key=f"{i}-{j}", size=(6,3), button_color=("white", "black")))
        else:
            layout[i].append(sg.Text("             "))
layout.append([sg.Text("")])
layout.append([sg.Radio("White", "color", key="white"), 
               sg.Radio("Blue", "color", key="blue"), 
               sg.Radio("Red", "color", key="red"), 
               sg.Radio("Green", "color", key="green"), 
               sg.Radio("Orange", "color", key="orange"), 
               sg.Radio("Yellow", "color", key="yellow"),
               sg.Radio("Cycle", "color", key="cycle", default=True)])
layout.append([sg.Button("Submit Cube Configuration", key="submit", size=(30,2))])
layout.append([sg.Text("", key="outputTxt", text_color="yellow", font=("Helvetica", 12, "bold"))])


#Draw the window
window = sg.Window("Rubik's Cube Configuration Input", layout, size=(625,920))

# #Define what happens when the button is clicked
cells = []
while True:
    event, values = window.read()
    if event == None:
        quit()
    elif event == "submit":
        for o in order:
            good = True
            btnColor = (color[(int(layout[o[0]][o[1]].metadata))%6][1]).upper()
            cells.append(btnColor[0])
        
        if cells.count('W') == 9 and cells.count('B') == 9 and cells.count('R') == 9 and cells.count('G') == 9 and cells.count('O') == 9 and cells.count('Y') == 9:   # Black cells show up as yellow in value
            with open("./testInput/GUI_Input.txt", "w") as f:
                for c in cells:
                    f.write(f"{c}\n")
            window['outputTxt'].update("Cube Configuration Exported", text_color="light green")
            cells = []
        else:
            for i in range(0, 6):
                print(cells.count(rawColor[i][0].upper()))
            print("\033[1;31mError: Invalid Cube Configuration\033[00m")
            window['outputTxt'].update("Error: Invalid Cube Configuration", text_color="yellow")
            cells = []
    else:
        if values["cycle"] == True:
            i, j= map(int, event.split("-"))
            coreBtn = False
            for c in cores:
                if [i,j] == c:
                    coreBtn = True
            if not coreBtn:
                k = int(layout[i][j].metadata)
                layout[i][j].metadata = k + 1
                layout[i][j].update(button_color = color[(k+1)%6])
        else:
            i, j= map(int, event.split("-"))
            coreBtn = False
            for c in cores:
                if [i,j] == c:
                    coreBtn = True
            if not coreBtn:
                k = int(layout[i][j].metadata)
                trueColor = findColor(values)
                layout[i][j].update(button_color = trueColor)
                layout[i][j].metadata = rawColor.index(trueColor)


