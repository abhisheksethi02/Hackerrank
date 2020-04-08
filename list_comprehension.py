'''
Let's learn about list comprehensions! You are given three integers representing the dimensions of a cuboid along with another integer . 
You have to print a list of all possible coordinates of a 3D grid where the sum of  is not equal to N. Here i,j,k are less than their
respective given values. 
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if (i+j+k != n)])