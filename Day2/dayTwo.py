


temperature = float(input("Enter the current temperature in Fahrenheit:"))
is_raining = ("it is currently raining? (yes/no)").lower()



   
if temperature < 50:
    print("were coat, hat, scarf, and gloves")
elif 50<= temperature  <=70:
 if is_raining:
    print(" wear a sweater or light jacket.")
 else:
    print("wear jacket and boots")


elif temperature >= 70:
    if is_raining:
        print("wear a t-shirt and shorts")   
    else:
       print("wear a light jacket and rain boots.")    
