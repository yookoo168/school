
#2-8 猜數字的遊戲
from random import randint
answer=''
count_a=0
count_b=0
times=1

numbers=[0,1,2,3,4,5,6,7,8,9]
random_answer= [] 

for i in range(4):
	j=randint(0,9-i)
	random_answer.append(numbers[j])
	numbers.remove(numbers[j])
	i=i+1
	
for  i in range(4):
	answer=answer+str(random_answer[i])

input_number=input('請輸入你的四個數：')
while times <8 and input_number != answer:
	for i in range(4):
		for j in range(4):
			if  i==j and input_number[i]==answer[j]:
				count_a=count_a+1
			elif input_number[i]==answer[j]:
				count_b=count_b+1
	print(str(count_a)+'A'+str(count_b)+'B')
	count_a=0
	count_b=0
	times=times+1
	input_number=input('請輸入您猜的4個數：')
if input_number==answer:
	print('您答對了，正確答案是'+answer)
else:
	print('作答已達8次，遊戲結束，正確答案是'+answer)
