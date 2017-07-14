import logging
logging.basicConfig(filename='calc_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Started')

def addition(x,y):      #Function for addition
    print str(x)+"+"+str(y)+"= "+str(x+y)

def sub(x,y):        #Function for subtraction
    print str(x)+"-"+str(y)+"= "+str(x-y)

def mul(x,y):    #Function for multiplication
    print str(x)+"*"+str(y)+"= "+str(x*y)

def div(x,y):    #Function for division
    try:
        print str(x)+"/"+str(y)+"= "+str(x/y)
    except ZeroDivisionError as e:
        logging.error('user enter y as %d '%y)
        print e

def square(x,y):     #Function for power
    print str(x)+"**"+str(y)+"= "+str(x**y)
t=1
while(t!=0):
    x = input("Enter 1st no.:")
    
    y = input("Enter 2nd no.:")
    
    op = raw_input("Enter operator(+,-,*,/,**):")
    logging.info('user enter operator as %s '%op)
    if((isinstance(x,str) or isinstance(y,str))):   #check if x or y is it string
        print "not possible"
        logging.info('user enter x as %s '%x)
        logging.info('user enter y as %s '%y)
        continue    #next iteration if string found
    else:       #if x or y not a string
        x = float(x)
        y = float(y)
        logging.info('user enter x as %d '%x)
        logging.info('user enter y as %d '%y)
    if(op=="+"):
        addition(x,y)   #calling to addition function
    elif(op=="-"):
        sub(x,y)    #calling to subtraction function
    elif(op=="*"):
        mul(x,y)    #calling to multiplication function
    elif(op=="/"):
            div(x,y)
    elif(op=="**"):     #calling to power function
        square(x,y)
    
    n=int(raw_input("Enter 1 for exit ELSE 2: "))
    if(n==1):   # exit condition if user enter 1
        t=0

logging.info('Finished')
