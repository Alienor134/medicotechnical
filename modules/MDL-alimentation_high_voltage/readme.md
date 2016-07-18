# Module

## Name
[`MDL-alimentation_high_voltage`]()

## Title
High voltage (-100v) alimentation

## Description
We need a high voltage negative pulse in order to exite efficiently the transducer.

##Inputs/Outpouts
input: depends on the solution
output: -100V DC

## Uses
[`ITF-10_gnd`](../../interfaces/ITF-10_gnd)

## Functions
Function: [`FCT-sensing`](../../functions/FCT-sensing)
Sub-Function:  [`FCT-emitting`](../../functions/FCT-emitting)

##Solutions: 

### Cascade de Cockroft

| version      | V1.0 |
| ------------- |: -------------: | ---------: |
| date     |11/04/2016|
| technology|home made|
| author|Jérôme/Gérard|

#### Visuals:

![](ioscheme.jpg)
*scheme*
![](circuit.jpg)
*electronic circuit*

#### Testing:

##### protocol:
##### results:

![](ioscheme.jpg)
*results*

#### Input/Output: 
**input**: alternative signal (square) 0 to -15V
**output**: -100V DC

#### Pros/Cons/Constraint:
**pros**: low electromagnetic scatterred field
**cons**: low intensity
**constraint**: alternative signal (squarre) 0 to -15V



### DC/DC Converter

| version      | V1.1 |
| ------------- |: -------------: |
| date     |18/04/2016|
| technology|integrated circuit|
| author|BM|

#### Scheme
![](ioscheme.jpg)
*scheme*
![](circuit.jpg)
*electronic circuit*

[Fiche du fournisseur](http://www.digikey.fr/product-detail/fr/recom-power/R05-100B/945-2051-5-ND/3776798)
#### Testing:

##### protocol:
##### results:

![](ioscheme.jpg)
*results*

####Input/Output: 
**input**: R05-100B 5V, higher 12V
**output**: +/-50 to 150V DC

#### Pros/Cons/Constraint:
**pros**: variable output
**cons**: price
**constraint**: 5V or 12V power supply

