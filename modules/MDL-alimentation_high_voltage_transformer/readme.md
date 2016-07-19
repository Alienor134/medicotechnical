# Module
![](viewme.png)

## Name
[`MDL-alimentation_high_voltage_transformer`]()

## Title
High voltage (-100V) alimentation

## Description

version      | VX.X  
------------- | -------------  
date     |XX/XX/20XX  
technology|hand made  
author|Farad  

## Functions
Function: [`FCT-sensing`](../../functions/FCT-sensing)  
Sub-Function:  [`FCT-emitting`](../../functions/FCT-emitting)  

## IOs
###Inputs
[`ITF-F_12v`](../../interfaces/ITF-B_5v)  

### Outputs
[`ITF-T_100v`](../../interfaces/ITF-T_100v)  

## Visuals
![circuit](/modules/MDL-alimentation_high_voltage_transformer/images/scheme_transfo.PNG)  
*circuit*    

## Observations

### pros
NA
### cons
NA
###constraints
alternative signal (square) 15 Vpp (+7.5 to -7.5)

## Discussions
A Transformer has been found. It has been taken from a system that can transform 230V to 12V. The aim is to transform 5V to 100V (Figure 1):  
![circuit](/modules/MDL-alimentation_high_voltage_transformer/images/transfo2.jpg)  

![circuit](/modules/MDL-alimentation_high_voltage_transformer/images/transfo1.jpg)  
*Figure 1: Transformer*  

Several tests on the transformer show that it could be used as an elevator for our system. The inductance of the coil inside the transformer has been calculated using the formula :  

F0 = 1/(2*pi*sqrt(LC))  
sqrt(LC) = 1/(2*pi*F0)  
L = 1/((2*pi*F0)^2 *C)  
Using the frequency generator to sweep the frequency, the resonnance frequency (F0) could be found. With a serie capacitor of 4.7 nF L1 = 11.13mH (F0 = 26 kHz) and L2 = 31.89 mH (F0 = 13 kHz) The elevation has a max tension at 13 kHz. A frequency generator has been used to determine this value (saw Figure 4). The Tension has been fixed to 15Vpp with a square signal at 13kHz.  

![circuit](/modules/MDL-alimentation_high_voltage_transformer/images/scheme2_transfo.PNG)  
![circuit](/modules/MDL-alimentation_high_voltage_transformer/images/unloaded.jpg)  
*Figure 2: Results: Tension Measurement of the elevation without load resistance*  

#### Input/Output: 
**input**: Oscillation: 
To create an oscillating circuit, the LM555 component has been chosen. The oscillation need to have the follow characteristics:  

15 Vpp (+7.5 to -7.5)  
square signal at 13kHz  
Duty Cycle around 50%  
The Figure 5 show the schema of the oscillating circuit with these characteristics:  

![circuit](/modules/MDL-alimentation_high_voltage_transformer/images/scheme3_transfo.PNG)  
![circuit](/modules/MDL-alimentation_high_voltage_transformer/images/square.jpg)  

*Figure 3 : Oscillating circuit and the output of the 555 component*  

**Observation** :  

With 12V from the generator, we find 130V  
Current loss is fixed using a coil between the alimentation and the transistor and by putting a capacitor between the transistor and the transformer  
Elevation and voltage rectification  

The Elevation requiers a transistor (a mosfet is used) to drive the power from the alimentation. The circuit is shown below:  

![circuit](/modules/MDL-alimentation_high_voltage_transformer/images/scheme_transfo.png)  
*Figure 4 : High Tension Generator*  

The multimeter shows :

![circuit](/modules/MDL-alimentation_high_voltage_transformer/images/loaded.jpg)  
*Figure 5: Result of the power circuit*  

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

