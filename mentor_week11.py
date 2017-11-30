students = [{"num":"1", "name":"강민균", "kor":90, "eng":80, "math":85,\
"total":0,"avg":0.0, "order":0},{"num":"2", "name":"최준민", "kor":90,\
"eng":85, "math":90,"total":0,"avg":0.0, "order":0},{"num":"3", "name":" 서수민",\
"kor":80, "eng":80, "math":80,"total":0,"avg":0.0, "order":0},\
{"num":"4", "name":"최대운", "kor":90, "eng":92, "math":83,"total":0,"avg":0.0,\
"order":0},{"num":"5", "name":"이창엽", "kor":85, "eng":85, "math":90,\
"total":0,"avg":0.0, "order":0}]

orders = {}

for student in students:
	student["total"] = student["kor"] + student["eng"] + student["math"]
	orders[student["name"]] = student["total"]

orders = sorted(orders.values(), reverse=True)
#print(orders)
rank = 1
for points in orders:
	for student in students:
		if student["total"] == points:
			student["order"] = rank
			rank += 1
			students.remove(student)
			print(student)




year = int(input("enter your birth year: "))
age = 2018 - year
status = ""

def isUniversityStudent(age):
	if 20 <= age & age <= 26:
		return True
	else:
		return False

def isHighSchoolStudent(age):
	if 17 <= age & age < 20:
		return True
	else:
		return False

def isMiddleSchoolStudent(age):
	if 14 <= age & age < 17:
		return True
	else:
		return False

def isElementarySchoolStudent(age):
	if 8 <= age & age < 14:
		return True
	else:
		return False

def main():
	if isUniversityStudent(age):
		status = "대"
	elif isHighSchoolStudent(age):
		status = "고등"
	elif isMiddleSchoolStudent(age):
		status = "중"
	elif isElementarySchoolStudent(age):
		status = "초등"
	elif age < 8:
		left = 8-age; status = "초등"
		print("%d년 후에.." % left)

	if status:
		print("안녕! %s학생" %status)

if __name__ == '__main__':
	main()