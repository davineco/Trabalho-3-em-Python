from datetime import datetime


class Veiculos(object):
    def __init__(self, marca="", modelo="", ano=0, valor=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.codigo = ""
        self.status = "DISPONÍVEL"


        codigo1 = []
        marca1 = []
        modelo1 = []
        ano1 = []
        valor1 = []
        status1 = []
        aluguelIn = []
        aluguelFi = []
        Cliente = []
        prazo = []
        objeto = []
        bot = 0
        now = datetime.now()
        dia = now.day
        mes = now.month
        anos = int(now.year)
        while comando != 7:
            print("LOCAÇÃO DE VEÍCULOS")
            print("DATA: |{} \ {} \ {}|\n".format(dia, mes, anos))
            print("Digite 1 para adicionar veículos.")
            print("Digite 2 para consultar veículos.")
            print("Digite 3 para alugar/reservar veículos.")
            print("Digite 4 para devolver/liberar veículos.")
            print("Digite 5 para excluir veículos.")
            print("Digite 6 para avançar data atual.")
            print("Digite 7 Para ""sair"" ")
            bot = int(input("Digite a operação desejada: "))
            print("")
            if bot == 1:
                print("CADASTRO DE VEÍCULOS \n")
                a = input("MARCA:")
                b = input("MODELO:")
                c = input("ANO:")
                d = input("VALOR DA DIÁRIA DO VEÍCULO:")
                marca1.append(a)
                modelo1.append(b)
                ano1.append(c)
                valor1.append(d)
                e = len(Modelo)
                codigo1.append("00"+str(e))
                obj = Veiculos()
                obj.codigo = e
                obj.valor = float(d)
                obj.ano = int(c)
                obj.modelo = b
                obj.marca = a
                objetos.append(obj)
                status1.append(obj.status)
                aluguelIn.append(str(dia)+str(mes)+str(anos))
                aluguelFi.append("")
                Cliente.append("")
                prazo.append(0)                
    if bot == 2:
        print("CONSULTAR VEÍCULOS \n")
        nCar = len(codigo1)
        c=0
        while c < nCar:
            print("|{}--{}--{}|".format(codigo1[c],modelo1[c],status1[c]))
            c=c+1
            print("\nTecle 1 para mais detalhes")        
            print("Tecle 2 para voltar para o menu principal")
            aux = int(input("Digite a operação desejada:"))
            print("")
            if aux == 1:
                print("MAIS DETALHES\n")
                c = 0
                while c < nCar:
                        print("{} - {} {} {} - Valor: R${},00 {}".format(Codigos[c], Marca[c], Modelo[c], Ano[c], Valor[c],Status[c]))
                        c = c + 1          
     if bot == 3:
        print("ALUGAR/RESERVAR VEÍCULOS")
        print("Tecle 1 para alugar veículo.")
        print("Digite 2 para reservar veículo.")
        x = input("Digite a operação desejada:")
        print("")
        if x == "1":
            local = input("Nome: ")
            prazo = int(input("Prazo de locação: "))
            if prazo > 30:
                prazo = input("Prazo grande. Por favor, digite um prazo de locação menor: ")
            cod = input("Código do veículo: ")
            if str(status1[int(cod)-1]) == "DISPONÍVEL":
                Prazo[int(cod)-1] = prazo
                Status[int(cod)-1] = "ALUGADO"
                Cliente[int(cod)-1] = local
                Ialuguel[int(cod)-1] = str(str(dia)+str(mes)+str(anos))
                d = dia + prazo
                m = mes
                a = anos
                if d > 30:
                    d = d - 30
                    m = m + 1
                    if m > 12:
                        m = m - 12
                        a = a + 1
                aluguelFi[int(cod) - 1] = str(str(d) + str(m) + str(a))
            elif str(Status[int(cod)-1]) == "ALUGADO":
                print("esse veículo não pode ser alugado")
                cod = input("Código de um outro veículo:")
                if str(Status[int(cod) - 1]) == "DISPONÍVEL":
                    status1[int(cod) - 1] = "ALUGADO"
                    Cliente[int(cod) - 1] = local
                    aluguelIn[int(cod) - 1] = str(str(dia) + str(mes) + str(anos))
                    d = dia + prazo
                    m = mes
                    a = anos
                    if d > 30:
                        d = d - 30
                        m = m + 1
                        if m > 12:
                            m = m - 12
                            a = a + 1
                    aluguelFi[int(cod) - 1] = str(str(d) + str(m) + str(a))
                if str(status1[int(cod) - 1]) == "RESERVADO":
                    print("Por favor, escolha outra data. Indeferimento na realização da locação.")
        elif x == "2":
            local = input("Nome do locatário: ")
            prazo = int(input("Prazo de locação: "))
            if prazo > 30 - dia:
                prazo = input("Prazo muito grande. Por favor, digite um prazo de locação menor: ")
            cod = input("Código do veículo: ")
            if str(Status[int(cod)-1]) == "DISPONÍVEL":
                prazo1[int(cod) - 1] = prazo
                status1[int(cod)-1] = "RESERVADO"
                Cliente[int(cod)-1] = local
                inicio = (input("Digite a data de inicio de aluguel: "))
                d = int(inicio[0] + inicio[1])
                m = int(inicio[2] + inicio[3])
                a = int(inicio[4] + inicio[5] + inicio[6] + inicio[7])
                d = d + prazo
                if d > 30:
                    d = d - 30
                    m = m + 1
                    if m > 12:
                        m = m - 12
                        a = a + 1
                aluguelFi[int(cod) - 1] = str(str(d) + str(m) + str(a))
    if bot == 4:
        print("DEVOLVER/LIBERAR VEICULOS")
        a = len(codigos1)
        b = 0
        while b < a:
            if status1[b] != "DISPONÍVEL":
                print(str(codigos1[b])+"--"+str(modelo1[b])+"--"+str(status1[b]))
            b = b + 1
        print("Digite 1 para Devolver Veículo")
        print("Digite 2 para Liberar Veículo")
        x = int(input("Digite a operação desejada:"))
        if x == 1:
            cod = int(input("Digite o Código do veículo:"))
            print("\nCliente: ", Cliente[cod - 1])
            valor = int(aluguelIn[cod - 1])//1000000
            d = valor
            m = (int(aluguelIn[cod - 1]) - d*1000000) // 10000
            a = (int(aluguelIn[cod - 1]) - d*1000000) % 10000
            if a == anos:
                if m > mes:
                    print("Total a pagar: R$", (((30-d)+dia) * float(valor1[cod - 1])))
                    status1[cod - 1] = "DISPONÍVEL"
                elif m == mes:
                    if dia == d:
                        print("Total a pagar: R$", (float(valor1[cod - 1])))
                        status1[cod - 1] = "DISPONÍVEL"
                    elif dia > d:
                        print("Total a pagar: R$", ((dia - d) * float(valor1[cod - 1])))
                        status1[cod - 1] = "DISPONÍVEL"
                    elif d > dia:
                        status1[cod - 1] = "DISPONÍVEL"
            elif a < anos:
                print("Total a pagar: R$", ((dia + (30 - d)) * float(valor1[cod - 1])))
                status1[cod - 1] = "DISPONÍVEL"
            elif a > Anos:
                status1[cod - 1] = "DISPONÍVEL"
        if x == 2:
            cod = int(input("Digite o Código do veículo:"))
            print("Cliente: ", Cliente[cod - 1])
            valor = int(aluguelIn[cod - 1]) // 1000000
            d = valor
            m = (int(aluguelIn[cod - 1]) - d * 1000000) // 10000
            a = (int(aluguelIn[cod - 1]) - d * 1000000) % 10000
            if a > anos:
                status1[cod - 1] = "DISPONÍVEL"
            elif a < anos:
                valor = dia + (30 - d)
                print("Total a pagar: R$", (valor * float(valor1[cod - 1])))
                status1[cod - 1] = "DISPONÍVEL"
            elif a == anos:
                if m == mes:
                    if d == dia:
                        print("Total a pagar: R$", (float(valor1[cod - 1])))
                        status1[cod - 1] = "DISPONÍVEL"
                    elif d > dia:
                        status1[cod - 1] = "DISPONÍVEL"
                    else:
                        valor = dia - d
                        print("Total a pagar: R$", (valor * float(valor1[cod - 1])))
                        status1[cod - 1] = "DISPONÍVEL"
    if bot == 5:
        print("========== EXCLUIR VEÍCULOS ===========\n")
        cod = int(input("Digite o Código do veículo: "))
        if status1[cod - 1] == "DISPONÍVEL":
            del codigo1[cod - 1]
            del marca1[cod - 1]
            del modelo1[cod - 1]
            del ano1[cod - 1]
            del valor1[cod - 1]
            del status1[cod - 1]
            del aluguelIn[cod - 1]
            del aluguelFi[cod - 1]
            del Cliente[cod - 1]
            del objetos[cod - 1]
        ve = len(Status)
        y = 1
        x = 0
        while x < ve:
            codigo1[x] = "00" + str(y)
            x = x + 1
    if bot == 6:
        dia = dia + 1
        if dia > 30:
            dia = dia - 30
            mes = mes + 1
            if mes > 12:
                mes = mes - 12
                anos = anos + 1
        cod = len(Status)
        while cod > 0:
            d = (int(aluguelIn[cod - 1])) // 1000000
            m = (int(aluguelIn[cod - 1]) - d * 1000000) // 10000
            a = (int(aluguelIn[cod - 1]) - d * 1000000) % 10000
            if status1[cod - 1] == "DISPONÍVEL":
                print()
            elif a == anos:
                if m > mes:
                    if ((30 - d) + dia) > prazo[cod - 1]:
                        status1[cod - 1] = "ATRASADO"
                elif m == mes:
                    if dia == d:
                        status1[cod - 1] = "ALUGADO"
                    elif dia > d:
                        if (dia - d) > prazo[cod - 1]:
                            status1[cod - 1] = "ATRASADO"
            elif a < anos:
                if (dia + (30 - d)) > prazo[cod - 1]:
                    status1[cod - 1] = "ATRASADO"
            cod = cod - 1
if bot == 7:
        break
