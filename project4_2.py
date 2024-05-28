print("1:addition operation \n"\
      "2:subtraction operation\n"\
      "3:multiply operation\n"\
      "4:division operation\n"\
      "5:modulo division operation")
def add(input1, input2):
    return input1 + input2

def sub(input1, input2):
    return input1 - input2
 
def mul(input1, input2):
    return input1 * input2
 
def div(input1, input2):
    return input1 / input2

def moddiv(input1,input2):
    return input1%input2

choice=int(input("select 1,2,3,4... :="))
input1=int(input("enter the number1:="))
input2=int(input("enter the number2:="))
if(choice==1):
    print(input1,"+",input2,"=",add(input1,input2))
elif(choice==2):
    print(input1,"-",input2,"=",sub(input1,input2))
elif(choice==3):
    print(input1,"*",input2,"=",mul(input1,input2))
elif(choice==4):
    print(input1,"/",input2,"=",div(input1,input2))
elif(choice==5):
    print(input1,"%",input2,"=",moddiv(input1,input2))
else:
    print("invalid input,give the valid input")


