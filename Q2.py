#Entrada
n = int(input('Digite um numero inteiro: '))
#Usando laço for
for i in range(n, 1, -1):
    #Usando a variavel i como variavel de controle
    #Usando end para ficar na mesma linha
    print(i, end = ' x ')
    #usando *= que corresponde a n = n * i
    n *= i - 1
 #print formatado   
print('1 = {}'.format(n))