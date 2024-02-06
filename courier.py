# a program to figure out the price to deliver a package
# first we ask the user a bunch of options to consider

price_of_package = input("please enter the price of the package you would like to purchase: ")
distance = input("please enter the total distance of the delivery in kilometres" )
type_of_delivery = input("would you like to send by air or freight? a/f ")
insurance = input("would you like full or limited insurance? f/l ")
gifting = input("would you like gift or no gift? g/n")
speed_of_delivery = input("would you like priority or standard delivery? p/s ")

# we are using if statements to try all the different combinations
if type_of_delivery == "a" and insurance == "f" and gifting == "g" and speed_of_delivery == "p":
    total_price = float(price_of_package) + 50 + 15 + 100 + float(distance) * 0.36
elif type_of_delivery == "a" and insurance == "l" and gifting == "g" and speed_of_delivery == "p":
    total_price = float(price_of_package) + 25 + 15 + 100 + float(distance) * 0.36
elif type_of_delivery == "a" and insurance == "f" and gifting == "n" and speed_of_delivery == "p":
    total_price = float(price_of_package) + 50 + 100 + float(distance) * 0.36
elif type_of_delivery == "a" and insurance == "f" and gifting == "g" and speed_of_delivery == "s":
    total_price = float(price_of_package) + 50 + 15 + 20 + float(distance) * 0.36
elif type_of_delivery == "f" and insurance == "f" and gifting == "g" and speed_of_delivery == "p":
    total_price = float(price_of_package) + 50 + 15 + 100 + float(distance) * 0.25
elif type_of_delivery == "f" and insurance == "l" and gifting == "g" and speed_of_delivery == "p":
    total_price = float(price_of_package) + 25 + 15 + 100 + float(distance) * 0.25
elif type_of_delivery == "f" and insurance == "f" and gifting == "n" and speed_of_delivery == "p":
    total_price = float(price_of_package) + 50 + 100 + float(distance) * 0.25
elif type_of_delivery == "f" and insurance == "f" and gifting == "g" and speed_of_delivery == "s":
    total_price = float(price_of_package) + 50 + 15 + 20 + float(distance) * 0.25
elif type_of_delivery == "f" and insurance == "l" and gifting == "n" and speed_of_delivery == "s":
    total_price = float(price_of_package) + 25 + 20 + float(distance) * 0.25
elif type_of_delivery == "f" and insurance == "l" and gifting == "n" and speed_of_delivery == "p":
    total_price = float(price_of_package) + 25 + 100 + float(distance) * 0.25
elif type_of_delivery == "f" and insurance == "f" and gifting == "n" and speed_of_delivery == "s":
    total_price = float(price_of_package) + 50 + 20 + float(distance) * 0.25
elif type_of_delivery == "f" and insurance == "l" and gifting == "n" and speed_of_delivery == "s":
    total_price = float(price_of_package) + 25 + 20 + float(distance) * 0.25
elif type_of_delivery == "a" and insurance == "l" and gifting == "n" and speed_of_delivery == "s":
    total_price = float(price_of_package) + 25 + 20 + float(distance) * 0.36
elif type_of_delivery == "a" and insurance == "l" and gifting == "g" and speed_of_delivery == "s":
    total_price = float(price_of_package) + 25 + 15 + 20 + float(distance) * 0.36
elif type_of_delivery == "a" and insurance == "l" and gifting == "n" and speed_of_delivery == "p":
    total_price = float(price_of_package) + 25 + 100 + float(distance) * 0.36
elif type_of_delivery == "a" and insurance == "f" and gifting == "n" and speed_of_delivery == "s":
    total_price = float(price_of_package) + 50 + 20 + float(distance) * 0.36

print(total_price)