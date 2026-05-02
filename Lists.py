# -----------------------------------------
#            <<    Lists     >>
# -----------------------------------------
# [1]  List Items Are Enclosed in Square Brackets
# [2]  List Are Orders, To Use Index To Access Item
# [3]  List Are Mutable => Add, Delete, Edit
# [4]  List Items Is Not Unique
# [5]  List Can Have Different Data Types
# -----------------------------------------

Horus =["Zero", "One", "Two", "One", 7, 77.65, False]

print(Horus)           #    Whole List   ["Zero", "One", "Two", "One", 7, 77.65, False]
print(Horus[1])        #    One
print(Horus[-1])       #    False
print(Horus[-2])       #    77.65

print(Horus[1:5])      #    ["One", "Two", "One", 7, 77.65]  
print(Horus[:4])       #    ["Zero", "One", "Two", "One"]
print(Horus[4:])       #    [7, 77.65, False]

print(Horus[::1])      #    ["Zero", "One", "Two", "One", 7, 77.65, False]
print(Horus[::2])      #    ["Zero", "Two", 7, False]

Horus[3] = "Three"     #    Replace
Horus[-1] = True       #    Replace
print(Horus)           #    ["Zero", "One", "Two", "Three", 7, 77.65, True]

Horus[0:4] = ["A", "B", "C", "D"]      #    Replace
print(Horus)                           #    ["A", "B", "C", "D", 7, 77.65, True]

Horus[0:3] = ["R"]     #    Replace
print(Horus)           #    ["R", "D", 7, 77.65, True]


# -----------------------------------------
#         <<    Lists Methods   >>
# -----------------------------------------

# append()           بتعمل اضافة للعناصر داخل القائمة كعنصر واحد فقط حتي لو كانت قائمة أخري

myFriends = ["Mohammed", "Hossam", "Eslam", "Fares", "Ahmed"]
myFriends.append("Mahmoud")
myFriends.append(100)
myFriends.append(70.5)
myFriends.append(False)
print(myFriends)       #   ["Mohammed", "Hossam", "Eslam", "Fares", "Ahmed", "Mahmoud", 100, 70.5, False]

myOldFriends = ["Samy", "Osama", "Hesham", "Arafa", "Saad"]
myFriends.append(myOldFriends)
print(myFriends)
print(myFriends[2])         #     Eslam
print(myFriends[-4])        #     100
print(myFriends[9])         #     ["Samy", "Osama", "Hesham", "Arafa", "Saad"]  
print(myFriends[9][3])      #     Arafa

# -----------------------------------------

# extend()           بتعمل اضافة للقائمة داخل قائمة أخري كعناصر متفرقة 

a = [1, 2, 3, 4, 5]
b = ['A', 'B', 'C', 'D', 'E']

a.extend(b)
print(a)          #   [1, 2, 3, 4, 5, 'A', 'B', 'C', 'D', 'E'] 

# -----------------------------------------

# remove()              ازالة ما بداخل القائمة (لو كان من الخانة كذا حاجة شبها..بيزيل أول شئ فقط)

x = [1, 2, 3, 'Horus', 'Elzaem', 'Rafat', 'Horus']
x.remove('Horus')
print(x)          #   [1, 2, 3, 'Elzaem', 'Rafat', 'Horus']

# -----------------------------------------

# sort()                    ترتيب الارقام

z = [28, 36 ,2, 45.5, -63, 100, 87]
z.sort()
print(z)           #   [-63, 2, 28, 36, 45.5, 87, 100]

w = ['D', 'H', 'R', 'C', 'A', 'N']
w.sort()
print(w)

z.sort(reverse=True)       #     كدا يرتبهم معكوسين
w.sort(reverse=True)       #     كدا يرتبهم معكوسين
print(z)           #   [100, 87, 45.5, 36, 28, 2, -63]
print(w)           #   ['R', 'N', 'H', 'D', 'C', 'A']

# -----------------------------------------

# reverse()             بتعكس ما بداخل القائمة

r = [65, 21, 87, 7, 14, 'Horus', 54, 23]
r.reverse()
print(r)           #   [23, 54, 'Horus', 14, 7, 87, 21, 65]

# -----------------------------------------

# clear()           بتمسح كل ما بداخل القائمة

s = [1, 2, 3, 4, 5]
s.clear()
print(s)          #   []

# -----------------------------------------

# copy()           بتعمل نسخة من القائمة متاح تعدل فيها لكن النسخة الأساسية بتفضل زي ما هي

d = [1, 2, 3, 4, 5]
e = d.copy()
print(d)             #   [1, 2, 3, 4, 5]
print(e)             #   [1, 2, 3, 4, 5]

d.append(6)          #   [1, 2, 3, 4, 5, 6]
print(d)             #   [1, 2, 3, 4, 5]
print(e)

# -----------------------------------------

# count()               بيعدلك عدد العنصر الموجود داخل القائمة

k = [6, 8, 7, 3, 1, 8, 4, 2, 9, 8, 5]
print(k.count(8))        #   3

# -----------------------------------------

# index()              بتوصل للأسم داخل القائمة

y = ['Samy', 'Horus', 'Hesham', 'Arafa', 'Horus', 'Saad']
print(y.index('Horus'))

# -----------------------------------------

# insert()             insert(index, object)

q = [1, 2, 3, 4, 'A', 'B', 'C']
q.insert(1, 'D')
print(q)             #   [1, 'D', 2, 3, 4, 'A', 'B', 'C']

# -----------------------------------------

# pop()               بيطلعلك من القائمة العنصر اللي عاوزه

f = [1, 2, 3, 4, 'A', 'B', 'C']
print(f.pop(3))      #   4
print(f.pop(-2))     #   B