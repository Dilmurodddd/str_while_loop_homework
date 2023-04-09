def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    b=0
    c=0
    d=len(s)
    while a<len(s):
        if s[a].isdigit():
            b+=1
        if s[a].isalpha():
            c+=1
        a+=1
    return d-(b+c)
print(main('xs$%^&BH656GG'))