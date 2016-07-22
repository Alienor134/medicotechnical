# Module
![](viewme.jpg)  

## Name
[`MDL-pulser_home_made`]()  

## Title
Pulser producing a high voltage (-100v) pulse

## Version
V16.04.12  

## Technology
Echopen Made 
 
## Author
[`Gérard`](../../contributors/CTB-gerard)  
[`Michel`](../../contributors/CTB-michel) 

## Functions
[`FCT-sensing_emitting`](../../functions/FCT-sensing_emitting)  

## IOs

###Inputs
[`ITF-F_12v`](../../interfaces/ITF-F_12v)  
[`IM_A_100v`](../../interfaces/IM-A_100v)  
[`ITF-I_pulse_on`](../../interfaces/ITF-I_pulse_on)  
[`ITF-J_pulse_off`](../../interfaces/ITF-J_pulse_off)  

### Outputs
[`IM_B_100v_pulse`](../../interfaces/IM_B_100v_pulse)  

## Description

### Module requirements
This module will provide a high voltage analogic pulse that will excite the transducer.

### Visuals
![circuit](/modules/MDL-pulser_home_made/images/scheme.jpg)  
*circuit*    

### Observations

#### Pros
NA

#### Cons
The pulse can be smaller (in time) than the logic pusle due to self effect of the cable going to the transducer
It worked perfectly on the initial board though.  
![board](/modules/MDL-pulser_home_made/images/board.jpg)

#### Constraints
Need 12V alimentation for the MOSFET
 

