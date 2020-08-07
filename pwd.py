
pwd = 'a123456'
print('你有三次機會輸入密碼喔!')
count = 1

while count <= 3:

	
	user_pwd = input('請輸入密碼:')
	pwd_count = 3 - count

	if user_pwd == pwd:
		print('登入成功!')
	elif pwd_count > 0:		
		count = count + 1
		print('密碼錯誤!還有' ,pwd_count, '次機會')

	elif pwd_count == 0:
		break
