## Loop Invariant:
A part of a loop that doesn't change throughout the iterations of 
the loop, this part (the invariant) is true before, during, and after each step of the 
loop.


## Loop Invariant of `mergeSort()` function:
Out of the mergeSort function, the **merge** step contains the loop invariant, 
specifically the line `if lefthalf[i] <= righthalf[j]:` 
```python
def mergeSort(alist):
    ...
        # the Merge Step
        i, j, k  = 0,0,0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
    ...
```


## Initialization Step: 
_What is true before the first iteration of loop_

`i,j,k = 0,0,0` are initialized and we have the empty subarrays `lefthalf[]` and 
`righthalf[]` which start out with only one element, 0, which is the smallest element 
of both arrays.

## Maintenance Step: 
_If true before iteration, it remains true_

When `lefthalf[i] <= righthalf[j]` the smallest element (`lefthalf[i]`) will be copied 
to `alist[k]`.

When `lefthalf[i] > righthalf[j]` the smallest element (`righthalf[i]`) will be copied 
to `alist[k]`.

In both instances, i will be incremented,  which will reinitialize the loop.
## Termination Step:
_The end of the loop shows us the desired outcome proving the algorithm was correct_

At the end of the loop, `k = k + 1`, which means that `A[k]` now contains the smallest 
element of the `lefthalf[]` and `righthalf[]`, giving the desired outcome of a sorted 
list from smallest to largest elements. 