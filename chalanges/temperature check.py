raining = True
haveUmbrella = True
temperature = 9
if temperature >= 40 or temperature <= 0:
    print("Extreme temperature, stay at home")
elif temperature >0 and temperature <10 and haveUmbrella and raining:
    print("It's cold but you can go out with your umbrella")
elif not raining and temperature >= 10:
    print("It's a nice day, you can go out")
else:    print("It's not a good day, stay at home")