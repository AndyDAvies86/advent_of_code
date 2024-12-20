#%%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphaup = alphabet.upper()
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
numlist = [str(x) for x in range(0,10)]
#%%
def lineparse(inputfile):
    file = open(inputfile,"r")
    start = file.read()
    return start.split("\n")