# Module
![](viewme.jpg)

## Name
[`MDL-alimentation_low_voltage_cui`]()

## Title
Low voltage (+5v, 12V, ...) alimentation

## Version  
V16.04.18  

## Technology

integrated circuit [`PYB30-Q24`](http://www.cui.com/product/resource/pyb30-u.pdf)   

## Author
[`BM`](../../contributors/CTB-bm)  

### Functions 
[`FCT-sensing_emitting`](../../functions/FCT-sensing_emitting)  
[`FCT-sensing_receiving`](../../functions/FCT-sensing_receiving)  
[`FCT-sensing_sweeping`](../../functions/FCT-sensing_sweeping)  
[`FCT-signal_processing_amplifying_time_gain_compensation`](../../functions/FCT-signal_processing_amplifying_time_gain_compensation)  
[`FCT-signal_processing_calculating_pixels`](../../functions/FCT-signal_processing_calculating_pixels)  
[`FCT-signal_processing_envelop_detecting`](../../functions/FCT-signal_processing_envelop_detecting)  
[`FCT-signal_processing_filtering`](../../functions/FCT-signal_processing_filtering)  

## IOs

### Inputs
* [`ITF-A_gnd`](../../interfaces/ITF-A_gnd)  
* [`ITF-L_18v_alimentation`](../../interfaces/ITF-L_18v_alimentation)    

### Outputs
* [`ITF-A_gnd`](../../interfaces/ITF-F_12v)  
* [`ITF-B_5v`](../../interfaces/ITF-29_5v)  
* [`ITF-H_neg_12v`](../../interfaces/ITF-H_neg_12v)    

## Description

### Module requirements
This module will provide the DC alimentation adapted to the electronic circuits' different requirements in terms of voltage.

### Observations

#### Pros
9 to 36 Vpp
#### Cons
price
#### Constraints
NA
