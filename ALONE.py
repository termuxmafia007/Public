import os,time
def clear():
	os.system('clear')
def banner():
	clear()
	print("""
\033[1;37m  
            ########      ##    ##
               ##         ###  ###
	       ##         ########
	       ##         ##    ##
	       ##    #    ##    ##  #  
(!)========================================
(!) Author   : Vahid Saiyad
(!) Guthub   : termuxmafia007
(!) Facebook : 100072661180552
(!) Type     : FREE
\033[1;37m(!)========================================""")
def Run():
	bit = platform.architecture()[0]
	os.system('clear')
	print(logo)
	print('[•] Choose Your Country For Cloning\n\033[1;37m(!)══════════════════════════════════════════')
	print('[1] Pak Cloning \n[2] BD Cloning\n[0] Exit')
	Aking = input('[•] Choose : ')
	if Aking =='1':
		if bit =='32bit':
			import AKING 
		elif bit =='64bit':
			import AKING 
	elif Aking =='2':
		if bit =='32bit':
			import AKING
		elif bit =='64bit':
			import AKING
Run() 
	
	
	
	
	
	
	
		
			
		
			
	
		
			
		
			
