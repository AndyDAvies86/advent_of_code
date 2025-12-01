#%%


#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
numlist = [str(x) for x in range(0,10)]
compass = 'NESW'
dir = [(0,1),(1,0),(0,-1),(-1,0)]
#%%
def lineparse(inputfile):
    file = open(inputfile,"r")
    start = file.read()
    return start.split("\n")

def dlineparse(inputfile):
    file = open(inputfile,"r")
    start = file.read()
    return start.split("\n\n")

def listnums(inputfile,dlm=','):
    return [[int(x) for x in y.split(dlm)] for y in lineparse(inputfile)]

def dsplit(inputfile,dlm1='\n',dlm2=','):
    file = open(inputfile,"r")
    start = file.read()
    return [[x for x in y.split(dlm2)] for y in start.split(dlm1)]

def drawgraph(G):
    import networkx as nx
    import matplotlib.pyplot as plt
    pos = {(x,y):(x,-y) for x,y in G.nodes()}
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        node_size = 300,
                        )
    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edges(G, pos, arrows=False)
    plt.show()  

def createmaze(stringlist):
    """
    Creates a path map from a list of strings to define maze where the maze is surrounded by #
    """
    import networkx as nx
    h = len(stringlist)
    w = len(stringlist[0])
    walls = []
    for jj in range(0,len(stringlist)):
        for ii in range(0, len(stringlist[0])):
            if stringlist[jj][ii] == '#':
                walls.append((ii,jj))
    G = nx.grid_2d_graph(w,h)
    G.remove_nodes_from(walls)
    return G

def createmazeSE(stringlist):
    """
    Creates a path map from a list of strings to define maze with start and end where the maze is surrounded by #
    """
    import networkx as nx
    h = len(stringlist)
    w = len(stringlist[0])
    walls = []
    for jj in range(0,len(stringlist)):
        for ii in range(0, len(stringlist[0])):
            if stringlist[jj][ii] == '#':
                walls.append((ii,jj))
            elif stringlist[jj][ii] == 'S':
                s = (ii,jj)
            elif stringlist[jj][ii] == 'E':
                e = (ii,jj)
    G = nx.grid_2d_graph(w,h)
    G.remove_nodes_from(walls)
    return G,s,e

def md(x,y):
    return sum([abs(x[i]-y[i]) for i in range(len(x))])