from sys import argv
n=int(argv[1])

def printParanthesis(n,pre="",open=0,close=0):
    if(close==n):
        print pre
        return 1

    count=0
    if(open<n):
        count+=printParanthesis(n,pre+"(",open+1,close)

    if(close<open):
        count+=printParanthesis(n,pre+")",open,close+1)

    return count
########################

print  printParanthesis(n)
   


