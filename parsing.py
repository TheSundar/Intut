__author__ = 'rajesh reddy'
import pip

# import glob
#
# list_of_files = glob.glob('./*.txt')
#
# with open("stripD.xls", "w") as fout:
#     for fileName in list_of_files:
#         data_list = open( fileName, "r" ).readlines()
#         fout.write(data_list[17])
#         fout.writelines(data_list[44:])


import glob
import time
import re

time1 = time.time()
# path = 'C:/Users/rajesh reddy/Downloads/Txt/*.txt'
path = 'C:/Users/rajesh reddy/Downloads/parsers/TXTS/*.txt'
L1 = ["DOCTOR", "BACHELOR", "B.E","POSTGRADUATE","GRADUATE","B.SC","BCA","MCA","MSC","MASTERS","B.TECH"]
# "Doctor" in line or "Bachelor" in line or "B.E." in line or "PostGraduate" in line or "Graduate" in line or "B.sc" in line\
#          or "BCA" in line or "MCA" in line or "MSC" in line or "Master"
files=glob.glob(path)
for file in files:
    f=open(file, 'r')
    search = f.readlines()
    count =0
    # print search
    for i, line in enumerate(search):
        for k in L1:
            if k in line.upper():
                count+=1
                for l in search[i:i+2]:
                    z = re.split(' in ',l)
                    print z
                    # print l,
        if count>2:
            break
            # print

    f.close()
print time.time()-time1