"""Temperature convertor between Celcius, Fahrenheit and Kelvin"""
# This code is part of a class assignment for ATMS 597, Spring 2020,
# at the University of Illinois at Urbana Champaign.
# Use this class function to convert temperature data from already
# known units to different units.
# It supports conversion to Celcius, Fahrenheit and Kelvin.
import numpy as np


class TempConvert:
    """Temperature convertor for numpy arrays and lists"""

    # mem attribute will keep memory of the input data type
    # Initialized as 0, it will become 1 if list is input
    mem = 0

    def __init__(self, in_temp, unit):
        """Create a temperature object.
        The input is assigned to the object as class instance. Method calls 
        are used to convert to desired units and retrieve output.

        **Arguments:** 

        *in_temp*
            Input temperature. This can be numpy ndarray, list, float, integer,
            or string. Missing values are not permitted.

        *units*
            Input units. The units of temperature must be known,
            and appropriate method be used to convert to desired units.

            Celsius: degC, C, or c

            Fahrenheit: degF, F, or f

            Kelvin: kelvin, K, k
          
        **Returns:**

        *temp*
            A temperature convertor instance

        **Example:**
        
        If in_temp is a numpy ndarray or a list:
            from tempconvert import tempconvert
            temperature = tempconvert(0, 'degC').to('degF')

        """
        # check if the input is a list or numpy array
        if isinstance(in_temp, list):
            # store as a numpy array in an instance variable
            self.__temp = np.asarray(in_temp)
            # change mem to 1
            self.mem = 1

        elif isinstance(in_temp, np.ndarray):
            # store numpy array in an instance variable
            self.__temp = in_temp

        # Check to see if it is an integer
        elif isinstance(in_temp, int):
            # store integer in an instance variable
            self.__temp = in_temp

        # Check to see if it is a float
        elif isinstance(in_temp, float):
            # store float in an instance variable
            self.__temp = in_temp

        elif isinstance(in_temp, str):
            # store float in an instance variable
            self.__temp = float(in_temp)

        else:
            raise Exception('Input not recognized')

        # Bring in the units and assign it to self.units
        self.unit = unit

    def _c2f(self):
        """Convert temperature from Celcius to Fahrenheit.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Fahrenheit.
        
        **Example:**
        
        If in_temp is in degrees Celcius:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).C2F()

        """
        # modify the .__temp attribute of object directly 
        self.__temp = (self.__temp*9/5) + 32
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def _f2c(self):
        """Convert temperature from Fahrenheit to Celcius.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Celcius.

        **Example:**
        
        If in_temp is in degrees Fahrenheit:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).F2C()

        """
        # modify the .__temp attribute of object directly
        self.__temp = (self.__temp-32) * (5/9)
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def _c2k(self):
        """Convert temperature from Celcius to Kelvin.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Kelvin.
        
        **Example:**
        
        If in_temp is in degrees Celcius:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).C2K()

        """
        # modify the .__temp attribute of object directly
        self.__temp = self.__temp + 273.15
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def _k2c(self):
        """Convert temperature from Kelvin to Celcius.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Celcius.
        
        **Example:**
        
        If in_temp is in degrees Kelvin:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).K2C()

        """
        # modify the .__temp attribute of object directly
        self.__temp = self.__temp - 273.15
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def _f2k(self):
        """Convert temperature from Fahrenheit to Kelvin.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Kelvin.
        
        **Example:**
        
        If in_temp is in degrees Fahrenheit:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).F2K()

        """
        # modify the .__temp attribute of object directly
        self.__temp = (self.__temp-32) * (5/9) + 273.15
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def _k2f(self):
        """Convert temperature from Kelvin to Fahrenheit.

        **Returns:**

        *temp*
            A temperature convertor instance, in degrees Fahrenheit.
        
        **Example:**
        
        If in_temp is in degrees Kelvin:
            from tempconvert import tempconvert
            output = tempconvert(in_temp).K2F()

        """
        # modify the .__temp attribute of object directly
        self.__temp = (self.__temp - 273.15) * (9/5) + 32
        # return the same numerical type as the input
        if self.mem > 0:
            return self.__temp.tolist()
        else:
            return self.__temp

    def to(self, out_unit):
        """
        Convert temperature from one unit to another unit defined by the user.

        **Arguments**

        *out_unit*
            Unit that the temperature will be converted to. As a string

        **Returns**

        *Temperature*
            Value of new temperature in same data type as was entered

        """
        # Handle input temperature in Fahrenheit
        if (self.unit == 'degF') or (self.unit == 'F') or (self.unit == 'f'):

            # Check if out_unit is Celsius
            if (out_unit == 'degC') or (out_unit == 'C') or (out_unit == 'c'):
                self.__temp = self._f2c()

            # Check to see if out_unit is Kelvin
            elif (out_unit == 'kelvin') or (out_unit == 'K') or (out_unit == 'k'):
                self.__temp = self._f2k()

            elif (out_unit == 'degF') or (out_unit == 'F') or (out_unit == 'f'):
                self.__temp = self.__temp

        # Handle input temperature in Celsius
        if (self.unit == 'degC') or (self.unit == 'C') or (self.unit == 'c'):

            # Check if out_unit is Celsius
            if (out_unit == 'degC') or (out_unit == 'C') or (out_unit == 'c'):
                self.__temp = self.__temp

            # Check to see if out_unit is Kelvin and convert
            elif (out_unit == 'kelvin') or (out_unit == 'K') or (out_unit == 'k'):
                self.__temp = self._c2k()

            # Check to see if out_unit is Fahrenheit and convert
            elif (out_unit == 'degF') or (out_unit == 'F') or (out_unit == 'f'):
                self.__temp = self._c2f()

        # Handle input temperature in Kelvin
        elif (self.unit == 'kelvin') or (self.unit == 'K') or (self.unit == 'k'):

            # Check if out_unit is Celsius
            if (out_unit == 'degC') or (out_unit == 'C') or (out_unit == 'c'):
                self.__temp = self._k2c()

            # Check to see if out_unit is Kelvin and convert
            elif (out_unit == 'kelvin') or (out_unit == 'K') or (out_unit == 'k'):
                self.__temp = self.__temp

            # Check to see if out_unit is Fahrenheit and convert
            elif (out_unit == 'degF') or (out_unit == 'F') or (out_unit == 'f'):
                self.__temp = self._k2f()

        return self.__temp
