print("PROGRAMA PARA ESCREVER POR EXTENSO VALORES MONETARIOS DE -999.99 A 999.99\n")
while True:
    try:
        print("Os valores devem ser digitados com ponto em vez de virgula!")
        valor=input("Digite um valor: ")
        numero=float(valor)
    except ValueError:
        print("Deve-se digitar um valor monetário entre -999.99 e 999.99!")
    else:
        if numero>=1000 or numero<=-1000:
            print("Deve-se digitar um valor monetário entre -999.99 e 999.99!")
        else:
            parte=valor.split(".")
            if parte[0]=="":
                parte[0]="0"
            elif parte[0]=="-":
                parte[0]="0"
            if len(parte)==1:
                parte.append("00")
            elif parte[1]=="":
                parte[1]=="00"
            elif len(parte[1])==1:
                parte[1]=parte[1]+"0"

            if parte[0] == "0" and parte[1] == "00":
                print("zero reais")

            if len(parte[1])>2:
                print("Deve-se digitar um valor monetário entre -999.99 e 999.99!")
            
            else:

                reais   =float(parte[0])
                centavos=float(parte[1])

                centena = float(reais)//100
                centena = float(centena)

                dezena = (float(reais) - (float(centena) * 100)) // 10
                dezena = float(dezena)

                unidade = float(reais) - (centena * 100) - (dezena * 10)

                dig1centavos=centavos//10
                dig2centavos=centavos%10

                if float(reais) < 0:
                    print("menos ", end="")
                
                if centena == 1 and dezena == 0 and unidade == 0:
                    print("cem ", end="")
                elif centena == 1:
                    print("cento ", end="")
                elif centena == 2:
                    print("duzentos ", end="")
                elif centena == 3:
                    print("trezentos ", end="")
                elif centena == 4:
                    print("quatroscentos ", end="")
                elif centena == 5:
                    print("quinhentos ", end="")
                elif centena == 6:
                    print("seiscentos ", end="")
                elif centena == 7:
                    print("setessentos ", end="")
                elif centena == 8:
                    print("oitocentos ", end="")
                elif centena == 9:
                    print("novecentos ", end="")

                if dezena != 0 and centena != 0:
                    print("e ", end="")

                if dezena == 1:
                    if unidade == 0:
                        print("dez ", end="")
                    if unidade == 1:
                        print("onze ", end="")
                    elif unidade == 2:
                        print("doze ", end="")
                    elif unidade == 3:
                        print("treze ", end="")
                    elif unidade == 4:
                        print("quatorze ", end="")
                    elif unidade == 5:
                        print("quinze ", end="")
                    elif unidade == 6:
                        print("dezesseis ", end="")
                    elif unidade == 7:
                        print("dezessete ", end="")
                    elif unidade == 8:
                        print("dezoito ", end="")
                    elif unidade == 9:
                        print("dezenove ", end="")
                elif dezena == 2:
                    print("vinte ", end="")
                elif dezena == 3:
                    print("trinta ", end="")
                elif dezena == 4:
                    print("quarenta ", end="")
                elif dezena == 5:
                    print("cinquenta ", end="")
                elif dezena == 6:
                    print("sessenta ", end="")
                elif dezena == 7:
                    print("setenta ", end="")
                elif dezena == 8:
                    print("oitenta ", end="")
                elif dezena == 9:
                    print("noventa ", end="")

                if dezena!=0 and unidade !=0:
                    print("e ", end="")

                if dezena != 1:
                    if unidade == 1:
                        print("um ", end="")
                    elif unidade == 2:
                        print("dois ", end="")
                    elif unidade == 3:
                        print("tres ", end="")
                    elif unidade == 4:
                        print("quatro ", end="")
                    elif unidade == 5:
                        print("cinco ", end="")
                    elif unidade == 6:
                        print("seis ", end="")
                    elif unidade == 7:
                        print("sete ", end="")
                    elif unidade == 8:
                        print("oito ", end="")
                    elif unidade == 9:
                        print("nove ", end="")

                if reais == 1:
                    print("real ", end="")
                elif reais !=0:
                    print("reais ", end="")

                if centavos != 0:
                    print("e ", end="")

                if dig1centavos == 1:
                    if dig2centavos == 1:
                        print("onze ", end="")
                    elif dig2centavos == 2:
                        print("doze ", end="")
                    elif dig2centavos == 3:
                        print("treze ", end="")
                    elif dig2centavos == 4:
                        print("quatorze ", end="")
                    elif dig2centavos == 5:
                        print("quinze ", end="")
                    elif dig2centavos == 6:
                        print("dezesseis ", end="")
                    elif dig2centavos == 7:
                        print("dezessete ", end="")
                    elif dig2centavos == 8:
                        print("dezoito ", end="")
                    elif dig2centavos == 9:
                        print("dezenove ", end="")
                elif dig1centavos==2:
                    print("vinte ",end="")
                elif dig1centavos==3:
                    print("trinta ",end="")
                elif dig1centavos==4:
                    print("quarenta ",end="")
                elif dig1centavos==5:
                    print("cinquenta ",end="")
                elif dig1centavos==6:
                    print("sessenta ",end="")
                elif dig1centavos==7:
                    print("setenta ",end="")
                elif dig1centavos==8:
                    print("oitenta ",end="")
                elif dig1centavos==9:
                    print("noventa ",end="")

                if dig1centavos!=0 and dig2centavos!=0:
                    print("e ",end="")

                if dig2centavos==1:
                    print("um ", end="")
                elif dig2centavos==2:
                    print("dois ", end="")
                elif dig2centavos==3:
                    print("tres ", end="")
                elif dig2centavos==4:
                    print("quatro ", end="")
                elif dig2centavos==5:
                    print("cinco ", end="")
                elif dig2centavos==6:
                    print("seis ", end="")
                elif dig2centavos==7:
                    print("sete ", end="")
                elif dig2centavos==8:
                    print("oito ", end="")
                elif dig2centavos==9:
                    print("nove ", end="")

                if centavos==1:
                    print("centavo")
                elif centavos!=0:
                    print("centavos")

                while True:
                    resposta=input("\nDeseja escrever por extenso mais valores monetários entre -999.99 e 999.99? (S/N): ").upper()
                    if resposta!="S" and resposta!="N":
                        print("Você deve responder ou S, ou N; tente novamente!")
                    else:
                        break
                if resposta=="N":
                    break
print("OBRIGADA POR USAR ESSE PROGRAMA!")