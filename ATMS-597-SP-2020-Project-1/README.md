# ATMS-597-SP-2020-Project-1
Project 1 for ATMS 597 SP 2020.

## Description 
This project provides an object-oriented python module that converts temperatures interchangeably between degrees Celsius, Fahrenheit, and Kelvin.

## Usage
*  Choose the proper function for the temperature conversion. For instance, if the user wants to convert Celsius to Kelvin, the user should use `tempconvert.C2K(temp_c)`.
*  Input a list or a numpy array of temperatures. String, tuple, or other types of input are not supported now.
*  Run the code, and the code will return the converted temperature in the same numerical type. Temperatures may be input as integers or floats, but note that floats will always be returned.
*  Optionally, with tempconvert.py, the temperatures are constrained above abosolut zero. One can remove the constraint via `tempconvert(temp, regularized = False).C2K()`.

## Authors and acknowledgment
Group D: Chu-Chun Chen, Michael Sessa, Yang Lu

The code was originally forked from the repository swnesbitt/ATMS-597-SP-2020 by Chu-Chun Chen.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details
