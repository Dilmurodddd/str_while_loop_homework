def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    b=0
    while a<len(s):
        if (int(s[a].isdigit())+1)%2==0:
            b+=int(s[a])
        a+=1
    return b
print(main('123456789'))