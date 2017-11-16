Grade = [[0 for col in range(5)] for row in range(4)]
kor_score = [49,79,20,100,80] 
math_score = [43,59,85,30,90] 
eng_score = [49,79,48,60,100] 
midterm_score = [kor_score, math_score, eng_score]
IDs = [201701, 201702, 201703, 201704, 201705]
def findGrade(N):
	if N >= 90:
		return 'A'
	elif N >= 80:
		return 'B'
	elif N >= 70:
		return 'C'
	elif N >= 60:
		return 'D' 
	else:
		return 'F'

def findGPA(G):
	if G == 'A':
		return 4
	elif G=='B':
		return 3
	elif G=='C':
		return 2
	elif G=='D':
		return 1
	else:
		return 0


def findAvg(i):
	sum = findGPA(Grade[0][i]) + findGPA(Grade[1][i]) + findGPA(Grade[2][i])
	return sum/3

print("학번 ", end="\t")
for ID in IDs:
	print(ID, end="\t")
print()

for i in range(len(IDs)):
	Grade[0][i] = findGrade(kor_score[i])
	Grade[1][i] = findGrade(math_score[i])
	Grade[2][i] = findGrade(eng_score[i])
	Grade[3][i] = findAvg(i)

print("국어 ", end="\t")
for grade in Grade[0]:
	print(grade, end="\t")
print()

print("수학 ", end="\t")
for grade in Grade[1]:
	print(grade, end="\t")
print()

print("영어 ", end="\t")
for grade in Grade[2]:
	print(grade, end="\t")
print()

print("학점 ", end="\t")
for grade in Grade[3]:
	print("%.3f" % grade, end="\t")
print()


