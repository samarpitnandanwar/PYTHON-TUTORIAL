# def sum(a,b):
#     s = a+b
#     return s

# num1 = 5
# num2 = 10
# sum_of_num = sum(num1,num2)
# print("The sum of the two numbers is:", sum_of_num)


def percentage(marks1,marks2,total_marks):
    p = (((marks1+marks2)/total_marks)*100)
    return p


m1 = 35
m2 = 47
t = 100
percent = percentage(m1,m2,t)
print("Percentage obtained by student is : ", percent,"%")