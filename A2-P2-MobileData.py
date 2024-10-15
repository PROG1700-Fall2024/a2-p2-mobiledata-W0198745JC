#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:W0198745     
#Student Name:  Jenille Cheney

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
#input Mb Useage:
    mb=int(input("Enter Data Usage (Mb) : "))
#Elif statement for mb useage
    if mb <= 200:                        # thought all variables needed "" but just string does
        cost= 20.00
    elif mb == 200 and mb <=500:         #orginally had or but quickly switched to and
        cost= .105*mb
    elif mb >=500 and mb <=1000:
        cost= .110*mb
    else:
        cost=118.00

#calculate cost  ( This was done within the if/elif statement)
    
#print cost 
    print("Total Charge is ${0:.2f}".format(cost))






    # YOUR CODE ENDS HERE

main()