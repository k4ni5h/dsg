import csv
import re
pattern = re.compile("\s*,\s*|\s+$")
pa=0
fa=0
a_p=[0.1303908637813203, 1.9019328217850615, 0.9635296442908282, 0.01989510882008876, 2.01954581857548, 0.026855856441815942, 0.5503665918838783, 0.21072470900749063, 0.14998589419255282, 12.973835137475719, 0.0009142705367632175, 1.007678881672292, 0.06739120923902397, 0.026855856441815942, 0.10891095084984513, 0.11564585923673676, 0.026855856441815942, 0.1203656167813437, 0.8210614225985617, 0.5503665918838773, 0.12527799783557694, 1.1768656113212714, 0.45059905005811585, 0.2732975838266239]
with open('mushroom_test.csv', 'r') as problem:
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
			print('e')
		else:
			print('p')