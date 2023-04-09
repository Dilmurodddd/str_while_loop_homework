def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    b=0
    while a<len(s):
        if s[a].isdigit():
           b+=int(s[a])
        a+=1 
    return b
print(main('126'))