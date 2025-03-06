def hello():
    return "hello batungbakal!"

hello()

if len(hello()) > 5:
    print('long text')
elif   len(hello())  > 0:
  print('short text')
else:
    print('zero text')  

name = "Jilian" 
age = 22        
height = 5.8    
is_programmer = True 


print(f"Hi, I am {name}. I am {age} years old and my height is {height}.")


print(f"{name} is a { 'programmer' if is_programmer else 'person'}")

print("{} is a {}".format(name, "programmer" if is_programmer else "person"))
