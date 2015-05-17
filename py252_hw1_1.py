#-*- coding: utf-8 -*-

# 分別用for,while迴圈各寫⼀一個nxn的乘法表
# 1. 程式可以讀取使用者輸入的值 n, n>1
# 2. 輸出樣式: (n=2) 1*1=1 1*2=2 2*1=1 2*2=4

n=input('enter the value:')

print ('-------------for loop--------------------')
for k in range(1, n+1):
	for h in range(1, n+1):
		print ('%s*%s=%s\t' % (k,h,k*h),end='')
	print ()

print ('-------------while loop------------------')
i=1
while  i<n+1:
	j=1
	while j<n+1:
		print ('%s*%s=%s\t' % (i,j,i*j),end='')
		j=j+1
	i=i+1
	print()
		
