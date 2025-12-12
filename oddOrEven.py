def oddOrEven():  # Function that returns if a number is even or odd
    while True:
        try:  # The try except allows to prompt an error when the user's input is not a number.
            userInput = input(
                'Enter an integer number to check if it is even or odd, or press "q" to quit: ')
            if userInput.lower() == 'q':
                print('Bye!')
                break  # Breaks the loop

            # Casting from string to number to do the calculation below# Casting from string to number to do the calculation below
            userInput = int(userInput)
            if userInput % 2 == 0:  # If dividing the number by 2 the remainder is 0:
                print(userInput, 'is even')
            else:
                print(userInput, 'is odd')
        except ValueError:  # This prints on screen when the input is not a number.
            print('Invalid input. Enter a valid integer.')


if __name__ == "__main__":
    print('ODD OR EVEN?')
    oddOrEven()
