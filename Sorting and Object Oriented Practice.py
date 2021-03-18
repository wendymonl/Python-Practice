## Assignment3 ES 122
## Name: Wendy Montano
## EID : wfm427

# Problem 1: Write a function that sorts an unknown number of numbers (integers and/or floats) and returns the sorted list
# Optional Paramaters:
# Each of these paramaters should have the value True if you are applying the paramater 
# Reverse: Sorts from highest to lowest.
# NoDuplicates: That does not print any duplicate numbers
# SortbyAbsoluteValues: That takes the absolute values of all transmitted numbers before 
# If a keyword argument is passed that is not one of the three above Print "Error: Not a valid Paramater" and return nothing 
# The function should return the sorted list
def sortedTheseNumbers(*args, **kwargs):
    #first make the input arguments into a list
    makelist=list(args)
    if len(kwargs)==0: #if no kwargs present, return the list in ascending order
         ascending_order=sorted(makelist)
         return ascending_order
    else:
        for key,value in kwargs.items(): #parameters are given by kwargs
            parameters={key} #parameters will be keys of kwargs
            if value is True: 
                for key in kwargs.keys():
                    parameters.update({key}) 
        #now build the output based on the parameters
        if 'NoDuplicates' in parameters:
            makelist=list(set(makelist)) #'set' function works to remove duplicates of a number in a list
        if 'SortbyAbsoluteValues' in parameters: 
            #manually sort the list based on absolute values, but  retain the original value in the ouutput list
            for index in range(1,len(makelist)):
                value_of_list = makelist[index] #iterate value of second to last element in list (since python lists start at 0, the value in makelist[0] is the first value in list)
                i=index-1 #this will be used to test the value of second element vs first element in list
                #sort from lowest to highest without sort function:
                while i>=0: 
                    if abs(value_of_list) < abs(makelist[i]): #absolute value of number  in list is what is being sorted
                        #put the number(not it's absolute value)
                        makelist[i+1]=makelist[i] #the next value becomes the value in the i place of list
                        makelist[i]=value_of_list #the value in the i place of list becomes the value in the for loop 
                        i -=1
                    else:
                        break
        elif 'SortbyAbsoluteValues' not in parameters:
            makelist=sorted(makelist) #if not sorting by absolute value, just use sort function to sort from highest to lowest
        if 'Reverse' in parameters:
            makelist=makelist[::-1] #update the list in reverse order
        #print an error and return nothing if kwargs is not any of the three above
        if 'SortbyAbsoluteValues' not in parameters:
            if 'Reverse' not in parameters:
                if 'NoDuplicates' not in parameters:
                    print('Error: Not a valid Paramater')
                    return 
        return makelist 
 

# Problem 2: One common way to check for collisions in robotics is to create bounding boxes from either CAD or sensor data.
#For this problem we are going to create a BoundingBox object generated from a PointCloudData data objects which store lists of objects as Points. 
#Thus we will need to create three classes to complete this problem. These classes are outlined below.

#A class that represents a point in space
# required variables and methods
# x - stores the x value of the point
# y - stores the y value of the point
# z - stores the z value of the point
# __init__  (method) - Should take in x, y, and z parameters and set their values
# __str__ (method) - Should return a string representation of the point. It should be formatted like a tuple ex: (x, y, z) 
# __eq__ (method) - Should take in a Point object and return true if the x, y and z values of the input point are the same as the x, y, and z values of the calling point

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return (str((self.x,self.y,self.z)))
    def __eq__(self,p):
        if self.x==self.y:
            if self.y==self.z:
                return True
            else:
                return False
        else:
            return False


# This class holds a list of 3D points which it uses to construct the bounding box
# required variables and methods
# points - stores the list of Point objects
# __init__ (method) - Should take in a list of Point objects and set the value of points
# add (method) - takes a Point object as input and inserts it in to the points list
# remove (method)- takes a Point object as input and removes it from Points list. Should do nothing if point is not in list
class PointCloudData:
    def __init__(self, Points):
        self.points=list(Points)
        for item in Points:
            points=str(item)
            points=points.strip('(')
            points=points.strip(')')
            points=points.split(', ')
            self.Points=points
    def add(self,p):
        #NewPoints=[]
        #x=p1.x
        #y=p1.y
        #z=p1.z
        #NewPoints.append(x)
        #NewPoints.append(y)
        #NewPoints.append(z)
        OldPoints=self.points
        newpoint=PointCloudData([p]).points
        OldPoints=OldPoints.append(newpoint)
    def remove(self,p):
        pnew=PointCloudData([p]).points
        if pnew in self.points:
            pold=self.points
            p.self=pold.remove(pnew)
        return

# This class represents a bounding box. It stores the center and dimensions of the box. This class is a subclass of PointCloudData
# center (variable) - A Point object used to store the location of the box in Cartesian space. The point should be at the center of the box.
# dimensions (variable) - A list with the width, height, and depth of the bounding box.
# __init__ (method) - Should take in a list of points as input and then call the superclass’s init method. It should then calculate and set the center and dimensions of the box.
# updateBox (method) - This method should take in a new list of points for the bounding box and should update the dimensions and center. 
# collisionCheck (method) - this method takes in a BoundingBox, b, as an input and checks to see if the passed bounding box b is in collision with it and returns true if so and otherwise false.
# __add__ (method) - This method should take in a BoundingBox, b, as an input and it should combine the two bounding boxes. It should return a bounding box that minimally contains both bounding boxes. Note: this method overrides the + operation. This means that if you say BoundingBox1 + BoundingBox2, what is really happening is you are saying BoundingBox1.__add__(BoundingBox2).
# __len__ (method) - This method should return the volume of the bounding box

class BoundingBox(PointCloudData):
    def __init__(self, Points):
        return 

    def updateBox(self, Points):
        return

    def collisionCheck(self, b):
        return

    def __add__(self, b):
        return

    def __len__(self):
        return
    
    
# test code by running testcases.py
