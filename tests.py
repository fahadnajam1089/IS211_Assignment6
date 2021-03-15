import unittest
from conversions import *
import conversions_refactored

class Temperature_conversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        self.assertAlmostEqual(convertCelsiusToKelvin(300.00), 573.15, places=2, msg="Celsius to  Kelvin conversion failed")
        self.assertAlmostEqual(convertCelsiusToKelvin(1), 274.15, places=2, msg="Celsius to  Kelvin conversion failed")
        self.assertAlmostEqual(convertCelsiusToKelvin(3), 276.15, places=2, msg="Celsius to  Kelvin conversion failed")
        self.assertAlmostEqual(convertCelsiusToKelvin(1000), 1273.15, places=2, msg="Celsius to  Kelvin conversion failed")
        self.assertAlmostEqual(convertCelsiusToKelvin(123), 396.15, places=2, msg="Celsius to  Kelvin conversion failed")

    def test_convertCelsiusToFahrenheit(self):
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300), 572, places=2, msg="Celsius to  Fahernheit conversion failed")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(123), 253.4, places=2, msg="Celsius to  Fahernheit conversion failed")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(200), 392, places=2, msg="Celsius to  Fahernheit conversion failed")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(23), 73.4, places=2, msg="Celsius to  Fahernheit conversion failed")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(12), 53.6, places=2, msg="Celsius to  Fahernheit conversion failed")

    def test_convertFarhenheitToCelsius(self):
        self.assertAlmostEqual(convertFarhenheitToCelsius(100), 37.777, places=2, msg="Fahernheit to Celsius conversion failed")
        self.assertAlmostEqual(convertFarhenheitToCelsius(1), -17.2222, places=2, msg="Fahernheit to Celsius conversion failed")
        self.assertAlmostEqual(convertFarhenheitToCelsius(500), 260, places=2, msg="Fahernheit to Celsius conversion failed")
        self.assertAlmostEqual(convertFarhenheitToCelsius(1000), 537.778, places=2, msg="Fahernheit to Celsius conversion failed")
        self.assertAlmostEqual(convertFarhenheitToCelsius(230), 110, places=2, msg="Fahernheit to Celsius conversion failed")

    def test_convertFarhenheitToKelvin(self):
        self.assertAlmostEqual(convertFarhenheitToKelvin(100.00), 310.928, places=2, msg="Fahernheit to Kelvin conversion failed")
        self.assertAlmostEqual(convertFarhenheitToKelvin(230.00), 383.15, places=2, msg="Fahernheit to Kelvin conversion failed")
        self.assertAlmostEqual(convertFarhenheitToKelvin(15), 263.706, places=2, msg="Fahernheit to Kelvin conversion failed")
        self.assertAlmostEqual(convertFarhenheitToKelvin(20), 266.483, places=2, msg="Fahernheit to Kelvin conversion failed")
        self.assertAlmostEqual(convertFarhenheitToKelvin(156), 342.039, places=2, msg="Fahernheit to Kelvin conversion failed")

    def test_convertKelvinToCelsius(self):
        self.assertAlmostEqual(convertKelvinToCelsius(230), -43.15, places=2, msg="Kelvin to Celsius conversion failed")
        self.assertAlmostEqual(convertKelvinToCelsius(273.15), 0, places=2, msg="Kelvin to Celsius conversion failed")
        self.assertAlmostEqual(convertKelvinToCelsius(1000), 726.85, places=2, msg="Kelvin to Celsius conversion failed")
        self.assertAlmostEqual(convertKelvinToCelsius(500), 226.85, places=2, msg="Kelvin to Celsius conversion failed")
        self.assertAlmostEqual(convertKelvinToCelsius(300), 26.85, places=2, msg="Kelvin to Celsius conversion failed")


    def test_convertKelvinToFarhenheit(self):
        self.assertAlmostEqual(convertKelvinToFarhenheit(300), 80.33, msg="Kelvin to Farhenheit conversion failed")
        self.assertAlmostEqual(convertKelvinToFarhenheit(1000), 1340.33, msg="Kelvin to Farhenheit conversion failed")
        self.assertAlmostEqual(convertKelvinToFarhenheit(500), 440.33, msg="Kelvin to Farhenheit conversion failed")
        self.assertAlmostEqual(convertKelvinToFarhenheit(56), -358.87, msg="Kelvin to Farhenheit conversion failed")
        self.assertAlmostEqual(convertKelvinToFarhenheit(400), 260.33, msg="Kelvin to Farhenheit conversion failed")

    def test_convert(self):
        fromUnit = 'Meters'
        toUnit = 'Kelvin'
        value = 300
        expected = 573.15
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to  Kelvin conversion failed")
        fromUnit = 'Celsius'
        toUnit = 'Fahrenheit'
        value = 300
        expected = 572
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to  Fahrenheit conversion failed")
