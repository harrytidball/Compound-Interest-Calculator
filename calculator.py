from tkinter import *
from tkinter import messagebox as msg
from tkinter import font as font

#Create root widget
root = Tk()

topframe = Frame(root, borderwidth=30)
topframe.pack()

middleframe = Frame(root)
middleframe.pack()

bottomframe = Frame(root, borderwidth=30)
bottomframe.pack()

confirmationLabel = Label(bottomframe, text="", pady=15, font=(16))
investmentInfoLabel = Label(bottomframe, text="", pady=5, font=(16))

def calculate():
    confirmationLabel.config(text="")
    investmentInfoLabel.config(text="")

    futureValue = 0
    noOfYears = 0
    valueWithoutContribution = 0
    valueWithContribution = 0
    interestAccrued = 0
    initialDeposit = 0
    monthlyDeposit = 0
    months = 0
    years = 0
    interestRate = 0

    if (len(interestRateEntry.get()) == 0):
        msg.showwarning(title="Invalid Input", message="Please enter an interest rate.")
    else:
        interestRate = float(float(interestRateEntry.get()) / 100)
        if (len(intialDepositEntry.get()) != 0):
            initialDeposit = float(intialDepositEntry.get())
        if (len(monthlyDepositEntry.get()) != 0):
            monthlyDeposit = float(monthlyDepositEntry.get())
        if (len(monthsEntry.get()) != 0):
            months = int(monthsEntry.get())
        if (len(yearsEntry.get()) != 0):
            years = int(yearsEntry.get())
        totalMonths = years * 12 + months
        if (months > 0):
            noOfYears = years + (months / 12)
        elif (months == 0):
            noOfYears = years
        interestRateDivided = interestRate / 12
        noOfYearsMultiplied = 12 * noOfYears

        valueWithoutContribution = initialDeposit * (1 + interestRateDivided)**noOfYearsMultiplied

        if (monthlyDeposit > 0):
            valueWithContribution = monthlyDeposit * (((1 + interestRateDivided)**noOfYearsMultiplied - 1) / interestRateDivided)

        futureValue = valueWithoutContribution + valueWithContribution
        futureValueFormatted = '£{:,.2f}'.format(futureValue)

        if (monthlyDeposit == 0):
            interestAccrued = futureValue - initialDeposit
        elif (monthlyDeposit > 0):
            interestAccrued = futureValue - initialDeposit - (totalMonths * monthlyDeposit) 

        interestAccruedFormated = '£{:,.2f}'.format(interestAccrued)

        confirmationLabel.config(text="Future value of investment is " + futureValueFormatted + ".")
        investmentInfoLabel.config(text="This includes " + interestAccruedFormated + " of accrued interest.")

        confirmationLabel.pack()
        investmentInfoLabel.pack()

#Set program title
root.title("Compound Interest Calculator")

#Set size of window
root.geometry("500x500")

#Create label widgets
titleLabel = Label(topframe, text="Compound Interest Calculator", padx=5, pady=5, font=(24))
initialDepositLabel = Label(middleframe, text="Initial Deposit", padx=5, pady=5, font=(18))
monthlyDepositLabel = Label(middleframe, text="Monthly Deposit", padx=5, pady=5, font=(18))
interestRateLabel = Label(middleframe, text="Interest Rate", padx=5, pady=5, font=(18))
yearsLabel = Label(middleframe, text="Years", padx=5, pady=5, font=(18))
monthsLabel = Label(middleframe, text="Months", padx=5, pady=5, font=(18))

#Create entry widgets
intialDepositEntry = Entry(middleframe, font=(18))
monthlyDepositEntry = Entry(middleframe, font=(18))
interestRateEntry = Entry(middleframe, font=(18))
yearsEntry = Entry(middleframe, font=(18))
monthsEntry = Entry(middleframe, font=(18))

#Create button widget
calculateButton = Button(bottomframe, text="Calculate", padx=5, pady=10, command=calculate, font=(18))

#Place title widget
titleLabel.pack()

#Set grid values for widgets
initialDepositLabel.grid(row=1, column=2)
intialDepositEntry.grid(row=1, column=3)
monthlyDepositLabel.grid(row=2, column=2)
monthlyDepositEntry.grid(row=2, column=3)
interestRateLabel.grid(row=3, column=2)
interestRateEntry.grid(row=3, column=3)
yearsLabel.grid(row=4, column=2)
yearsEntry.grid(row=4, column=3)
monthsLabel.grid(row=5, column=2)
monthsEntry.grid(row=5, column=3)

#Place calculate widget
calculateButton.pack()

#Display root widget
root.mainloop()