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
        self.tiempoLlegada.sort()
        time = self.tiempoLlegada[0][0]
        for i in range(n):
            index = self.tiempoLlegada[i][1]
            if self.tiempoLlegada[i][0] > time:
                time = self.tiempoLlegada[i][0] + self.testbt[index]
            else:
                time += self.testbt[index]
            self.tiempoFinalizacion[index] = time

    def getTiempoRespuesta(self):
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
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera : " + str(sum(self.tiempoEspera) / n))


class RR(inputs):

    def getTiempoFinalizacion(self, tq):
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

    def getTiempoRespuesta(self):
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
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


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

    def getTiempoRespuesta(self):
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
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


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

    def getTiempoRespuesta(self):
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
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


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

    def getTiempoRespuesta(self):
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
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


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

    def getTiempoRespuesta(self):
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
        print("\n Tiempo promedio de respuesta : " + str(sum(self.tiempoRespuesta) / n))
        print(" Tiempo promedio de espera  : " + str(sum(self.tiempoEspera) / n))


class HRN:
    def processData(self, numeroProcesos):
        process_data = []
        for i in range(numeroProcesos):
            temporary = []
            process_id = int(input("Enter Process ID: "))

            arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))

            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))

            temporary.extend([process_id, arrival_time, burst_time, 0])
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete
            '''
            process_data.append(temporary)
        HRN.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_processes = []
        process_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    response_ratio = 0
                    response_ratio = float(((s_time - process_data[j][1]) + process_data[j][2]) / process_data[j][2])
                    '''
                    Calculating the Response Ratio foe each process
                    '''
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], response_ratio])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                '''
                Sort the processes according to the Highest Response Ratio
                '''
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
        t_time = HRN.calculateTurnaroundTime(self, process_data)
        w_time = HRN.calculateWaitingTime(self, process_data)
        HRN.printData(self, process_data, t_time, w_time, sequence_of_processes)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / numeroProcesos
        '''
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / numeroProcesos
        '''
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_processes):
        process_data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        print("Process_ID  Arrival_Time  Burst_Time      Completed  Completion_Time  Turnaround_Time  Waiting_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="\t\t\t\t")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

        print(f'Sequence of Processes: {sequence_of_processes}')


# driver's code


while (1):

    print(" \n\tElija la opcion que desea \n")

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
    print(" **   7.                    HRN         **")
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
        numeroProcesos = n
        hrn = HRN()
        hrn.processData(numeroProcesos)
