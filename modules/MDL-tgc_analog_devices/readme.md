# Module
![](viewme.jpg)

## Name
[`MDL-tgc_analog_devices`]()

## Title
Time Gain Amplification

## Version
V16.04.12


## Technology
Integrated circuit [`AD8331 EVALZ`](http://www.analog.com/media/en/technical-documentation/evaluation-documentation/154207235AD8331EB_a.pdf)

## Contributor
[`BM`](../../contributors/CTB-bm)  


## Functions  
[`FCT-signal_processing_amplifying_time_gain_compensation`](../../functions/FCT-signal_processing_amplifying_time_gain_compensation)  

## IOs
###Inputs
[`ITF-B_5v`](../../interfaces/ITF-B_5v)  
[`ITF-A_gnd`](../../interfaces/ITF-A_gnd)  
[`IM-C_echo received`](../../interfaces/IM-C_echo_received)  
[`ITF-G_gain_control`](../../interfaces/ITF-G_gain_control) 

### Outputs
[`ITF-C_amplified_raw_signal`](../../interfaces/ITF-C_amplified_raw_signal)  


## Description

### Module requirements 
The living tissues attenuate the acoustic wave that propagates inside them. 
In order to compensate this attenuation the module will amplify the received echoes gradually with the time.


### Observations

#### Pros
high amplification factor accessible  

#### Cons
takes a lot of space (evaluation kit)   
#### Constraints
5V alimenation and a ramp from 0 to 1V to modify the gain of the VGA  


