i= 9;
while i>1:
	a=input("1��������棬0���������Ϸ�����������֣�");
	a=int(a);
	if a==1:
		print("��Ϸ��ʼ");
		age= input("��������������:");
        print(age);
        if age>=18:
	       print("��������");
        elif age>=17:
	       print("����������������");
		elif age>=12:
			print("����Ǯ���ţ���������������");
		else:
			print("��δ���꣬��ֹ����");
	elif a==0:
		break;
	else:
		print("����������1��0")
