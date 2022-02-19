import csv
import os
import sys
import subprocess
import filecmp
functitle=[]
funcvalue=[]
statetitle=[]
statevalue=[]
pq=0
g=0
with open('functionResult.csv', 'w') as csvfile1, open('statementResult.csv','w') as csvfile2 :
        spamwriter1 = csv.writer(csvfile1, delimiter=',')
        spamwriter2 = csv.writer(csvfile2, delimiter=',')
	fp1=open("universe");
        i=0
	for l1 in fp1:
	   os.system("gcc -fprofile-arcs -ftest-coverage tcas_m1.c")	
	   os.system("./a.out "+l1)
           i=i+1
           j=1
           k=1
	   os.system("gcov -abcfu tcas_m1.c")  
	   fp=open("tcas_m1.c.gcov");
	   for line in fp:
		try: 
			if "block:" in line:
				f_call=line.split(",")[1];
                                functitle.append(j)
                                j=j+1
                                if 1 <=int(f_call):
                                  funcvalue.append("1")
                                else: 
                                  funcvalue.append("0")
			elif "lcount:" in line:
				break;
		except:
			print "exiting"		
			exit(1)

	   os.system("gcov tcas_m1.c")  
	   fp1=open("tcas_m1.c.gcov");
	   for line1 in fp1:
		try:    
                        flag=line1.split(":")[0];
			if "-" in flag:
                            continue
                        elif "#####" in flag:
                            statevalue.append("0")
                            statetitle.append(k)
                            k=k+1
                        else: 
                            statevalue.append("1")
                            statetitle.append(k)
                            k=k+1
		except:
			print "exiting"		
			exit(1)

           p=filecmp.cmp('/home/saksham/Desktop/BTP-2/tcas/outputs/t'+str(i), '/home/saksham/Desktop/BTP-2/tcas/outputs_m1/t'+str(i)) 
           if p==True:
             statevalue.append(int('0'))
             funcvalue.append(int('0'))
           else:
             statevalue.append(int('1'))
             funcvalue.append(int('1'))
           if pq==0:
                functitle.append("Result")
                statetitle.append("Result")
		spamwriter1.writerow(functitle)
                spamwriter2.writerow(statetitle)
		pq=1
           if len(funcvalue)>1:		
	        spamwriter1.writerow(funcvalue)
                funcvalue=[]
           else:
	        funcvalue=[]
           if len(statevalue)>1:		
	        spamwriter2.writerow(statevalue)
                statevalue=[]
           else:
	        statevalue=[]



