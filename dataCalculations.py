# Homework #2: Big Al's Inventory Problem
#
# (Philip Weinthal)
#
#
carDB = [ [2008,"Toyota","Corolla CE",95990,81000,"gray","N"], [2009,"Ford","F150 King Ranch",189980,120000,"black","Y"], [2010,"Toyota","Corolla S",9599,122000,"gray","N"], [2009,"Toyota","Tacoma PreRunner",82998,66000,"white","Y"], [2009,"Toyota","Prius Touring",93998,67000,"red","Y"], [2009,"Ford","Flex Limited",125990,95000,"white","Y"], [2010,"Honda","CR-V LX",119980,71000,"blue","N"], [2011,"Toyota","RAV4",86998,106000,"white","N"], [2011,"Honda","Fit Sport",95099,95000,"red","Y"], [2012,"Honda","Accord SE",99098,124000,"silver","N"], [2011,"Honda","CR-V LX",120998,71000,"blue","N"], [2009,"BMW","335 I",160998,46000,"gold","N"], [2011,"Toyota","RAV4",129098,78000,"blue","Y"], [2009,"BMW","Cooper Mini",99098,85000,"red","Y"], [2010,"BMW","328 I",14599,76000,"black","N"], [2010,"Toyota","RAV4",150998,27000,"red","N"], [2011,"Toyota","Avalon Limited",140998,65000,"silver","Y"], [2011,"Toyota","Tacoma PreRunner",81998,51000,"white","Y"], [2012,"Toyota","Camry XLE",82599,97000,"green","Y"], [2010,"Mazda","Mazda 3",89980,108000,"gray","N"] ]
#Part One
for i in carDB:
    print("Year built {0:4d}\t Number of Miles {1:7d}\t Manufacturer {2:10s}\t Model {3:16s}\t Price {4:7,d}".format(i[0],i[3],i[1],i[2],i[4]))
#Part Two
count = 0 #Counter
for i in carDB:
    if(i[5] == "red"):
        count += 1 #Basically adds one every time a red car is found
print("You have ", count," red cars.")
#Part Three
count2 = 0
for i in carDB:
    if(i[0] < 2010):
        count2 += 1 #Basically adds one every time a car before 2010 is found
print("You have ", count2," cars from before 2010.")
#Part 4
count3 = 0
hondaType = []
for i in carDB:
    if(i[1] == "Honda"):
        count3 += 1 #Basically adds one every time a honda car is found
        hondaType.append(i[2]) #Basically adds the type to the list every time a honda is found
print("You have ", count3," Hondas. The types are: ", hondaType[0],", ", hondaType[1],", ", hondaType[2],", ", hondaType[3],".")
#Part 5
count4 = 0
manuAndModel = []
for i in carDB:
    if(i[6] == "Y"):
        count4 += 1 #Basically adds one every time a car with SiriusXM is found
        manuAndModel.append("Car {2} Manufacturer {0}, \tModel {1}".format(i[1],i[2],count4)) #Basically adds the manufacturer and type when a car with siriusXM is found
print("You have ", count4," cars with Sirius XM. The Manufacturers and models are: {0}; {1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}; {9}".format(manuAndModel[0],manuAndModel[1],manuAndModel[2],manuAndModel[3],manuAndModel[4],manuAndModel[5],manuAndModel[6],manuAndModel[7],manuAndModel[8],manuAndModel[9]))
#Part 6
count5 = 0
manuAndModel2 = []
for i in carDB:
    if(i[3] > 80000 and i[3] < 90000):
        count5 += 1 #Basically adds one every time a car with between 80000 and 90000 miles on it is found
        manuAndModel2.append("Car {2} Manufacturer {0}, \tModel {1}".format(i[1],i[2],count4))
print("You have ", count5," cars with between 80,000 and 90,000 miles on them. The Manufacturers and models are: {0}; {1}; {2}; {3}; {4}".format(manuAndModel2[0],manuAndModel2[1],manuAndModel2[2],manuAndModel2[3],manuAndModel2[4]))
#Part 7
Has = False
for i in carDB:
    if(i[5] == "green" and i[1] == "Toyota" and i[2] == "Camry XLE" and i[3]<100000):
         Has = True
if Has == True:
    print("You do have the car.")
if Has == False:
    print("You do not have the car.")
#Part 8
for i in carDB:
    resellprice = i[4]
    residualVal = resellprice * 0.57
    depreciationAmount = -residualVal + resellprice
    basePayment = depreciationAmount / (3 * 12)
    rentCharge = (basePayment + residualVal) * 0.00125
    monthlyLeasePayment = rentCharge + basePayment
    ThreeYearLeasePayment = monthlyLeasePayment * (3 * 12)
    print(
        "Manufacturer {0:10s}\t Model {1:10s}\t\t\t How much money a three year lease brings in ${2:9,.2f}\t Monthly lease payment ${3:6.2f}".format(i[1],
                                                                                                                   i[2],
                                                                                                                   ThreeYearLeasePayment,
                                                                                                                   monthlyLeasePayment))
