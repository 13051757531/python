i= 9;
while i>1:
	a=input("1代表继续玩，0代表结束游戏，请输入数字：");
	a=int(a);
	if a==1:
		print("游戏开始");
		age= input("请输入您的年龄:");
        print(age);
        if age>=18:
	       print("可以上网");
        elif age>=17:
	       print("您过两天来上网哈");
		elif age>=12:
			print("您把钱存着，过两年来上网哈");
		else:
			print("尚未成年，禁止上网");
	elif a==0:
		break;
	else:
		print("请输入数字1或0")
