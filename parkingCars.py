import os

lots = [] #list of car license plates
spots = 10 #number of parking spaces

#addCar - add a car in the lots list
def addCar():
  plate = input('Enter the license plate:')
  lots.append(plate)
  clearScreen()

#leaveCar - remove a specific car in the lots list
def leaveCar():
  plate = int(input('Enter the Lot number:'))
  lots.pop(plate-1)
  clearScreen()
  listCar()

#listCar - display a list of registered cars
def listCar():
  clearScreen()
  for lot, plate in enumerate(lots):
     print(f"Lot: {lot+1} - Car: {plate}")

#clearScreen - clear the prompt
def clearScreen():
  os.system('cls' if os.name == 'nt' else 'clear')

while len(lots) < spots:
  print(f"We still have {spots - len(lots)} lots!") 

  option = int(input('Enter [1] to parking / [2] to release lot / [3] to list: '))

  if option == 1:
    addCar()
  elif option == 2:
    leaveCar()
  elif option == 3:
    listCar()
  else:
    clearScreen()
    print('Invalid option! :(')
