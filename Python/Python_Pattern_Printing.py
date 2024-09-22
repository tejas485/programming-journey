def rectangle():
    #input dimensions
    m=int(input("Enter length : "))
    n=int(input("Enter breath : "))
    #loop
    for i in range (n):
        for j in range (m):
            print("*",end=" ")
        print("")
        
def hollow_rectangle():
    #input dimensions
    m=int(input("Enter length : "))
    n=int(input("Enter breath : "))
    #loop
    for i in range (n):
        for j in range (m):
            if (i==0 or j==0 or i==n-1 or j==m-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("")
        
def inverted_half_pyramid():
    n=int(input("Enter Number of Rows : "))
    for i in range (n):
        for j in range (n-i):
            print("*",end=" ")
        print("")
        
def half_pyramid_reverse():
    n=int(input("Enter Number of Rows : "))
    for i in range (n):
        for j in range (n-i+1):
            print(" ",end=" ")
        for j in range (i+1):
            print("*",end=" ")
        print("")

def half_pyramid_number():
    n=int(input("Enter Number of Rows : "))
    m=1
    for i in range (n):
        for j in range (m):
            print(m,end="")
        m+=1
        print("")
        
def floyd_triangle():
    n=int(input("Enter Number of Rows : "))
    m=1
    for i in range (n+1):
        for j in range (i):
            print(m,end=" ")
            m+=1
        print("")
        
def butterfly():
    n=int(input("Enter Size : "))
    for i in range (1,n+1):
        for j in range (i):
            print("*",end=" ")
        for j in range (2*n-2*i):
            print(" ",end=" ")
        for j in range (i):
            print("*",end=" ")
        print("")

    for i in range (n,0,-1):
        for j in range (i):
            print("*",end=" ")
        for j in range (2*n-2*i):
            print(" ",end=" ")
        for j in range (i):
            print("*",end=" ")
        print("")

def inverted_pattern():
    n=int(input("Enter Number of Rows : "))
    for i in range (n):
        for j in range (n-i):
            m=j+1
            print(m,end=" ")
        print("")

def pattern_one_zero():
    n=int(input("Enter Number of Rows : "))
    for i in range (n):
        for j in range (i+1):
            m=i+j
            if (m%2==0):
                r=0
            else:
                r=1
            print(r,end=" ")
        print("")
        
def rhombus():
    n=int(input("Enter Number of Rows : "))
    for i in range (n):
        for j in range (n-i):
            print("",end=" ")
        for j in range (n):
            print("*",end=" ")
        print("")

def number_pyramid():
    n=int(input("Enter Number of Rows : "))
    for i in range (n):
        for j in range (n-i+1):
            print("",end=" ")
        for j in range (i+1):
            print(j+1,end=" ")
        print("")

def number_palindrome():
    n=int(input("Enter Number of Rows : "))
    for i in range (n+1):
        for j in range (n-i):
            print(" ",end=" ")
        for j in range (n-(n-i),0,-1):
            print(j,end=" ")
        for j in range (2,n-(n-i)+1):
            print(j,end=" ")
        print("")

def star_pattern():
    n=int(input("Enter Size : "))
    for i in range (n):
        for j in range (n-i+1):
            print(" ",end=" ")
        for j in range ((2*i)+1):
            print("*",end=" ")
        print("")
    for i in range (n,-1,-1):
        for j in range (n-i+1):
            print(" ",end=" ")
        for j in range ((2*i)+1):
            print("*",end=" ")
        print("")

def zig_zag():
    n=int(input("Enter Number of Loops : "))
    for i in range (3):
        for j in range (n):
            if (((i+j+2)%4==0) or ((i+1)==2 and (j+1)%4==0)):
                print("*",end="")
            else:
                print(" ",end="")
        print("")

def main():
    #menu-->
    print("\t\tMENU \n1.Rectangle\n2.Hollow Rectangle\n3.Inverted Half Pyramid")    
    print("4.Half Pyramid After 180 Degree Rotation\n5.Half Pyramid Using Numbers")
    print("6.Floyd's Triangle\n7.Butterfly\n8.Inverted Pattern\n9.0-1 pattern\n10.Rhombus")
    print("11.Number Pyramid\n12.Number Palindrom\n13.Star Pattern\n14.Zig Zag pattern\n")
    ch = int(input("Enter Choice : "))     #input
    if (ch == 1):
        rectangle()
    elif (ch == 2):
        hollow_rectangle()
    elif (ch == 3):
        inverted_half_pyramid() 
    elif (ch == 4):
        half_pyramid_reverse()
    elif (ch == 5):
        half_pyramid_number()
    elif (ch == 6):
        floyd_triangle()
    elif (ch == 7):
        butterfly()
    elif (ch == 8):
        inverted_pattern()
    elif (ch == 9):
        pattern_one_zero()
    elif (ch == 10):
        rhombus()
    elif (ch == 11):
        number_pyramid()
    elif (ch == 12):
        number_palindrome()
    elif (ch == 13):
        star_pattern()
    elif (ch == 14):
        zig_zag()
    else:
        print("Invalid Choice")
        
main()