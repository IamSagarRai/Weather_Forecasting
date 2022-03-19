import requests

cn = input("Enter the city name: \n")
print("Initializing the location of the city " + cn+"...")

urL = 'http://wttr.in/{}'.format(cn) # --> Passing city as a parameter through .format function
rP = requests.get(urL)
print(rP.text)

