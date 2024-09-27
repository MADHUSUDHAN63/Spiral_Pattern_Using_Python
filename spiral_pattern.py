n = int(input('ENter a number:'))
eve = (n%2 ==0 )
val = 0
mid = n//2
c1 = (n-1)*4

for i in range(1,n+1):
    inc = (mid*8)+1
    dec = (mid*8)-3

    for j in range(1,n+1):
        if i<=j and i+j <= n+1:
            val+=1
            print(val,end=' ')

        elif i>j and i+j <=n+1:
            if j==1:
                val = c1-(i-2)
                print(val,end=' ')
            elif eve:
                dec-=8
                val+=dec
                print(val,end=' ')
            else:
                inc-=8
                val+=inc
                print(val,end=' ')

        elif i+j > n+1 and i<j:
            if eve:
                val-= 1+((j-(mid+1))*8)
                print(val,end=' ')
            else:
                val -= 5+ ((j-(mid+2))*8)
                print(val,end=' ')

        else:
            val-=1
            print(val,end=' ')

    print()
