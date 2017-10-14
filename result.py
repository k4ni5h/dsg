import csv
import re
pattern = re.compile("\s*,\s*|\s+$")
pa=0
fa=0
a_p=[0.15860409826337477, 1.2747435360228356, 0.845964766110488, 0.00547585256576903, 2.0192923810152448, 0.0263207712091735, 0.32197017209078854, 0.15956111134532647, 0.17740154992449803, 12.946288524809457, 0.00035780949462392835, 1.1181562054708174, 0.1003224215778459, 0.0263207712091735, 0.09429281893071245, 0.10889749898807095, 0.0263207712091735, 0.11867734359936588, 0.8946856696230235, 0.42515720755683806, 0.12083303762333343, 1.1980906307383978, 0.3453133725306612, 0.26785230966307916]
with open('mushroom_test.csv', 'r') as problem:
	sol= open("result.txt","w+")
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
						if value[i+1]==p[i] and value[0]=='p':
							p_p[i]+=1000
						elif value[i+1]==p[i] and value[0]=='e':
							e_p[i]+=1000
						elif value[0]=='p':
							p_p[i]+=1/(int(value[i+1])-int(p[i]))**2
						elif value[0]=='e':
							e_p[i]+=1/(int(value[i+1])-int(p[i]))**2
					else:
						if value[i+1]==p[i] and value[0]=='p':
							p_p[i]+=1
						elif value[i+1]==p[i] and value[0]=='e':
							e_p[i]+=1
		ep=pp=0
		for i in range(24):
			if(e_p[i]+p_p[i]!=0):
				ep+=e_p[i]*a_p[i]/(e_p[i]+p_p[i])
				pp+=p_p[i]*a_p[i]/(e_p[i]+p_p[i])
		if(ep>pp):
			sol.write('e\n')
		else:
			sol.write('p\n')
	sol.close()