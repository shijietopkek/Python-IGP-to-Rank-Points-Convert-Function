

def convert_to_rp(igp):
    h2rp={"A":0,"B":2.5,"C":5,"D":7.5,"E":10,"S":15,"U":20}
    h1rp={"A":0,"B":1.25,"C":2.5,"D":3.75,"E":5,"S":7.5, "U":10}
    
    rank_point = 85 #assuming GP and PW Cs
    array=igp.split("/")
    h2=array[0]
    h1=array[1]
    for char in h2:
        rank_point-=h2rp[char]
    rank_point-=h1rp[h1]
    return rank_point

igps=[]
f = open("A-levels IGPs.txt", "r")
for lines in f:
    igps.append(lines[:len(lines)-1])
f.close()

new_f=open("A-Levels IGP Rank Points.txt","w")
for item in igps:
    new_f.write("{0}\n".format(convert_to_rp(item)))

new_f.close()
## code below are for testing purposes

##testarray=["AAA/A","UUU/U","AAB/C","CCC/B","AAA/B","CCD/C","CCC/D"]
##for test in testarray:
##    print(convert_to_rp(test))
