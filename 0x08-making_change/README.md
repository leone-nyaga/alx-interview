# 0x08. Making Change

The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations.

### The question

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

+ Prototype: ``` def makeChange(coins, total)```
+ Return: fewest number of coins needed to meet total
  + If total is 0 or less, return 0
  + If total cannot be met by any number of coins you have, return -1
+ "coins" is a list of the values of the coins in your possession
+ The value of a coin will always be an integer greater than 0
+ You can assume you have an infinite number of each denomination of coin in the list
+ Your solution’s runtime will be evaluated in this task

```bash
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```
