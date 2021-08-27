import os
import argparse
import filecmp
import time

parser = argparse.ArgumentParser()

parser.add_argument("-duplicates", action="store_true")
parser.add_argument("-large", action="store_true")
parser.add_argument("-size")
parser.add_argument("-images", action="store_true")
parser.add_argument("-old", action="store_true")
parser.add_argument("path")
parser.add_argument("-o")

args = parser.parse_args()
path = args.path+"\\"
files = os.listdir(path)
if args.images == True:
    temp = files[:]
    files.clear()
    for file in temp:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
           files.append(file)

if args.duplicates == True:
    haveDuplicate = [False]*len(files)
    for i in range(0, len(files)):
        for j in range(0, len(files)):
            if i == j:
                continue
            if filecmp.cmp(path+files[i],path+files[j]):
                haveDuplicate[i] = True 
    for i in range(0, len(haveDuplicate)):
        if haveDuplicate[i] == False:
           files.remove(files[i])
           i = i-1

def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size

def getFileSize(str):
    numbers = []
    vel = []
    for i in str:
        if i.isdigit():
            numbers.append(i)
        else:
            vel.append(i)
    return getFileSizeInByte(''.join(numbers), ''.join(vel))


def getFileSizeInByte(num, vel):
    if vel == "b":
        return int(num)
    elif vel == "kb":
        return int(num)*1024
    elif vel == "mb":
        return int(num)*1024*1024
    elif vel == "gb":
        return int(num)*1024*1024*1024
    else:
        return int(num)*1024*1024*1024*1024

if args.large == True:
    for i in files[:]:
        if file_size(path+i) < getFileSize(args.size):
            files.remove(i)

if args.old == True:
    for i in files[:]:
        if time.time() - os.path.getctime(path+i) >= 86400*365 :
            files.remove(i)

if not args.o == None:
    f = open(args.o, mode="w")
    for i in files:
        f.write(path+i+"\n")
    f.close()
else:
    for i in files:
        print(path+i+"\n")
