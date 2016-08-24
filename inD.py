def inD(x,y,mode='single'):
    check=type(x) is dict and type(y) is dict
    if not check:
        print('x and y must both be dictionaries')
        return
    if mode!='single' and mode!='multiple':
        print("argument 'mode' must be either 'single' or 'multiple'")
        return

    if mode=='single':
        keys=list(x.keys())
        for key in keys:
            check=key in list(y.keys())
            if check==False:
                return(False)
        return(True)

    if mode=='multiple':
        checks=dict()
        keys=list(x.keys())
        for key in keys:
            check=key in list(y.keys())
            checks[key]=check
        return(checks)