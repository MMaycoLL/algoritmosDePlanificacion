class inputs:
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


class FCFS(inputs):

    def getTiempoFinalizacion(self):
        # tiempoFinalizacion
        self.tiempoLlegada.sort()
        time = self.tiempoLlegada[0][0]
        for i in range(n):
            index = self.tiempoLlegada[i][1]
            if self.tiempoLlegada[i][0] > time:
                time = self.tiempoLlegada[i][0] + self.testbt[index]
            else:
                time += self.testbt[index]
            self.tiempoFinalizacion[index] = time

    def gettiempoRespuesta(self):
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.tiempoRafaga[i][0]

    def printFcfs(self):
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.tiempoRafaga[x][0], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Average TurnAround Time : " + str(sum(self.tiempoRespuesta) / n))
        print(" tiempo promedio de espera : " + str(sum(self.tiempoEspera) / n))


class RR(inputs):

    def getTiempoFinalizacion(self, tq):
        self.tiempoLlegada.sort()
        time = self.tiempoLlegada[0][0]
        queue = []
        k = 0
        index = self.tiempoLlegada[0][1]
        queue.append(index)
        while len(queue) != 0:
            # print("len : " + str(len(queue)))
            index = queue.pop(0)
            # print("index : " + str(index))
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

    def gettiempoRespuesta(self):
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.tiempoRafaga[i][0]

    def printRr(self):
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.tiempoRafaga[x][0], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Average TurnAround Time : " + str(sum(self.tiempoRespuesta) / n))
        print(" tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class priority_nonprem(inputs):

    def getTiempoFinalizacion(self):
        self.tiempoLlegada.sort()
        self.prioridad.sort()
        time = self.tiempoLlegada[0][0]
        sums = self.tiempoLlegada[0][0] + sum(self.testbt)
        while time != (sums):
            for i in range(n):
                index = self.prioridad[i][1]
                if self.testbt[index] != 0 and self.testat[index] <= time:
                    time += self.testbt[index]
                    self.testbt[index] = 0
                    self.tiempoFinalizacion[index] = time
                    break

    def gettiempoRespuesta(self):
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.tiempoRafaga[i][0]

    def printPnp(self):
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.tiempoRafaga[x][0], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Average TurnAround Time : " + str(sum(self.tiempoRespuesta) / n))
        print(" tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class priority_prem(inputs):

    def getTiempoFinalizacion(self):
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

    def gettiempoRespuesta(self):
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.tiempoRafaga[i][0]

    def printPp(self):
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.tiempoRafaga[x][0], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Average TurnAround Time : " + str(sum(self.tiempoRespuesta) / n))
        print(" tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class SJF(inputs):

    def getTiempoFinalizacion(self):
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

    def gettiempoRespuesta(self):
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.testbt[i]

    def printSjf(self):
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.testbt[x], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Average TurnAround Time : " + str(sum(self.tiempoRespuesta) / n))
        print(" tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class SRTF(inputs):

    def getTiempoFinalizacion(self):
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

    def gettiempoRespuesta(self):
        for i in range(n):
            self.tiempoRespuesta[i] = self.tiempoFinalizacion[i] - self.testat[i]

    def getTiempoEspera(self):
        for i in range(n):
            self.tiempoEspera[i] = self.tiempoRespuesta[i] - self.testbt[i]

    def printSrtf(self):
        print("\n")
        print(" Proceso  tiempoLlegada  tiempoRafaga  tiempoFinalizacion  tiempoRespuesta  tiempoEspera")
        for x in range(n):
            txt = "    {}          {}              {}               {}                  {}               {} "
            print(txt.format(self.nombreProceso[x], self.testat[x], self.testbt[x], self.tiempoFinalizacion[x],
                             self.tiempoRespuesta[x], self.tiempoEspera[x]))
        print("\n Average TurnAround Time : " + str(sum(self.tiempoRespuesta) / n))
        print(" tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


# driver's code


while (1):

    print(" \n\t\tElija la opcion que desea \n")

    print(" ***************** MENU ******************")
    print(" *****************************************")
    print(" ** Opcion               Algoritmo      **")
    print(" **                                     **")
    print(" **   1.                   FCFS         **")
    print(" **   2.                    RR          **")
    print(" **   3.            Prioridad expulsiva **")
    print(" **   4.         Prioridad no expulsiva **")
    print(" **   5.                    SJF         **")
    print(" **   6.                   SRTF         **")
    print(" **   0.                   Salir        **")
    print(" *****************************************")

    option = int(str(input(" \nOpcion: ")))

    n = int(str(input(" \nIngrese el numero de procesos : ")))
    input1 = inputs(n)

    if option == 0:
        print("\n Saliste del programa! ")
        break

    if option == 1:
        fcfs = FCFS(n)
        fcfs.getInput(option)
        fcfs.getTiempoFinalizacion()
        fcfs.gettiempoRespuesta()
        fcfs.getTiempoEspera()
        fcfs.printFcfs()

    if option == 2:
        rr = RR(n)
        tq = int(input(" input the time quantum : "))
        rr.getInput(option)
        rr.getTiempoFinalizacion(tq)
        rr.gettiempoRespuesta()
        rr.getTiempoEspera()
        rr.printRr()

    if option == 3:
        print(
            " \nNota : Al ingresar la prioridad tenga en cuenta que los numeros mas bajos equivalen a una prioridad mas alta ")
        pnp = priority_nonprem(n)
        pnp.getInput(option)
        pnp.getTiempoFinalizacion()
        pnp.gettiempoRespuesta()
        pnp.getTiempoEspera()
        pnp.printPnp()

    if option == 4:
        print(
            " \nNota : Al ingresar la prioridad tenga en cuenta que los numeros mas bajos equivalen a una prioridad mas alta ")
        pp = priority_prem(n)
        pp.getInput(option)
        pp.getTiempoFinalizacion()
        pp.gettiempoRespuesta()
        pp.getTiempoEspera()
        pp.printPp()

    if option == 5:
        sjf = SJF(n)
        sjf.getInput(option)
        sjf.getTiempoFinalizacion()
        sjf.gettiempoRespuesta()
        sjf.getTiempoEspera()
        sjf.printSjf()

    if option == 6:
        srtf = SRTF(n)
        srtf.getInput(option)
        srtf.getTiempoFinalizacion()
        srtf.gettiempoRespuesta()
        srtf.getTiempoEspera()
        srtf.printSrtf()
