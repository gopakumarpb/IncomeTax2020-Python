from Tkinter import *
from reportlab.pdfgen import canvas
#Red Salute to Akhil without whom this script was not possible.
#List is used
##Clear button is used
#Modified on 18-08-2020
#global variable
#RIGHT ALIGNED AMOUNT

akhilGui = Tk()
akhilGui.title("Income Tax CalcuHelveticar")


#Setting the Title Label

titleLabel = Label(akhilGui,text="INCOMETAX CALCULATION FOR THE FINANCIAL YEAR 2020-21",
                   bg="#0C542D", fg="white",font = "Roboto 18 bold italic ", justify='center')
titleLabel.grid(row=1, columnspan=10, rowspan=2, padx=15, sticky=EW)
incsubtitleLabel = Label(akhilGui,text="Income:",fg="#113B53",
                         font = "Helvetica 13 bold ", justify='center')
incsubtitleLabel.grid(row= 3, columnspan=2, pady=5, padx=15, sticky=EW)
nameLabel=Label(akhilGui,text="Name:",
                   fg="black",font = "Lacto 13 bold italic ", justify='left')
nameLabel.grid(row= 3, column= 3, sticky=W)
nameEntry          = Entry(akhilGui, bd =1, fg= "#113B53",
                                justify='left')
nameEntry.grid(row= 3, column=4, pady=2,sticky= W)
panLabel=Label(akhilGui,text="PAN:",
                    fg="black",font = "Lacto 13 bold italic ", justify='left')
panLabel.grid(row= 4, column= 3, sticky=W)
panEntry          = Entry(akhilGui, bd =1, fg= "#113B53",
                                justify='left')
panEntry.grid(row= 4, column=4, pady=2,sticky= W)

global deductionssumLabel
deductionssumLabel = Label()
incomesumLabel = Label()
global differenceLabel 
differenceLabel = Label()
global differencereLabel 
differencereLabel = Label()
global benefitLabel 
benefitLabel = Label()
global newtaxableLabel
newtaxableLabel = Label()     
global newtaxLabel
newtaxLabel = Label()
global exitaxLabel
exitaxLabel = Label()
global exitaxableLabel
exitaxableLabel = Label()


def func_clear():

    global exitaxLabel
    exitaxLabel.destroy()

    global exitaxableLabel
    exitaxableLabel.destroy()

    global newtaxLabel
    newtaxLabel.destroy()

    global newtaxableLabel
    newtaxableLabel.destroy()

    global differenceLabel
    differenceLabel.destroy()

    global differencereLabel  
    differencereLabel.destroy()

    global benefitLabel
    benefitLabel.destroy()

    row_value          = 1 #initialise the variable row_value to be used in grid()
    lab_list.clear()       #label list created to hold th labels
    entry_list.clear()     #entry list created to hold entry values
    
    label_printing()

    labded_list.clear()
    entryded_list.clear()

    labelded_printing()

    global incomesumLabel
    incomesumLabel.destroy()
    
    global deductionssumLabel
    deductionssumLabel.destroy()

    return

def func_total_income():

    global incomesumLabel 
    incomesumLabel.destroy() #delete if exists
    income_sum = 0
    for m in entry_list:
        income_sum = income_sum + int(m.get())
   
    incomesumLabel = Label(akhilGui, text=str(income_sum), fg = "#113B53", #"#093145"
                           font = "Helvetica 15 bold ",justify='right')
    incomesumLabel.grid(row= 30, column= 1, sticky=W)
    return income_sum

# create the list of all input entries required
def label_printing():

    row_value          = 5 #initialise the variable row_value to be used in grid()

    for i in income_list:                        #iterating through the list, creating label
        #iLabel          = str(i) + "Label"
        #iEntry          = str(i) + "Entry"
        iLabel          = Label(akhilGui, text= str(i),
                                fg="#113B53",font = "Helvetica  12 bold ", justify='right')
        lab_list.append(iLabel)
        iLabel.grid(row = row_value, column=0, pady=2, padx=15, sticky= W)
        v               = StringVar(akhilGui, value='0')
        iEntry          = Entry(akhilGui, bd =1, fg= "#093145",
                                textvariable = v,justify='right')
        entry_list.append(iEntry)
       
        iEntry.grid(row= row_value, column=1, pady=2,sticky= W)
        row_value       = row_value + 1
    return()

def func_total_deductions():
##
    global deductionssumLabel 
    #deductionssumLabel.destroy() #delete if present

    z = entryded_list
    sec80c = 0
    deductions_sum = 0
    for i,m in enumerate(z):
        if (i==3 or i==4 or i==5 or i==6):
            sec80c = sec80c + int(m.get())
        elif(i==0):
            deductions_sum = deductions_sum + 50000
        elif (i==2):
            if int(m.get()) >= 250000:
                deductions_sum = deductions_sum + 250000
            else :
                deductions_sum = deductions_sum + int(m.get())
        elif (i==7):
            if int(m.get()) > 25000:
                deductions_sum = deductions_sum + 25000
            else :
                deductions_sum = deductions_sum + int(m.get())

        elif (i==8):
            if int(m.get()) > 5000:
                deductions_sum = deductions_sum + 5000
            else :
                deductions_sum = deductions_sum + int(m.get())
        elif (i==9):
            if int(m.get()) > 50000:
                deductions_sum = deductions_sum + 50000
            else :
                deductions_sum = deductions_sum + int(m.get())               

        else:
            deductions_sum = deductions_sum + int(m.get())

    if sec80c >= 150000:
        deductions_sum = deductions_sum  + 150000
    elif sec80c <= 149999:
        deductions_sum = deductions_sum + sec80c
     
    deductionssumLabel = Label(akhilGui, text=deductions_sum,
                               fg = "red",font = "Helvetica 15 bold ",justify='right')
    deductionssumLabel.grid(row= 30, column= 4, sticky=W)
    return deductions_sum

def func_eligible_deductions():

    z = entryded_list
    zl= []
    sec80c = 0
    deductions_sum = 0
    for i,m in enumerate(z):
        if (i==3 or i==4 or i==5 or i==6):
            sec80c = sec80c + int(m.get())
           
        elif(i==0):
            zl.insert(0,50000)
        elif (i==2):
            if int(m.get()) >= 250000:
                zl = zl.insert(2,int(250000))
            else :

                zl = zl.insert(2,int(m.get()))
        elif (i==7):
            if int(m.get()) > 25000:
                zl = zl.insert(4,int(25000))
            else :
                zl = zl.insert(4,int(m.get()))
        elif (i==8):
            if int(m.get()) > 5000:
                zl = zl.insert(5,int(5000))
            else :

                zl = zl.insert(5,int(m.get()))
        elif (i==9):
            if int(m.get()) > 50000:
                zl = zl.insert(6,int(50000))
            else :

                zl = zl.insert(6,int(m.get()))             

        else:
            zl = zl.insert(8,int(m.get()))

    if sec80c >= 150000:

        zl = zl.insert(3,150000)
    elif sec80c <= 149999:

        zl = zl.insert(3,sec80c)


##    global deductionssumLabel 
##    #deductionssumLabel.destroy() #delete if present
##    
##    z = entryded_list
##    zl= entryeli_list
##    sec80c = 0
##    deductions_sum = 0
##    for i,m in enumerate(z):
##        if (i==3 or i==4 or i==5 or i==6):
##            sec80c = sec80c + int(m.get())
##           
##        elif(i==0):
##            deductions_sum = deductions_sum + 50000
##            zl.insert(1,deductions_sum)
##        elif (i==2):
##            if int(m.get()) >= 250000:
##                deductions_sum = deductions_sum + 250000
##                zl = zl.append(deductions_sum)
##            else :
##                deductions_sum = deductions_sum + int(m.get())
##                zl = zl.append(deductions_sum)
##        elif (i==7):
##            if int(m.get()) > 25000:
##                deductions_sum = deductions_sum + 25000
##                zl = zl.insert(6,deductions_sum)
##            else :
##                deductions_sum = deductions_sum + int(m.get())
##                zl = zl.insert(6,deductions_sum)
##        elif (i==8):
##            if int(m.get()) > 5000:
##                deductions_sum = deductions_sum + 5000
##                zl = zl.insert(7,deductions_sum)
##            else :
##                deductions_sum = deductions_sum + int(m.get())
##                zl = zl.insert(7,deductions_sum)
##        elif (i==9):
##            if int(m.get()) > 50000:
##                deductions_sum = deductions_sum + 50000
##                zl = zl.insert(8,deductions_sum)
##            else :
##                deductions_sum = deductions_sum + int(m.get())
##                zl = zl.insert(8,deductions_sum)             
##
##        else:
##            deductions_sum = deductions_sum + int(m.get())
##            zl = zl.insert(9,deductions_sum)
##
##    if sec80c >= 150000:
##        deductions_sum = deductions_sum  + 150000
##        zl = zl.insert(4,150000)
##    elif sec80c <= 149999:
##        deductions_sum = deductions_sum + sec80c
##        zl = zl.insert(4,150000)
##     
##    deductionssumLabel = Label(akhilGui, text=deductions_sum,
##                               fg = "red",font = "Helvetica 15 bold ",justify='right')
##    deductionssumLabel.grid(row= 30, column= 4, sticky=W)
##    return deductions_sum

def labelded_printing():
    row_value          = 7 #initialise the variable row_value to be used in grid()

    for i,k in enumerate(deduction_list):                        #iterating through the list, creating label
        #kLabel          = str(k) + "Label"
        #kEntry          = str(k) + "Entry"
        kLabel          = Label(akhilGui, text= str(k), fg="#113B53",
                                font = "Helvetica  12 bold ", justify='right')
        labded_list.append(kLabel)
        kLabel.grid(row = row_value, column=3, pady=2, padx=15, sticky= W)
        if i == 0:
            v               = StringVar(akhilGui, value='50000')
        else:
            v               = StringVar(akhilGui, value='0')
        kEntry          = Entry(akhilGui, bd =1, fg = "red",textvariable = v,justify='right')
        entryded_list.append(kEntry)
       
        kEntry.grid(row= row_value, pady=2, column=4,sticky= W)
        row_value       = row_value + 1
    return()

##Print Result using ReportLab
def func_makepdf():
    
    global deductionssumLabel 
    #deductionssumLabel.destroy() #delete if present

    global deductionssumLabel 
    #deductionssumLabel.destroy() #delete if present
    
     
##    deductionssumLabel = Label(akhilGui, text=deductions_sum,
##                               fg = "red",font = "Helvetica 15 bold ",justify='right')
##    deductionssumLabel.grid(row= 30, column= 4, sticky=W)
##    return deductions_sum

    v1= nameEntry.get()
    v2= panEntry.get()
    c = canvas.Canvas("ITStatement-2020-21_"+v2+".pdf")
    c.drawString(50,800,"INCOME TAX CALCULATIONS FOR THE FINANCIAL YEAR 2020-21")
    c.drawString(50,785,"Name: "+str(v1))
    c.drawString(300,785,"PAN:"+str(v2))
    c.drawString(50,770,"Income Details:")
    v=765
    for i in income_list:
        v=v-10
        c.drawString(50,v-10,str(i))
    vinc=765
    for i in entry_list:
        vinc=vinc-10
        c.drawRightString(250,vinc-10,'{:>10,.2f}'.format(int(i.get())))
        c.drawString(290,770,"Deduction Details:")

    vdl=765
    for k in deduction_list:
        vdl=vdl-10
        c.drawString(290,vdl-10,k)


    vded=765
    for i in entryded_list:
        vded=vded-10
        c.drawRightString(490,vded-10,'{:>10,.2f}'.format(int(i.get())))

    vel=540
    for k in deduction_eligible_list:
        c.drawString(50,540,"Eligible Deductions:")
        vel=vel-10
        c.drawString(50,vel-10,k)
        
    veld=540
    for g in entryeli_list:
        veld=veld-10
        c.drawRightString(250,veld-10,'{:>10,.2f}'.format(g))
        
        
    c.save()
    

##Calculation of tax in two patterns

##Up to Rs. 2,50,000                  0%
##Rs. 2,50,001 to Rs. 5,00,000        5%
##Rs. 5,00,001 to Rs. 10,00,000      20%
##Above Rs. 15,00,000                30%

def tax_existing (income_sum,deductions_sum):

    global exitaxLabel
    global exitaxableLabel
    
    exi_inc = income_sum - deductions_sum

    
    exi_inc >= 0
    tax_old = 0
    if exi_inc < 250001:
        tax_old = 0
    elif exi_inc > 250000 and exi_inc < 500001:
        tax_old = (exi_inc-250000)*0.05
    elif exi_inc > 500000 and exi_inc < 1000001:
        tax_old = (0.2 * (exi_inc - 500000)) + 12500
    elif exi_inc > 150000:
        tax_old = ((exi_inc - 1000000) * 0.30) +162500
        
    exitaxableLabel = Label(akhilGui, text=str(exi_inc), fg = "#093145",
                           font = "Helvetica 15 bold ",justify='right')
    exitaxableLabel.grid(row= 7, column= 6, sticky=W) 

        
    exitaxLabel = Label(akhilGui, text=str(tax_old), fg = "tomato",
                           font = "Helvetica 15 bold ",justify='right')
    exitaxLabel.grid(row= 13, column= 6, sticky=W)        
   
    return tax_old

##Taxable income	Tax Rate (New Scheme)
##Up to Rs. 2,50,000	                Nil
##Rs. 2,50,001 to Rs. 5,00,000          5%
##Rs. 5,00,001 to Rs. 7,50,000	        10%
##Rs. 7,50,001 to Rs. 10,00,000  	15%
##Rs. 10,00,001 to Rs. 12,50,000	20%
##Rs. 12,50,001 to Rs. 15,00,000	25%
##Above Rs. 15,00,000	                30%

def tax_newscheme (income_sum):

    global newtaxLabel
    global newtaxableLabel
    
    income_sum>= 0
    tax_new = 0
    if income_sum< 250001:
        tax_new = 0
    elif income_sum> 250000 and income_sum< 500001:
        tax_new = (incnew-250000)*0.05
    elif income_sum> 500000 and income_sum< 750001:
        tax_new = (0.1 * (income_sum- 500000)) + 12500
    elif income_sum> 750000 and income_sum< 1000001:
        tax_new = (0.15 * (income_sum- 750000)) + 37500
    elif income_sum> 1000000 and income_sum< 1250001:
        tax_new = (0.20 * (income_sum- 1000000)) + 75000
    elif income_sum> 1250000 and income_sum< 1500001:
        tax_new = (0.25 * (income_sum- 1250000)) + 125000

    elif income_sum> 150000:
        tax_new = ((income_sum- 1000000) * 0.30) +162500
    newtaxableLabel = Label(akhilGui, text=str(income_sum), fg = "#093145",
                           font = "Helvetica 15 bold ",justify='right')
    newtaxableLabel.grid(row= 9, column= 6, sticky=W )       
        
    newtaxLabel = Label(akhilGui, text=str(tax_new), fg = "tomato",
                           font = "Helvetica 15 bold ",justify='right')
    newtaxLabel.grid(row= 15, column= 6, sticky=W)        

    return tax_new

def tax_diff(tax_new, tax_old):

    global differenceLabel
    global differencereLabel
    global benefitLabel

    benefit = tax_old - tax_new
    if benefit < 0 :
        h = "Existing Scheme is beneficial!"
    elif  benefit > 0:
        h = "New Scheme is beneficial!"
        
    else:
        h = "No Tax as per both the schemes!"
    
    differenceLabel = Label(akhilGui, text= "iii)Difference", fg = "#093145",
                           font = "Helvetica 15 bold ",justify='right')
    differenceLabel.grid(row= 17, column= 5, sticky=W)           
        
    differencereLabel = Label(akhilGui, text=str(benefit), fg = "#113B53",
                           font = "Helvetica 15 bold ",justify='right')
    differencereLabel.grid(row= 17, column= 6, sticky=W)
    
    benefitLabel = Label(akhilGui, text=str(h), bg="blue",fg = "#ffa500",
                           font = "Helvetica 15 bold ",justify='right')
    benefitLabel.grid(row= 19, column= 5, sticky=W)
    return benefit

def func_call_arguments():
    global incomesumLabel
    incomesumLabel.destroy()
    
    global deductionssumLabel
    deductionssumLabel.destroy()
    
    income_sum = func_total_income()
    deductions_sum = func_total_deductions()
    tax_old = tax_existing (income_sum,deductions_sum)
    tax_new = tax_newscheme (income_sum)
    benefit = tax_diff(tax_new, tax_old)
    return

#subtitle Income
incsubtitleLabel = Label(akhilGui,text="Income:",fg="#113B53",
                         font = "Helvetica 13 bold ", justify='center')
incsubtitleLabel.grid(row= 3, columnspan=2, sticky=EW)


income_list = [ "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December",
                "January", "February", "Leave Surrender", "L/S Arrear-Cash", "L/S Arrear-GPF",
                "Festival Allowance", "DA arrear(CASH)", "DA Arrear(GPF)", "Family Pension" ]

row_value          = 5 #initialise the variable row_value to be used in grid()
lab_list           = []
entry_list         = []  

label_printing()

b1= Button(text="Total Income", fg="#113B53",font = "Helvetica 18 bold ",
           command=func_total_income, justify='center')
b1.grid(row=30,column=0, pady=20, sticky= W)


#Deduction Label and entry boxes printing
dedsubtitleLabel = Label(akhilGui,text="Deductions:",fg="#113B53",
                         font = "Helvetica 13 bold ", pady=5, justify='center')
dedsubtitleLabel.grid(row= 6,column=3, columnspan=2, sticky=EW)


deduction_list = [ "1.Standard Deduction", "2.Profession Tax", "3.Interest on HCL", "4.GPF Subscription",
                  "5.GPF (Arrears)", "6.Insurance Premia", "7.NSC", "8.i)Medical Insurance",
                  "8.ii)Yearly Health Checkup", "9.NPS 80CCDIB","9.80G Donations","10.Others" ]
row_value          = 5 #initialise the variable row_value to be used in grid()
labded_list           = []
entryded_list         = []
entryeli_list         = []
zl= entryeli_list

labelded_printing()

b2= Button(text="Total Deduction", fg="#113B53",
           font = "Helvetica 18 bold ",command=func_total_deductions, justify='center')
b2.grid(row=30,column=3, pady=20, sticky= W)
deduction_eligible_list = ["1.Standard Deduction", "2.Profession Tax", "3.Interest on HCL",
                           "4.Section 80C", "5.Section 80D (i)","6.Section 80 D(ii)","7.80CCDIB","8.80G Donations","9.Others"]


taxsubtitleLabel = Label(akhilGui,text="Calculation of Tax:",fg="#113B53",
                         font = "Helvetica 15 bold ", pady=5, justify='center')
taxsubtitleLabel.grid(row= 3,column=5, columnspan=2, sticky=EW)
taxableIncomeLabel = Label(akhilGui, text="Taxable Income ",fg = "#113B53",font = "Helvetica 13 bold ",justify='right')
taxableIncomeLabel.grid(row= 5, column= 5, padx=15, sticky=W)

existingLabel = Label(akhilGui, text="i)Existing scheme",fg = "#113B53",font = "Helvetica 11 bold ",justify='right')
existingLabel.grid(row= 7, column= 5, padx=15, sticky=W)
newSchemeLabel= Label(akhilGui, text="ii) New Scheme",fg = "#113B53",font = "Helvetica 11 bold ",justify='right')
newSchemeLabel.grid(row= 9, column= 5, padx=15, sticky=W)
incomeTax1Label = Label(akhilGui, text="Income Tax",fg = "#113B53",font = "Helvetica 13 bold ",justify='right')
incomeTax1Label.grid(row= 11, column= 5, padx=15, sticky=W)

extaxSchemeLabel = Label(akhilGui, text="i)Existing scheme",fg = "#113B53",font = "Helvetica 11 bold ",justify='right')
extaxSchemeLabel.grid(row= 13, column= 5, padx=15, sticky=W)
newtaxSchemetaxLabel = Label(akhilGui, text="ii) New scheme",fg = "#113B53",font = "Helvetica 11 bold ",justify='right')
newtaxSchemetaxLabel.grid(row= 15, column= 5, padx=15, sticky=W)



b3= Button(text="CALCULATE", fg="#113B53",
           font = "Helvetica 16 bold ",command=func_call_arguments, justify='center')
b3.grid(row=30,column=5, pady=20, padx=15, sticky= W)

button_clear= Button(text="CLEAR", fg="#113B53",
           font = "Helvetica 16 bold",command=func_clear, justify='center')
button_clear.grid(row=30,column=7, pady=20, padx=15, sticky= EW)
button_pdf= Button(text="PRINT", fg="#113B53",
           font = "Helvetica 16 bold",command=func_makepdf, justify='center')
button_pdf.grid(row=30,column=6, pady=20, padx=15, sticky= EW)

akhilGui.mainloop()
