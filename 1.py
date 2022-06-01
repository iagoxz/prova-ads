dia =int(input("digite o dia: "))#primeira entrad
mes =int(input("digite o mes: "))#segunda entrada
ano =int(input("digite o ano: "))#terceira entrada
#usando validaçao do mes com tipo boleano true or false
validaçao = False

#usando o if para testar os meses com 31 dias
if  mes==1 or mes==3 or mes==5 or mes==7 or \
    mes==8 or mes==10 or mes==12:#todos os meses listados nesse if tem 31 dias
     if dia<=31:
            validaçao = True #se algum desses meses tiver 31 dias vai ser valido

elif mes==4 or mes==6 or mes==9 or mes==11:#todos os meses com 30 dias
    if dia<=30: #se o mes for menor ou igual a 30 o resultado vai ser verdadeiro (true)
        validaçao= True

elif mes == 2:
    if ano%4==0 and ano%100!=0 or ano%400==0: #testando se o ano for bissexto 
        if dia <= 29:
            validaçao = True #validando o mes 2 com - ou = 29 dias se for 30 dias daria invalido
        elif(dia<=29):
                        validaçao = True 


if validaçao:
    print('A data {}/{}/{} é VÁLIDA!'.format(dia,mes,ano)) #usando print formatado
else:
    print('A data {}/{}/{} é INVÁLIDA!'.format(dia,mes,ano)) #usando print formatado
