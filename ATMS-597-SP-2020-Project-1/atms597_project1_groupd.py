# ATMS 597 Project 1 Group D
# Authors: Chu-Chun Chen and Michael Sessa

# Import the necessary modules
import numpy as np

# Create a method from which the temperature conversion functions can be called
class tempconvert_class:
    """A method to convert temperatures between
    degrees Celcius, degrees Fahrenheit, and Kelvin"""

    # Convert a user provided temperature from Celcius to Fahrenheit.
    def C2F(self, temp_c):
        if type(temp_c) == list:
            return ([item * 1.8 + 32 for item in temp_c])
        else:
            return temp_c * 1.8 + 32

    # Convert a user provided temperature from Celcius to Kelvin.
    def C2K(self, temp_c):
        if type(temp_c) == list:
            return ([item + 273.15 for item in temp_c])
        else:
            return temp_c + 273.15

    # Convert a user provided temperature from Fahrenheit to Celcius.
    def F2C(self, temp_f):
        if type(temp_f) == list:
            return ([(item - 32) / 1.8 for item in temp_f])
        else:
            return (temp_f - 32) / 1.8

    # Convert a user provided temperature from Fahrenheit to Kelvin.
    def F2K(self, temp_f):
        if type(temp_f) == list:
            return ([(item - 32)/1.8 + 273.15 for item in temp_f])
        else:
            return (temp_f - 32)/1.8 + 273.15

    # Convert a user provided temperature from Kelvin to Celcius.
    def K2C(self, temp_k):
        if type(temp_k) == list:
            return ([item - 273.15 for item in temp_k])
        else:
            return temp_k - 273.15

    # Convert a user provided temperature from Kelvin to Fahrenheit.
    def K2F(self, temp_k):
        if type(temp_k) == list:
            return ([(item - 273.15) * 1.8 + 32 for item in temp_k])
        else:
            return (temp_k - 273.15) * 1.8 + 32

tempconvert = tempconvert_class()  # Initialized instance
tempconvert.C2F  # bound method
tempconvert.C2F([10, 20, 30])  # Example of object-oriented calculation

# Checking the functions
a_list = [10, 20, 30]
print(type(a_list))
print(type(tempconvert.K2F(a_list)))

a_nparray = np.array([10, 20, 30])
print(type(a_nparray))
print(type(tempconvert.K2F(a_nparray)))
