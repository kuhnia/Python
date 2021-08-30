import os#Бібліотека для роботи з файловою системою
import argparse#Бібліотека для роботи з консольними командами
import filecmp#Бібліотека для порівняння файлів і каталогів
import time#Бібліотека для роботи з часом

parser = argparse.ArgumentParser()#Створення об'єкту, який відповідає за парсинг команд

#Додання аргументів, які можна використовувати в командах
parser.add_argument("-duplicates", action="store_true", help="insert duplicates(optional)")
parser.add_argument("-large", action="store_true", help="insert files large than -size(optional)")
parser.add_argument("-size", help="minimal size of insertions files(requaired after large argument)")
parser.add_argument("-images", action="store_true", help="insert images(optional)")
parser.add_argument("-old", action="store_true", help="insert files elder than one year(optional)")
parser.add_argument("path", help="insertion path(requaired)")
parser.add_argument("-o", help="file path where result will be saved saved(optional)")

args = parser.parse_args()#Парсинг команди

path = args.path+"\\"#Отриання шляху до заданої директорії

files = os.listdir(path)#Отримання списку файлів в заданій директорії

#Видалення не картинок зі списку файлів, якщо опція вказана в команді
if args.images == True:
    for file in files[:]:
        if not (file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")):
           files.remove(file)

#Пошук файлів дублікатів і видалення файлів зі списку, які ними не є, якщо це вказано в команді
if args.duplicates == True:
    for i in files[:]:
        haveDupl = False
        for j in files[:]:
            if i.index == j.index:
                continue
            if filecmp.cmp(path+i,path+j):
                haveDupl = True
        if haveDupl == False:
            files.remove(i)

#Отримання розміру файлу байтах
def file_size(file_path):
    file_info = os.stat(file_path)
    return file_info.st_size

#Розділення стрічки на частину з величиною, та частину зі значенням(перетворення зі string в int)
def getFileSize(str):
    numbers = []
    vel = []
    for i in str:
        if i.isdigit():
            numbers.append(i)
        else:
            vel.append(i)
    return getFileSizeInByte(int(''.join(numbers)), ''.join(vel))

#Перетворення розміру файлу з користувацьких одиниць до кількості байтів
def getFileSizeInByte(num, vel):
    vel = vel.lower()
    if vel == "b":
        return num
    elif vel == "kb":
        return num*1024
    elif vel == "mb":
        return num*1024*1024
    elif vel == "gb":
        return num*1024*1024*1024
    else:
        return num*1024*1024*1024*1024

#Видалення файлів зі списку, що мають менший розмір ніж вказаний користувачем, якщо задано командою
if args.large == True:
    for i in files[:]:
        if file_size(path+i) < getFileSize(args.size):
            files.remove(i)

#Видалення файлів зі списку, якщо вони створені більше року тому і якщо це задано командою
if args.old == True:
    for i in files[:]:
        if time.time() - os.path.getctime(path+i) >= 86400*365 :
            files.remove(i)

#формування стрічки з результатом вибірки
result = ""
for i in files:
        result += path+i+"\n"

#Запис результату вибірки у файл заданий користувачем, або вивід у консоль
if not args.o == None:
    f = open(args.o, mode="w")
    f.write(result)
else:
    print(result)
