while True:
     print("""Menu for conversion:
1.Lenght
2.Weight
3.Temperature """)
     choice = input("Enter your choice: ")
     if choice == "1":
          while True:
               len = input("Enter the value: ")
               if float(len) < 0:
                    print("Please enter positive value.")
               else:
                    break
          len_unit = input("""Enter the unit: 
'm' for 'meters'
'km' for 'kilometers'
: """)
          if len_unit == "m":
               print(f"The length in kilometer is: {format(float(len) / 1000, '.2f')} kilometers.")
          elif len_unit == "km":
               print(f"The length in meters is: {format(float(len) * 1000, '.2f')} meters.")
          else:
               print("Enter valid option.")
     elif choice == "2":
          while True:
               wei = input("Enter the value: ")
               if float(wei) < 0:
                    print("Please enter positive value.")
               else:
                    break
          wei_unit = input("""Enter the unit: 
'g' for 'grams'
'kg' for 'kilograms'
: """)
          if wei_unit == "g":
               print(f"The weight in kilograms is: {format(float(wei) / 1000, '.2f')} kilograms.")
          elif wei_unit == "kg":
               print(f"The weight in grams is: {format(float(wei) * 1000, '.2f')} grams.")
          else:
               print("Enter valid input.")
     elif choice == "3":
          temp = input("Enter the value: ")
          temp_unit = input("""Enter the unit:
'C' for Celsius 
'F' for Fahrenheit
:""")
          if temp_unit == "C":
               print(f"The temperature in deg F is: {format(float(temp) * 9/5 + 32, '.2f')} °F.")
          elif temp_unit == "F":
               print(f"The temperature in deg C is: {format((float(temp) - 32) * 5 / 9, '.2f')} °C")
          else:
               print("Enter valid option.")
     elif choice == "":
          break
     else:
          print("Enter appropriate choice.\n")
