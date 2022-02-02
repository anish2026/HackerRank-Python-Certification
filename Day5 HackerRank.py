``` 

# Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for
# more detail).

# Note:  is considered to be an even index.

```

T=int(input())
for _ in range(0,T):
        a=input()
        ans1=[]
        ans2=[]
        for i in range(len(a)):
            if i%2==0:
                ans1 += a[i]
            else:
                ans2 += a[i]
        print(''.join(map(str,ans1)),''.join(map(str,ans2)))
        



