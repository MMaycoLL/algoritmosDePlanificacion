class inputs:
    def __init__(self, n):
        self.processName = [0] * n
        self.arrivalTime = [] * n
        self.testat = [0] * n
        self.burstTime = [] * n
        self.testbt = [0] * n
        self.completionTime = [0] * n
        self.turnAroundTime = [0] * n
        self.waitingTime = [0] * n
        self.priority = [] * n

    def getInput(self, option):
        for i in range(n):
            print("\n")
            txt = "Process {} : "
            print(txt.format(i + 1))
            process = input(" input the process : ")
            self.processName[i] = process
            at = int(input(" input the arrival time : "))
            self.arrivalTime.append([at, i])
            self.testat[i] = at
            bt = int(input(" input the burst time : "))
            self.burstTime.append([bt, i])
            self.testbt[i] = bt
            if option == 3 or option == 4:  # 3 for priority_nonprem  4 fro priority_prem
                p = int(input(" input the priority of the process : "))
                self.priority.append([p, i])


class FCFS(inputs):

    def getCompletionTime(self):
        self.arrivalTime.sort()
        time = self.arrivalTime[0][0]
        for i in range(n):
            index = self.arrivalTime[i][1]
            if self.arrivalTime[i][0] > time:
                time = self.arrivalTime[i][0] + self.testbt[index]
            else:
                time += self.testbt[index]
            self.completionTime[index] = time

    def getTurnAroundTime(self):
        for i in range(n):
            self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]

    def getWaitingTime(self):
        for i in range(n):
            self.waitingTime[i] = self.turnAroundTime[i] - self.burstTime[i][0]

    def printFcfs(self):
        print("\n")
        print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
        for x in range(n):
            txt = "    {}          {}           {}            {}             {}              {} "
            print(txt.format(self.processName[x], self.testat[x], self.burstTime[x][0], self.completionTime[x],
                             self.turnAroundTime[x], self.waitingTime[x]))
        print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime) / n))
        print(" Average Waiting Time : " + str(sum(self.waitingTime) / n))


class RR(inputs):

    def getCompletionTime(self, tq):
        self.arrivalTime.sort()
        time = self.arrivalTime[0][0]
        queue = []
        k = 0
        # print(queue)
        index = self.arrivalTime[0][1]
        # print("index : " + str(index))
        queue.append(index)
        while len(queue) != 0:
            # print("len : " + str(len(queue)))
            index = queue.pop(0)
            # print("index : " + str(index))
            if self.testbt[index] <= tq and self.testbt[index] > 0 and time >= self.testat[index]:
                time += self.testbt[index]
                # print("time : " + str(time))
                self.completionTime[index] = time
                # print("completionTime of " + str(index) + " is " + str(time))
                self.testbt[index] = 0
            elif self.testbt[index] > tq and time >= self.testat[index]:
                self.testbt[index] -= tq
                time += tq
            j = k + 1
            while j < n:
                z = self.arrivalTime[j][1]
                if self.testat[z] <= time and self.testbt[z] > 0 and z not in queue: queue.append(z)
                j += 1
            if self.testbt[index] > 0 and index not in queue: queue.append(index)
            k += 1
            # print(queue)

    def getTurnAroundTime(self):
        for i in range(n):
            self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]

    def getWaitingTime(self):
        for i in range(n):
            self.waitingTime[i] = self.turnAroundTime[i] - self.burstTime[i][0]

    def printRr(self):
        print("\n")
        print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
        for x in range(n):
            txt = "    {}          {}           {}            {}             {}              {} "
            print(txt.format(self.processName[x], self.testat[x], self.burstTime[x][0], self.completionTime[x],
                             self.turnAroundTime[x], self.waitingTime[x]))
        print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime) / n))
        print(" Average Waiting Time : " + str(sum(self.waitingTime) / n))


class priority_nonprem(inputs):

    def getCompletionTime(self):
        self.arrivalTime.sort()
        self.priority.sort()
        time = self.arrivalTime[0][0]
        sums = self.arrivalTime[0][0] + sum(self.testbt)
        while time != (sums):
            for i in range(n):
                index = self.priority[i][1]
                if self.testbt[index] != 0 and self.testat[index] <= time:
                    time += self.testbt[index]
                    self.testbt[index] = 0
                    self.completionTime[index] = time
                    break

    def getTurnAroundTime(self):
        for i in range(n):
            self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]

    def getWaitingTime(self):
        for i in range(n):
            self.waitingTime[i] = self.turnAroundTime[i] - self.burstTime[i][0]

    def printPnp(self):
        print("\n")
        print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
        for x in range(n):
            txt = "    {}          {}           {}            {}             {}              {} "
            print(txt.format(self.processName[x], self.testat[x], self.burstTime[x][0], self.completionTime[x],
                             self.turnAroundTime[x], self.waitingTime[x]))
        print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime) / n))
        print(" Average Waiting Time : " + str(sum(self.waitingTime) / n))


class priority_prem(inputs):

    def getCompletionTime(self):
        self.arrivalTime.sort()
        self.priority.sort()
        time = self.arrivalTime[0][0]
        sums = self.arrivalTime[0][0] + sum(self.testbt)
        while time != (sums):
            for i in range(n):
                index = self.priority[i][1]
                if self.testbt[index] != 0 and self.testat[index] <= time:
                    self.testbt[index] -= 1
                    time += 1
                    if self.testbt[index] == 0: self.completionTime[index] = time
                    break

    def getTurnAroundTime(self):
        for i in range(n):
            self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]

    def getWaitingTime(self):
        for i in range(n):
            self.waitingTime[i] = self.turnAroundTime[i] - self.burstTime[i][0]

    def printPp(self):
        print("\n")
        print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
        for x in range(n):
            txt = "    {}          {}           {}            {}             {}              {} "
            print(txt.format(self.processName[x], self.testat[x], self.burstTime[x][0], self.completionTime[x],
                             self.turnAroundTime[x], self.waitingTime[x]))
        print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime) / n))
        print(" Average Waiting Time : " + str(sum(self.waitingTime) / n))


class SJF(inputs):

    def getCompletionTime(self):
        self.arrivalTime.sort()
        self.burstTime.sort()
        time = self.arrivalTime[0][0]
        while time != self.arrivalTime[0][0] + sum(self.testbt):
            for i in range(n):
                index = self.burstTime[i][1]
                if self.burstTime[i][0] != 0 and self.testat[index] <= time:
                    time += self.burstTime[i][0]
                    self.burstTime[i][0] = 0
                    self.completionTime[index] = time
                    break

    def getTurnAroundTime(self):
        for i in range(n):
            self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]

    def getWaitingTime(self):
        for i in range(n):
            self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]

    def printSjf(self):
        print("\n")
        print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
        for x in range(n):
            txt = "    {}          {}           {}            {}             {}              {} "
            print(txt.format(self.processName[x], self.testat[x], self.testbt[x], self.completionTime[x],
                             self.turnAroundTime[x], self.waitingTime[x]))
        print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime) / n))
        print(" Average Waiting Time : " + str(sum(self.waitingTime) / n))


class SRTF(inputs):

    def getCompletionTime(self):
        self.arrivalTime.sort()
        self.burstTime.sort()
        time = self.arrivalTime[0][0]
        while time != (self.arrivalTime[0][0] + sum(self.testbt)):
            for i in range(n):
                index = self.burstTime[i][1]
                if self.burstTime[i][0] > 0 and self.testat[index] <= time:
                    self.burstTime[i][0] -= 1
                    time += 1
                    self.burstTime.sort()
                    if self.burstTime[i][0] == 0: self.completionTime[index] = time
                    break

    def getTurnAroundTime(self):
        for i in range(n):
            self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]

    def getWaitingTime(self):
        for i in range(n):
            self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]

    def printSrtf(self):
        print("\n")
        print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
        for x in range(n):
            txt = "    {}          {}           {}            {}             {}              {} "
            print(txt.format(self.processName[x], self.testat[x], self.testbt[x], self.completionTime[x],
                             self.turnAroundTime[x], self.waitingTime[x]))
        print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime) / n))
        print(" Average Waiting Time : " + str(sum(self.waitingTime) / n))


# driver's code


while (1):

    print(" \n\t\tElija la opcion que desea \n")

    print(" ***************** MENU ******************")
    print(" *****************************************")
    print(" ** Opcion               Algoritmo      **")
    print(" **                                     **")
    print(" **   1.                   FCFS         **")
    print(" **   2.                    RR          **")
    print(" **   3.            Priority expulsiva  **")
    print(" **   4.          Priority no expulsiva **")
    print(" **   5.                    SJF         **")
    print(" **   6.                   SRTF         **")
    print(" **   0.                   Salir        **")
    print(" *****************************************")

    option = int(str(input(" \noption : ")))

    n = int(str(input(" \nIngrese el numero de procesos : ")))
    input1 = inputs(n)

    if option == 0:
        print("\n you exited the program! ")
        break

    if option == 1:
        fcfs = FCFS(n)
        fcfs.getInput(option)
        fcfs.getCompletionTime()
        fcfs.getTurnAroundTime()
        fcfs.getWaitingTime()
        fcfs.printFcfs()

    if option == 2:
        rr = RR(n)
        tq = int(input(" input the time quantum : "))
        rr.getInput(option)
        rr.getCompletionTime(tq)
        rr.getTurnAroundTime()
        rr.getWaitingTime()
        rr.printRr()

    if option == 3:
        print(" \nNote : While entering priority assume lower the number higher the priority ")
        pnp = priority_nonprem(n)
        pnp.getInput(option)
        pnp.getCompletionTime()
        pnp.getTurnAroundTime()
        pnp.getWaitingTime()
        pnp.printPnp()

    if option == 4:
        print(" \nNote : While entering priority assume lower the number higher the priority ")
        pp = priority_prem(n)
        pp.getInput(option)
        pp.getCompletionTime()
        pp.getTurnAroundTime()
        pp.getWaitingTime()
        pp.printPp()

    if option == 5:
        sjf = SJF(n)
        sjf.getInput(option)
        sjf.getCompletionTime()
        sjf.getTurnAroundTime()
        sjf.getWaitingTime()
        sjf.printSjf()

    if option == 6:
        srtf = SRTF(n)
        srtf.getInput(option)
        srtf.getCompletionTime()
        srtf.getTurnAroundTime()
        srtf.getWaitingTime()
        srtf.printSrtf()
