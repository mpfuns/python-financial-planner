from classesFunctions import NumberHandler
from datetime import datetime, timedelta
import re
# This  varible will help with storing the information from the user
planner = {
     "peopleNum": "",
     "peopleArray" : [ ],
     "totalBills" : "",
     "vfBillNum" : "",
    "vfBillArray": [ ],
     "fixedBillNum": "",
     "fixedBillArray": [] }

# This function will help with getting the information from the user
def inputInformation():
    #this  variable will help with checking the correct format of the date
    pattern = r"^(0[1-9]|1[0-2])/([0-2][0-9]|3[0-1])/(\d{4})$"
    
    # while loop check correct format  if it's a number
    while planner["peopleNum"] == "" or planner["peopleNum"].isnumeric() == False:
     # asking about people who are  paying the bills information
     planner["peopleNum"] = input("Number of people who are paying bills?:")
    #for loop to get the information of the people
    for i in range(int(planner["peopleNum"])):
        #this  variable will help with storing the information of the person and  set up  the layout of the organization later in the code
        personInfo = {
                "name": "",
                "checkDate": "",
                "checkAmount": "",
                "futurePeriods": []
            }
        #check to make sure name is not empty
        while personInfo["name"] == "":
            personInfo["name"] = input("Enter your name: " if int(planner["peopleNum"]) == 1  else f"Enter person {i + 1} name: ")
        #add check correct format of date 
        while personInfo["checkDate"] == "" or re.match(pattern, personInfo["checkDate"]) == None:
            personInfo["checkDate"] = input("Enter the date when you got your last paid check(mm/dd/yyyy):"if int(planner["peopleNum"]) == 1  else f"Enter the date when {personInfo['name']} got their last paid check(mm/dd/yyyy):")
            #check to make sure the amount is a number
        while personInfo["checkAmount"] == "" or not NumberHandler.is_number(personInfo["checkAmount"]):
            personInfo["checkAmount"] = input("Enter the amount of your check $: " if int(planner["peopleNum"]) == 1  else f"Enter the amount of {personInfo['name']}'s check $: ")  
        #add the information to the array
        planner["peopleArray"].append(personInfo)
# asking about  bills  
    # check correct format if it's a number   
    while planner["totalBills"] == "" or planner["totalBills"].isnumeric() == False:
     planner["totalBills"] = input("Enter the number of total bills:")
    # check correct format if it's a number 
    while planner["vfBillNum"] == "" or planner["vfBillNum"].isnumeric() == False or int(planner["vfBillNum"]) > int(planner["totalBills"]):  
     planner["vfBillNum"] = input("Enter the number of variable/fluctuate bills(can't be over the total bills):")
    if int(planner["vfBillNum"]) > 0:
       #for loop to get the information of the variable/fluctuate bills
        for i in range(int(planner["vfBillNum"])):
            #this billInfo variable will help with storing the information of the variable/fluctuate bills and  set up  the layout of the organization later in the code
            billInfo = {
                "name": "",
                "billDate": "",
                "billAmount": "",
                "futurePeriods": []
            }
            #check to make sure name is  fill out
            while billInfo["name"] == "":  
             billInfo["name"] = input(f"Enter variable/fluctuate bill {i + 1} name:")
            #add check correct format of date
            while billInfo["billDate"] == "" or re.match(pattern, billInfo["billDate"]) == None:
             billInfo["billDate"] = input(f"Enter the date of the last due date for this bill(mm/dd/yyyy):")
            #check correct format  if it's a number
            while billInfo["billAmount"] == "" or not NumberHandler.is_number(billInfo["billAmount"]):
             billInfo["billAmount"] = input(f"Enter the estimated amount of {billInfo['name']} $:")
            #add the information to the array
            planner["vfBillArray"].append(billInfo)
    #We will calculate the fixed bills based on the total bills and the variable/fluctuate bills
    planner["fixedBillNum"] = int(planner["totalBills"]) - int(planner["vfBillNum"])
   #for loop to get the information of the fixed bills
    for i in range(int(planner["fixedBillNum"])):
        #this billInfo variable will help with storing the information of the fixed bills and  set up  the layout of the organization later in the code
        billInfo = {
            "name": "",
            "billDay": "",
            "billAmount": "",
            "futurePeriods": []
        }
        #add check to make sure name is  fill out
        while billInfo["name"] == "":
         billInfo["name"] = input(f"Enter fixed bill {i + 1} name: ")
        #add check correct format  if it's a number
        while billInfo["billDay"] == "" or billInfo["billDay"].isnumeric() == False or int(billInfo["billDay"]) >= 31:
         billInfo["billDay"] = input(f"Enter the day of the month this bill is due:")
        #add check correct format  if it's a number
        while billInfo["billAmount"] == "" or not NumberHandler.is_number(billInfo["billAmount"]):
         billInfo["billAmount"] = input(f"Enter the estimated or exact amount of {billInfo['name']} $:")
        planner["fixedBillArray"].append(billInfo)

def calculation():
    #the following code will help get the  future periods for the checks
    for i in range(len(planner["peopleArray"])):
        # this nextPeriod variable is a placeholder for the next period
        nextPeriod = ""
        # for loop to get the future periods for the checks
        for j in range(26):
            #this checkDateSetup variable will help with storing the information of the future periods for the checks and the  format of the date
            checkDateSetup= {"format": "", "compare": ""}
            previous = nextPeriod if nextPeriod !="" else planner["peopleArray"][i]["checkDate"]
            #this formatPrevious variable will help with the format of the date
            formatPrevious = datetime.strptime(previous, "%m/%d/%Y")
            #this  futureDate variable will help with getting the future date
            futureDate = formatPrevious + timedelta(days=14)
            checkDateSetup["format"] = futureDate.strftime("%m/%d/%Y")
            checkDateSetup["compare"] = futureDate 
            #add the information to the array
            planner["peopleArray"][i]["futurePeriods"].append(checkDateSetup)
            #set the next period to the future date
            nextPeriod = futureDate.strftime("%m/%d/%Y")
          
    #the following code will help get the  future periods for the fixed  bills
    for i in range(int(planner["fixedBillNum"])):
        todayDate = datetime.today()
        todayMonth = todayDate.month
        todayYear = todayDate.year
        # this  month variable will help with getting the correct format of the month
        month = todayMonth if todayMonth > 9 else f'0{todayMonth}'
        day = planner['fixedBillArray'][i]['billDay']
       # this  day variable will help with getting the correct format of the day
        day = day if int(day) > 9 else f'0{day}'
        # this  standardBillDate variable will help with getting the correct format of the date
        standardBillDate = f"{month}/{day}/{todayYear}"
        # this nextPeriod variable is a placeholder for the next period
        nextPeriod = ""
        for j in range(12):
            #this dateSetup variable will help with storing the information of the future periods for the fixed bills and the  format of the date
            dateSetup = {"format": "","compare": ""}
            current = nextPeriod if nextPeriod != "" else standardBillDate
            #this startDate variable will help with the format of the date
            startDate = datetime.strptime(current, "%m/%d/%Y")
            nextMonth = startDate.month if j == 0 else (startDate.month + 1)
            nextYear = startDate.year
            # this  section of code will help with getting the correct format of the month and year
            if nextMonth > 12:
                nextMonth = 1
                nextYear = startDate.year + 1
            monthWithZero = nextMonth if nextMonth > 9 else f'0{nextMonth}'
            futureBillDate = f"{monthWithZero}/{day}/{nextYear}"
            dateSetup["format"] = futureBillDate
            dateSetup["compare"] = datetime.strptime(futureBillDate, "%m/%d/%Y")
           #add the information to the array
            planner["fixedBillArray"][i]["futurePeriods"].append(dateSetup)
            nextPeriod = futureBillDate
   #the following code will help get the  future periods for the variable/fluctuate bills
    for i in range(int(planner["vfBillNum"])):
        lastDate = planner["vfBillArray"][i]["billDate"]
        #this nextDate variable is a placeholder for the next date
        nextDate = ""
        for j in range(11):
            #this rangeSetup variable will help with storing the information of the future periods for the variable/fluctuate bills and the  format of the
            rangeSetup = {"min": "", "middle": "", "max": "", "compare": ""}
            currentDate = nextDate if nextDate !="" else lastDate
            formatCurrentDate = datetime.strptime(currentDate, "%m/%d/%Y")
           #this middleDate variable will help with getting the middle date
            middleDate = formatCurrentDate + timedelta(days=30)
            rangeSetup["middle"] = middleDate.strftime("%m/%d/%Y")
            #this minDate variable will help with getting the min date
            minDate = middleDate - timedelta(days=2)
            rangeSetup["min"] = minDate.strftime("%m/%d/%Y")
            rangeSetup["compare"] = minDate
           #this maxDate variable will help with getting the max date 
            maxDate = middleDate + timedelta(days=8) 
            rangeSetup["max"] = maxDate.strftime("%m/%d/%Y")
            #add the information to the array
            planner["vfBillArray"][i]["futurePeriods"].append(rangeSetup)
            nextDate = middleDate.strftime("%m/%d/%Y")
    #the following code will help with organizing the checks
   #this allChecks variable will help with storing the information of the checks
    allChecks = []
    for i in range(len(planner["peopleArray"])):
        for j in range(len(planner["peopleArray"][i]["futurePeriods"])):
            #this checkLayout variable will help with storing the information of the checks
            checkLayout = {"name": "", "date": "", "amount": ""}
            checkLayout["name"] = planner["peopleArray"][i]["name"]
            checkLayout["date"] = planner["peopleArray"][i]["futurePeriods"][j]
            checkLayout["amount"] = planner["peopleArray"][i]["checkAmount"]
            allChecks.append(checkLayout)
    #this organizedChecks variable will help with organizing the checks from the allChecks variable 
    organizedChecks = sorted(allChecks, key=lambda x: x["date"]["compare"])
    #the following code will help with organizing the bills
    #this allBills variable will help with storing the information of the bills
    allBills = []
    # for loop for  fixed bills
    for i in range(len(planner["fixedBillArray"])):
        for j in range(len(planner["fixedBillArray"][i]["futurePeriods"])):
            billLayout = {"name": " ", "date": " ", "amount": " ", "type": "fixed"}
            billLayout["name"] = planner["fixedBillArray"][i]["name"]
            billLayout["date"] = planner["fixedBillArray"][i]["futurePeriods"][j]
            billLayout["amount"] = planner["fixedBillArray"][i]["billAmount"]
            allBills.append(billLayout)
    # for loop for  variable/fluctuate bills
    for i in range(len(planner["vfBillArray"])):
        for j in range(len(planner["vfBillArray"][i]["futurePeriods"])):
            billLayout = {"name": " ", "date": {}, "amount": " ", "type": "variable/fluctuate"}
            billLayout["name"] = planner["vfBillArray"][i]["name"]
            billLayout["date"] = planner["vfBillArray"][i]["futurePeriods"][j]
            billLayout["amount"] = planner["vfBillArray"][i]["billAmount"]
            allBills.append(billLayout)
    #this organizedBills variable will help with organizing the bills from the allBills variable
    organizedBills = sorted(allBills, key=lambda x: x["date"]["compare"])
    # This loop will help with displaying the information in the correct format for  the file
    #this displayOutput variable will help with storing the information of the display
    displayOutput = []
    # for loop  to put the  bills under the correct check
    for i in range(len(organizedChecks)):
        totalBillAmount = 0
        #this maxAmount variable will help with getting the max amount of the check
        maxAmount = float(organizedChecks[i]["amount"])
        #this periodLayout variable will help with storing the information of the display and the  format of the display
        periodLayout = {"check": {"name": " ", "date": " ", "amount": " "}, "bills": [], "totalBills": " ", "overAmount": "none"}
        periodLayout["check"]["name"] = organizedChecks[i]["name"]
        periodLayout["check"]["date"] = organizedChecks[i]["date"]["format"]
        periodLayout["check"]["amount"] = organizedChecks[i]["amount"]
        # for loop to put the  bills under the correct check
        for j in range(len(organizedBills)):
            #this fixedbillDetail variable will help with storing the information of the fixed bills and the  format of the display
            fixedbillDetail = {"name": " ", "date": " ", "amount": " ", "type": "Fixed", "note": " "}
            #this vfBillDetail variable will help with storing the information of the variable/fluctuate bills and the  format of the display
            vfBillDetail = {"name": " ", "date": {}, "amount": " ", "type": "variable/fluctuate", "note": " "}
           #this compareDate variable will help with getting the compare date
            compareDate = organizedBills[j]["date"]["compare"]
            #this if statement will help with organizing the bills based if it's a variable/fluctuate or fixed bill
            if organizedBills[j]["type"] == "variable/fluctuate":
                if compareDate >= organizedChecks[i]["date"]["compare"] and (i + 1 < len(organizedChecks) and compareDate < organizedChecks[i + 1]["date"]["compare"]):
                    vfBillDetail["name"] = organizedBills[j]["name"]
                    vfBillDetail["date"] = organizedBills[j]["date"]
                    vfBillDetail["amount"] = organizedBills[j]["amount"]
                    if float(organizedBills[j]["amount"]) >= 0.5 * float(organizedChecks[i]["amount"]):
                        vfBillDetail["note"] = "---this bill will take all or most of your check, you will have to split this amount in smaller chunks---"
                        periodLayout["bills"].append(vfBillDetail)
                    else:
                        totalBillAmount +=  float(organizedBills[j]["amount"])
                        periodLayout["bills"].append(vfBillDetail)
            else:
                if compareDate >= organizedChecks[i]["date"]["compare"] and (i + 1 < len(organizedChecks) and compareDate < organizedChecks[i + 1]["date"]["compare"]):
                    fixedbillDetail["name"] = organizedBills[j]["name"]
                    fixedbillDetail["date"] = organizedBills[j]["date"]["format"]
                    fixedbillDetail["amount"] = organizedBills[j]["amount"]
                    if float(organizedBills[j]["amount"]) >= 0.5 * float(organizedChecks[i]["amount"]):
                        fixedbillDetail["note"] = "---this bill will take all or most of your check, you will have to split this amount in smaller chunks---"
                        periodLayout["bills"].append(fixedbillDetail)
                    else:
                        totalBillAmount += float(organizedBills[j]["amount"])
                        periodLayout["bills"].append(fixedbillDetail)
                else:
                    continue
        #add the information to the array and round the total bill amount
        periodLayout["totalBills"] =  round(totalBillAmount, 2)
       #this over variable will help with getting the over amount
        over = maxAmount - totalBillAmount
        if over < 0:
            periodLayout["overAmount"] = round(over, 2)
        #add the information to the array
        displayOutput.append(periodLayout)
    #return the information
    return displayOutput
#this function will help with displaying the information in the correct format for  the file and  run the program
def output():
    
    #this userAnswer variable will help with getting the user input
    userAnswer = ""
    #this while loop is the main loop for the program
    while userAnswer.lower() != "exit" and userAnswer.lower() != "enter":
     #this userinput variable will help with getting the user input and give the user instructions
     userinput = input("Welcome to the Financial Planner\n_________________________________________________________\nThis program will help you organize your bills and checks.\nThis program will ask some questions so please gather all of your bills and information.\nIf you want to look at an example of the output please look at the sample.txt file.\nPlease follow the instructions below.\nWhen entering the date please use the following format: mm/dd/yyyy\nWhen entering the amount please use numbers only.\n_________________________________________________________\nTo continue type enter or type exit to leave the program:")
     userAnswer = userinput
    if userAnswer.lower() == "exit":
        return
    else:
     #getting the information from the user
     inputInformation()
    #getting the results
     result= calculation()
     #putting  results in a file
     with open("output.txt", "w") as file:
        #this file.write will help with writing the information in the file and it  put it in a layout to be easy to read
        file.write(f"Financial Planner Todays date: {datetime.today().strftime('%m/%d/%Y')}\n\n")
        file.write("**Variable/fluctuate bills Minimum Days Between Bills are 28 days and the Maximum Days Between Bills are 35 days.**\n ***Rare Extremes are 15 days(starting or ending services) and 45 days(In unusual circumstances, such as major system overhauls or natural disasters) between bills.***\n\n")
        for i in range(len(result)):
            file.write("___________________________________________")
            file.write("Check " if int(planner["peopleNum"]) == 1 else f"Check for {result[i]['check']['name']} ")
            file.write(f"on {result[i]['check']['date']} amount:${result[i]['check']['amount']}\n")
            for j in range(len(result[i]['bills'])):
                if result[i]['bills'][j]['type'] == "variable/fluctuate":
                    file.write(f"Variable/fluctuate bill:{result[i]['bills'][j]['name']} between {result[i]['bills'][j]['date']['min']}-{result[i]['bills'][j]['date']['max']} amount:${result[i]['bills'][j]['amount']}\n{result[i]['bills'][j]['note']}\n")
                else:
                    file.write(f"Fixed bill:{result[i]['bills'][j]['name']} on {result[i]['bills'][j]['date']} amount:${result[i]['bills'][j]['amount']}\n{result[i]['bills'][j]['note']}\n")
            file.write(f"Total bills:${result[i]['totalBills']}\n")
            file.write(f"Over amount: {result[i]['overAmount']}\n")
            file.write("___________________________________________\n\n\n")
        file.close()
        #this print statement will help with letting the user know the information has been saved in the file
        print("The information has been saved in output.txt file")
#run the program
output()