f=open('hexout.txt') 
ff=open('hxoutput.txt','w') 
arr=[]
for line in f:
    if len(line)>128:
        l=len(line)//4 
        dec=int(line,2)
        X=hex(dec)
        mystring=str(X)
        padded = '0x' + '0' * (l - len(mystring)+2) + mystring[2:]
        if len(padded)>35:
            print(line)
            print(padded) 
        #hx=f"{42:#0{l}X[2:]}" 
        arr.append(padded) 
ff.write('input message   output message   key \n')
for i in range(0,len(arr),3):
    ff.write("Round ")
    ff.write(str(i//3)) 
    ff.write("\n")
    for j in range(2,32,8):
        ff.write(arr[i][j+0:j+2])
        ff.write(" ")
        ff.write(arr[i][j+2:j+4])
        ff.write(" ")
        ff.write(arr[i][j+4:j+6])
        ff.write(" ")
        ff.write(arr[i][j+6:j+8])
        ff.write(" ") 
        ff.write("  ")
        ff.write(arr[i+2][j:j+2])
        ff.write(" ")
        ff.write(arr[i+2][j+2:j+4])
        ff.write(" ")
        ff.write(arr[i+2][j+4:j+6])
        ff.write(" ")
        ff.write(arr[i+2][j+6:j+8])
        ff.write(" ") 
        ff.write("  ")
        ff.write(arr[i+1][j:j+2])
        ff.write(" ")
        ff.write(arr[i+1][j+2:j+4])
        ff.write(" ")
        ff.write(arr[i+1][j+4:j+6])  
        ff.write(" ")
        ff.write(arr[i+1][j+6:j+8])
        ff.write(" ") 
        ff.write(" ") 
        ff.write("\n")
    for j in range(34,64,8):
        for k in range(28):
            ff.write(' ')
        ff.write(arr[i+1][j:j+2])
        ff.write(" ")
        ff.write(arr[i+1][j+2:j+4])
        ff.write(" ")
        ff.write(arr[i+1][j+4:j+6])  
        ff.write(" ")
        ff.write(arr[i+1][j+6:j+8])
        ff.write(" ") 
        ff.write(" ") 
        ff.write("\n") 
