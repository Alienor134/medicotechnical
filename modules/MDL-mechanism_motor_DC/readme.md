# Module
![](viewme.png)

## Name
[`MDL-mechanism_motor_DC`]()

## Title
Motor accomplishing the sweeping

## Version
V16.05.02

## Technology
motor [`RB-Pol-123`](http://www.robotshop.com/media/files/pdf/datasheet-1442.pdf)  
integrated circuit [`encodor`](http://www.robotshop.com/ca/fr/moteur-12v-engrenage-191-avec-encodeur-64-cpr.html)

## Contributor
[`Jérôme`](../../contributors/CTB-jerome)  

## Functions  
[`FCT-sensing_sweeping`](../../functions/FCT-sensing_sweeping)  

## IOs
###Inputs
[`ITF-N_cc_motor_pwm`](../../interfaces/ITF-N_cc_motor_pwm)  
 

### Outputs
[`ITF-M_abs_angle`](../../interfaces/ITF-M_abs_angle)  
Rotary movement

## Information

### Module requirements 
In order to construct a 2D image, we have to move the transducer with a sweeping movement.
This can be done with a motor (and a movement convertor).
### Visuals
![circuit](/modules/MDL-alimentation_high_voltage_cockroft/images/scheme2_cockroft.png)  
*circuit*    
![circuit](/modules/MDL-alimentation_high_voltage_cockroft/images/scheme_cockroft.jpg)  
*square alimentation 0-18V*

### Observations

#### Pros
simple
#### Cons
low intensity  
#### Constraints
need movement converter  
need encodor


