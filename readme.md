# CLI GIF Generator
A command line python app for generating bar chart graph visualizations of sorting algorithms. 

how to use:
1. navigate to the root folder (sorting_visualized)
2. run `python3 ./main algorithim`
3. find output in ./out/images

## Positional Arguments
`algorithim`: sorting algorithm for the animation, one of
* selection
* insertion
* bubble
* cocktail
* comb
* gnome
* oddeven
* merge

## Optional Arguements
`-q, --quantity`: number of values to be generated, must be within [0, 100]
* 10 (default)

`-i, --input`: pattern for generating the input list, one of
* increasing
* decreasing (default)
* nearly sorted
* few unique
* random

`-d, --dimensions`: dimension (in pixels) for the animation (width & height)
* 500 (default)

`-b, --border`: width (in pixels), for the border of the animation
* 25 (default)

`-c, --color`: colors for the animation, one of 
* red
* blue (default) 
* green

`-s, --speed`: number of frames for each step of the animation, must be within [0, 100]
* 1 (default)

`-p, --path`: the file path and name relative to sorting_visualized/
* ./out/images/gif (default)

# Sorting Algorithms
1. Do a little write up on each sort
2. Category meanings
4. Individualized Sorting Theories
5. Time complexity
6. Space complexity
7. Stability

## Comparison Sorts
### Selection
#### Selection Sort
#### Heapsort
#### Smoothsort
#### Strandsort
#### Tournament Sort

### Partioning
#### Introsort (Partion & Selection)
#### Quicksort
#### Quicksort3

### Merging
#### Merge Sort
#### In-place Merge Sort
#### Quadsort

### Insertion
#### Insertion Sort
#### Shell Sort
#### Cube Sort
#### Binary Tree Sort
#### Cycle Sort
#### Library Sort
#### Patience Sort (Insertion & Selection)
#### Block Sort    (Insertion & Merging)
#### Timsort       (Insertion & Merging)

### Exchanging
#### Bubble Sort
#### Cocktail Sort
#### Comb Sort
#### Gnome Sort
#### Odd-Even Sort

### Other
#### Unshuffle Sort (Distribution & Merge)
#### Franceschini's Method (Uncategorized?)


# Extension  Ideas
Sorting approximation, partial sorting, different visuals (scatterplot, different colored pixels)

## Non-Comparison Sorts
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