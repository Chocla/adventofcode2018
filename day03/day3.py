fSize = 1000
fabric = [] 
for i in range(fSize):
    fabric.append([0]*fSize)

claims = open('input.txt','r').read().splitlines()

def parseClaims(claim):
    a = claim.split("@ ")[1]
    b = a.split(": ")
    x,y = b[0].split(",")
    l,w = b[1].split("x")
    return int(x),int(y),int(l),int(w)

def inputClaim(a,b,c,d):
    for i in range(a,a+c):
        for j in range(b,b+d):
            fabric[j][i] += 1

for claim in claims:
    x,y,l,w = parseClaims(claim)
    inputClaim(x,y,l,w)

c = 0
for i in range(len(fabric)):
    for j in range(len(fabric[i])):
        if fabric[i][j] > 1:
            c += 1
print c