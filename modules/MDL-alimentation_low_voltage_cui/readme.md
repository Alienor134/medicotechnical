# Module
![](viewme.jpg)

## Name
[`MDL-alimentation_low_voltage`]()

## Title
Low voltage (+5v, +3.3v, ...) alimentation

## Description
version      | V1.0  
------------- | -------------  
date     |18/04/2016  
technology|commercial circuit [`PYB30-Q24`](http://www.cui.com/product/resource/pyb30-u.pdf)   
author|BM 

## Functional analysis

### Function 
[`FCT-sensing`](../../functions/FCT-sensing)

### Sub-Function
[`FCT-sensing`](../../functions/FCT-emitting)
[`FCT-sensing`](../../functions/FCT-receiving)
[`FCT-sensing`](../../functions/FCT-sweeping)

### Module requirements
This module will provide the DC alimentation adapted to the electronic circuits different requirements in terms of voltage.

## IOs

### Inputs
* [`ITF-A_gnd`](../../interfaces/ITF-A_gnd)
* [`ITF-L_18v_alimentation`](../../interfaces/ITF-L_18v_alimentation)

### Outputs
* [`ITF-29_5v`](../../interfaces/ITF-29_5v)
* [`ITF-H_neg_12v`](../../interfaces/ITF-H_neg_12v)
* [`ITF-10_gnd`](../../interfaces/ITF-F_12v)

## Visuals
![circuit](/modules/MDL-alimentation_low_voltage_cui/images/circuit1.jpg)  
*scheme*    

## Observations

### pros
9 to 36 Vpp
### cons
price
### constraints
NA
