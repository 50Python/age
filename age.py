driving = input('請問您有沒有開過車:')
if driving != 'yes' and driving != 'no':
	print('只能輸入"yes" / "no"')
	raise SystemExit #raise:觸發 SystemExit:系統離開

age = input('請問您的年齡:')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('您通過測驗了')
	else:
		print('奇怪、您怎麼有開過車')
elif driving == 'no':
	if age >= 18:
		print('你可以考駕照了啊、加油')
	else:
		print('很好、在幾年就可以考駕照了')

