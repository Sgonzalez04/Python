def mifactorial(n):
    if(n==1):
        return(1)
    else:
        f=n*mifactorial(n-1)
        return(n)