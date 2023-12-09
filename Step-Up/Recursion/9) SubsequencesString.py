def subSequences(idx,str,newstr):
    if idx >= len(str):
        res.append(newstr)
        return

    newstr += str[idx]
    subSequences(idx+1,str,newstr)

    newstr = newstr[:-1]
    subSequences(idx+1,str,newstr)

    return res


str = "abc"
res = []
subSequences(0,str,"")
print(res)

# Output : 
# ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']

