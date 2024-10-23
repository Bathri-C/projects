'''To find armstrong number'''
def digits(num1):
    s = 0
    while num1 > 0:
        num1//=10
        s+=1
    return s

def sum(num1):
        s = digits(num1)
        sum1 = 0
        while num1>0:
          dig=num1%10
          num1 //= 10
          sum1+=dig**s
        return sum1

num = int(input('enter a integer value : '))
mi=sum(num)

if mi== num:
    print(f'the given {num} is armstrong number')
else:
    print(f'the given {num} is not a armstrong number')


'''Armstrong number for given interval'''
start = int(input("enter the starting value for armstrong number : "))
ends = int(input('enter the ending value for armstrong number : '))
print(f'the given interval of {start} and {ends} of armstrong number is  :',end = " ")

for i in range(start,ends+1):
    j = i
    sum = 0
    while j > 0:
        k=j%10
        f = len(str(i))
        sum+=k**f
        j//=10

    if i == sum:
        print(i,end=' ')

'''To check armstrong number'''
num = int(input('enter the number : '))
find = num
sum = 0

pov = len(str(find))

while find !=0:
    k= find % 10  # k = 15%10 = 5
    sum = sum + k**pov  # 3**3 + 5**3 + 1**3
    find = find // 10 # find = 1

if sum==num:
           print(f'the given {num} is armstrong number')
elif num<0:
    print('enter the positive number ')
else:
    print('it\'s not a armstrong number')
#
#
def LCM(arr, n):
    # Find the maximum value in arr[]
    max_num = 0;
    for i in range(n):
        if (max_num < arr[i]):
            max_num = arr[i];

    # Initialize result
    res = 1;

    # Find all factors that are present
    # in two or more array elements.
    x = 2;  # Current factor.
    while (x <= max_num):

        # To store indexes of all array
        # elements that are divisible by x.
        indexes = [];
        for j in range(n):
            if (arr[j] % x == 0):
                indexes.append(j);

        # If there are 2 or more array
        # elements that are divisible by x.
        if (len(indexes) >= 2):

            # Reduce all array elements
            # divisible by x.
            for j in range(len(indexes)):
                arr[indexes[j]] = int(arr[indexes[j]] / x);

            res = res * x;
        else:
            x += 1;

    # Then multiply all reduced
    # array elements
    for i in range(n):
        res = res * arr[i];

    return res;


# Driver code
arr= list(map(int,input().split(',')))
n = len(arr);
print(LCM(arr, n));