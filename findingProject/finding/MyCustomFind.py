import os#Бібліотека для роботи з файловою системою
import argparse#Бібліотека для роботи з консольними командами
import filecmp#Бібліотека для порівняння файлів і каталогів
import time#Бібліотека для роботи з часом

def parse_args(args):
    parser = argparse.ArgumentParser()#Створення об'єкту, який відповідає за парсинг команд

    #Додання аргументів, які можна використовувати в командах
    parser.add_argument("-duplicates", action="store_true", help="insert duplicates(optional)")
    parser.add_argument("-large", action="store_true", help="insert files large than -size(optional)")
    parser.add_argument("-size", help="minimal size of insertions files(requaired after large argument)")
    parser.add_argument("-images", action="store_true", help="insert images(optional)")
    parser.add_argument("-old", action="store_true", help="insert files elder than one year(optional)")
    parser.add_argument("path", help="insertion path(requaired)")
    parser.add_argument("-o", help="file path where result will be saved saved(optional)")

    return parser.parse_args(args)

#Видалення не картинок зі списку файлів, якщо опція вказана в команді
def getImages(files):
    for file in files[:]:
        if not (file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")):
           files.remove(file)
    return files
    
#формування стрічки з результатом вибірки
def getResult(files, path):
    result = ""
    for i in files:
            result += path+i+"\n"
    return result
    
#Запис результату вибірки у файл заданий користувачем, або вивід у консоль
def writeResult(o, result):
    if not o == None:
        f = open(o, mode="w")
        f.write(result)
    else:
        print(result)
        
def main():
    args = parse_args(["-images", "D:\\InPc\\Downloads\\"])#Парсинг команди
    path = args.path+"\\"#Отриання шляху до заданої директорії
    files = os.listdir(path)#Отримання списку файлів в заданій директорії
    if args.images:
        files = getImages(files)
    if args.duplicates:
        files = getDuplicates(files, path)
    if args.large:
        files = getLarge(files, path, args.size)
    if args.old:
        files = getOld(files, path)
    result = getResult(files, path)
    writeResult(args.o, result)

if __name__ == "__main__":
    main()





#Пошук файлів дублікатів і видалення файлів зі списку, які ними не є, якщо це вказано в команді
def getDuplicates(files, path):
    for i in files[:]:
        haveDupl = False
        for j in files[:]:
            if i.index == j.index:
                continue
            if filecmp.cmp(path+i,path+j):
                haveDupl = True
        if haveDupl == False:
            files.remove(i)
    return files



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
def getLarge(files, path, size):
    for i in files[:]:
        if file_size(path+i) < getFileSize(size):
            files.remove(i)
    return files

#Видалення файлів зі списку, якщо вони створені більше року тому і якщо це задано командою
def getOld(files, path):
    for i in files[:]:
        if time.time() - os.path.getctime(path+i) >= 86400*365 :
            files.remove(i)
    return files




