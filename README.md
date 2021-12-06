# Exercise_Pokemon_Damage_Calculator
This exercise create a function that calculates the battle damage in the attack of one pokemon to another. 
## Description
In the Japanese pokemon game, during a pokemon battle you have two pokemon (assuming single battles) and when one attacks another, then the game uses the following formula to calculate the damage that attack will do to your opponent:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b8c51fed93bb9a80ae8febc13700a40b8a5da402">

This program create a function that, given two pokemon and the attack to use, makes these calculations and gives you as a result the value of how many points of damage this attack will do to the defending pokemon. At the end of doing all the calculations round up to the previous integer.

where:
- Level is the level of the attacking pokemon.
- Power is the power of the attack
- A is the value of the attack statistic of the attacking pokemon based on the type of attack performed (can be physical or special attack)
- D is the value of the pokemon's defense statistic based on the type of attack performed (it can be physical or special attack)
- Target refers to how many pokemon the pokemon is attacking, the value of this variable is always 1 in single battles and 0.75 in double battles when the attack touches more than one pokemon.
- Weather when the type of attack of the pokemon is affected by the weather of the fight, for example in rain the water attacks are multiplied by 1.5 and the fire attacks by 0.5.
- Badge is 1 in all cases.
- Critical is a random variable that is 1 in 93.75% of the cases and 1.5 in the remaining 6.25%.
- Random is a uniform random variable that can take any value between 0.85 and 1.
- STAB shows if the attack is of the same type as the type of the attacking pokemon, then it has value 1.5, if not it is 1
- Type means if the type of the attack is doubly super effective against the type of the attacker, then it is 4, if it is super effective, then 2, if it is normally effective it is 1, if it is ineffective then it is 0.5, if it is doubly ineffective, then 0.25 and if it is not effective at all 0. For simplicity of this exercise we will assume that this variable is always 1.
- Burn is 0.5 if the pokemon is burned and uses a physical attack 1 otherwise 1.
- Other is 1 in any case

Each Pokemon is representad by an Object wich includes name, level, physical (no special) attack, physical (no special) defense. In this case it was assumed that the values related to the types are worth 1.

As an example, imagine we have an Ice-type Glaceon level 75 with a physical attack statistic of 123 and it uses the Ice Fang attack with power of 65 on a Dregon/Earth-type Garchomp with a physical defense statistic of 163. What is the result of an attack? What is the minimum and maximum value that this attack can give?

## BONUS (this program not includes this BONUS yet)
Do the calculations in such a way that the pokemon variable has the type information, and calculates the Type variable in the formula based on these, likewise do the calculations in such a way that you always truncate to the previous integer whenever you perform a multiplication or a division, instead of doing it at the end.
