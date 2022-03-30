#hüseyin özdemir 200444013
  
#q1

def body(a,b):
     for i in range(b,a):
         
          if i > 1 :
               for j in range(2, i):
                    if i % j == 0:
                         
                         break
               else:
                    print(i)

def prime(num1,num2):
     if num1 > num2:
          body(num1,num2)
     else:
          body(num2,num1)

prime(15,30)
     


#question1

#question2
def smallestnumber(lists):

    smallest_num = lists[0]
    for i in lists:
        if i < smallest_num:
            smallest_num = i
    return smallest_num
print(smallestnumber([2342,23423,23,5,45,45,6]))

#question_3
def counts(number):
    ct = 0
    if number < 0:
        number = -1*number
    if number == 0:
        ct = 1
    while number > 0:
        number = number//10
        print("The number value", number)
        ct+=1
        print("Number of digits: ", ct)
    print("Total number of digits",ct)
counts(79)