
import workone

path="/Users/renren/study/utfw.txt"

ROWS=12

file=open(path)

i=0
j=0
work=['']*ROWS

for line in file :
    work[i]=line
    i=i+1
    if ( i % ROWS == 0 ):
        workone.workone(work)
        j=j+1
        print "-- "+str(j)+" --"
        work=['']*ROWS
        i=0

