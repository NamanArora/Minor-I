from sharedetail import code
from bollingerband import fun 
from linear import linereg
from svm import svmalgo
from pa import assistant

sharename = raw_input("Enter the name of the share: ")

while True:

        print"****************************************************"
        print"            MENU      "

        print"1. Current Status Of The Share"
        print"2. Bollinger Bands Of The Share"
        print"3. Prediction Of The Share Using Linear Regression"
        print"4. Prediction Of The Share Using Support Vector Machine Algorithm"
        print"5. Personal Assistant"
        print"6. EXIT"
        choice=int(raw_input("Enter your choice: "))


        if(choice==1):
            print "..........SHARE DETAILS..........."
            print"                   "
            print sharename.upper()
            print"             "
            code(sharename)

        elif(choice==2):     
            print "...........Bollinger Bands Representation Of The Share............."
            fun(sharename)



        elif(choice==3):
            print "...........Prediction Using Linear Regression................"
            linereg(sharename)



        elif(choice==4):

            print "............Prediction Using SVM [RBF Model].................."
            svmalgo(sharename)

        elif(choice==5):
            print "............Activating personal assistant.................."
            assistant(sharename)
        
        elif(choice==6):
            break














        




        
