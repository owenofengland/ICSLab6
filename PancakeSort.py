def pancake(mylist):
    if len(mylist) == 1:
        return mylist

    mymax = 0
    for x in range(0, len(mylist)):
        vala = mylist[x]
        if vala > mymax:
            mymax = mylist[x]
            maxidx = x

    mylist[0:maxidx+1] = reversed(mylist[0:maxidx+1])
    mylist.reverse()
    pancake(mylist[0:len(mylist)-1])

    finallist = [mylist[len(mylist) - 1]] + pancake(mylist[0:len(mylist)-1])
    return finallist


print(pancake([3,34,9,7,22]))