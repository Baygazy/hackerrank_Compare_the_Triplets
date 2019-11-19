# def start
    ar = 0
    br = 0
    if a[0] > b[0]:
        ar += 1
    elif a[0] == b[0]:
        None
    else:
        br += 1
    print("[0] ", ar, br)

    if a[1] > b[1]:
        ar += 1
    elif a[1] == b[1]:
        None
    else:
        br += 1
    print("[1] ", ar, br)

    if a[2] > b[2]:
        ar += 1
    elif a[2] == b[2]:
        None
    else:
        br += 1
    print("[2] ", ar, br)

    a = ar
    b = br
    return (a, b)

#def stop