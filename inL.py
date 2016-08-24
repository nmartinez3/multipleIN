def inL(x,y,mode='single'):
    checkx=(type(x) is list or type(x) is tuple) and type(x) is not str
    checky=(type(y) is list or type(y) is tuple) and type(y) is not str
    if not checkx:
        print('x must be a list or tuple')
        return
    if not checky:
        print('y must be a list or tuple')
        return
    if mode!='single' and mode!='multiple':
        print("argument 'mode' must be either 'single' or 'multiple'")
        return

    if mode=='single':
        for entry in x:
            check=entry in y
            if check==False:
                return(False)
        return(True)

    if mode=='multiple':
        checks=dict()
        for entry in x:
            check=entry in y
            checks[entry]=check
        return(checks)