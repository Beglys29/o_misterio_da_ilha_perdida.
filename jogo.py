
# Projeto: O Misterio da Ilha Perdida
# jOgo de aventura e exploração com os personagens Helen, Junior e Kheller.
# Adicionei  objetos secretos, pistas escondidas e diferentes finais.
# As decisões dos jogadores podem mudar o destino dos personagens. 
# Compartilhei meu projeto com duas pessoas e expliquei como o jogo funciona.
# Foi interessante apresentar minha criação e conhecer as opiniões delas.

print("=========================")
print("O MISTÉRIO DA ILHA PERDIDA")
print("UMA AVENTURA DE EXPLORAÇÃO")
print("==========================")

print("Helen, Junior e Kheller estavam viajando de barco pelo oceano.")
print("Durante a viagem, uma forte tempestade surpreendeu o grupo.")
print("As ondas ficaram cada vez mais fortes e o barco acabou naufragando.")
print("Os três conseguiram chegar a uma ilha desconhecida.")
print("Agora, eles precisam explorar a ilha, encontrar pistas e descobrir uma maneira de voltar para casa.")

print("O QUE DESEJA FAZER?")
print("EXPLORAR")
print("INVESTIGAR")
print("SEGUIR")

escolha =  input("Digite sua escolha: ").strip().upper()
if escolha == "EXPLORAR": 
    print("Ao Explorar a floresta, os três encontraram uma cabana abandonada.")
    print("O QUE DESEJAM FAZER?")
    print("ENTRAR - Entrar na cabana.")
    print("RODEAR - Contornar a cabana e procurar outra entrada.")
    
    escolha_cabana = input("Digite sua escolha: ").strip().upper()
   
    if escolha_cabana == "ENTRAR":
        print("Dentro da cabana, eles encontraram um diário antigo.") 
        print("O QUE DESEJAM FAZER?")
        print("LER -Ler o diário.")
        print("IGNORAR - Ignorar o diário.")

        escolha_diario = input("Digite sua escolha: ").strip().upper()

        if escolha_diario == "LER":
            print("O diário revelava a localização de um tesouro escondido.")
        elif escolha_diario == "IGNORAR":
            print("Os três decidiram ignorar o diário e continuar explorando.")
            print("Durante a caminhada, encontraram uma trilha que levava até a praia.")
            print("Eles conseguiram encontrar ajuda e voltar para casa em segurança.")
            print("==============================")
            print("       FINAL DA AVENTURA!")
            print("==============================")
            print("             FIM!")

        else:
            print("Opção inválida. Escolha LER ou IGNORAR.")

    elif escolha_cabana == "RODEAR":
        print("Ao rodear a cabana, eles descobriram uma passagem secreta escondida atrás das árvores.")
        print("O QUE DESEJAM FAZER?")
        print("ENTRAR - Entrar na passagem secreta.")
        print("CONTINUAR - Continuar explorando a floresta.")

        escolha_passagem = input("Digite sua escolha: ").strip().upper()

        if escolha_passagem == "ENTRAR":
            print("A passagem levava a uma sala subterrânea com um mapa do tesouro.")

        elif escolha_passagem == "CONTINUAR":
            print("Os três encontraram um caminho seguro para sair da floresta.")

        else:
            print("Opção inválida. Escolha ENTRAR ou CONTINUAR.")


    else:
        print("Opção inválida. Escolha ENTRAR ou RODEAR")
   
elif escolha == "INVESTIGAR":
        print("Os três encontraram uma caverna misteriosa.")
        print("O QUE DESEJAM FAZER?")
        print("AVANÇAR - Entrar mais profundamente na caverna.")
        print("REGRESSAR - Voltar pelo caminho anterior.")

        escolha_caverna = input("Digite sua escolha: ").strip().upper()

        if escolha_caverna == "AVANÇAR":
            print("Os três entraram mais profundamente na caverna e encontraram um cristal brilhante.")
            print("O QUE DESEJAM FAZER?")
            print("PEGAR - Pegar o cristal.")
            print("DEIXAR - Deixar o cristal no lugar.")

            escolha_cristal = input("Digite sua escolha: ").strip().upper()

            if escolha_cristal == "PEGAR":
                print("O cristal brilhava intensamente e revelou uma passagem secreta para fora da ilha.")
                print("Os três seguiram pela passagem e encontraram uma embarcação abandonada.")
                print("Com a embarcação, Helen, Junior e Kheller conseguiram escapar da ilha!")
                print("==============================")
                print("       FINAL DA AVENTURA!")
                print("==============================")
                print("             FIM!")

            elif escolha_cristal == "DEIXAR":
                print("Ao deixar o cristal, os três descobriram uma inscrição antiga na parede.")
                print("A inscrição revelava um caminho escondido até a praia.")
                print("Os três seguiram o caminho e conseguiram escapar da ilha.")
                print("==============================")
                print("       FINAL DA AVENTURA!")
                print("==============================")
                print("             FIM!")

            else:
                print("Opção inválida. Escolha PEGAR ou DEIXAR.")

        elif escolha_caverna == "REGRESSAR":
            print("Ao voltar pelo caminho anterior, eles encontraram pegadas misteriosas.")
            print("O QUE DESEJAM FAZER?")
            print("SEGUIR - Seguir as pegadas.")
            print("FUGIR - Fugir das pegadas.")

            escolha_pegadas = input("Digite sua escolha: ").strip().upper()

            if escolha_pegadas == "SEGUIR":
                print("As pegadas levaram os três até uma antiga saída da ilha.")
                print("Ao atravessar a saída, encontraram um barco escondido.")
                print("Helen, Junior e Kheller usaram o barco para voltar para casa.")
                print("Antes de partir, descobriram um pequeno baú com moedas de ouro!")
                print("==============================")
                print("       FINAL DA AVENTURA!")
                print("==============================")
                print("             FIM!")

            elif escolha_pegadas == "FUGIR":
                print("Os três fugiram da caverna e encontraram abrigo na praia.")

            else:
                print("Opção inválida. Escolha SEGUIR ou FUGIR.")

        else:
             print("Opção inválida. Escolha AVANÇAR ou REGRESSAR.") 

elif escolha == "SEGUIR":
    print("Os três seguiram pela praia e encontraram os restos do barco.")
    print("O QUE DESEJAM FAZER?")
    print("SUBIR - Subir nos restos do barco.")
    print("PROCURAR - Procurar algo na praia.")
    print("NADAR - Nadar até uma pequena ilha próxima.")

    escolha_barco = input("Digite sua escolha: ").strip().upper()

    if escolha_barco == "SUBIR":
        print("Ao subir nos restos do barco, eles encontraram um mapa de navegação.")
        print("O QUE DESEJAM FAZER?")
        print("SEGUIR - Seguir as indicações do mapa.")
        print("INVESTIGAR - Investigar os símbolos do mapa.")

        escolha_mapa = input("Digite sua escolha: ").strip().upper()

        if escolha_mapa == "SEGUIR":
            print("O mapa indicava um caminho secreto para sair da ilha.")
            print("==============================")
            print("       FINAL ALTERNATIVO")
            print("==============================")
            print("Helen, Junior e Kheller encontraram uma saída secreta.")
            print("Eles conseguiram escapar da ilha, mas o tesouro permaneceu escondido.")
            print("Mesmo sem o tesouro, os três voltaram para casa em segurança!")
            print("==============================")
            print("             FIM!")
            print("==============================")

        elif escolha_mapa == "INVESTIGAR":
            print("Os três descobriram que os símbolos indicavam um tesouro escondido.")
            print("==============================")
            print("         FINAL FELIZ!")
            print("==============================")
            print("Helen, Junior e Kheller encontraram o tesouro perdido da ilha.")
            print("Dentro do tesouro havia ouro e joias preciosas.")
            print("Com a ajuda do mapa, descobriram uma rota secreta para escapar.")
            print("Os três conseguiram voltar para casa em segurança, levando o tesouro.")
            print("Eles viveram uma aventura que jamais esqueceriam!")
            print("==============================")
            print("           FIM!")
            print("==============================")

        else:
            print("Opção inválida. Escolha SEGUIR ou INVESTIGAR.")
        
    elif escolha_barco == "PROCURAR":
        print("Ao procurar na praia, encontraram uma caixa enterrada na areia.")
        print("O QUE DESEJAM FAZER?")
        print("ABRIR - Abrir a caixa.")
        print("DEIXAR - Deixar a caixa onde está.")

        escolha_caixa = input("Digite sua escolha: ").strip().upper()

        if escolha_caixa == "ABRIR":
            print("Dentro da caixa, encontraram uma chave misteriosa.")
            print("Depois de procurar pela praia, encontraram uma porta escondida entre as rochas.")
            print("A chave abriu a porta e revelou uma sala cheia de tesouros.")
            print("Helen, Junior e Kheller encontraram ouro e joias preciosas.")
            print("Usando uma passagem secreta da sala, os três conseguiram escapar da ilha com o tesouro!")
            print("==============================")
            print("       FINAL DO TESOURO!")
            print("==============================")
            print("             FIM!")

        elif escolha_caixa == "DEIXAR":
            print("Os três decidiram deixar a caixa e continuar explorando.")

        else:
            print("Opção inválida. Escolha ABRIR ou DEIXAR.")

    elif escolha_barco == "NADAR":
        print("Ao nadar, chegaram a uma pequena ilha próxima.")
        print("O QUE DESEJAM FAZER?")
        print("EXPLORAR - Explorar a pequena ilha.")
        print("VOLTAR - Voltar para a praia.")

        escolha_ilha = input("Digite sua escolha: ").upper()

        if escolha_ilha == "EXPLORAR":
            print("Ao explorar a ilha, encontraram uma antiga bússola.")

        elif escolha_ilha == "VOLTAR":
            print("Os três decidiram voltar para a praia em segurança.")

        else:
            print("Opção inválida. Escolha EXPLORAR ou VOLTAR.")

    else:
        print("Opção inválida. Escolha SUBIR, PROCURAR ou NADAR.")

else:
    print("Opção inválida. Escolha EXPLORAR, INVESTIGAR ou SEGUIR.") 

