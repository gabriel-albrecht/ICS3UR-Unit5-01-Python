#!/usr/bin/env python3

# Created by Gabriel A
# Created on Dec 2020
# This program converts celcius to fahrenheit


def fahrenheit():
    # calculate celcius to fahrenheit

    try:
        # input
        celcius = float(input("Enter the temperature in celcius: "))
        print("")

        fahrenheit = (9 / 5) * celcius + 32

        # output
        print("{0}ºc is {1}ºf".format(celcius, fahrenheit))

        if celcius < -273.15:
            print("")
            print("*this temperature is impossible.")

    except ValueError:
        print("")
        print("That is not a number.")


def main():
    fahrenheit()
    # calls functions

if __name__ == "__main__":
    main()
