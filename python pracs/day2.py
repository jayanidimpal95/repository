

#print x,y,op

def addition(x,y):
    print str(x)+"+"+str(y)+"= "+str(x+y)

def sub(x,y):
    print str(x)+"-"+str(y)+"= "+str(x-y)

def mul(x,y):
    print str(x)+"*"+str(y)+"= "+str(x*y)

def div(x,y):
    print str(x)+"/"+str(y)+"= "+str(x/y)

def square(x,y):
    print str(x)+"**"+str(y)+"= "+str(x**y)
t=1
while(t!=0):
    x = float(raw_input("Enter 1st no.:"))
    y = float(raw_input("Enter 2nd no.:"))
    op = raw_input("Enter operator(+,-,*,/,**):")
    if(op=="+"):
        addition(x,y)
    elif(op=="-"):
        sub(x,y)
    elif(op=="*"):
        mul(x,y)
    elif(op=="/"):
        if(y==0):
            print "Not possible"
        else:
            div(x,y)
    elif(op=="**"):
        square(x,y)
    
    n=int(raw_input("Enter 1 for exit ELSE 2: "))
    if(n==1):
        t=0


