x = 0
while x <= 3:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	x = x + 1
	if x == 1:
		print('密碼錯誤，還有2次機會')
	elif x == 2:
		print('密碼錯誤，還有1次機會')
	else:
		print('密碼錯誤，已無機會')
		break