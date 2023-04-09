def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a='a'
    e='e'
    i='i'
    o='o'
    u='u'
    k=0
    l=0
    while k<len(s):
        if s[k]!=a and s[k]!=e and s[k]!=i and s[k]!=o and s[k]!=u:
            l+=1
        k+=1
    return l
print(main('codeschool'))