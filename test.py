def blue():
    print("blue")

def red():
    print("red")

def green():
    print("green")


functionDict = {'G': green, 'B': blue, 'R': red}

functionDict[input()]()