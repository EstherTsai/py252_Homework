#-*- coding: utf-8 -*-
# 寫一個名為student的類別
# 其中屬性包含: name, gender, grades
# 函數包含:
#  1.avg: 回傳grades list的平均值
#  2.add(grade): 新增成績到grades list中
#  3. fcount: 回傳不及格(<60)的總數
# 於類別外寫一個top的函數:
#  1. 傳入值為學生物件的序列
#  2.將平均分數最高的學生回傳

class student:
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
		self.grades = []

	def avg(self):
		sum = 0
		for i in range(len(self.grades)):
			sum = sum + self.grades[i]
		avg = sum/len(self.grades)
		return avg

	def add(self, grade):
		self.grades.append(grade)

	def fcount(self):
		count = 0
		for i in range(len(self.grades)):
			if self.grades[i] < 60:
				count = count + 1
		return count

def top(*students):
	top_avg = 0
	for student in students:
		if student.avg() > top_avg:
			top_avg = student.avg()
	print ('%s\'s average grade is top. His/Her average grade is %f' % (student.name, top_avg)) 


s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)


print ('%s\'s average grade is %.2f and have %d grade less than 60.' % (s1.name, s1.avg(), s1.fcount()))
print ('%s\'s average grade is %.2f and have %d grade less than 60.' % (s2.name, s2.avg(), s2.fcount()))
print ('%s\'s average grade is %.2f and have %d grade less than 60.' % (s3.name, s3.avg(), s3.fcount()))
print ('%s\'s average grade is %.2f and have %d grade less than 60.' % (s4.name, s4.avg(), s4.fcount()))
print ('%s\'s average grade is %.2f and have %d grade less than 60.' % (s5.name, s5.avg(), s5.fcount()))

top(s1,s2,s3)
