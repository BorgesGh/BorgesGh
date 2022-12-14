import random 
import pyautogui 

pyautogui.move(100,100)
letras = "abcdefghijklmnopqrstuvwxyz" 
LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
Nums = "0123456789" 
Especi = "@#$%¨&*/\?" 

senha = letras + LETRAS + Nums + Especi 

tamanho = 8 
#for i in range(10):

 #   final = "".join(random.sample(senha,tamanho))
  #  print(final) 
    
nums = [1,6,3,4,10,2] 
carros = ["EuQuero","Tepossuir","1234532","@#$pasivo"]
random.shuffle(nums)
peixe = "".join(random.sample(carros,2)) 


print(nums) 
print(peixe)