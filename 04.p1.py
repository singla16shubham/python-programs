a='''Dear <|NAME|>,
     you are Selected!
 
     Date: <|DATE|>
 '''
name=input("Enter your name\n")
date=input("Enter the date\n")
a=a.replace("<|NAME|>",name)
a=a.replace("<|DATE|>",date)
print(a)