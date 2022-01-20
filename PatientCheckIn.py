#Patient Check in program
name = input('name: ')
age = input("age: ")
age = int(age)
age+=10
status = input("is "+name+" new patient? (Y/N): ")
status = status.upper()
if(status=="Y"):
  status = "New Patient"
else:
  status = "Existing Patient"


print("---------Patient Info------")
print("name: "+name+"\nage: ",age, "\nstatus: "+status)

