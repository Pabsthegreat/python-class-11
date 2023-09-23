''' SOLUCIONES DE LA PHYSICA
    By
    Adarsh Arun Hoskere XI A
    Adarsh Sasikumar XI C
    Rishabh Kartik Jawagal XI C
    In this project we provide the students of class 11 a platform to quickly check their answers by providing the input of the given information in the questions.
    This helps the students to save time as they don’t have to search across the internet to verify their answers.
    INDEX
    1.MOTION IN STRAIGHT LINE
    2.PROJECTILE MOTION
    3.NEWTON’S LAWS OF MOTION
    4.WORK POWER ENERGY
    5.GRAVITATION
'''
import math

print("Hello, user")
print("This is a program where you can get solutions for your physics problems.\nPlease enter all inputs in lowercase!")
top = {1:"Motion in a Straight Line", 2: "Projectile Motion", 3:"Newton's Laws of Motion",4:"Work Power Energy", 5:"Gravitation",0:"Exit"}
g=10
while (True):   

    
    #getting user input for the topic
    chp = int(input(
'''
Available Topics are:

1)MOTION IN STRAIGHT LINE
2)PROJECTILE MOTION
3)NEWTON’S LAWS OF MOTION
4)WORK POWER ENERGY
5)GRAVITATION
0)Exit

Enter Topic number : '''))

    if (top.get(chp) == None):
        print("Please choose the correct Topic Name to continue our application. If you want to Exit Please enter 0")




    #Motion in a straight line

    elif chp == 1:

        misl = {"1) average velocity":"avgv", "2) equations of motion":["v","s","v^2"], "3) Relative velocity":"relvel"}
        x = list(misl.keys())
        print("The subtopics are:")

        for i in x:
            print(i)
        sub = int(input("Enter the number of the subtopic: "))


        #average velocity

        if sub == 1:
            vel = int(input("How many velocities to average?: "))
            total = 0

            for i in range(vel):
                v = int(input("Enter velocity:"))
                total += v
            print("Average velocity =", total / vel)

        #equations of motion    
        elif sub == 2:

            print("Please Enter None if value is unknown")

            #getting user input for values and unknowns

            u = input("Enter the intital velocity:")
            if len(u.strip()) != 0:
                u = int(u)
            else:
                u=None

            v = input("Enter the final velocity:")
            if len(v.strip()) != 0:
                v = int(v)
            else:
                v=None

            s = input("Enter the distance or displacement:")
            if len(s.strip()) != 0:
                s = int(s)
            else:
                s=None

            a = input("Enter the acceleration:")
            if len(a.strip()) != 0:
                a = int(a)
            else:
                a=None

            t = input("Enter the time period:")
            if len(t.strip()) != 0:
                t = int(t)
            else:
                t=None        

            #calculating the variables when different combinations of variables are unknown
                        
            if v is None and u is None:
                u = (s - 0.5 * a * t ** 2) / t
                v = u + a * (t)

            if v is None and a is None:
                a = 2 * (s - u * t) / t ** 2
                v = u + a * t
            
            if v is None and t is None:
                v = math.sqrt(u ** 2 + 2 * a * s)
                t = (v - u) / a
            
            if v is None and s is None:
                v = u + a * t
                s = (v ** 2 - u ** 2) / 2 * a
            
            if u is None and t is None:
                u = v ** 2 - 2 * a * s
                t = (v - u) / a
                
            if u is None and s is None:
                u = v - a * t
                s = (v ** 2 - u ** 2) / 2 * a

            if t is None and s is None:
                t = (v - u) / a
                s = (v ** 2 - u ** 2) / 2 * a
            
            if t is None and a is None:
                a = (v ** 2 - u ** 2) / 2 * s
                t = (v - u) / a


            if a is None and s is None:
                a = (v - u) / t
                s = (v ** 2 - u ** 2) / 2 * a

            print("initial velocity:",u,"final velocity:",v,"Displacement",s,"Acceleration:",a,"time period",t)

        #relative velocity

        elif sub == 3:
            vel1 = int(input("Enter velocity A:"))
            vel2 = int(input("Enter velocity B:"))
            print("Relative velocity of A with respect to B is :", vel1 - vel2)
            print("Relative velocity of B with respect to A is :", vel2 - vel1)
        else:
            print("The Sub topic choosen is wrong ")
            
             


    #Projectile Motion

    elif chp == 2:

        print("The value of gravity is taken as 10m/s^2")

        proj = {"1) Horizontal Range at given time":"x", "2) Vertical Range at given time ":"y", "3) Max height":"H" ,"4)Time at which the projectile will attain maximum height":" T"}
        x = list(proj.keys())
        print("The subtopics are:")

        for i in x:
            print(i)
        sub = int(input("Enter the number of the subtopic:"))

        #horizontal range of projectile at any given time

        if sub == 1:

            print("Please enter the values. All values are mandatory")

            #getting user input for values and unknown

            u = input("Enter the intital velocity:")

            while(len(u.strip()) == 0):                
                print("Intial Velocity cannot be blank or null.")
                u = input("Enter the intital velocity:")

            else:
                u = int(u)


            t = input("Enter the time period:")

            while(len(t.strip()) == 0):
                print("Time Period cannot be blank or null.")
                t = input("Enter the time period:")

            else:
                t = int(t)


            degree=input("Enter angle of projection in degree form:")

            while(len(degree.strip()) == 0):
                print("Angle of Projection cannot be blank or null.")
                degree=input("Enter angle of projection in degree form:")    

            else:
                degree = int(degree)


            thetaP = math.radians(degree)
            costheta = math.cos(thetaP)
            Range1 = (u * t * costheta)
            print("Horizontal Range of the projectile is :", Range1)


        #vertical range of projectile at any given time

        elif sub == 2:

            print("Please enter the values. All values are mandatory")

            #getting user input for values and unknown

            u = input("Enter the intital velocity:")

            while(len(u.strip()) == 0):                
                print("Intial Velocity cannot be blank or null.")
                u = input("Enter the intital velocity:")

            else:
                u = int(u)


            t = input("Enter the time period:")

            while (len(t.strip()) == 0):
                print("Time Period cannot be blank or null.")
                t = input("Enter the time period:")

            else:
                t = int(t)


            degree=input("Enter angle of projection in degree form:")

            while (len(degree.strip()) == 0):
                print("Angle of Projection cannot be blank or null.")
                degree=input("Enter angle of projection in degree form:")            
            else:
                degree = int(degree)


            thetaP = math.radians(degree)
            sintheta = math.sin(thetaP)
            Range2 = ((u * t * sintheta) - ((g * t * t) / 2))
            print("vertical range of projectile is :", Range2)


        #To find maximum height of the projectile

        elif sub == 3:

            print("Please enter the values. All values are mandatory")

            #getting user input for values and unknown

            u = input("Enter the intital velocity:")

            while (len(u.strip()) == 0):                
                print("Intial Velocity cannot be blank or null.")
                u = input("Enter the intital velocity:")

            else:
                u = int(u)


            degree=input("Enter angle of projection in degree form:")

            while (len(degree.strip()) == 0):
                print("Angle of Projection cannot be blank or null.")
                degree = input("Enter angle of projection in degree form:") 

            else:
                degree = int(degree)


            thetaP = math.radians(degree)
            sintheta = math.sin(thetaP)
            maxH = (math.pow(u,2) * math.pow(sintheta,2)) / (2 * g)
            print("The maximum height for the projectile is:", maxH)


        #To find time at which the projectile will attain maximum height

        elif sub == 4:

            print("Please enter the values. All values are mandatory")

            #getting user input for values and unknown

            u = input("Enter the intital velocity:")

            while (len(u.strip()) == 0):                
                print("Intial Velocity cannot be blank or null.")
                u = input("Enter the intital velocity:")

            else:
                u = int(u)


            degree=input("Enter angle of projection in degree form:")

            while (len(degree.strip()) == 0):
                print("Angle of Projection cannot be blank or null.")
                degree = input("Enter angle of projection in degree form:") 

            else:
                degree = int(degree)


            thetaP = math.radians(degree)
            sintheta = math.sin(thetaP)
            time = (2 * u * sintheta) / g
            print("Time at which projectile will attain maximum height is", time)
        



    #Newton's Laws of Motion

    elif chp == 3:

        nlm = {"1) force":"f", "2) linear momentum":"lm", "3) impulse": "im","4) limiting friction":"lf"}
        x = list(nlm.keys())
        print("The subtopics are:")

        for i in x:
            print(i)
        sub = int(input("Enter the number of the subtopic: "))

        #To find force

        if sub == 1:

            m = input("Enter the mass:")

            while (len(m.strip()) == 0):
                print("mass cannot be blank or null.")
                m = input("Enter the mass:")   

            else:
                m = int(m)


            a = input("Enter the acceleration:")

            if len(a.strip()) == 0:
                a = int(0)
            else:
                a = int(a)


            f = m * a
            print("The required force is", f)


        #To find linear momentum of the object

        elif sub == 2:

            m = input("Enter the mass:")

            while (len(m.strip()) == 0):

                print("mass cannot be blank or null.")
                m = input("Enter the mass:")

            else:
                m = int(m)


            v = input("Enter the velocity:")

            if len(v.strip()) == 0:
                v = int(0)

            else:
                v = int(v)


            lm = m  * v

            print("The linear momentum of the object is", lm)


        #To find impulse and verify impulse momentum theory

        elif sub == 3:

            t1 = input("Enter the initial time:")

            while (len(t1.strip()) == 0):
                print("initial time cannot be blank or null.")
                t1 = input("Enter the initial time:")

            else:
                t1 = int(t1)


            t2 = input("Enter the final time:")

            while (len(t2.strip()) == 0):
                print("final time cannot be blank or null.")
                t2 = input("Enter the final time:") 

            else:
                t2 = int(t2)


            f = input("Enter the force:")

            if len(f.strip()) == 0:
                f = int(0)

            else:
                f = int(f)


            im = f * (t2 - t1)

            print("The Impulse of the Object is", im)


            p1 = input("Enter the initial momentum:")

            while (len(p1.strip()) == 0):
                print("Initial momentum cannot be blank or null.")
                p1 = input("Enter the initial momentum:")

            else:
                p1 = int(p1)


            p2 = input("Enter the final momentum:")

            while (len(p2.strip()) == 0):
                print("Final momentum cannot be blank or null.")
                p2 = input("Enter the final momentum:")

            else:
                p2 = int(p2)


            if im == (p2 - p1):
                print("Impulse momentum theorem is verified")

            else:
                print("Impulse momentum theorem violated")



        #To find limiting friction force

        elif sub == 4:


            meus = input("Enter the static friction:")
            if len(meus.strip()) == 0:
                meus = int(0)

            else:
                meus = int(meus)


            R = input("Enter the value of R:")

            if len(R.strip()) == 0:
                R = int(0)

            else:
                R = int(R)


            lf  = meus * R
            print("The value of limiting friction is", lf)
            



    #Work Power Energy

    elif chp == 4:

        wpe = {"1) work":"wk", "2) kinetic energy":"ke", "3) potential energy":"pe", "4) power":"pw"}
        x = list(wpe.keys())
        print("The subtopics are:")

        for i in x:
            print(i)
        sub = int(input("Enter the number of the subtopic: "))

        #To find work done

        if sub == 1:


            f = input("Enter the force:")

            while (len(f.strip()) == 0):
                print("force cannot be blank or null.")
                f = input("Enter the force:")  

            else:
                f = int(f)


            s = input("Enter the displacement:")

            while (len(s.strip()) == 0):
                print("displacement cannot be blank or null.")
                s = input("Enter the displacement:") 

            else:
                s = int(s)


            degree=input("Enter angle between force and displacement in degree form:")

            while (len(degree.strip()) == 0):
                print("Angle cannot be blank or null.")
                degree=input("Enter angle between force and displacement in degree form:")

            else:
                degree = int(degree)


            thetaP = math.radians(degree)
            costheta = math.cos(thetaP)
            wk = f * s * costheta
            print("work done is:", wk)
            
            
            #To find kinetic energy

        elif sub == 2:


            print("Please leave blank if value is unknown")

            #getting user input for values and unknowns

            m = input("Enter the mass:")

            while (len(m.strip()) == 0):
                print("mass cannot be blank or null.")
                m = input("Enter the mass:")

            else:
                m = int(m)


            v = input("Enter the velocity:")

            if len(v.strip()) != 0:
                v = int(v)

            else:
                v = None


            p = input("Enter the momentum:")

            if len(p.strip()) != 0:
                p = int(p)

            else:
                p = None


            #calculating the variables when different combinations of variables are unknown

            if p is None and v is None:
                print("Both momentum and velocity cannot be blank. Either one should be entered ")

            elif p is None:
                ke = 0.5 * (m * (v ** 2))
                print("The kinetic energy is", ke)
            
            elif v is None:
                ke = (p ** 2) / (2 * m)
                print("The kinetic energy is", ke)



        #To find potential energy

        elif sub == 3:


            m = input("Enter the mass:")

            while (len(m.strip()) == 0):
                print("mass cannot be blank or null.")
                m = input("Enter the mass:")

            else:
                m = int(m)


            h = input("Enter the height:")

            while (len(h.strip()) == 0):
                print("Height cannot be blank or null.")
                h = input("Enter the height:")       

            else:
                h = int(h)


            pe_grav = m * g * h
            print("The gravitational potential energy is", pe_grav)


            k = input("Enter the force constant:")

            while (len(k.strip()) == 0):
                print("Force constant cannot be blank or null.")
                k = input("Enter the force constant:")

            else:
                k = int(k)


            x = input("Enter the displacement:")

            if len(x.strip()) == 0:
                x = int(0)

            else:
                x = int(x)


            pe_spring = 0.5 * k * (x ** 2)
            print("The spring potential energy is", pe_spring)



        #To find power

        elif sub == 4:


            f = input("Enter the force:")
            if len(f.strip()) == 0:
                f = int(0)

            else:
                f = int(f)


            v = input("Enter the velocity:")

            if len(v.strip()) == 0:
                v =int(0) 

            else:
                v = int(v)


            pw = f * v
            print("The Power is", pw)
            



    #Gravitation

    elif chp == 5:

        grav = {"1) gravitational force":"gf", "2) gravitational acceleration":"ga", "3) orbital velocity":"ov", "4) potential energy": "gpe"}
        x = list(grav.keys())
        print("The subtopics are:")

        for i in x:
            print(i)
        sub = int(input("Enter the number of the subtopic:"))


    #Exit

    elif chp == 0:
        print("Thanks for using our application to get solutions for your physics problem")
        print("Bye Have a Great Day !!!")
        break
    






