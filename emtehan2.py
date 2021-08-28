n = int(input())
l = []
for i in range(n):
    tmp = int(input())
    l.append(tmp)


ans =[l[0]]


for j in range(1,n):
    ans.append(l[j])
    print(ans)
    for i in range(len(ans)):
        if(ans[n-i] < ans[n-1-i]):
            ans[n-i],ans[n-i-l] = ans[n-i-l],ans[n-i]
        else:
            break
    print(ans)
                                             
    print()
