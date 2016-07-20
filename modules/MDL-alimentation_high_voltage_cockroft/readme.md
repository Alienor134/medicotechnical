# Module
![](viewme.png)

## Name
[`MDL-alimentation_high_voltage_cockroft`]()

## Title
High voltage (-100V) alimentation

## Description

version      | V1.0  
------------- | -------------  
date     |11/04/2016  
technology|hand made  
author|Jérôme/Gérard  

## Functional analysis

### Function [`FCT-sensing`](../../functions/FCT-sensing)  

### Sub-Function  [`FCT-emitting`](../../functions/FCT-emitting)  

### Module requirements 
This module will provide a high voltage negative DC in order to increase the pulse voltage to exite efficiently the transducer.

## IOs
###Inputs
[`ITF-B_5v`](../../interfaces/ITF-B_5v)  
[`ITF-L_18v alimentation`](../../interfaces/ITF-L_18v_alimentation)  

### Outputs
[`ITF-T_100v`](../../interfaces/ITF-T_100v)  


## Visuals
![circuit](/modules/MDL-alimentation_high_voltage_cockroft/images/scheme2_cockroft.png)  
*circuit*    
![circuit](/modules/MDL-alimentation_high_voltage_cockroft/images/scheme_cockroft.jpg)  
*square alimentation 0-18V*

## Observations

###pros
low electromagnetic scatterred field  
###cons
low intensity  
###constraints
alternative signal (square) 0 to -15V input




