class Triangle:
    def __init__(self, level):
        self.__level = level
        
    def show(self):
        for i in range(self.__level):
            for j in range(i + 1):
                print('*', end='')
            print()
        print()  # 添加一个空行，方便分隔不同形状的输出

class RTriangle:
    def __init__(self, level):
        self.__level = level
        
    def show(self):
        for i in range(self.__level, 0, -1):
            for j in range(i):
                print('*', end='')
            print()
        print()  # 添加一个空行，方便分隔不同形状的输出

class Rectangle:
    def __init__(self, level):
        self.__level = level
        
    def show(self):
        for i in range(self.__level):
            for j in range(self.__level):
                print('*', end='')
            print()
        print()  # 添加一个空行，方便分隔不同形状的输出

class Line:
    def __init__(self, level):
        self.__level = level
        
    def show(self):
        for i in range(self.__level):
            print('**')
        print()  # 添加一个空行，方便分隔不同形状的输出

graph = []
graph.append(Triangle(5))
graph.append(Rectangle(3))
graph.append(RTriangle(5))
graph.append(Line(5))

for obj in graph:
    obj.show()  # 修正拼写错误，从 "odj" 改为 "obj"


