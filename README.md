# RaspberryPiTutorial-1
Basic Tutorial To Demonstrate Using Github To Get Code to a Raspberry Pi

This tutorial is used to demonstrate how to push code from a development laptop onto a Raspberry Pi using github.
This satisfies two objectives:
* learn how to git clone a repo onto a Raspberry Pi
* Introduce the code concepts to use the [Gpiozero](https://gpiozero.readthedocs.io/en/stable/#) library to drive a [simple circuit](https://gpiozero.readthedocs.io/en/stable/recipes.html#led) from a Raspberry Pi

Simple Instructions:
* From you Raspberry Pi issue the following commands:
```
git clone https://github.com/JohnFunkCode/RaspberryPiTutorial-1.git
```
* to run the code issue the following commands:
```
cd RaspberryPiTutorial-1
python3 blinkled.py
```
