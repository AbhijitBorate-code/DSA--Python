def string(s):
    for i in range(len(s)):
        for i in s:
            if i.count(s) == 1:
                #print(i.count(s),s[i])
                return s.index(i)
            else:
                return -1
s = "loveleetcode"
print(string(s))
