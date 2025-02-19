# planner equal {
#     peopleNum: “ ”,
#     peopleArray : [ ],
#     totalBills: “ ”,
#     vfBillNum: “ ”,
#     vfBillArray: [ ],
#     fixedBillNum: “ ”,
#     fixedBillArray: [ ]
# }
#
# Function input ()
#     Ask user to enter how many people are paying bills
#     Store input into planner.peopleNum
#
#     if planner.peopleNum is greater than 1
#         For loop with length based on planner.peopleNum
# personInfo equal { name: “ ”, checkDate: “ ”, checkAmount:“ ”, futurePeriods: [ ] }
#             Ask User to enter person[i + 1] name
#             Store input in personInfo.name
#             Ask User to enter the date when person[i + 1] got their last paid check (personInfo.name)
#             Store input in personInfo.checkDate
#             Ask User to enter the amount of person[i + 1]’s check (personInfo.name)
#             Store input in personInfo.checkAmount
#             personInfo will be pushed to planner.peopleArray
#     else
#         personInfo equal { name: “ ”, checkDate: “ ”, checkAmount:“ ”, futurePeriods: [ ] }
#         Ask User to enter their name
#         Store input in personInfo.name
#         Ask User to enter the date when they got their last paid check
#         Store input in personInfo.checkDate
#         Ask User to enter the amount of check
#         Store input in personInfo.checkAmount
#         personInfo will be pushed to planner.peopleArray
#
#     Ask user to enter the number of bills
#     Store input to planner.totalBills
#
#     Ask User if they have any variable/fluctuate bills (yes or no)
#     Store input in answerVfBills
#
#     if answerVfBills equal yes
#         Ask user to enter the number of variable/fluctuate bills
#         Store input in planner.vfBillNum
#         For loop with length based on planner.vfBillNum
#             billInfo equal { name: “ ”, billDate: “ ”, billAmount:“ ”, futurePeriods: [ ] }
#             Ask User to enter variable/fluctuate bill[i + 1] name
#             Store input in billInfo.name
#             Ask User to enter the date of their last due date for this bill (billInfo.name)
#             Store input in billInfo.billDate
#             Ask User to enter the estimated amount of bill (billInfo.name)
#             Store input in billInfo.billAmount
#             billInfo will be pushed to planner.vfBillArray
#     else
#         Store 0 in planner.vfBillNum
#
#     planner.fixedBillNum equal planner.totalBills minus planner.vfBillNum
#     For loop with length based on planner.fixedBillNum
#         billInfo equal { name: “ ”, billDay: “ ”, billAmount:“ ”, futurePeriods: [ ] }
#         Ask User to enter fixed bill[i + 1] name
#         Store input in billInfo.name
#         Ask User to enter the day of the month this bill is due (billInfo.name)
#         Store input in billInfo.billDay
#         Ask User to enter the estimated or exact amount of bill (billInfo.name)
#         Store input in billInfo.billAmount
#         billInfo will be pushed to planner.fixedBillArray
#
# Function calculation()
# For loop with length based on planner.peopleArray
#         For loop with length 26
#             nextPeriod equal “ ”
#             previous equal nextPeriod not equal “ ” or planner.peopleArray[i].checkDate
#             futureDate equal previous plus 2 weeks (14 days)
#             push futureDate to planner.peopleArray[i].futurePeriods
#             nextPeriod equal futureDate
#
#     For loop with length based on planner.fixedBillNum
#         todayMonth equal get today month
#         todayYear equal get today year
#         standardBillDate equal todayMonth plus planner.fixedBillArray[i].billDay plus todayYear
#         push standardBillDate to planner.fixedBillArray[i].futurePeriods
#         For loop with length 11
#             nextPeriod equal “ ”
#             current equal nextPeriod not equal “ ” or standardBillDate
#             futureBillDate equal current plus 30 days
#             push futureBillDate to planner.fixedBillArray[i].futurePeriods
#             nextPeriod equal futureBillDate
#
#     For loop with length based on planner.vfBillNum
#         lastDate equal planner.vfBillArray[i].billDate
#         For loop with length 11
#             range equal {min: “ ”, middle: “ ” , max: “ ” }
#             nextDate equal “ ”
#             currentDate equal nextDate not equal “ ” or lastDate
#             middleDate equal currentDate plus 30 days
#             range.middle equal middleDate
#             minDate equal middleDate minus 2 days
#             range.min equal minDate
#             maxDate equal middleDate plus 8 days
#             range.max equal maxDate
#             push range to planner.vfBillArray[i].futurePeriods
#             nextDate equal middleDate
#
#     allChecks equal [ ]
#     For loop based on planner.peopleArray
#         For loop based on planner.peopleArray[i].futurePeriods
#             checkLayout equal { name: “ ”, date: “ ”, amount: “ ”}
#             checkLayout.name equal planner.peopleArray[i].name
#             checkLayout.date equal planner.peopleArray[i].futurePeriods[j]
#             checkLayout.amount equal planner.peopleArray[i].amount
#             push checkLayout to allChecks
#
#     organizedChecks equal allChecks sort by earlier date
#
#     allBills equal [ ]
#     For loop based on planner.fixedBillArray
#         For loop based on planner.fixedBillArray[i].futurePeriods
#             billLayout equal { name: “ ”, date: “ ”, amount: “ ”, type: “fixed” }
#             billLayout.name equal planner.fixedBillArray[i].name
#             billLayout.date equal planner.fixedBillArray[i].futurePeriods[j]
#             billLayout.amount equal planner.fixedBillArray[i].amount
#             push billLayout to allBills
#     For loop based on planner.vfBillArray
#         For loop based on planner.vfBillArray[i].futurePeriods
#             billLayout equal { name: “ ”, date: {}, amount: “ ”, type: “variable/fluctuate” }
#             billLayout.name equal planner.vfBillArray[i].name
#             billLayout.date equal planner.vfBillArray[i].futurePeriods[j]
#             billLayout.amount equal planner.vfBillArray[i].amount
#             push billLayout to allBills
#
#     organizedBills equal allBills sort by earliest date
#
#     displayOutput equal [ ]
#     For loop with length based on organizedChecks
#         totalBillAmount equal 0
#         maxAmount equal organizedChecks[i].amount
#         periodLayout equal {check: {name: “ ”, date: “ ”, amount: “ ”}, bills: [ ], totalBills:“ ”, overAmount: “ ”}
#         periodLayout.check.name equal organizedChecks[i].name
#         periodLayout.check.date equal organizedChecks[i].date
#         periodLayout.check.amount equal organizedChecks[i].amount
#
#         For loop with length based on organizedBills
#             fixedbillDetail equal {name: “ ”, date: “ ”, amount: “ ”, type: “Fixed”, note:“ ”}
#             vfBillDetail equal {name: “ ”, date:{}, amount: “ ”, type:“variable/fluctuate”, note:“ ”}
#             if organizedBills[j].type equal “variable/fluctuate”
#                 compareDate equal organizedBills[j].date.min
#                 if compareDate is greater or equal to organizedChecks[i].date and is less than organizedChecks[i + 1].date
#                     vfBillDetail.name equal to organizedBills[j].name
#                     vfBillDetail.date equal to organizedBills[j].date
#                     vfBillDetail.amount equal to organizedBills[j].amount
#                     if organizedBills[j].amount is greater than or equal to half of organizedChecks[i].Amount
#                         vfBillDetail.note equal to “this bill will take all or most of your check, you will have to split this amount in smaller chunks”
#                         push vfBillDetail to periodLayout.bills
#                     else
#                         totalBillAmount + organizedBills[j].amount
#                         push vfBillDetail to periodLayout.bills
#             else
#                 if organizedBills[j].date is greater or equal to organizedChecks[i].date and is less than organizedChecks[i + 1].date
#                     fixedbillDetail.name equal to organizedBills[j].name
#                     fixedbillDetail.date equal to organizedBills[j].date
#                     fixedbillDetail.amount equal to organizedBills[j].amount
#                     if organizedBills[j].amount is greater than or equal to half of organizedChecks[i].Amount
#                         fixedbillDetail.note equal to “this bill will take all or most of your check, you will have to split this amount in smaller chunks”
#                                            push fixedbillDetail to periodLayout.bills
#                     else
#                     totalBillAmount + organizedBills[j].amount
#                     push fixedbillDetail to periodLayout.bills
#       push totalBillAmount to periodLayout.totalBills
#        over equal maxAmount minus totalBillAmount
#        if over is less than 0
#            push over to periodLayout.overAmount
#        push periodLayout to displayOutput
#Main function
#  Call input ()
#  Call calculation()
#    create a file and store displayOutput in file and design the format of how to display the information
#    output the results
#
#