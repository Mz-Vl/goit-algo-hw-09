# Comparison of Greedy and Dynamic Programming Algorithms

## Time Complexity
- **Greedy algorithm:** O(n) where n is the number of coin denominations. Goes through denominations only once.
- **Dynamic programming:** O(n*k) where k is the target change sum. Needs to fill a table of size k x k.
  - With increasing k, dynamic programming runtime grows much faster than greedy.

## Performance Test
```
Time for the greedy algorithm: 0.004358700010925531 s
Dynamic programming algorithm time: 3.7361657000146806 s
```
- Greedy algorithm is faster for this test case

## Result
- **Greedy always finds a correct change, but not necessarily the optimal one by the number of coins.**
- **Dynamic programming always finds the optimal change.**

## Conclusion
- For small change sums, the greedy algorithm works very fast and gives a good approximation of the optimum.
- But for large sums, where finding the optimal result is crucial, dynamic programming is preferable despite being slower. Its complexity is justified by the optimality of the result.

**Therefore, it's best to use:**
- **Greedy algorithm - when the sum is small**
- **Dynamic programming - when dealing with large sums**
