## Assignment 2 ES 122
## Name: Wendy Montano
## EID : wfm427
##
## Fill in the functions and class below

def star_wars():
    ## Write Code Here
    f=open("starwars.txt")
    txtlines=f.readlines()
    character=[]
    linesspoken=[]
    c=[]
    lengthoflist=len(txtlines)
    word="a"
    f.close
    for i in range (0,lengthoflist):
        scriptline=txtlines[i]
        lineelements=scriptline.split()
        charactername=lineelements[1].strip('/"')
        spokenline=' '.join(lineelements[2::]).strip('/"')
        spokenline_words=spokenline.strip(".?")
        wordsinspokenline=spokenline_words.split()
        character.append(charactername)
        if "Force" in spokenline:
            c.append(character[i])
        if "force" in spokenline:
            c.append(character[i])
        for sublist in wordsinspokenline: #this is to see which character says the longest word
            if len(sublist)>len(word):
                word=sublist #longest word so far 
                b=i
        linesspoken.append(spokenline)
    characterdict={} #create a dictioary of all the unique characters and how many lines they have
    from collections import Counter
    for key, value in sorted(Counter(character).items()):
        characterdict.update({key:value}) #my character dictionary is sorted in alphabetical order
    descending_order = sorted(characterdict, key=characterdict.get, reverse=True)
    print(descending_order[0], "had the most lines")
    a=linesspoken.index(max(linesspoken, key=len))
    print(character[a], "had the longest line")
    charswhosaidforcecounter={}
    for key, value in Counter(c).items():
        charswhosaidforcecounter.update({key:value})   
    descending_order2= sorted(charswhosaidforcecounter, key=charswhosaidforcecounter.get, reverse=True)
    print(descending_order2[0], "said force the most")
    print(character[b], "said the longest word which was", word)
    ## Use instructions from the assignment document
    ## Use starwars.txt as file


'''
Assume if a kwarg is not present, you should create the basic matrix
Assume the style is default to random
Assume the set is default to [0, 1]
kwargs can be :
    n =>  size of nxn matrix NOTE: You can assume if n is passed, i and j won't be
    i =>  number of rows     NOTE: If i is passed, assume j will be too
    j =>  number of columns
    range => [min, max] list
    set   => [number1, ..., numberN]
                NOTE: If set is specified, use that over range
                NOTE: If not specified, assume the set is the range
    style => a string which can be anything in {diagonal, upper, lower, symmetric, random}
                NOTE: any non-square matrix will be random
                NOTE: different styles will always be square matrices
    format => string that will be formatted as 1st and last element of each row
'''

import numpy as np
import random
def generateMatrix(**kwargs):
    ## Write Code Here
    ## print out matrix with newlines between rows
    ## print out elements in rows 1 space apart, no space at the beginning
    Matrix=[]
    if len(kwargs)==0:
        kwargs={'n':4}
    else:
        kwargs=kwargs
    for key,values in kwargs.items():
        if 'n' in kwargs.keys():
            n=kwargs['n']
            m=kwargs['n']
        elif'i' and 'j' in kwargs.keys():
            size=list(kwargs.values())
            n=size[0]
            m=size[1]
    if kwargs is not None:
        if 'range' in kwargs.keys():
            ran=kwargs['range']
            lower=ran[0]
            upper=ran[1]+1
            set1=list(range(lower,upper))
            #print(set1)
        if 'set' in kwargs.keys():
            set1=kwargs['set']
        elif 'set' and 'range' not in kwargs.keys():
            set1=[0,1]
        if 'style' in kwargs.keys():
            style=kwargs['style']
            #return style
        elif 'style' not in kwargs.keys():
            style='random'
            #print('style is', style)
        if 'format' in kwargs.keys():
            format1=kwargs['format']
            style='random'
        for j in range(n):
            res=[]
            for i in range(m):
                res.append(random.choice(set1))
            Matrix.append(res)
    if style=="random":
        Matrix=Matrix
    if style=="diagonal":
            for i in range(0,n):
                for j in range(0,m):
                    if (i<j):
                        Matrix[i][j]=0
                    elif (i>j):
                        Matrix[i][j]=0
    if style=="upperdiagonal":
            for i in range(0, n):
                for j in range(0, m):
                    if (i>j):
                        Matrix[i][j]=0
    if style=="lowerdiagonal":        
            for i in range(0, n):
                for j in range(0, m):
                    if (i<j):
                        Matrix[i][j]=0
    if style=="symmetric":
            Matrix=np.maximum(Matrix, np.transpose(Matrix) )
    for d in range(0,n):
        row=str(Matrix[d]).strip('[]')
        row=row.replace(', ',' ')  
        if 'format' in kwargs.keys():
           print(format1, row, format1[::-1]) 
        else:
            print(row)      

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
        if type(a) is list:
            if len(a) != len(b) !=len(c):
                print('Error. Please input lists of the same length for a, b, and c')
    def GetA(self):
        return self.a
    def GetB(self):
        return self.b
    def GetC(self):
        return self.c
    def SetA(self,n):
        self.a=n
    def SetB(self,n):
        self.b=n
    def SetC(self,n):
        self.c=n
    def getDiscriminant(self):
        a=self.a
        b=self.b
        c=self.c
        discr=[]
        if type(a) is list and type(b) is list and type(c) is list:
            iteration=len(a)
            for i in range (0,iteration):
                calcdisc=(b[i])**2- (4 * a[i]* c[i])
                discr.append(calcdisc)
        else:
            discr=((self.b)**2) - (4 * self.a * self.c)
        return discr
    def getRoots(self): 
        import math
        a=self.a
        b=self.b
        c=self.c
        if type(a) is list and type(b) is list and type(c) is list:
            iteration=len(a)
        else:
            iteration=1
            a=[a]
            b=[b]
            c=[c]
        rootslist=[]
        discrlist=[]
        for i in range (0,iteration):
            discr=self.getDiscriminant()
            if type(discr) == int:
                discrlist.append(discr)
            else:
                discrlist=discr
            if discrlist[i] < 0:
                import cmath
                A=a[i]
                B=b[i]
                sqrtdisct=cmath.sqrt(discrlist[i])
                up1=(sqrtdisct) - float(B)
                up2=-(sqrtdisct) - float(B)
                root1= up1/(2 * float(A))
                imag_root1=root1.imag
                if imag_root1>=0:
                    root1=["%.5f"% root1.real + ' + ' + "%.5f"% + root1.imag + 'i']
                if imag_root1<0:
                    root1=["%.5f"% root1.real + ' - ' + "%.5f"% + abs(root1.imag) + 'i']
                root1=' '.join(root1)
                root2= up2/(2 * float(A))
                imag_root2=root2.imag
                if imag_root2>=0:
                    root2=' '.join(["%.5f"% root2.real + ' + ' "%.5f"% + root2.imag + 'i'])
                if imag_root2<0:
                    root2=' '.join(["%.5f"% root2.real + ' - ' + "%.5f"% abs(root2.imag) + 'i'])
                if iteration==1:
                    roots=(root1,root2)
                else:
                    rootsi=[root1,root2]
                    rootslist.append(rootsi)
                    roots=rootslist
                    roots=tuple(rootslist)
            if discrlist[i] >= 0:
                A=a[i]
                B=b[i]
                sqrtdisct="%.5f"% math.sqrt(discrlist[i])
                up1=-float(sqrtdisct) - float(B)
                up2=float(sqrtdisct) - float(B)
                root1= up1/(2 * float(A))
                root2= up2/(2 * float(A))
                if abs(float(root1))==abs(float(root2)):
                    root1=root2
                if iteration==1:
                    roots=("%.5f"%root1,"%.5f"%root2)
                else:
                    rootsi=["%.5f"%root1,"%.5f"%root2]
                    rootslist.append(rootsi)
                    roots=rootslist
                    roots=tuple(rootslist)
        return roots

if __name__ == '__main__':
    star_wars()
    generateMatrix()
    # You can do any testing you want here
    # Anycode you run here will not run when being graded...
    # Here are some examples of how QuadraticEquation will be used..
    equation1 = QuadraticEquation(1,-8,16)
    discr1=equation1.getDiscriminant()
    roots1=equation1.getRoots()
    
    equation = QuadraticEquation([1,3,1],[1,5,-8],[1,5,16])
    A = equation.GetA()
    B = equation.GetB()
    discr = equation.getDiscriminant()
    roots = equation.getRoots()
