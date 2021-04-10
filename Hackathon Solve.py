import time

"""
Heart rate
Breath rate
Blood Pressure
Blood Flow
Blood levels
Temperature

"""






Age = int(input("Age: "))

heartRate = float(input("Heart rate (beats/min): ")) #heart rate

breathRate = float(input("breath Rate (pumps/min): ")) #Breath rate

BloodPressure = float(input("Blood Pressure (systolic): ")) #Blood pressure

Bloodflow = float(input("Blood flow (mL/min): ")) #Blood Flow

BloodLevels = float(input("Blood Level (mL): ")) #Blood levels

Temp = float(input("Temperature (F): ")) #Temp






if heartRate == 0 or heartRate < 60:
    x = "Dead"

if heartRate > 110:
    x = "Hos"

if heartRate > 60 and heartRate <110:
    x = "home"

if Temp > 100:
    x = "Hos"

if Temp < 100 and Temp > 95:
    x = "home"


print("\n")


print("Hmm...")
time.sleep(1)
print("(The computer is thinking)")
time.sleep(5)
print("\n")
print("AHA!")
time.sleep(1)
print("I found it!")
time.sleep(1)
print("\n\n")





if x == "Dead":
    print("Unfortunatley, the person is dead.")

if x == "home":
    print("The person is healthy and can go home!")

if x == "Hos":
    print("I think the person may need to stay in the hospital for a bit longer...")
    print("(He/she is sick)")


