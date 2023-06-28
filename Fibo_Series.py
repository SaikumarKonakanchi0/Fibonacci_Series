#Write a Python program to get the Fibonacci series between 0 to 50
f=0
n=1
print(f)
print(n)
for i in range(2,20):
    t=f+n
    f=n
    n=t
    if t<=50:
        print(t)

#Another better version of code
fib_series=[0,1]
for i in range(2,20):
    next_num=fib_series[i-1]+fib_series[i-2]
    fib_series.append(next_num)
for i in fib_series:
    if i<=50:
        print(i)
