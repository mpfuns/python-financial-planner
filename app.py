from datetime import datetime, timedelta
import re

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
    pattern = r"^\d{2}/\d{2}/\d{4}$"
    # asking about people who are  paying the bills information
    #add check correct format  if it's a number
    planner["peopleNum"] = int(input("How many people are paying bills? "))
    if planner["peopleNum"] > 1:
        for i in range(planner["peopleNum"]):
            personInfo = {
                "name": "",
                "checkDate": "",
                "checkAmount": "",
                "futurePeriods": []
            }
            #check to make sure name is not empty
            while personInfo["name"] == "":
                personInfo["name"] = input(f"Enter person {i + 1} name: ")
            #add check correct format of date 
            while personInfo["checkDate"] == "" or re.match(pattern, personInfo["checkDate"]) == None:
             personInfo["checkDate"] = input(f"Enter the date when {personInfo['name']} got their last paid check(mm/dd/yyyy): ")
            #check to make sure the amount is a number
            while personInfo["checkAmount"] == "" or personInfo["checkAmount"].isnumeric() == False:
             personInfo["checkAmount"] = input(f"Enter the amount of {personInfo['name']}'s check $: ")
            planner["peopleArray"].append(personInfo)
    else:
        personInfo = {
            "name": "",
            "checkDate": "",
            "checkAmount": "",
            "futurePeriods": []
        } 
        #check to make sure name is not empty
        while personInfo["name"] == "":
          personInfo["name"] = input("Enter your name: ")
        #add check correct format of date 
        while personInfo["checkDate"] == "" or re.match(pattern, personInfo["checkDate"]) == False:
         personInfo["checkDate"] = input("Enter the date when you got your last paid check(mm/dd/yyyy): ") 
        #check to make sure the amount is a number
        while personInfo["checkAmount"] == "" or personInfo["checkAmount"].isnumeric() == False:
         personInfo["checkAmount"] = input("Enter the amount of your check $: ")
        planner["peopleArray"].append(personInfo)
# asking about  bills  
    # check correct format if it's a number   
    while planner["totalBills"] == "" or planner["totalBills"].isnumeric() == False:
     planner["totalBills"] = int(input("Enter the number of bills: "))
    # check correct format if it's a number 
    while planner["vfBillNum"] == "" or planner["vfBillNum"].isnumeric() == False:  
     planner["vfBillNum"] = int(input("Enter the number of variable/fluctuate bills: "))
    if planner["vfBillNum"] > 0:
       
        for i in range(planner["vfBillNum"]):
            billInfo = {
                "name": "",
                "billDate": "",
                "billAmount": "",
                "futurePeriods": []
            }
            #check to make sure name is  fill out
            while billInfo["name"] == "":  
             billInfo["name"] = input(f"Enter variable/fluctuate bill {i + 1} name: ")
            #add check correct format of date
            while billInfo["billDate"] == "" or re.match(pattern, billInfo["billDate"]) == False:
             billInfo["billDate"] = input(f"Enter the date of the last due date for this bill(mm/dd/yyyy): ")
            #check correct format  if it's a number
            while billInfo["billAmount"] == "" or billInfo["billAmount"].isnumeric() == False:
             billInfo["billAmount"] = input(f"Enter the estimated amount of {billInfo['name']}: ")
            planner["vfBillArray"].append(billInfo)
    else:
     planner["fixedBillNum"] = planner["totalBills"] - planner["vfBillNum"]
    for i in range(planner["fixedBillNum"]):
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
         billInfo["billDay"] = input(f"Enter the day of the month this bill is due: ")
        #add check correct format  if it's a number
        while billInfo["billAmount"] == "" or billInfo["billAmount"].isnumeric() == False:
         billInfo["billAmount"] = input(f"Enter the estimated or exact amount of {billInfo['name']} $: ")
        planner["fixedBillArray"].append(billInfo)

def calculation():
    #the following code will help get the  future periods for the checks
    for i in range(len(planner["peopleArray"])):
        for j in range(26):
            nextPeriod = " "
            previous = nextPeriod != " " or planner["peopleArray"][i]["checkDate"]
            formatPrevious = datetime.strptime(previous, "%m/%d/%Y")
            futureDate = formatPrevious + timedelta(days=14) 
            planner["peopleArray"][i]["futurePeriods"].append(futureDate)
            nextPeriod = futureDate
    #the following code will help get the  future periods for the fixed  bills
    for i in range(planner["fixedBillNum"]):
        todayDate = datetime.today()
        todayMonth = todayDate.month
        todayYear = todayDate.year
        standardBillDate = f"{todayMonth}/ {planner['fixedBillArray'][i]['billDay']} / {todayYear}"
        planner["fixedBillArray"][i]["futurePeriods"].append(standardBillDate)
        for j in range(11):
            nextPeriod = " "
            current = nextPeriod != " " or standardBillDate
            formatCurrent = datetime.strptime(current, "%m/%d/%Y")
            futureBillDate = formatCurrent + timedelta(days=30)
            planner["fixedBillArray"][i]["futurePeriods"].append(futureBillDate)
            nextPeriod = futureBillDate
   #the following code will help get the  future periods for the variable/fluctuate bills
    for i in range(planner["vfBillNum"]):
        lastDate = planner["vfBillArray"][i]["billDate"]
        for j in range(11):
            range = {"min": " ", "middle": " ", "max": " "}
            nextDate = " "
            currentDate = nextDate != " " or lastDate
            formatCurrentDate = datetime.strptime(currentDate, "%m/%d/%Y")
            middleDate = formatCurrentDate + timedelta(days=30)
            range["middle"] = middleDate
            minDate = middleDate - timedelta(days=2)
            range["min"] = minDate
            maxDate = middleDate + timedelta(days=8) 
            range["max"] = maxDate
            planner["vfBillArray"][i]["futurePeriods"].append(range)
            nextDate = middleDate
    #the following code will help with organizing the checks
    allChecks = []
    for i in range(len(planner["peopleArray"])):
        for j in range(len(planner["peopleArray"][i]["futurePeriods"])):
            checkLayout = {"name": " ", "date": " ", "amount": " "}
            checkLayout["name"] = planner["peopleArray"][i]["name"]
            checkLayout["date"] = planner["peopleArray"][i]["futurePeriods"][j]
            checkLayout["amount"] = planner["peopleArray"][i]["checkAmount"]
            allChecks.append(checkLayout)
    organizedChecks = sorted(allChecks, key=lambda x: x["date"])
    #the following code will help with organizing the bills
    allBills = []
    for i in range(len(planner["fixedBillArray"])):
        for j in range(len(planner["fixedBillArray"][i]["futurePeriods"])):
            billLayout = {"name": " ", "date": " ", "amount": " ", "type": "fixed"}
            billLayout["name"] = planner["fixedBillArray"][i]["name"]
            billLayout["date"] = planner["fixedBillArray"][i]["futurePeriods"][j]
            billLayout["amount"] = planner["fixedBillArray"][i]["billAmount"]
            allBills.append(billLayout)
    for i in range(len(planner["vfBillArray"])):
        for j in range(len(planner["vfBillArray"][i]["futurePeriods"])):
            billLayout = {"name": " ", "date": {}, "amount": " ", "type": "variable/fluctuate"}
            billLayout["name"] = planner["vfBillArray"][i]["name"]
            billLayout["date"] = planner["vfBillArray"][i]["futurePeriods"][j]
            billLayout["amount"] = planner["vfBillArray"][i]["billAmount"]
            allBills.append(billLayout)
    organizedBills = sorted(allBills, key=lambda x: x["date"])
    # This loop will help with displaying the information in the correct format for  the file
    displayOutput = []
    for i in range(len(organizedChecks)):
        totalBillAmount = 0
        maxAmount = organizedChecks[i]["amount"]
        periodLayout = {"check": {"name": " ", "date": " ", "amount": " "}, "bills": [], "totalBills": " ", "overAmount": " "}
        periodLayout["check"]["name"] = organizedChecks[i]["name"]
        periodLayout["check"]["date"] = organizedChecks[i]["date"]
        periodLayout["check"]["amount"] = organizedChecks[i]["amount"]
        for j in range(len(organizedBills)):
            fixedbillDetail = {"name": " ", "date": " ", "amount": " ", "type": "Fixed", "note": " "}
            vfBillDetail = {"name": " ", "date": {}, "amount": " ", "type": "variable/fluctuate", "note": " "}
            if organizedBills[j]["type"] == "variable/fluctuate":
                compareDate = organizedBills[j]["date"]["min"]
                if compareDate >= organizedChecks[i]["date"] and compareDate < organizedChecks[i + 1]["date"]:
                    vfBillDetail["name"] = organizedBills[j]["name"]
                    vfBillDetail["date"] = organizedBills[j]["date"]
                    vfBillDetail["amount"] = organizedBills[j]["amount"]
                    if organizedBills[j]["amount"] >= 0.5 * organizedChecks[i]["amount"]:
                        vfBillDetail["note"] = "this bill will take all or most of your check, you will have to split this amount in smaller chunks"
                        periodLayout["bills"].append(vfBillDetail)
                    else:
                        totalBillAmount += organizedBills[j]["amount"]
                        periodLayout["bills"].append(vfBillDetail)
            else:
                if organizedBills[j]["date"] >= organizedChecks[i]["date"] and organizedBills[j]["date"] < organizedChecks[i + 1]["date"]:
                    fixedbillDetail["name"] = organizedBills[j]["name"]
                    fixedbillDetail["date"] = organizedBills[j]["date"]
                    fixedbillDetail["amount"] = organizedBills[j]["amount"]
                    if organizedBills[j]["amount"] >= 0.5 * organizedChecks[i]["amount"]:
                        fixedbillDetail["note"] = "this bill will take all or most of your check, you will have to split this amount in smaller chunks"
                        periodLayout["bills"].append(fixedbillDetail)
                    else:
                        totalBillAmount += organizedBills[j]["amount"]
                        periodLayout["bills"].append(fixedbillDetail)
        periodLayout["totalBills"] = totalBillAmount
        over = maxAmount - totalBillAmount
        if over < 0:
            periodLayout["overAmount"] = over
        displayOutput.append(periodLayout)
    return displayOutput
def output():
    inputInformation()
    result= calculation()
    #putting  results in a file
    with open("output.txt", "w") as file:
        for i in range(len(result)):
            file.write(f"Check for {result[i]['check']['name']} on {result[i]['check']['date']} amount {result[i]['check']['amount']}\n")
            for j in range(len(result[i]['bills'])):
                if result[i]['bills'][j]['type'] == "variable/fluctuate":
                    file.write(f"Variable/fluctuate bill {result[i]['bills'][j]['name']} on {result[i]['bills'][j]['date']} amount {result[i]['bills'][j]['amount']} {result[i]['bills'][j]['note']}\n")
                else:
                    file.write(f"Fixed bill {result[i]['bills'][j]['name']} on {result[i]['bills'][j]['date']} amount {result[i]['bills'][j]['amount']} {result[i]['bills'][j]['note']}\n")
            file.write(f"Total bills: {result[i]['totalBills']}\n")
            file.write(f"Over amount: {result[i]['overAmount']}\n")
            file.write("\n")
        file.close()
        print("The information has been saved in output.txt file")
output()