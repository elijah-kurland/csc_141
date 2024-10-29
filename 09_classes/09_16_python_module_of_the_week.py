'''I looked at the the random module which provides a fast pseudorandom number generator based on the 
Mersenne Twister algorithm. This algorithm was originally developed to produce inputs for  
simulations, Mersenne Twister generates numbers with nearly uniform distribution 
and a large period, making it suited for a wide range of applications. 

Random() produces different values each time it is called. This is useful for producing unique values or variations. 
One technique is to use a program to generate random values and save them to be processed by a separate step. 
That may not be practical for large amounts of data, though. Random also includes the seed() function for 
initializing the pseudorandom generator so that it produces an expected set of values.

The internal state of the pseudorandom algorithm used by random() can be saved and used to control the 
numbers produced in subsequent runs. Restoring the previous state before continuing reduces the likelihood 
of repeating values or sequences of values from the earlier input. The getstate() function returns data that 
can be used to re-initialize the random number generator later with setstate().

One common use for random number generators is to select a random item from a sequence of enumerated values, 
even if those values are not numbers. random includes the choice() function for making a random selection from 
a sequence. This example simulates flipping a coin 10,000 times to count how many times it comes up heads and how 
many times tails.'''