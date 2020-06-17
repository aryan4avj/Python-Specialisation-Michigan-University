def nested_list():
    n = int(input())
    a = [[input(),float(input())] for i in range(0,n)]
    s = sorted(list([x[1] for x in a]))
    s.remove(min(s))
    s = sorted(list([x[1] for x in a if x[1]==min(s)]))
    lst =  [i[0] for i in a if i[1] == s[1]]
    lst.sort()
    for i in lst:
        print(i)
