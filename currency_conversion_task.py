#18-09-14
#Toby Kerslake
#currency conversion task

total = int(input("Please enter your amount of money"))

total20 = total // 20
remainder = total % 20

total10 = remainder // 10
remainder = remainder % 10

total5 = remainder // 5
remainder = remainder % 5

total2 = remainder // 2
remainder = remainder % 2

total1 = remainder // 1
remainder = remainder % 1

print("Your money can be divided into {0} 20 pound notes, {1} 10 pound notes, {2} 5 pound notes, {3} 2 pound coins, and {4} 1 pound coins.".format(total20,total10,total5,total2,total1))







