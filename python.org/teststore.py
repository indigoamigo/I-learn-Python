def teststore(variable, *arguments, **keywords):
    print(variable)
    for arg in arguments:
        print(arg)
    for key in keywords:
        print(key + ":" + keywords[key])
