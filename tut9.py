list = ["kurkure", "harpic", "eno", "sope", "dhokla powder", "spray", 45]
print(list[6])
print(list)


number = [2, 4, 2, 6, 9, 4, 0]
number.sort()
number.reverse()
print(number)
print(number[0:7])
print(number[1:8])
print(number)
print(number[::1])
print(number[::])
print(number[::2])
print(number[::-1])
print(number[::-3])
print(number[0:7:-3])
print(number[::3])
print(number[0:7:3])



var1 = [1, 2, 3, 4, 5, 6, 7, 8]
var1.append(112)
print(var1)
print(len(var1))
print(max(var1))
print(min(var1))



var2=[]
var2.append(264723468273658237)
var2.append(24324250)
var2.append(6545132)
print(var2)

var3=[]
var3.append(1)
var3.append(1)
var3.append(1)
var3.append(1)
var3.append(1)
var3.append(1)
print(var3)



var4=[1, 2, 3, 5, 7, 8, 8]
var4.insert(2, 5)
print(var4)

var5=[2,4,1,4,7,3]
var5.remove(2)
print(var5)

var6=[1,2,3,4,5,6,7]
var6.pop()
print(var6)

var7 = (1,)
print(var7)

a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)



p = 89
q = 98
p, q = q, p
print(p,q)
