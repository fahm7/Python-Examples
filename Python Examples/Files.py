
f=open("../guido_bio.txt")
txt=f.read()
f.close()


#print(txt)

#print f

try:
    with open("../future.txt")as fabj:
        txt = fabj.read()
except IOError:

   txt= "This file is not Yet created!"

#print(txt)

seasons = ["winter", "summer","spring","rainy"]

with open("../seasons.txt","w") as sea_file:
    for season in seasons:
        sea_file.write(season)
        sea_file.write("\n")
# ******* Read it line by Line
# print >> f, 'Filename:', filename  # Python 2.x
# print('Filename:', filename, file=f)  # Python 3.x

with open("../seasons.txt","a") as f:
    f.write(23*"=")
    f.write("\nThere are 4 seasons")
