def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    b=0
    c=0
    d=''
    f=0
    e=''
    k=0
    while a<len(s):
        if s[a].isalpha():
            b+=1
        if s[a].isdigit():
            e+=s[a]
        
        a+=1
    while k<len(e):
        if int(e[k])%2==0:
            c+=1
        if int(e[k])%2!=0:
            f+=1
        k+=1
    return f"Hariflar soni: {b}, Raqamlar : {e}, Juft raqamlar soni: {c}, Toq raqamlar soni: {f}"


print(main('123456789a'))
    #if int(s[a])==0 or int(s[a])==1 or int(s[a])==2 or int(s[a])==3 or int(s[a])==4 or int(s[a])==5 or int(s[a])==6 or int(s[a])==7 or int(s[a])==8 or int(s[a])==9:

    # a=0
    # b=0
    # e=0
    # k=0
    # c=''
    # d=0
    # while a<len(s):
    #     if s[a].isalpha():
    #         c=c+s[a]
    #         if c.isalpha():
    #             e+=1  
    #     if int(s[a].isdigit())%2==0:
    #         k+=1
    #     if int(s[a].isdigit())%2!=0:
    #         d+=1
    #     a+=1
    # return e,k,d


