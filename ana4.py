import csv
import re
pattern = re.compile("\s*,\s*|\s+$")
pa=0
fa=0
a_p=[0.17167278422211904, 0.9554910412380235, 0.7309995247496145, 0.0018142153893401301, 2.0351962306959814, 0.026528072337391993, 0.20936392517620978, 0.1225636014273695, 0.19620909566760428, 12.845097809887832, 0.00016191148635004977, 1.0966195603450535, 0.13384230968813587, 0.026528072337391993, 0.08225960277695289, 0.09561408693113416, 0.026528072337391993, 0.11961204065010102, 0.8658291025794785, 0.32657580591923413, 0.11017575207206826, 1.18872612080697, 0.3016427678886841, 0.26162517345464853]
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
					if type(p[i+1]) == int:
						if value[i+1]==p[i+1] and value[0]=='p':
							p_p[i]+=1000
						elif value[i+1]==p[i+1] and value[0]=='e':
							e_p[i]+=1000
						elif value[0]=='p':
							p_p[i]+=1/(int(value[i+1])-int(p[i+1]))**2
						elif value[0]=='e':
							e_p[i]+=1/(int(value[i+1])-int(p[i+1]))**2
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
			while((ep<pp and p[0]=='e') or (ep>pp and p[0]=='p')):
				for i in range(24):
					if((p[0]=='e' and e_p[i]>p_p[i]) or (p[0]=='p' and e_p[i]<p_p[i])):
						a_p[i]*=1.00000001
					elif((p[0]=='p' and e_p[i]>p_p[i]) or (p[0]=='e' and e_p[i]<p_p[i])):
						a_p[i]*=.99999999
				ep=pp=0
				for i in range(24):
					if(e_p[i]+p_p[i]!=0):
						ep+=e_p[i]*a_p[i]/(e_p[i]+p_p[i])
						pp+=p_p[i]*a_p[i]/(e_p[i]+p_p[i])
print(pa*100/(pa+fa),a_p)