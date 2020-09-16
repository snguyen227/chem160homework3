from random import choice
n=8
Emax=-5.0
Emin=+5.0
deltaE=0.001
n2=64
# Initialize all spin up case
spins=[[1 for i in range(n)] for j in range(n)]
# Calculate the system energy
energy=0
energy+=2*deltaE/n2
for i in range(n):
    for j in range(n):
        energy-=(spins[i][j]*(spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                                spins[(i+1)%n][j]+spins[(i+n-1)%n][j]))
    if energy > Emax:
        Emax=energy
print("<E>=%4.2f"%(float(energy)/(n*n)))
# Check this result before continuing
#
# Initialize random spin case (copy & edit the code given above)
spins=[[choice((-1,1)) for x in range(n)] for y in range(n)]
# Calculate the system energy
energy=0
energy+=2*deltaE/n2
for i in range(n):
    for j in range(n):
        energy-=(spins[i][j]*(spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                            spins[(i+1)%n][j]+spins[(i+n-1)%n][j]))
    if energy < Emin:
        Emin=energy
print("<E>=%4.2f"%(float(energy)/(n*n)))

#Print out ising model
## Add lines here from lecture notes
sym=["d","u"]
for i in range(n):
    for j in range(n):
        print("%s"%(sym[(spins[i][j]+1)//2]),end=" ")
    print("")
print('%10.6f %10.6f'%(Emin, Emax))