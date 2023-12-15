class Cube:
    def __init__(self, cells):
        self.cells = cells
    
    def swap(self, a: int, b: int, c: int, d: int):
        if a < c and b < d:
            arr = self.cells
            s1 = arr[0:a]
            s2 = arr[a:b]
            s3 = arr[b:c]
            s4 = arr[c:d]
            s5 = arr[d:len(arr)]
        else:
            s1 = arr[0:c]
            s2 = arr[c:d]
            s3 = arr[d:a]
            s4 = arr[a:b]
            s5 = arr[b:len(arr)]
        
        # print(s1, s2, s3, s4, s5)
        self.cells = s1 + s4 + s3 + s2 + s5
    
    def push(a, b, c, d):
        if a < c and b < d:
            s1 = arr[0:a]
            s2 = arr[a:b]
            s3 = arr[b:c]
            s4 = arr[c:d]
            s5 = arr[d:len(arr)]

            print(s1, s2, s3, s4, s5)
            self.cells = s1 + [-1]*len(s2) + s3 + s2 + s5
            return s4
        else:
            s1 = arr[0:c]
            s2 = arr[c:d]
            s3 = arr[d:a]
            s4 = arr[a:b]
            s5 = arr[b:len(arr)]

            print(s1, s2, s3, s4, s5)
            self.cells = s1 + s4 + s3 + [-1]*len(s4) + s5
            return s2


    def white_CW(self):
        self.swap(1, 7, 7, 9) # rotating white cells CW
        self.swap()

    def white_CCW(self):
        self.swap(1, 3, 3, 9) # rotating white cells CCW

    def white_Dub(self):
        self.swap(1, 5, 5, 9) # rotating white cells Double

    def blue_CW(self):
        pass 

    def blue_CCW(self):
        pass 

    def blue_Dub(self):
        pass 
    
    def red_CW(self):
        pass 

    def red_CCW(self):
        pass 

    def red_Dub(self):
        pass 

    def green_CW(self):
        pass 

    def green_CCW(self):
        pass 

    def green_Dub(self):
        pass 

    def orange_CW(self):
        pass 

    def orange_CCW(self):
        pass 

    def orange_Dub(self):
        pass 

    def yellow_CW(self):
        pass 

    def yellow_CCW(self):
        pass 

    def yellow_Dub(self):
        pass 