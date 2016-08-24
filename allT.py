def allT(D):
    check=type(D) is dict
    if not check:
        print('D must be a dictionary')
        return
    for keys in D:
        check=D[keys]==True
        if check==False:
            return(False)
    return(True)