def checkVal(s,a):


    invalidR = [(2,5,4),(1,2,4),(1,3,4)]
    invalidL = [(3,5,3),(3,3,3),(4,2,3)]
    invalidU = [(2,1,1),(3,1,1),(5,3,1)]
    invalidD = [(2,4,2),(3,3,2),(5,4,2)]

    invalidR2 =[(1,5,4),(4,1,4),(4,2,4),(4,3,4),(4,4,4),(4,5,4)]
    invalidL2 =[(2,1,3),(2,2,3),(2,3,3),(2,4,3),(2,5,3),(4,5,3),(4,3,3),(5,2,3)]
    invalidU2 =[(1,4,1),(2,4,1),(3,4,1),(4,4,1),(5,4,1),(5,2,1)]
    invalidD2 =[(1,2,2),(2,2,2),(3,2,2),(4,2,2),(5,2,2),(5,5,2),(3,4,2),(2,5,2)]


    if a == 1:
        if s[2] == 3 and s[0] != 1:
            for i in invalidL:
                if s == i:
                    return None
            x = list(s)
            x[0] += -1
            s = tuple(x)
            return s;
        elif (s[2] == 4 and s[0] != 5):
            for i in invalidR:
                if s == i:
                    return None
            x = list(s)
            x[0] += 1
            s = tuple(x)
            return s;
        elif (s[2] == 1 and s[1] != 5):
            for i in invalidU:
                if s == i:
                    return None
            x = list(s)
            x[1] += 1
            s = tuple(x)
            return s;
        elif (s[2] == 2 and s[1] != 1):
            for i in invalidD:
                if s == i:
                    return None
            x = list(s)
            x[1] += -1
            s = tuple(x)
            return s;

    elif a == 2:

        if (s[2] == 3 and s[0] != 1 and s[0] != 2):
            for i in invalidL:
                if s == i:
                    return None
            for i2 in invalidL2:
                if s == i2:
                    return None
            x = list(s)
            x[0] += -2
            s = tuple(x)
            return s;
        elif (s[2] == 4 and s[0] != 4 and s[0] != 5):
            for i in invalidR:
                if s == i:
                    return None
            for i2 in invalidR2:
                if s == i2:
                    return None
            x = list(s)
            x[0] += 2
            s = tuple(x)
            return s;
        elif (s[2] == 1 and s[1] != 4 and s[1] != 5):
            for i in invalidU:
                if s == i:
                    return None
            for i2 in invalidU2:
                if s == i2:
                    return None
            x = list(s)
            x[1] += 2
            s = tuple(x)
            return s;
        elif (s[2] == 2 and s[1] != 1 and s[1] != 2):
            for i in invalidD:
                if s == i:
                    return None
            for i2 in invalidD2:
                if s == i2:
                    return None
            x = list(s)
            x[1] += -2
            s = tuple(x)
            return s;

    elif a == 3:

        if s[2] == 1:
            x = list(s)
            x[2] = 3
            s = tuple(x)
            return s;
        elif s[2] == 3:
            x = list(s)
            x[2] = 2
            s = tuple(x)
            return s;
        elif s[2] == 4:
            x = list(s)
            x[2] = 1
            s = tuple(x)
            return s;
        elif s[2] == 2:
            x = list(s)
            x[2] = 4
            s = tuple(x)
            return s;

    elif a == 4:

        if s[2] == 1:
            x = list(s)
            x[2] = 4
            s = tuple(x)
            return s;
        elif s[2] == 3:
            x = list(s)
            x[2] = 1
            s = tuple(x)
            return s;
        elif s[2] == 2:
            x = list(s)
            x[2] = 3
            s = tuple(x)
            return s;
        elif s[2] == 4:
            x = list(s)
            x[2] = 2
            s = tuple(x)
            return s;
    
    return None

def R(s, a):
    if checkVal(s,a) != None:
        if a == 1:
            return -1.5;
        elif a == 2:
            return -2;
        elif a == 3:
            return -0.5;
        elif a == 4:
            return -0.5;

def valueIteration(S,V,G,N):
    States = S
    VCur = V
    gamma = G
    noise = N
    s_rate = 1- N
    VLast = []
    actions = []

    
    if noise == 0:
    
        for i in range(100):
            if i < 10:
                print("\n")
                print("Iter: " + str(i+1))
            j = 0
            VLast = VCur.copy()
            for s in States:
                
                Q = []
                actions = []
                for a in range(1,5):
                    s_next = checkVal(s,a)
                    if s_next != None and j < 100:  
                        index = States.index(s_next)
                        Q.append(R(s,a) + gamma * VLast[index])
                        actions.append(a)

                if s[0]==5 and s[1]==5:  
                    VCur[j] = 100
                    if i < 10:
                        print(str(s) + "  V = " + str(round(VCur[j], 3)))
                elif s[0]==4 and s[1] ==4:
                    VCur[j] = -1000
                    if i < 10:
                        print(str(s) + "  V = " + str(round(VCur[j], 3)))
                elif (s[0] == 2 and s[1] == 2) or (s[0] == 2 and s[1] == 3) or (s[0] == 3 and s[1] == 2):
                    VCur[j] = 0
                    if i < 10:
                        print(str(s) + "  V = " + str(round(VCur[j], 3)))
                else: 
                    VCur[j] = max(Q)
                    a_index = Q.index(VCur[j])
                    if i < 10:
                        print(str(s) + "  V = " + str(round(VCur[j], 3)) + "       Best Action: A" + str(actions[a_index]))
                j += 1
    else:
        
        for i in range(100):
            if i < 40:
                print("\n")
                print("Iter: " + str(i+1))
            j = 0
            VLast = VCur.copy()
            for s in States:
                Q = []
                actions = []
                valid_actions = []

                for a in range(1,5):
                    valid = checkVal(s,a)
                    if valid != None:
                        valid_actions.append(valid)
                
                
                
                for a in range(1,5):
                    val = 0;
                    s_next = checkVal(s,a)
                    if s_next != None and j < 100:  
                        prob = noise / (len(valid_actions)-1)
                        actions.append(a)
                        for b in range(1,5):
                            s_next1 = checkVal(s,b)
                            if s_next1 != None:
                                index = States.index(s_next1)
                                if a == b:
                                    val += s_rate * (R(s,b) + gamma * VLast[index])
                                else:
                                    val += prob * (R(s,b) + gamma * VLast[index])
                    elif s_next == None and j < 100:
                        prob = 1 / len(valid_actions)
                        actions.append(a)
                        for b in range(1,5):
                            s_next1 = checkVal(s,b)
                            if s_next1 != None:
                                index = States.index(s_next1)
                                val += prob * (R(s,b) + gamma * VLast[index])
                    
                    Q.append(val) 
                    

                if s[0] == 5 and s[1] == 5:  
                    VCur[j] = 100
                    if i < 40:
                        print(str(s) + "  V = " + str(round(VCur[j], 3)))
                elif s[0] == 4 and s[1] == 4:
                    VCur[j] = -1000
                    if i < 40:
                        print(str(s) + "  V = " + str(round(VCur[j], 3)))
                elif (s[0] == 2 and s[1] == 2) or (s[0] == 2 and s[1] == 3) or (s[0] == 3 and s[1] == 2):
                    VCur[j] = 0
                    if i < 40:
                        print(str(s) + "  V = " + str(round(VCur[j], 3)))
                else: 
                    VCur[j] = max(Q)
                    a_index = Q.index(VCur[j])
                    if i < 40:
                        print(str(s) + "  V = " + str(round(VCur[j], 3)) + "       Best Action: A" + str(actions[a_index]))
                j += 1   
    return VCur



def main():
    S = []
    V = []


    for i in range(1,6):
        for j in range(1,6):
            for x in range(1,5):
                S.append((i,j,x))
                if i == 5 and j == 5:
                    V.append(100)
                elif i == 4 and j == 4:
                    V.append(-1000)
                else:
                    V.append(0)

    G = float(input("Choose the value for gamma: "))
    N = float(input("Choose the value for noise: "))
    valueIteration(S,V,G,N)
    

        
if __name__ == '__main__':
    main()

    