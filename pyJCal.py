#! /usr/bin/python2
# coding=utf-8

class pyJCal:
	def __init__(self):
		pass
		
	def div(self, a, b):
		return a / b
		
	def gregorian_to_jalali(self, g_y, g_m, g_d):
		"""
		this function returns result of converting ye gregorian date to jalali
		"""
		g_days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) 
		j_days_in_month = (31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29)
		
		gy = g_y - 1600
		gm = g_m - 1
		gd = g_d - 1
		
		g_day_no = 365 * gy + self.div(gy+3, 4) - self.div(gy+99, 100) + self.div(gy+399, 400)
		
		i = 0
		while i < gm:
			g_day_no += g_days_in_month[i]
			i += 1
			
		if(gm > 1 and ((gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0))):
			g_day_no += 1
			
		g_day_no += gd
		
		j_day_no = g_day_no - 79
		
		j_np = self.div(j_day_no, 12053)
		j_day_no = j_day_no % 12053
		
		jy = 979 + 33 * j_np + 4 * self.div(j_day_no, 1461)
		
		j_day_no %= 1461
		
		if j_day_no >= 365:
			jy += self.div(j_day_no - 1, 365)
			j_day_no = (j_day_no - 1) % 365
			
		i = 0
		while (i < 11 and j_day_no >= j_days_in_month[i]):
			j_day_no -= j_days_in_month[i]
			i += 1
			
		jm = i + 1
		jd = j_day_no + 1
		
		return (jy, jm, jd)
		
	def MonthName(self, _m_num):
		_m_num = int(_m_num)

		if _m_num == 1:
			return 'فروردین'
		elif _m_num == 2:
			return 'اردیبهشت'
		elif _m_num == 3:
			return 'خرداد'
		elif _m_num == 4:
			return 'تیر'
		elif _m_num == 5:
			return 'مرداد'
		elif _m_num == 6:
			return 'شهریور'
		elif _m_num == 7:
			return 'مهر'
		elif _m_num == 8:
			return 'آبان'
		elif _m_num == 9:
			return 'آذر'
		elif _m_num == 10:
			return 'دی'
		elif _m_num == 11:
			return 'بهمن'
		elif _m_num == 12:
			return 'اسفند'
		else:
			return False
			
	def WeekDayName(self, _d):
		if _d == 'Saturday':
			return 'شنبه'
		elif _d == 'Sunday':
			return 'یکشنبه'
		elif _d == 'Monday':
			return 'دوشنبه'
		elif _d == 'Tuesday':
			return 'سه شنبه'
		elif _d == 'Wednesday':
			return 'چهارشنبه'
		elif _d == 'Thursday':
			return 'پنجشنبه'
		elif _d == 'Friday':
			return 'جمعه'
		else:
			return _d
