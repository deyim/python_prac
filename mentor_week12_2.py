import sys
fo = open("PythonOutFile.txt","w")
linecount = 0
for line in sys.stdin:
    linecount+=1
    fo.write(line)
fo.writelines("\n\n입력한 행의개수 {}\n".format(str(linecount)))
fo.close()
