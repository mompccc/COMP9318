## import modules here 
import math
import re

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    temp = x/2
    Min = 0
    Max = x
    while abs(temp**2 - x)> 0.000001:
        if (temp**2 > x):
            Max = temp
            temp = Min + (temp - Min)/2
        else:
            Min = temp
            temp = Max - (Max - temp)/2
    if (round(temp)**2 == x):
        temp = round(temp)
    return int(temp)


################# Question 2 #################

# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000):
    x = x_0
    count = 0
    x_new = x_0 - f(x_0)/fprime(x_0)
    while abs(x - x_new) >= EPSILON and count < MAX_ITER:
        x = x_new
        x_new = x_new - f(x_new)/fprime(x_new)
        count += 1
    return x_new


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def print_tree(root, indent=0):
    print(' ' * indent, root)
    if len(root.children) > 0:
        for child in root.children:
            print_tree(child, indent+4)

def make_tree(tokens): # do not change the heading of the function
    String = "Tree('" + tokens[0] + "', "
    for i in range(1, len(tokens)-1):
        if tokens[i] == ']' and tokens[i+1] == ']':
            temp1 = "])"
        elif tokens[i] == ']':
            temp1 = "]), "
        elif tokens[i] == '[':
            temp1 = "["
        elif tokens[i+1] == '[':
            temp1 = "Tree('" + tokens[i] + "', "
        elif tokens[i+1] == ']':
            temp1 = "Tree('" + tokens[i] + "')"
        else:
            temp1 = "Tree('" + tokens[i] + "'), "
        String += temp1
    String += "])"
    return eval(String)

def max_depth(root): # do not change the heading of the function
    depth = []
    if root.children:
        for child in root.children:
            depth.append(max_depth(child))
        return max(depth) + 1
    else:
        return 1
