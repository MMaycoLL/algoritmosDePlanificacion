class inputs:
   # declaramos las funciones iniciales a usar en los algorirmos
    def __init__(self, n):
        self.nombreProceso = [0] * n
        self.tiempoLlegada = [] * n
        self.testat = [0] * n
        self.tiempoRafaga = [] * n
        self.testbt = [0] * n
        self.tiempoFinalizacion = [0] * n
        self.tiempoRespuesta = [0] * n
        self.tiempoEspera = [0] * n
        self.prioridad = [] * n

   # funcion que pedira los datos, teniendo en cuenta que se esta condicionando para que el proceso 3 y 4 pidan prioridad
    def getInput(self, option):
        for i in range(n):
            print("\n")
            txt = "Proceso {} : "
            print(txt.format(i + 1))
            proceso = input(" Ingrese el proceso : ")
            self.nombreProceso[i] = proceso
            at = int(input(" Ingrese el tiempo de llegada : "))
            self.tiempoLlegada.append([at, i])
            self.testat[i] = at
            bt = int(input(" Ingrese el tiempo de ejecucion : "))
            self.tiempoRafaga.append([bt, i])
            self.testbt[i] = bt
            if option == 3 or option == 4:  # 3 La prioridad del proceso solo se solicita si es un algoritmo de prioridad
                p = int(input(" Ingrese la prioridad del proceso : "))
                self.prioridad.append([p, i])

class FCFS(inputs):  # algoritmo fcfs (First Come First Served)
    def getTiempoFinalizacion(self):  # Calcular tiempo de finalizacion
        self.tiempoLlegada.sort()
        time = self.tiempoLlegada[0][0]
        for i in range(n):
            index = self.tiempoLlegada[i][1]
            if self.tiempoLlegada[i][0] > time:
                time = self.tiempoLlegada[i][0] + self.testbt[index]
            else:
                time += self.testbt[index]
            self.tiempoFinalizacion[index] = time

    def getTiempoRespuesta(self):  # Calcular tiempo de respuesta
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):  # Calcular tiempo de espera
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.tiempoRafaga[i][0]

    def printFcfs(self):  # Imprimir los datos con la respectiva informacion
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.tiempoRafaga[x][0], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera : " + str(sum(self.tiempoEspera) / n))


class RR(inputs):  # Algoritmo RR (Round-robin)

    def getTiempoFinalizacion(self, tq):  # Calcular tiempo de finalizacion
        self.tiempoLlegada.sort()
        time = self.tiempoLlegada[0][0]
        queue = []
        k = 0
        index = self.tiempoLlegada[0][1]
        queue.append(index)
        while len(queue) != 0:
            index = queue.pop(0)
            if self.testbt[index] <= tq and self.testbt[index] > 0 and time >= self.testat[index]:
                time += self.testbt[index]
                # print("time : " + str(time))
                self.tiempoFinalizacion[index] = time
                # print("tiempoFinalizacion de " + str(index) + " is " + str(time))
                self.testbt[index] = 0
            elif self.testbt[index] > tq and time >= self.testat[index]:
                self.testbt[index] -= tq
                time += tq
            j = k + 1
            while j < n:
                z = self.tiempoLlegada[j][1]
                if self.testat[z] <= time and self.testbt[z] > 0 and z not in queue: queue.append(z)
                j += 1
            if self.testbt[index] > 0 and index not in queue: queue.append(index)
            k += 1
            # print(queue)

    def getTiempoRespuesta(self):  # Calcular tiempo de respuesta
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):  # Calcular tiempo de espera
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.tiempoRafaga[i][0]

    def printRr(self):  # Imprimir los datos con la respectiva informacion
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.tiempoRafaga[x][0], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class priority_nonprem(inputs):

    def getTiempoFinalizacion(self):  # Calcular tiempo de finalizacion
        self.tiempoLlegada.sort()
        self.prioridad.sort()
        time = self.tiempoLlegada[0][0]
        sums = self.tiempoLlegada[0][0] + sum(self.testbt)
        while time != sums:
            for i in range(n):
                index = self.prioridad[i][1]
                if self.testbt[index] != 0 and self.testat[index] <= time:
                    time += self.testbt[index]
                    self.testbt[index] = 0
                    self.tiempoFinalizacion[index] = time
                    break

    def getTiempoRespuesta(self):  # Calcular tiempo de respuesta
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):  # Calcular tiempo de espera
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.tiempoRafaga[i][0]

    def printPnp(self):  # Imprimir los datos con la respectiva informacion
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.tiempoRafaga[x][0], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class priority_prem(inputs):

    def getTiempoFinalizacion(self):  # Calcular tiempo de finalizacion
        self.tiempoLlegada.sort()
        self.prioridad.sort()
        time = self.tiempoLlegada[0][0]
        sums = self.tiempoLlegada[0][0] + sum(self.testbt)
        while time != (sums):
            for i in range(n):
                index = self.prioridad[i][1]
                if self.testbt[index] != 0 and self.testat[index] <= time:
                    self.testbt[index] -= 1
                    time += 1
                    if self.testbt[index] == 0: self.tiempoFinalizacion[index] = time
                    break

    def getTiempoRespuesta(self):  # Calcular tiempo de respuesta
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):  # Calcular tiempo de espera
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.tiempoRafaga[i][0]

    def printPp(self):  # Imprimir los datos con la respectiva informacion
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.tiempoRafaga[x][0], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class SJF(inputs):

    def getTiempoFinalizacion(self):  # Calcular tiempo de finalizacion
        self.tiempoLlegada.sort()
        self.tiempoRafaga.sort()
        time = self.tiempoLlegada[0][0]
        while time != self.tiempoLlegada[0][0] + sum(self.testbt):
            for i in range(n):
                index = self.tiempoRafaga[i][1]
                if self.tiempoRafaga[i][0] != 0 and self.testat[index] <= time:
                    time += self.tiempoRafaga[i][0]
                    self.tiempoRafaga[i][0] = 0
                    self.tiempoFinalizacion[index] = time
                    break

    def getTiempoRespuesta(self):  # Calcular tiempo de respuesta
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):  # Calcular tiempo de espera
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.testbt[i]

    def printSjf(self):  # Imprimir los datos con la respectiva informacion
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.testbt[x], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class SRTF(inputs):

    def getTiempoFinalizacion(self):  # Calcular tiempo de finalizacion
        self.tiempoLlegada.sort()
        self.tiempoRafaga.sort()
        time = self.tiempoLlegada[0][0]
        while time != (self.tiempoLlegada[0][0] + sum(self.testbt)):
            for i in range(n):
                index = self.tiempoRafaga[i][1]
                if self.tiempoRafaga[i][0] > 0 and self.testat[index] <= time:
                    self.tiempoRafaga[i][0] -= 1
                    time += 1
                    self.tiempoRafaga.sort()
                    if self.tiempoRafaga[i][0] == 0: self.tiempoFinalizacion[index] = time
                    break

    def getTiempoRespuesta(self):  # Calcular tiempo de respuesta
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):  # Calcular tiempo de espera
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.testbt[i]

    def printSrtf(self):  # Imprimir los datos con la respectiva informacion
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.testbt[x], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class HRN:
    def datoProceso(self, numeroProceso):
        datoProceso = []
        for i in range(numeroProceso):
            temporary = []
            idProceso = (input("Ingrese ID del proceso: "))

            tiempoLlegada = int(input(f"Ingrese el tiempo de llegada del proceso {idProceso}: "))

            tiempoRafaga = int(input(f"Ingrese el tiempo de rafaga del proceso {idProceso}: "))
            # 0 es el estado por defecto. 0 significa no ejecutado y 1 ejecucion completa
            temporary.extend([idProceso, tiempoLlegada, tiempoRafaga, 0])
            datoProceso.append(temporary)
        HRN.procesoPlanificacion(self, datoProceso)

    def procesoPlanificacion(self, datoProceso):
        start_time = []
        exit_time = []
        s_time = 0
        secuenciaProcesos = []
        datoProceso.sort(key=lambda x: x[1])
        for i in range(len(datoProceso)):  # ordenar procesos de acuerdo a la hora de llegada
            ready_queue = []
            temp = []
            normal_queue = []
            for j in range(len(datoProceso)):
                if (datoProceso[j][1] <= s_time) and (datoProceso[j][3] == 0):
                    relacionRespuesta = 0
                    relacionRespuesta = float(((s_time - datoProceso[j][1]) + datoProceso[j][2]) / datoProceso[j][2])
                    # Se calcula la relacion de respuesta de cada proceso
                    temp.extend([datoProceso[j][0], datoProceso[j][1], datoProceso[j][2], relacionRespuesta])
                    ready_queue.append(temp)
                    temp = []
                elif datoProceso[j][3] == 0:
                    temp.extend([datoProceso[j][0], datoProceso[j][1], datoProceso[j][2]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                start_time.append(s_time)  # Ordenar los procesos segun el mayor ratio de respuesta
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                secuenciaProcesos.append(ready_queue[0][0])
                for k in range(len(datoProceso)):
                    if datoProceso[k][0] == ready_queue[0][0]:
                        break
                datoProceso[k][3] = 1
                datoProceso[k].append(e_time)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                secuenciaProcesos.append(normal_queue[0][0])
                for k in range(len(datoProceso)):
                    if datoProceso[k][0] == normal_queue[0][0]:
                        break
                datoProceso[k][3] = 1
                datoProceso[k].append(e_time)
        t_time = HRN.calcularTiempoRespuesta(self, datoProceso)
        w_time = HRN.calcularTiempoEspera(self, datoProceso)
        HRN.printData(self, datoProceso, t_time, w_time, secuenciaProcesos)

    def calcularTiempoRespuesta(self, datoProceso):  # Calcular tiempo de respuesta
        totalTiempoRespuesta = 0
        for i in range(len(datoProceso)):
            tiempoRespuesta = datoProceso[i][4] - datoProceso[i][1]
            # tiempoRespuesta = tiempoFinalizacion - tiempoLegada
            totalTiempoRespuesta = totalTiempoRespuesta + tiempoRespuesta
            datoProceso[i].append(tiempoRespuesta)
        promedioTiempoRespuesta = totalTiempoRespuesta / len(datoProceso)
        # promedioTiempoRespuesta = totalTiempoRespuesta / numeroProceso
        return promedioTiempoRespuesta

    def calcularTiempoEspera(self, datoProceso):  # Calcular tiempo de espera
        totalTiempoEspera = 0
        for i in range(len(datoProceso)):
            tiempoEspera = datoProceso[i][5] - datoProceso[i][2]
            #  tiempoEspera = tiempoRespueta - tiempoRafaga
            totalTiempoEspera = totalTiempoEspera + tiempoEspera
            datoProceso[i].append(tiempoEspera)
        promedioTiempoEspera = totalTiempoEspera / len(datoProceso)
        # promedioTiempoEspera = totalTiempoEspera / numeroProceso
        return promedioTiempoEspera

    def printData(self, datoProceso, promedioTiempoRespuesta, promedioTiempoEspera, secuenciaProcesos):
        datoProceso.sort(key=lambda x: x[0])  # Imprimir los datos con los respectivos datos
        # Ordenar los procesos segun el ID del proceso
        print("")
        print(
            "IdProceso  tiempoLegada  tiempoRafaga      completado  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for i in range(len(datoProceso)):
            for j in range(len(datoProceso[i])):
                print(datoProceso[i][j], end="\t\t\t\t")
            print()
        print("")
        print(f'Tiempo medio de respuesta: {promedioTiempoRespuesta}')

        print(f'Tiempo medio de espera: {promedioTiempoEspera}')

        print(f'Secuencia de los procesos: {secuenciaProcesos}')


# Ciclo while para generar menu
while (1):
    # banner
    print("               __   __   __    ___        __   __        ")
    print("     /\  |    / _` /  \ |__) |  |   |\/| /  \ /__`       ")
    print("    /~~\ |___ \__> \__/ |  \ |  |   |  | \__/ .__/       ")
    print("                       __   ___                          ")
    print("                      |  \ |__                           ")
    print("                      |__/ |___                          ")
    print("  __                    ___    __        __     __       ")
    print(" |__) |     /\  |\ | | |__  | /  `  /\  /  ` | /  \ |\ | ")
    print(" |    |___ /~~\ | \| | |    | \__, /~~\ \__, | \__/ | \| ")

    print("        *****************************************")
    print("        ** Opcion               Algoritmo      **")
    print("        **                                     **")
    print("        **   1.                   FCFS         **")
    print("        **   2.                    RR          **")
    print("        **   3.            Prioridad expulsiva **")
    print("        **   4.         Prioridad no expulsiva **")
    print("        **   5.                    SJF         **")
    print("        **   6.                   SRTF         **")
    print("        **   7.                    HRN         **")
    print("        **   0.                   Salir        **")
    print("        *****************************************")

    option = int(str(input(" \n\tOPCION: ")))

    n = int(str(input(" \nCantidad de procesos a iterar : ")))
    input1 = inputs(n)

    if option == 0:
        print("\n Saliste del programa! ")
        break

    if option == 1:
        fcfs = FCFS(n)
        fcfs.getInput(option)
        fcfs.getTiempoFinalizacion()
        fcfs.getTiempoRespuesta()
        fcfs.getTiempoEspera()
        fcfs.printFcfs()

    if option == 2:
        rr = RR(n)
        tq = int(input(" Ingrese el rango de tiempo : "))
        rr.getInput(option)
        rr.getTiempoFinalizacion(tq)
        rr.getTiempoRespuesta()
        rr.getTiempoEspera()
        rr.printRr()

    if option == 3:
        print(
            " \nNota : Al ingresar la prioridad tenga en cuenta que los numeros mas bajos equivalen a una prioridad mas alta ")
        pnp = priority_nonprem(n)
        pnp.getInput(option)
        pnp.getTiempoFinalizacion()
        pnp.getTiempoRespuesta()
        pnp.getTiempoEspera()
        pnp.printPnp()

    if option == 4:
        print(
            " \nNota : Al ingresar la prioridad tenga en cuenta que los numeros mas bajos equivalen a una prioridad mas alta ")
        pp = priority_prem(n)
        pp.getInput(option)
        pp.getTiempoFinalizacion()
        pp.getTiempoRespuesta()
        pp.getTiempoEspera()
        pp.printPp()

    if option == 5:
        sjf = SJF(n)
        sjf.getInput(option)
        sjf.getTiempoFinalizacion()
        sjf.getTiempoRespuesta()
        sjf.getTiempoEspera()
        sjf.printSjf()

    if option == 6:
        srtf = SRTF(n)
        srtf.getInput(option)
        srtf.getTiempoFinalizacion()
        srtf.getTiempoRespuesta()
        srtf.getTiempoEspera()
        srtf.printSrtf()

    if option == 7:
        numeroProceso = n
        hrn = HRN()
        hrn.datoProceso(numeroProceso)
