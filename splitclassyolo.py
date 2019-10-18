import shutil
import os
import glob
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--input_img", type=str, default="./imgdir",
                help="paht to input folder")
ap.add_argument("-o","--output_img", type=str, default="./output",
                help="paht to output folder")
ap.add_argument("-c","--class_img", type=str, default="0",
                help="class")
ap.add_argument("-m","--move_img", action="store_true",
                help="move image")
args = vars(ap.parse_args())
                                
data_path = os.path.join(args["input_img"],'*txt')
files = sorted(glob.glob(data_path))

name_img = None
last_name_img = None

count = 0

for f1 in files:
    head, tail = os.path.split(f1)
    token = open(f1,'r')
    linestoken=token.readlines()
    tokens_column_number = 0
    resulttoken=[]
    for x in linestoken:
        resulttoken.append(x.split()[tokens_column_number])
    token.close()
    for y in resulttoken:
        if (int(y) == int(args["class_img"])):
            print(y)
            count += 1
            print("counter :"+ str(count))
            name_img = tail
            if name_img != last_name_img:
                shutil.move(f1, args["output_img"])
                print("config moved")
                last_name_img = name_img
            
                if args["move_img"]:
                    pathImg = os.path.splitext(f1)[0]
                    shutil.move(("{}.jpg").format(pathImg), args["output_img"])
                    print("image moved")

