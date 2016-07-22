# Module
![](viewme.jpg)

## Name
[`MDL-motor_control`]()

## Title
Motor Control

## Version
V16.04.15 

## Technology
Echopen Made and Arduino

## Functions  
[`FCT-sensing_sweeping`](../../functions/FCT-sensing_sweeping)  

## IOs
###Inputs
[`ITF-O_cc_motor_encoder`](../../interfaces/ITF-O_cc_motor_encoder)  
[`ITF-M_abs_angle`](../../interfaces/ITF-M_abs_angle)  
[`ITF-N_cc_motor_pwm`](../../interfaces/ITF-N_cc_motor_pwm)  
[`ITF-O_stepper_b1`](../../interfaces/ITF-O_stepper_b1)  
[`ITF-N_stepper_b2`](../../interfaces/ITF-N_stepper_b2)  
[`ITF-P_stepper_a1`](../../interfaces/ITF-P_stepper_a1)  
[`ITF-P_stepper_a2`](../../interfaces/ITF-P_stepper_a2)  

### Outputs
[`ITF-I_pulse_on`](../../interfaces/ITF-I_pulse_on)  
[`ITF-I_pulse_off`](../../interfaces/ITF-I_pulse_off)  


## Information

### Module requirements 
This module will realise the sweeping

## Visuals
![scheme](/modules/MDL-alimentation_high_voltage_recom/images/scheme.jpg)  


### Observations

#### Pros
Na

#### Cons
the transducer position is calculated depending on an
 absolute position and instantaneous motor velocity.

#### Constraints
Need to use an encoder

