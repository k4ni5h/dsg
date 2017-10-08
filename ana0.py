import csv
import re
def mul(numbers):
	total = 1
	for x in numbers:
		total *= x  
	return total  
pattern = re.compile("\s*,\s*|\s+$")
pa=0
fa=0
with open('mushroom.csv', 'r') as problem:
	spam = csv.reader(problem, delimiter=' ', quotechar='|')
	for pro in spam:
		p=[x for x in pattern.split(pro[0]) if x]
		e_p=[0]*24
		p_p=[0]*24
		with open('mushroom_train.csv', 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for string in spamreader:
				value=[x for x in pattern.split(string[0]) if x]
				for i in range(24):
					if type(p[i]) == int:
						if value[i+1]==p[i+1] and value[0]=='p':
							p_p[i]+=1000
						elif value[i+1]==p[i+1] and value[0]=='e':
							e_p[i]+=1000
						elif value[0]=='p':
							p_p[i]+=1/(int(value[i+1])-int(p[i]))**2
						elif value[0]=='e':
							e_p[i]+=1/(int(value[i+1])-int(p[i]))**2
					else:
						if value[i+1]==p[i+1] and value[0]=='p':
							p_p[i]+=1
						elif value[i+1]==p[i+1] and value[0]=='e':
							e_p[i]+=1
		ep=pp=0
		for i in range(24):
			if(e_p[i]+p_p[i]!=0):
				ep+=e_p[i]*a_p[i]/(e_p[i]+p_p[i])
				pp+=p_p[i]*a_p[i]/(e_p[i]+p_p[i])
		if((ep>pp and p[0]=='e') or (ep<pp and p[0]=='p')):
			pa+=1
			print('pass', pa*100/(pa+fa))
		else:
			fa+=1
			print('fail', ep, pp, fa*100/(pa+fa))
print(pa*100/(pa+fa))