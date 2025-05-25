def reverseword(s):
    s=s.split()
    arr=s[::-1]
    return " ".join(arr)


s = "the sky is blue"
print(reverseword(s))