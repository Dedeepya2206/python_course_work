'''
fa=eval(input("follows account: "))
cf=eval(input("close friend: "))
if fa:
    if cf:
        print("story visible")
    else:
        print("not in close friends list")
else:
    print("follow the Account first")
    '''
'''
reg=eval(input("registered"))
if reg:
    ef=eval(input("fee paid"))
    if ef:
        print("Tournament entry confirmed")
    else:
        print("fee pending")
else:
    print("registration required")
    '''
la=eval(input("link active: "))
if la:
    pd=eval(input("permission granted: "))
    if pd:
        print("file open successfully")
    else:
        print("permission denied")
else:
    print("invalid file link")