# Module
![](viewme.jpg)

## Name
[`MDL-band_pass_filter_opamp`]()

## Title
Band-pass filter

## Version
V1.1  

## Date
18/04/2016  

## Technology
Home made using [`OPA625`](www.ti.com/product/OPA625)
 
## Contributor
[`BM`](../../contributors/CTB-BM)  

## Functions
[`FCT-sensing_emitting`](../../functions/FCT-sensing_emitting)  

## IOs

###Inputs
[`ITF-C_amplified_raw_signal`](../../interfaces/ITF-C_amplified_raw_signal)  
Supply voltage for opamps

### Outputs
[`ITF-D_amplified_filtered_signal`](../../interfaces/ITF-D_amplified_filtered_signal)  

## Description

### Module requirements
This module will filter the noise from the raw signal coming out of the TGC.

### Visuals
![circuit](/modules/MDL-band_pass_filter_rcl/images/scheme.jpg)  
*circuit*    

### Observations

#### Pros
active filter

#### Cons
supply voltage to operational amplifiers  

#### Constraints
NA
 
