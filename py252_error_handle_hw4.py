# -*- coding: utf-8 -*-

while  True:
	try:
		divisor, dividend = input('輸入除數與被除數:')
		result = float(divisor)/float(dividend)
		print ('%d / %d = %.2f' % (divisor,dividend,result))
		break
	except Exception, e:
		print '發生 %s exception, 請重新輸入' % (e)
