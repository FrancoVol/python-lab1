flag=True
lista=[]
while flag==True:
    print ("""Insert the command:
    [1: insert a new task
    2: remove a task
    3: show all the tasks
    4: close the program]""")
    command= int(input())
    if command==1:
        print ("Scrivere al task da inserire:")
        new=input()
        lista.append(new)
    elif command==2:
        print ("Scrivere la task da rimuovere:")
        rem=input()
        if rem in lista:
            lista.remove(rem)
        else:
            print ("Task not in the list")
    elif command==3:
        for task in lista:
            print (task)
    elif command==4:
        flag=False

