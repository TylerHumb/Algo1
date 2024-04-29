# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', 'Tyler Humbert'
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        #Create a dictionary to keep track of coordonates and their neighbours
        self.Vertices = {}
        self.Walls = {}
        pass


        
    def addVertex(self, label:Coordinates):
        #create a entry for the coordinate and initialize the list for its neighbours
        self.Vertices[label] = []
        self.Walls[label] = []



    def addVertices(self, vertLabels:List[Coordinates]):
        for vertex in vertLabels:
            self.Vertices[vertex] = []
            self.Walls[vertex] = []
        pass



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        #ensures that the vertices actually exist
        if not self.hasVertex(vert1) and self.hasVertex(vert2):
            return False
        self.Vertices[vert1].append(vert2)
        #since its an undirected graph add it to both vertices neighbour list
        self.Vertices[vert2].append(vert1)
        if addWall:
            self.Walls[vert1].append(vert2)
            self.Walls[vert2].append(vert1)
        return True
            
        


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        #ensures that the vertices actually exist
        if not self.hasVertex(vert1) and self.hasVertex(vert2):
            return False

        #check if we're adding or removing a wall
        if wallStatus:
            if self.hasEdge(vert1,vert2):
                return self.addEdge(vert1,vert2, True)
            else:
                return False
                
        else:
            self.Walls[vert1].remove(vert2)
            self.Walls[vert2].remove(vert1)
            return True
            



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if not self.hasVertex(vert1) and self.hasVertex(vert2):
            return False

        if not self.hasEdge(vert1,vert2):
            return False
        self.Vertices[vert1].remove(vert2)
        self.Vertices[vert2].remove(vert1)
        return True
        
        


    def hasVertex(self, label:Coordinates)->bool:
        if label in self.Vertices:
            return True
        return False



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if vert2 in self.Vertices[vert1]:
            return True
        return False



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if vert1 in self.Walls[vert2]:
            return True
        return False
        
    


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        return self.Vertices[label]