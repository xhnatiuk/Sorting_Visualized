# CLI GIF Generator

Bar chart graphs for visualizing sorting algorithms. Could always do sorting approximation or partial sort if this becomes too straightforward.

General Idea: 

swtich statement based on cli to decide sorting strategy. GifGenerator class has field of sorter interface. Sorting algorithms are concrete implementations of sorting interface. 

Premade Cases:
-(Psuedo)Random
-Nearly Sorted
-Increasing
-Decreasing
-Few Unique

Premade Problem Sizes:
-10 (small)
-25 (medium)
-30 (large)

## Sorting Algorithms
1. Do a little write up on each sort
2. Category meanings
3. Stability meaning
4. Individualized Sorting Theories
5. Time complexity
6. Space complexity
7. Stability


### Comparison Sorts
#### Selection
* Selection Sort
* Heapsort
* Smoothsort
* Strandsort
* Tournament Sort

#### Partioning
* Introsort (Partion & Selection)
* Quicksort
* Quicksort3??? or are there variations?

#### Merging
* Merge Sort
* In-place Merge Sort
* Quadsort???

#### Insertion
* Patience Sort (Insertion & Selection)
* Block Sort    (Insertion & Merging)
* Timsort       (Insertion & Merging)
* Insertion Sort
* Shell Sort
* Cube Sort
* Binary Tree Sort
* Cycle Sort
* Library Sort

#### Exchanging
* Bubble Sort
* Cocktail Sort
* Comb Sort
* Gnome Sort
* Odd-Even Sort

#### Other
* Unshuffle Sort (Distribution & Merge)
* Franceschini's Method (Uncategorized?)

### Non-Comparison Sorts
#### Stable
* Pigeonhole Sort
* Bucket Sort (uniform keys)
* Bucket Sort (integer keys)
* Counting Sort
* LSD Radix Sort
* MSD Radix Sort

#### Unstable
* MSD Radix Sort (in-place)
* Spreadsort
* Burstsort
* Flashsort
* Postman Sort

### Other
* Bead Sort
* Pancake Sort
* Sorting Network
* Bitonic Sorter
* Han's Algorithm
* Thorup's Algorithm


## Visualization
Sorted Columns: Black
Unsorted Columns: Grey

Red arrow representing row currently being considered

Merge sort will have to look different, maybe grey out area not 
being considered

Quicksort will need two pointers for when its determining high
and low