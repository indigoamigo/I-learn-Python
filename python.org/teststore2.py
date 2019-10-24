def teststore2(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key + ":" + kwargs[key])
    pass
