# Print all possible subsets.

## Example
[1, 2]'s subset > [1, 2], [1], [2], [] > 2^2 in total  
[1, 2, 3]'s subset > [1, 2, 3], [1, 2], [1], ..., [] > 2^3 in total  
[1, ..., n]'s subset > [1, ..., n], ..., [] > 2^n in total

## Insight
Given arbitrary set [1, 2, ..., n], each element of the set can be picked or not. It means we can convert each subset as binary number.  
For Example, when original set [1, 2] is given, 
```
[1, 2] > [picked, picked] > 11(2) > 3
[1] > [picked, not-picked] > 10(2) > 2
[2] > [not-picked, picked] > 01(2) > 1
[] > [not-picked, not-picked] > 00(2) > 0
```

## Solution
### 1. Convert number to binary string
### 2. Calculate subset according binary string above
### 3. Loop from 0 to 2**len(array) - 1 and print according subset
