import copy
import json

team1=input("Enter team 1 name:")
team2=input("Enter team 2 name:")
venue = input("Enter venue name")

t1 = {"a":[] ,"b":[], "e":[]}
t2 = {"c":[] , "d":[], "f":[]}

runs = 0
wickets = 0
innings = ()
wicket = {}
over = ""



print(team1,"=",t1) 
print(team2,"=",t2)                                                   

toss = input("\nwho chose to bat?")

while toss != team1 and toss != team2:
    print("Please enter one of the two teams entered")
    toss = input("who chose to bat?")

#assigning batting and bowling to teams

if toss == team1:

    bat1 = t1
    bow = t2

else:

    bat1 = t2
    bow = t1


#initializing the innings , executes for 2 innings

a=0
while a < 2:

    print("\nINNINGS OF", toss)
    print("\n")

#getting opening batsmen names, cheking if they are from the batting team

    b1 = input("Enter striker's name:")
    while b1 not in bat1:
        print("Please enter a player of batting team.")
        b1 = input("Enter striker's name:")

    b2 = input("Enter non striker's name:")

    while b2 not in bat1:
        
        print("Please enter a player of batting team")
        b2 = input("Enter non striker's name:")


#same batsman, bowler entered again?
#keeping the active batsmen in a separate list to make it easier to change strike and replace batsmen during wickets

    bat = [b1 , b2]
    striker = bat1[bat[0]]

#initializing the loop of number of overs 
       
    for j in range (1):

        print("\nOVER", j)

#getting bowler's name and checking if he is in the bowling team, if he has bowled the previous over

        bo1 = input("\nEnter bowler's name:")

        while bo1 not in bow:

            print("Please enter a player of bowling team")
            bo1 = input("Enter bowler's name:")
            print("\n")

        
        k = 1
#initializing the 6 ball over
        while k <= 6:

#menu based input
            print("\na)1run b)2runs c)3runs d)4runs e)6runs f)wicket g)wide h)noball i)dot j)byes,leg-byes k)penalties")

            ball = input("What happend this ball?  :")
            print("\n")

            while len(ball.strip()) == 0 or ball not in ("a","b","c","d","e","f","g","h","i","j","k"):

                print("Please enter a valid value!\n")

                print("a)1run b)2runs c)3runs d)4runs e)6runs f)wicket g)wide h)noball i)dot j)leg byes or byes k)penalties ")
                ball = input("What happend this ball?  :")
                print("\n")
            
            over += ball

#1 run
            if ball == "a":

                bow[bo1] += [1]
                runs += 1
                striker += [1]
                if striker == bat1[bat[0]]:          #changing strike
                    striker = bat1[bat[1]]
                else:
                    striker = bat1[bat[0]]
                k += 1
                if a == 1 and runs > innings[0][0]:
                    break

#2 runs
            if ball == "b":

                bow[bo1] += [2]
                striker += [2]
                runs += 2
                k += 1
                if a == 1 and runs > innings[0][0]:
                    break
            
#3 runs
            if ball =="c":

                bow[bo1] += [3]
                runs += 3
                striker += [3]
                if striker == bat1[bat[0]]:
                    striker = bat1[bat[1]]
                else:
                    striker = bat1[bat[0]]
                k += 1
                if a == 1 and runs > innings[0][0]:
                    break

#4 runs
            if ball == "d":

                bow[bo1] += [4]
                striker += [4]
                runs += 4
                k+=1
                if a == 1 and runs > innings[0][0]:
                    break

#6 runs
            if ball == "e":
    
                bow[bo1] += [6]
                striker += [6]
                runs += 6
                k += 1
                if a == 1 and runs > innings[0][0]:
                    break
            
#wicket
            if ball == "f":

                wickets += 1
                if wickets == 10:
                    break

                #checking for run out , if runs were run before run out
                
                out = input("Is it a Run out (yes/no)? :")                 
                if out.lower() == "yes":
                    ex = input("Enter number of extras(number):")

                    while ex.isdigit() == False:
                        ex = input("Enter number of extras(number):")
                    runs += int(ex)
                    striker += [int(ex)]
                    bow[bo1] += [int(ex)]

                elif out.lower() == "no":

                    bow[bo1] += [0]
                    striker += [0]

                #taking new batsman's name and checking if has already batted , if he is of the batting team
                   
                n = input("Enter new batsman name :")

                while n not in bat1:

                    print("Please enter a player of batting team")
                    n = input("Enter batsman's name:")


                while len(bat1[n]) > 0:

                    print("Please enter a new batsman's name")
                    n = input("Enter batsman's name:")

                #checking if new batsman is on strike, changing the list of active batsmen

                q = input("Is the new batsman on strike? :")

                if q == "yes":

                    if striker == bat1[bat[0]]:
                        bat[0] = n
                        striker = bat1[bat[0]]
                    else:
                        bat[1] = n
                        striker = bat1[bat[1]]

                else:

                    if striker == bat1[bat[0]]:
                        bat[1] = n
                        
                    else:
                        bat[0] = n
                        

                if bo1 not in wicket:
                    wicket[bo1] = 1
                else:
                    wicket[bo1] += 1

                if a == 1 and runs > innings[0][0]:
                    break

                k += 1

#noball
            if ball == "h":

                qn = input("Was the ball hit by the batsman(yes/no)? :")
                if qn.lower() == "yes":
                    ex = input("Enter number of runs(number):")
                    while ex.isdigit() == False:
                        ex = input("Enter number of extras(number):")
                    bow[bo1] += [1 + int(ex)]
                    runs += 1 + int(ex)
                    striker += [int(ex)]

                elif qn.lower() == "no":
                    
                    ex = input("Enter number of extras(number):")
                    while ex.isdigit() == False:
                        ex = input("Enter number of extras(number):")
                    bow[bo1] += [1 + int(ex)]
                    runs += 1 + int(ex)
                    striker += [0]                                    #no ball counts for person?
                
                if int(ex) % 2 != 0:
                    if striker == bat1[bat[0]]:
                        striker = bat1[bat[1]]
                    else:
                        striker = bat1[bat[0]]

                    
                if a == 1 and runs > innings[0][0]:
                    break
#wide
            if ball == "g":

                wkt = input("Is it a wicket? (yes/no):")

                if wkt == "yes":
                    runs += 1
                    bow[bo1] += [1]

                    wickets += 1
                    if wickets == 10:
                        break

                    out = input("Is it a Run out (yes/no)? :")

                    if out.lower() == "yes":
                        ex = input("Enter number of runs before wicket(number):")

                        while ex.isdigit() == False:
                            ex = input("Enter number of runs before wicket(number):")
                        runs += int(ex)
                        bow[bo1] += [int(ex)]
                        striker += [int(ex)]

                    elif out.lower() == "no":
                        continue

                    n = input("Enter new batsman name :")

                    while n not in bat1:

                        print("Please enter a player of batting team")
                        n = input("Enter batsman's name:")


                    while len(bat1[n]) > 0:

                        print("Please enter a new batsman's name")
                        n = input("Enter batsman's name:")

                    #checking if new batsman is on strike, changing the list of active batsmen

                    q = input("Is the new batsman on strike? :")

                    if q == "yes":

                        if striker == bat1[bat[0]]:
                            bat[0] = n
                            striker = bat1[bat[0]]
                        else:
                            bat[1] = n
                            striker = bat1[bat[1]]

                    else:

                        if striker == bat1[bat[0]]:
                            bat[1] = n
                            
                        else:
                            bat[0] = n
                            

                    if bo1 not in wicket:
                        wicket[bo1] = 1
                    else:
                        wicket[bo1] += 1

                elif wkt == "no":

                    ex = input("Enter number of extras(number):")
                    while ex.isdigit() == False:
                            ex = input("Enter number of extras(number):")
                    bow[bo1] += [1 + int(ex)]
                    runs += 1 + int(ex)
                    
                    if int(ex) % 2 != 0:
                        if striker == bat1[bat[0]]:
                            striker = bat1[bat[1]]
                        else:
                            striker = bat1[bat[0]]

                        
                if a == 1 and runs > innings[0][0]:
                        break

            #not adding +1 for ball so that it redoes the loop for the the same ball i.e multiple wides, no balls can be accomodated

#dot balls
            if ball == "i":

                bow[bo1] += [0]
                striker += [0]
                k += 1

#byes and leg byes
            if ball == "j":

                ex = input("Enter number of extras(number):")
                while ex.isdigit() == False:
                    ex = input("Enter number of extras(number):")
                bow[bo1] += [int(ex)]
                striker += [0]

                if int(ex) % 2 != 0:
                    if striker == bat1[bat[0]]:
                        striker = bat1[bat[1]]
                    else:
                        striker = bat1[bat[0]]

                runs += int(ex)
                k += 1
                if a == 1 and runs > innings[0][0]:
                    break

#penalties            
            if ball == "k":

                ex = input("Enter number of extras(number):")
                while ex.isdigit() == False:
                    ex = input("Enter number of extras(number):")
                bow[bo1] += [0]
                striker += [0]

                runs += int(ex)
                k += 1
                
                if a == 1 and runs > innings[0][0]:
                    break


#changing striker at end of over
        if striker == bat1[bat[0]]:
            striker = bat1[bat[1]]

        else:
            striker = bat1[bat[0]]

#ending innings if 10 wickets have fallen or runs are scored
        if wickets == 10:
            break
        
        if a == 1 and runs > innings[0][0]:
            break

#printing bat, bowl, runs at end of over            
        print("BATTING"+":\n",bat[0],":",sum(bat1[bat[0]]),"(",len(bat1[bat[0]]),")\n",\
            bat[1],":",sum(bat1[bat[1]]),"(",len(bat1[bat[1]]),")""\n",\
                "BOWLER"+":",bo1,":",sum(bow[bo1]),"-",bo1,"\n",\
                    "TOTAL",runs,"-",wickets,"\n\n")

#summing up all batsmen's socores and bowlers figures

    if a == 0:

        innb1 = copy.deepcopy(bat1)
        innbo1 = copy.deepcopy(bow)

        for i in innb1:

            if len(innb1[i]) > 0:
                run = str(sum(innb1[i]))     
                ballss = str(len(innb1[i]))
                fours = str(innb1[i].count(4))
                sixes = str(innb1[i].count(6))
                innb1[i] = run + "("+ballss+")" + "\t\t4 x " + fours + "\t\t6 x" + sixes

            else:
                innb1[i] = "DNB"
        

        for i in innbo1:
            
                run = str(sum(innbo1[i]))
                wkt = str(wicket.get(i, "0"))
                innbo1[i] = run +"-"+ wkt       #+ str((int(run) / (len(innbo1[i]) / 6)))

    


#storing runs and wickets of innings , so it is easy to print later

    innings += ((runs,wickets),)

#setting runs and wickets as 0 for next inning
    
    wickets = 0
    runs = 0

#clearing values associated to all names of all teams so new values for 2nd innings can be added
# (change 'a ==' condition for multiple innings)

    if a == 0:
        for x in t1:
            t1[x] = []
        for y in t2:
            t2[y] = []
        
#re-assigning batting and bowling for 2nd innings 
          
        if toss == team1:
            
            bat1 = t2
            bow = t1
            toss = team2

        else:

            bat1 = t1
            bow = t2
            toss = team1

#going to next innings
    a += 1

#update wickets for bowlers.

#printing score card

#print(team1, "v/s", team2, "\n",venue,"\n\n")
innb2 = copy.deepcopy(bat1)
innbo2 = copy.deepcopy(bow)

for i in innb2:
    run = str(sum(innb2[i]))
    ballss = str(len(innb2[i]))
    fours = str(innb2[i].count(4))
    sixes = str(innb2[i].count(6))
    innb2[i] = run + "("+ballss+")" + "\t\t4 x " + fours + "\t\t6 x" + sixes   ####+ str(int(runs) / int(ballss) * 100)


for i in innbo2:                

    run = str(sum(innbo2[i]))
    wkt = str(wicket.get(i, "0"))
    innbo2[i] = run +"-"+ wkt       #+ str((int(run) / (len(innbo1[i]) / 6)))
    
#printing winner

if innings[1][0] - innings[0][0] > 0:

    if toss == team1:
        print(team1, "WON BY", 10 - innings[1][1], "Wickets")

    else:
        print(team2, "WON BY", 10 - innings[1][1], "Wickets")
        
elif innings[1][0] == innings[0][0]:
    print("IT IS A TIE!")

else:

    if toss == team1:
        print(team2, "WON BY", innings[0][0] - innings[1][0], "RUNS")

    else:
        print(team1, "WON BY", innings[0][0] - innings[1][0], "RUNS")

#printing scorecard
#details of first innings printed by using the previously stored values in dictionary

print("\n")
print("\nInnings 1\n\n","Batting\n")

print(json.dumps(innb1, indent = 3),"\n","TOTAL :", innings[0][0], "/", innings[0][1], "\n", "TARGET :", innings[0][0] + 1, "\n")

print("Bowling\n") 

print(json.dumps(innbo1, indent = 3))

print("\n\n")


#printing 2nd innings details

print("Innings 2\n\n","Batting\n","TOTAL :", innings[1][0], "/", innings[1][1], "\n")

print(json.dumps(innb2, indent = 3),"\n")

print("Bowling\n")

print(json.dumps(innbo2, indent = 3))

#*********************************************************************************************************************************************************************

#use fromkeys to create dictionary from names

#CORRECTIONS TO BE MADE

#giving user multiple chances to change the input value only for wicket

#handling input in different cases(lower,upper)

#runout on no ball
