# Module
<img src="https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/ioscheme.PNG" width="400">

## Name
[`MDL-alimentation_high_voltage`]()

## Title
High voltage (-100V) alimentation

## Description
We need a high voltage negative pulse in order to exite efficiently the transducer.

##Inputs/Outpouts
input: depends on the solution  
output: -100V DC

## Uses
[`ITF-10_gnd`](../../interfaces/ITF-10_gnd)

## Functions
Function: [`FCT-sensing`](../../functions/FCT-sensing)  
Sub-Function:  [`FCT-emitting`](../../functions/FCT-emitting)

##Solutions: 

### Cockroft-Walton multiplier

version      | V1.0  
------------- | -------------  
date     |11/04/2016  
technology|home made  
author|Jérôme/Gérard  

#### Visuals:
<img src="https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/scheme_V1.0.png" width="400">  
*scheme*  
<img src="https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/circuit_V1.0.JPG" width="400">  
*electronic circuit*

#### Testing:

##### protocol:
##### results:

![](doc/images/results_V1.0.jpg)
*results*

#### Input/Output: 
**input**: alternative signal (square) 0 to -15V  
**output**: -100V DC

#### Pros/Cons/Constraint:
**pros**: low electromagnetic scatterred field  
**cons**: low intensity  
**constraint**: alternative signal (squarre) 0 to -15V  



### DC/DC Converter

version      | V1.1  
------------- | -------------  
date     |18/04/2016  
technology|integrated circuit  
author|BM  

#### Scheme
<img src="https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/scheme_V1.1.png" width="400">  
*scheme*  
<p align="center"><img src="https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/circuit_V1.1.JPG" width="400"></p>  
*electronic circuit*  

[Fiche du fournisseur](http://www.digikey.fr/product-detail/fr/recom-power/R05-100B/945-2051-5-ND/3776798)
#### Testing:

##### protocol:
##### results:

![](doc/images/results_V1.1.jpg)
*results*

####Input/Output: 
**input**: R05-100B 5V, higher 12V  
**output**: +/-50 to 150V DC

#### Pros/Cons/Constraint:
**pros**: variable output  
**cons**: price  
**constraint**: 5V or 12V power supply

### Transformer

version      | V1.2  
------------- | -------------  
date     |XX/XX/201X  
technology|home made  
author|Farad  

A Transformer has been found. It has been taken from a system that can transform 230V to 12V. The aim is to transform 5V to 100V (Figure 1):  
<img src="https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/circuit1_V1.2.jpg" width="400">  

<img src="https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/circuit2_V1.2.jpg" width="400">  
*Figure 1: Transformer*  

Several tests on the transformer show that it could be used as an elevator for our system. The inductance of the coil inside the transformer has been calculated using the formula :  

F0 = 1/(2*pi*sqrt(LC))  
sqrt(LC) = 1/(2*pi*F0)  
L = 1/((2*pi*F0)^2 *C)  
Using the frequency generator to sweep the frequency, the resonnance frequency (F0) could be found. With a serie capacitor of 4.7 nF L1 = 11.13mH (F0 = 26 kHz) and L2 = 31.89 mH (F0 = 13 kHz) The elevation has a max tension at 13 kHz. A frequency generator has been used to determine this value (saw Figure 4). The Tension has been fixed to 15Vpp with a square signal at 13kHz.  

![](https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/scheme1_V1.2.PNG)
![](https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/results1_V1.2.jpg)  
*Figure 2: Results: Tension Measurement of the elevation without load resistance*  

#### Input/Output: 
**input**: Oscillation: 
To create an oscillating circuit, the LM555 component has been chosen. The oscillation need to have the follow characteristics:  

15 Vpp (+7.5 to -7.5)  
square signal at 13kHz  
Duty Cycle around 50%  
The Figure 5 show the schema of the oscillating circuit with these characteristics:  

![](https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/input1_V1.2.PNG)
![](https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/input2_V1.2.jpg)  
*Figure 3 : Oscillating circuit and the output of the 555 component*  

**Observation** :  

With 12V from the generator, we find 130V  
Current loss is fixed using a coil between the alimentation and the transistor and by putting a capacitor between the transistor and the transformer  
Elevation and voltage rectification  

The Elevation requiers a transistor (a mosfet is used) to drive the power from the alimentation. The circuit is shown below:  

![](https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/input3_V1.2.PNG)  
*Figure 6 : High Tension Generator*  

The multimeter shows :

![](https://github.com/Alienor134/medicotechnical/blob/master/modules/MDL-alimentation_high_voltage/doc/images/input4_V1.2.jpg)  
*Figure 7: Result of the power circuit*  

The coil has to be choosen with this formula:  
Ipeak = (Vsupply * DutyCycle) / L  

The recitification has to follow the formula:  
C = I/(deltaV * F)  
with deltaV the admissible variation of the tension  
F the fréquency of the alternative tension from the transformer  
C the rectification capacitor  
I the current from the transformer  

**Numerical Application**:  
F = 10kHz, I = 10mA and deltaV = 1V  
C = 1µF  

**Observation**:  
The transformer is noisy  
A power resistance is required  
C6 capacitor is needed to reduce the loss inductance and make the signal symmetric

