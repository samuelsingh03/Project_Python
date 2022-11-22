def prime_number(start,end):
    lst=[]
    for num in range(start,end + 1):
        if num > 1: 
            for j in range(2,num):
                if num % j==0:
                    break
            else:
                lst.append(num)
    print(lst)
    print()
    print("\nCount of prime numbers in the given range is: ",len(lst))
                
def composite_number(start,end):
    lst=[]
    for x in range(start,end+1):
        num=x
        count=0
        for y in range(1,num+1):
            if num%y==0:
                count+=1
        if count>2:
            lst.append(num)
    print(lst)
    print()
    print("\nCount of composite numbers in the given range is: ",len(lst))
#main
start=int(input('Enter starting number: '))
end=int(input('Enter ending number: '))
print('\nPrime numbers between',start,'and',end,'are:')
prime_number(start,end)
print()
print('\nComposite numbers between',start,'and',end,'are:')
composite_number(start,end)
