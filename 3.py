#Primeira entrada
x = int(input("Digite o valor de y: "))

#segunda entrada
y = int(input("Digite o valor de x: "))
#Variavel de controle
mdc = x
#entrando no laço usando as condiçoes
while x % mdc != 0 or y % mdc != 0: #usando os operadores aritméticos 
        mdc -= 1 

print("MDC({}, {}) = {}".format(x,y,mdc))  #usando o print formatado