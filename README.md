# Hokkaido-Test
A simulation model for the admission exam in the Hokkaido University

The question is asking the student to pick an integer from 1-100. The student who picks a number without repeating other's value would have a bonus mark of 60, otherwise he will get no mark. The one with highest mark wins this game.

Which value should you choose to maximize your probability to win?

A online statistic sampling result is listed in *result.txt*.

A randomness ratio is added so that the user can control the degree of randomness other than just using the statistical result.

The idea is to use statistical result as a probability distribution function in binomial distribution. The aim is to find the value which only repeat once. 

i.e. f(x)*(1-f(x))^(N-1). 

Where x is the choosed number and f(x) is the probability distribution function. N is the number of player in this game.