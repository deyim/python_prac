students = [{"num" : "1", "name": "강민균", "kor": 90, "eng": 85, "math": 90, "total": 0, "avg": 0, "order": 0},
	{"num" : "2", "name": "최준민", "kor": 90, "eng": 92, "math": 83, "total": 0, "avg": 0, "order": 0},
	{"num" : "3", "name": "서수민", "kor": 85, "eng": 85, "math": 90, "total": 0, "avg": 0, "order": 0},
	{"num" : "4", "name": "최대운", "kor": 80, "eng": 80, "math": 85, "total": 0, "avg": 0, "order": 0},
	{"num" : "5", "name": "이창엽", "kor": 80, "eng": 80, "math": 80, "total": 0, "avg": 0, "order": 0}]

classtotal = 0
kortot =0;engtot=0;mathtot=0

for student in students:
	student["total"] = student["kor"] + student["eng"] + student["math"]
	student["order"] = 1
	classtotal += student["total"]
	kortot += student["kor"]
	engtot += student["eng"]
	mathtot += student["math"]
	student["avg"] = student["total"]/3

newlist = sorted(students, key=lambda k: k['total']) 
#print(newlist)
i=5
for student in newlist:

	student["order"] = i
	i -=1

print(newlist)

classtotal /= 5 ; kortot /=5 ; engtot/=5; mathtot/=5
print("총점의 반 평균: %.2f\n" % classtotal)
print("과목별 평균 국어 평균: %.2f\n\
	   영어 평균: %.2f\n\
	   수학 평균: %.2f" %(kortot, engtot, mathtot))