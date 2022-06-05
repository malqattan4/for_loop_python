#Basic - Print all integers from 0 to 150.

for x in range (151):
    print(x)



#Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for y in range (5,1001):
    if y%5==0:
        print(y)



#Counting, the Dojo Way - Print integers 1 to 100. 
# If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".

for z in range (1,101,1):
    if z%10==0:
        print("Coding Dojo.")
    elif z%5==0:
        print("Coding")



#That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum=0
for a in range (500000):
    if a%2!=0:
        sum+=a
print(sum)



#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for b in range (2018, 0, -4):
    print(b)



#Flexible Counter - Set three variables: lowNum, highNum, mult. 
#Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
#For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum =4
highNum =10
mult =2

for c in range(lowNum, highNum+1):
    if c%mult==0:
        print(c)