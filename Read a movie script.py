## Assignment1 ES 122
## Name: Wendy Montano
## EID : wfm427
##

#open "star wars" script and identify characters
def star_wars():
    f=open("starwars.txt")
    lines=f.readlines()
    character= []
    lengthoflist=len(lines)
    f.close
    for i in range (0,lengthoflist):
        scriptline=lines[i]
        lineelements=scriptline.split()
        charactername=lineelements[1].strip('/"')
        character.append(charactername)
    characterdict={} #create a dictioary of all the unique characters and how many lines they have
    from collections import Counter
    for key, value in sorted(Counter(character).items()):
        characterdict.update({key:value}) #my character dictionary is sorted in alphabetical order
#from stackoverflow: Python's sort algorithm (TimSort) is a stable sort, so any items that have the same sort 'value', are kept in the order they were in before sorting.
    descending_order = sorted(characterdict, key=characterdict.get, reverse=True)
    for k in descending_order:
        print(k, characterdict[k])
    ## Use starwars.txt
    return

#identify stars from a text file and identify the closest/furthest ones
def star_travel():
    ## Write Code Here
    f=open("stars.txt")
    textaslines=f.readlines()
    star_names=[]
    coordinate_vectors=[]
    lengthoflist=len(textaslines)
    f.close

    for i in range (0,lengthoflist):
        starline=textaslines[i]
        star=starline.split('[')[0]
        star_names.append(star) #list of star names is created
        coordinatestripspaces1=starline.replace("[ ", "[")
        coordinatewithendbracket=coordinatestripspaces1.split('[',1)[1]
        coordinatestripspaces2=coordinatewithendbracket.replace(" ]", "]")
        coordinate=coordinatestripspaces2.split(']',1)[0] #coordinates saved as string     
        coordinatex=coordinate.split()[0]
        coordinatey=coordinate.split()[1]
        coordinatez=coordinate.split()[2]
        coordinate_vector=[coordinatex, coordinatey, coordinatez] #coordinates saved as a list with x,y, and z
        coordinate_vectors.append(coordinate_vector) #list of coordinates

    #Thank you stack overflow for the following so that I could find the closest and farthest stars
    import numpy as np
    from numpy import nanmax, nanmin, argmax, unravel_index
    from scipy.spatial.distance import pdist, squareform

    D = squareform(pdist(coordinate_vectors)); 
    #creates an array with all of the distances individual stars as both rows and columns
    maxdist, [Star1, Star2] = nanmax(D), unravel_index( argmax(D), D.shape) #find the maximum value of distance in array and which two stars create it
    mindist = nanmin(D[np.nonzero(D)]) #same as maxdist but different way to find which stars create it
    ClosestStars= np.where(D==np.min(D[np.nonzero(D)]))
    [Star3, Star4]=ClosestStars[0]
    #now call the stars by their names:
    Star1_Name=star_names[Star1] 
    Star2_Name=star_names[Star2]
    Star3_Name=star_names[Star3]
    Star4_Name=star_names[Star4]
    print("Farthest stars are " + Star1_Name + "and " + Star2_Name + "at a distance of ""{:.5f}".format(maxdist) + ".")
    print("Closest stars are " + Star3_Name + "and " + Star4_Name + "at a distance of ""{:.5f}".format(mindist) + ".")
    ## Use stars.txt
    return

#make a calculator
def calculator():
    ## Write Code Here
    Operation=(input("Enter Operation: "))
    while Operation != 'q':
        FirstNum=float(input("Enter First Number: "))  
        SecNum=float(input("Enter Second Number: "))
        if Operation == '+':
            sum=(FirstNum)+(SecNum)
            outcome=sum
        elif Operation == '-':
            outcome=(FirstNum)-(SecNum)
        elif  Operation == '*':
            outcome=(FirstNum)*(SecNum)
        elif  Operation == '/':
            outcome=(FirstNum)/(SecNum)
        elif  Operation == '^':
            outcome=(FirstNum)**(SecNum)
        print("{:.1f}".format(outcome))
        Operation=(input("Enter Operation: "))
    return


if __name__ == '__main__':
    star_wars()
    star_travel()
    calculator()
    print("Done")
