print ("Meu nome é Mickael")
print ('Óla mundo!')

Área do Cículo

raio = int(input("Digite um raio: "))
pi = 3.14159

area_raio = (raio * raio) * pi 

print (f"A area do raio é de:(area_raio)")


    aula2 
exemplo
a = 1
print(a)

def teste():
   a = 2 
   print(a)

teste()
print(a)

exemoplo2

num = float(input(f"Digite o numero real: "))

def converter_para_inteiro(num):
   return int(num)

print(converter_para_inteiro(num))

exemplo3

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))
d = int(input("Digite o quarto numero: "))

def soma(a,b,c,d):
    return(a+b+c+d)

print(soma(a,b,c,d))

exemplo4

print("Óla mundo!")
print('Óla', 'mundo!', end='\n' )
#sep='...' (exemplo para separar)
print('I agora')

exemplo5

a = 'Mickael'
b = 'Silva'

def funcao(a,b="default"):
    return f'{a} {b}'

print(funcao(a, b))

exercícios

exercício1

a = 'mickael'

def imprima(a="default"):
    return f'{a}'

print(imprima(a))

exercício2

a = int(input('Digite o numero: '))
def funcao(a='default'):
    if a%2 == 0:
     print('O numero e par')
    else:
     print('Onumero e impar')
     
     return f'{a}'

funcao(a)

exercício3

a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))

def maoirque(a,b):
 
 if a > b:
    print("A é maior que B")
 else:
   print("B maior qu A")   
   
maoirque(a, b)

exercício4


