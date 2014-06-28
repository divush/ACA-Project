#necessary module
import sys                
from turtle import *
from time import sleep

operators=('=','==','+','-','*','/','<','>')
all_comm=('MOVE','TURN','FIRE','BOMB','SHIELD')
loops=['REPEAT',['REPEAT','UNTIL']]
count={'{':0,'}':0}
value={}
block={}	#it stores codes in block
stack=[]    #stack acts as a stack for conditional strings
len_stack=0 
assembly=[[],[]]
counter=0
def cond(l,value):
	pos=l-1
	c=stack[pos]
	a=c.split()
	if(a[0]=='IF'):
		i=c.index('IF')
		s=c[i+2:]
		s=s.strip()
		t=eval(s,value)
		return t
	elif(a[1]=='UNTIL'):
		i=c.index('UNTIL')
		s=c[i+5:]
		t=eval(s,value)
		return t
	elif(a[1].isdigit()):
		x=int(a[1])
		if(x==0):
			t= False
		else:
			t=True
			x-=1
		a[1]=str(x)
	c=a[0]+' '+a[1]+' '+ a[2]
	stack[pos]=c	
	return t                 
def execute(s,counter):
	global len_stack
	condcounter=0;
	l=s.split("\n")
	ifcounter=False
	for y in l:
		y=y.strip()
		h=y.split()
		if(h==[]):
		  continue
		if h[0] in all_comm:
			x=all_comm.index(h[0])
			if(x==0):
				try:
					d=int(h[1])
					i=0		
					while(i<d):
						assembly[counter].append("moving")
						i=i+1
				except:
					sys.exit("no arguments for MOVE")
			elif(x==1):
				assembly[counter].append("turning "+h[1].lower())
			elif(x==2):
				assembly[counter].append("firing")
			elif(x==3):
				assembly[counter].append("bombing")
			elif(x==4):
				assembly[counter].append("shielding")
		elif h[0] in loops:
			stack.append(y)
			len_stack+=1
			mode=0
		elif (h[0]=='IF'):
			stack.append(y)
			elsecond=y
			len_stack+=1
			ifcounter=True
			mode=1
		elif(h[0]=='ELSE'):
			if(ifcounter):	
				mode=2
				stack.append(elsecond)
				len_stack+=1
			else:
				sys.exit("MISPLACE ELSE")
		elif h[0] in block:
			if(mode==0):
				while(cond(len_stack,value)):
					execute(block[h[0]],counter)
			elif(mode==1):
				if(cond(len_stack,value)):
					execute(block[h[0]],counter)
			elif(mode==2):
				if(cond(len_stack,value)):
					continue
				else:
					execute(block[h[0]],counter)
			stack.pop()
			len_stack-=1	
		elif (h[0][0]=="$"):
			a=y.index("=")
			z=y[1:a]
			z=z.strip()
			value[z]=eval(y[a+1:],value)
		else:
			sys.exit(h[0]+"is not a keyword")
def check(s):
	c=0
	for x in s:
		if(x.isalnum() or x=='{' or x=='}'or x=='$' or x==' ' or x=='\n'or x in operators):
			continue
		else:
			 c=1
	if(c):
		sys.exit('alphanumerics only')
def blocking(s):
	j=0
	y=len(s)
	i=0
	while(i<y):
		if(s[i]=='{'):
			count['{']+=1
		elif(s[i]=='}'):
			count['}']+=1
		if(count['}']==1):
			x=s[:i].rfind('{')
			block['@'+str(j)]=s[x+1:i]
			j+=1
			s=s[:x]+'\n@'+str(j-1)+s[i+1:]
			count['}']-=1
			count['{']-=1
			y=len(s)
			i=x-1
		i+=1	
	if(count['{']!=count['}']):
		sys.exit('braces incomplete')
	return s
try:
	f=open(sys.argv[1],'r')
except:
	sys.exit("file cannot be opened") #for error while execution
s=f.read()                         #s is string holding input from file
s=s.strip("\n")
print("reading and interpreting file 1")
check(s)
s=blocking(s)
execute(s,counter)
print("done")
try:
	f=open(sys.argv[2],'r')
except:
	sys.exit("file cannot be opened") #for error while execution
s=f.read()                         #s is string holding input from file
s=s.strip("\n")
print("reading and interpreting file 1")
check(s)
s=blocking(s)
execute(s,1)
print("done")
print(assembly[0])
print(assembly[1])
f.close()


poly=((6,-10),(4,-6),(4,2),(10,2),(0,10),(-10,2),(-4,2),(-4,-6),(-6,-10))

s1=Shape("compound")
s1.addcomponent(poly,'blue','black')
register_shape("myshape1",s1)

s2=Shape("compound")
s2.addcomponent(poly,'green','black')
register_shape("myshape2",s2)

s3=Shape("compound")
s3.addcomponent(poly,'white','black')
register_shape("myshape3",s3)

life=3
health=4
shield=5
n_bomb=6
n_shield=7
N=400

main1=Turtle(shape="myshape1")
main1.pu()
main1.speed(0)
main1.setpos(-200,0)
supp1=Turtle()
supp1.ht()
shielder1=Turtle(shape="myshape3")
shielder1.ht()
shielder1.pu()

main2=Turtle(shape="myshape2")
main2.pu()
main2.speed(0)
main2.setpos(200,0)
main2.lt(180)
supp2=Turtle()
supp2.ht()
shielder2=Turtle(shape="myshape3")
shielder2.ht()
shielder2.pu()

ht()

robo1=[main1,supp1,shielder1,True,500,0,20,5]
robo2=[main2,supp2,shielder2,True,500,0,20,5]
def health_dec(a,pensize):
	if a[shield]:
		a[shield]-=10*pensize
		if a[shield]<=0:
			a[health]=a[health]+a[shield]
			a[shield]=0
	else:
		a[health]-=10*pensize
		if a[health]<0:
			a[life]=False
			a[health]=0
	if(a[health]<0):
		a[life]=False
		a[health]=0

def fire(a,b,pensize):
	a[1].pensize(pensize)
	a[1].seth(a[0].heading())
	a[1].pu()
	a[1].setpos(a[0].pos())
	a[1].fd(13)
	a[1].pu()
	a[1].speed(3)
	hit=False
	if(int(a[1].heading())==0):
		if (abs(a[0].ycor()-b[0].ycor())<=10):
			m=int(b[0].xcor()-10)
			b[health]-=50*pensize
			hit=True
		else:
			m=N
		for i in range(int(a[1].xcor()), m, 10):
			a[1].pd()
			a[1].st()
			a[1].fd(10)
			a[1].ht()
			a[1].fd(10)
		if hit:
			b[0].ht()
			sleep(0.2)
			b[0].st()
	elif(int(a[1].heading())==90):
		if (abs(a[0].xcor()-b[0].xcor())<=10):
			m=int(b[0].ycor()-10)
			b[health]-=50*pensize
			hit=True
		else:
			m=N
		for i in range(int(a[1].ycor()), m, 10):
			a[1].st()
			a[1].fd(10)
			a[1].ht()
			a[1].fd(10)
		if hit:
			b[0].ht()
			sleep(0.2)
			b[0].st()
	elif(int(a[1].heading())==180):
		if (abs(a[0].ycor()-b[0].ycor())<=10):
			m=int(b[0].xcor()+10)
			b[health]-=50*pensize
			hit=True
		else:
			m=N
		for i in range(int(a[1].xcor()), -m, -10):
			a[1].st()
			a[1].fd(10)
			a[1].ht()
			a[1].fd(10)
		if hit:
			b[0].ht()
			sleep(0.2)
			b[0].st()
	else:
		if (abs(a[0].xcor()-b[0].xcor())<=10):
			m=int(b[0].ycor()-10)
			b[health]-=50*pensize
			hit=True
		else:
			m=N
		for i in range(int(a[1].ycor()), -m, -10):
			a[1].st()
			a[1].fd(10)
			a[1].ht()
			a[1].fd(10)
		if hit:
			b[0].ht()
			sleep(0.2)
			b[0].st()
def create_shield(a):
	a[2].pu()
	a[2].setpos(a[0].pos())
	a[2].seth(270)
	a[1].fd(13)
	a[1].pd()
	a[1].seth(0)
	a[1].speed(0)
	a[1].circle(13)
	a[1].speed(3)
screen=getscreen()
inp_len1 = len(assembly[0])
inp_len2 = len(assembly[1])
line1=0
line2=0
while(True):
	if((line1==inp_len1) & (line2==inp_len2) & robo1[life] & robo2[life]):
		print("Match was a tie")
		break
	if(robo1[life] & robo2[life]):
		if(line1!=inp_len1):
			if(assembly[0][line1]=='moving'):
				main1.fd(20)
			elif(assembly[0][line1]=='turning left'):
				main1.lt(90)
			elif(assembly[0][line1]=='turning right'):
				main1.rt(90)
			elif(assembly[0][line1]=='firing'):
				fire(robo1,robo2,1)
			elif(assembly[0][line1]=='bombimg'):
				fire(robo1,robo2,2)
			elif(assembly[0][line1]=='shielding'):
				robo1[shield]=50	
		if(line2!=inp_len2):
			if(assembly[1][line2]=='moving'):
				main2.fd(10)
			elif(assembly[1][line2]=='turning left'):
				main2.lt(90)
			elif(assembly[1][line2]=='turning right'):
				main2.lt(90)
			elif(assembly[1][line2]=='firing'):
				fire(robo2,robo1,1)
			elif(assembly[1][line2]=='bombimg'):
				fire(robo2,robo1,2)
			elif(assembly[1][line2]=='shielding'):
				robo1[shield]=50
	elif(robo1[life]):
		print("robo 1 is winner")
		break
	elif(robo2[life]):
		print("robo2 is winner")
		break
	else:
		print("Match was a tie")
		break
	print(line1)
	print(line2)
	if(line1<inp_len1):
		line1+=1
	if(line2<inp_len2):
		line2+=1
	if(robo1[shield]):
		create_shield(robo1)
	if(robo2[shield]):
		create_shield(robo2)
	sleep(1)
