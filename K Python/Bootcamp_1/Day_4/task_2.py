# Class Object 2

class Square():
    def __init__(self, height="0", weight="0"):
        self.height = height
        self.weight = weight
    
    @property
    def height(self):
        print("Retriving the Height.....")
        return self.__height
    
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please input numbers.. Only..")
    
    @property
    def weight(self):
        print("Retriving the Weight.....")
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        if value.isdigit():
            self.__weight = value
        else:
            print("Please input numbers.. Only..")
    
    def area(self):
        return int(self.__height) * int(self.__weight)
    
    
def main():
    sqr = Square()
    height = input("The Height = ")
    weight = input("The Weight = ")
    sqr.height = height
    sqr.weight = weight
    print("Square height: {}".format(sqr.height))
    print("Square weight: {}".format(sqr.weight))
    print("The Area of the Square is : {}".format(sqr.area()))

main()