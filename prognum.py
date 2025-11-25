def term(n):
    if n<3:
        return 1
    return term(n-2)+term(n-1)