#      *
#     **
#    ***
#  *****
# ******
for i in range(1,6):
    for j in range(6,i,-1):
        print(" ",end="")
    for k in range(0, i) :  
        print("*",end="") 
    print("")