# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', "Tyler Humbert"
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.Connections = []
        self.Walls = []
        #reference associates coordonates with their index's in the above lists
        self.references = {}
        pass

    def addVertex(self, label:Coordinates):
        #make a new reference to connect coordonates with an index in the graph
        index = len(self.references)
        self.references[label] = index
        #first add a new entry to the top row of the matrix and fill it with zeros
        self.Connections.append([0] * index)

        #then make every list within the top row one deeper to represent the new possible connection
        for row in self.Connections:
            #make it a zero as there are no connections yet
            row.append(0)
        #do the same for the wall chart
        self.Walls.append([0] * index)
        for row in self.Walls:
            row.append(0)




    def addVertices(self, vertLabels:List[Coordinates]):
        for cord in vertLabels:
            self.addVertex(cord)



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        #checks if both vertices exist
        if not self.hasVertex(vert1) and self.hasVertex(vert2):
            return False

        #use the reference dict to find the associated index for the matrix
        self.Connections[self.references[vert1]][self.references[vert2]] = 1
        self.Connections[self.references[vert2]][self.references[vert1]] = 1
        if addWall:
            self.Walls[self.references[vert1]][self.references[vert2]] = 1
            self.Walls[self.references[vert2]][self.references[vert1]] = 1
        return True        
    


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        if not self.hasVertex(vert1) and self.hasVertex(vert2):
            return False
        
        if wallStatus:
            if self.hasEdge(vert1,vert2):
                return self.addEdge(vert1,vert2,True)
            else:
                return False
            
        else:
            self.Walls[self.references[vert1]][self.references[vert2]] = 0
            self.Walls[self.references[vert2]][self.references[vert1]] = 0
            return True



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if not self.hasVertex(vert1) and self.hasVertex(vert2):
            return False
        
        if not self.hasEdge(vert1,vert2):
            return False
        self.Connections[self.references[vert1]][self.references[vert2]] = 0
        self.Connections[self.references[vert2]][self.references[vert1]] = 0
        return True
        


    def hasVertex(self, label:Coordinates)->bool:
        #Just check if the coordinates are listed in the reference list
        if label in self.references.keys():
            return True
        return False



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if self.Connections[self.references[vert1]][self.references[vert2]] == 1:
            return True
        return False



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if self.Walls[self.references[vert1]][self.references[vert2]] == 1:
            return True
        return False

    
    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        neighbours = []
        reverse_references = {v: k for k, v in self.references.items()}  
        # the references so that the index is now the key, making it easier to access relevant coordinates

        #Checks every node to see if its neighbours with the one being checked
        for index, value in enumerate(self.Connections[self.references[label]]):
            if value == 1:
                neighbours.append(reverse_references[index])
        return neighbours
        