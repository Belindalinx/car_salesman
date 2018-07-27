car_price=int(input("What's your car price?"))
car_tax=int(car_price)*0.2
car_license=int(car_price)*0.1
car_dealer_prpe=int(5000)
car_destination_charge=int(2000)
OTD=car_price+car_tax+car_license+car_dealer_prpe+car_destination_charge

print("Tax of car : ",car_tax)
print("License of car : ",car_license)
print("Dealer prpe of car : ",car_dealer_prpe)
print("Destination charge of car : ",car_destination_charge)
print("Out the door price",OTD)