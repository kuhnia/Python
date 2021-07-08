def f2():
    myStr = ""
    for i in range(1000, 3100):
        if (i % 7 == 0) and (i % 5 != 0):
            myStr += str(i)+', '
    print(myStr)

def f3(num):
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        return num*f3(num-1)

def f4(num):
    res = 1
    for i in range(2, num+1):
        res*=num
        num-=1
    return res

def f5(n):
    dictionary = {}
    for i in range(1, n):
        dictionary[i] = i**2
    return dictionary

def f7(s):
    tpl = []
    for i in s:
        if(i.isdigit()):
            tpl.append(i)
        tuple(tpl)
    return tpl

def f8(s):
    lst = []
    count = -1
    for i in s:
        if i.isalpha() and count == -1 :
            lst.append(i)
            count+=1
        elif i.isalpha():
            lst[count] += i
        else:
            lst.append("")
            count+=1
    return sorted(lst)

def f9(s):
    for i in s:
        print(i.title())

def f10(s):
    prev = True
    words = []
    count = -1
    for i in s:
        if not i.isspace() and prev == True:
            words.append(i)
            prev = False
            count+=1
        elif not i.isspace() and prev == False:
            words[count] += i
        else:
            prev = True
    return set(words)


def f11(s):
    numericStr = []
    numeric = []
    prev = True
    count = -1
    for i in s:
        if i.isdigit() and prev == True:
            numericStr.append(i)
            prev = False
            count+=1
        elif i.isdigit() and prev == False:
            numericStr[count] += i
        else:
            prev = True
    for i in numericStr:
        num = int(i, 2)
        if num % 5 == 0:
            numeric.append(num)
    return numeric

def f12(a):
    forSum = []
    for i in range(4):
        temp = a
        for j in range(i):
            temp = temp * 10 + a
        forSum.append(temp)
    return sum(forSum)

def f13(s):
    if not (6 <= len(s) <= 12):
        return "Кількість символів повинна бути в межах від 6 до 12 включно"
    aToZ = False
    zeroToNine = False
    AtoZ = False
    specSym = False
    for i in s:
        if i.islower():
            aToZ = True
        elif i.isupper():
            AToZ = True
        elif i.isdigit():
            zeroToNine = True
        elif i == "$" or i == "#" or i == "@":
            specSym = True
        else:
            return "Вводьте лише лише латинські символи у верхньому і нижньому регістрі, а також цифри і $ # @"
    if not aToZ:
        return "Пароль повинен містити хочаб одну маленьку літеру"
    if not aToZ:
        return "Пароль повинен містити хочаб одну велику літеру"
    if not zeroToNine:
        return "Пароль має містити хочаб одну цифру"
    if not specSym:
        return "Пароль має містити хочаб один з символів: $ # @"
    return "Пароль відповідає правилам валідації"

def f14(listOfTuples):
    listOfTuples.sort(key=lambda val: val[2])
    listOfTuples.sort(key=lambda val: val[1])
    listOfTuples.sort(key=lambda val: val[0])
    return listOfTuples

#print(f14([
#    ("Mykola", 18, 9),
#    ("Artem", 18, 8),
#    ("Vika", 17, 9),
#    ("Masha", 17, 7)
#]))

def f15(s):
    x = 0
    y = 0
    for i in s:
        if i == "1 UP":
            y+=1
        elif i == "2 LEFT":
            x-=1
        elif i == "3 DOWN":
            y-=1
        elif i == "4 RIGHT":
            x+=1
    return (x**2 + y**2)**(1/2)

def f16(s):
    prev = True
    words = []
    count = -1
    for i in s:
        if not i.isspace() and prev == True:
            words.append(i)
            prev = False
            count+=1
        elif not i.isspace() and prev == False:
            words[count] += i
        else:
            prev = True
    unicWords = sorted(set(words))
    dictionary = {}
    for i in unicWords:
        dictionary[i] = s.count(i)
    return dictionary

#print(f16('''Вот дом,
#Который построил Джек.
#А это пшеница,
#Которая в темном чулане хранится
#В доме,
#Который построил Джек.
#А это веселая птица-синица,
#Которая часто ворует пшеницу,
#Которая в темном чулане хранится
#В доме,
#Который построил Джек.''')) 

