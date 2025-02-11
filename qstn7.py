instances = [
    "nano", "micro", "small", "medium", "large","xlarge", "2xlarge", "4xlarge", "8xlarge", 
    "16xlarge", "32xlarge"
]

currentInstance = input("Enter current Instance : ").lower()
currentCpu = int(input("Enter CPU Utilization : "))

if(currentInstance == "nano" and currentCpu < 20):
    print("sry dude cant do smaller")
if(currentInstance == "32xlarge" and currentCpu >80):
    print("sry dude cant do any larger")
else:
    for i in range (0,len(instances)):
        if(instances[i] == currentInstance):
            ptr = i
    
    if(currentCpu < 20):
        print("StepDown to : " + instances[ptr -1]);
    elif(currentCpu > 80):
        print("StepUp to : " + instances[ptr +1]);
    else:
          print("Current Instance is OK :" + instances[ptr]);  
        