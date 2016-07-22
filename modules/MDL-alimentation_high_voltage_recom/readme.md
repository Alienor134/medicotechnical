# Module
![](viewme.jpg)

## Name
[`MDL-alimentation_high_voltage_recom`]()

## Title
High voltage (-100V) alimentation

## Version
V16.04.18

## Technology
integrated circuit [`R05-100B`](http://www.digikey.fr/product-detail/fr/recom-power/R05-100B/945-2051-5-ND/3776798)  

## Author
[`BM`](../../contributors/CTB-bm)  

## Functions
[`FCT-sensing_emitting`](../../functions/FCT-sensing_emitting)  

## IOs
###Inputs
[`ITF-A_gnd`](../../interfaces/ITF-A_gnd)  
[`ITF-B_5v`](../../interfaces/ITF-B_5v) or [`ITF-F_12v`](../../interfaces/ITF-F_12v)  

### Outputs
[`IM-A_100v`](../../interfaces/IM-A_100v) variable output: +/-50 to 150V DC  

## Information

### Module requirements
This module will provide a high negative DC voltage (-100V) in order to increase the pulse voltage to exite efficiently the transducer.  

### Visuals

![circuit](/modules/MDL-alimentation_high_voltage_recom/images/scheme_recom.png)  
*circuit*  

### Observations

#### Pros
variable output  
#### Cons
price  
#### Constraints
5V or 12V power supply  



