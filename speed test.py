import speedtest

sd = speedtest.Speedtest()

user = int(input("Welcome to the speed test program \nPleaseSelect the given option:-\n1 = Downlaod speed \n2 = Upload speed \n"))

if user == 1:  
  
    print("Your Downlaod speed is : ",sd.download())  
  
elif user == 2: 
  
    print("Your upload speed is : ",sd.upload()) 
else:
    print("Enter the correct values")    