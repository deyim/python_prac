def searchList(L, x):
	for i in range(len(L)):
		if(x == L[i]):
			return i
	return -1

def main():
	fp_r = open("DataIn_02.txt", "r")
	fp_w = open("Out_02.txt", "w")

	for r in fp_r:
		key = int(r)
		values = fp_r.readline()
		i = searchList(values, key)
		if i != -1:
			fp_w.write("Key %d is at %d in " % (key, i))
		else:
			fp_w.write("Key %d is not in " % (key))
		fp_w.write(values)

	fp_r.close()
	fp_w.close()

if __name__ == '__main__':
	main()

'''
fp_r = open("DataIn_01.txt", "r")
fp_w = open("Out_01.txt", "w")

fp_w.write("The square results are\n")

num = []
for s in fp_r:
	for x in s.split():
		x = int(x) ; square = x*x
		num.append(x)
		fp_w.write("%2d " % square)
	fp_w.write("\n")

fp_w.write("--------------------------------\n")

totsum = 0 ; cnt = 0
for number in num:
	totsum = totsum + number
	cnt = cnt + 1

fp_w.write("The sum of input data is %d\n" % totsum)
fp_w.write("--------------------------------\n")

average = float(totsum)/cnt
fp_w.write("The average of input data is %.3f\n" % average)
fp_r.close()
fp_w.close()
'''