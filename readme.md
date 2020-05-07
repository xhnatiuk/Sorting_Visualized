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

# Documentation
## src.gif\_generator

### Change

```python
class Change()
```

Class for defining changes that have taken place during sorting.

**Attributes**:

- `indentifier` _str_ - the indentifier of a change. Identifiers:
  draw - a value at a single index was changed.
  overlay - a value at a single index will be changed.
  exchange - values at two different indicies were swapped.
  add_cursor - values were considered at 1 or more indicies.
  remove_cursor - values were no longer being considered at 1 or more indicies.
  color - values were re-colored at 0 or more indicies.
- `involved` _List[int]_ - values involved in a change. See GifGenerator.apply_<indentifier>
  for information on how the invovled list should be used for each identifier.

#### \_\_init\_\_

```python
 | __init__(indentifier: str, involved: List[int])
```

Constructor for Change class.

**Arguments**:

- `identifier` _str_ - the indentifier of the change applied.
- `involved` _List[int]_ - values involved in the change.

### Step

```python
class Step()
```

Object for tracking steps taken while sorting a list.

**Attributes**:

- `position` _int_ - the index of the value being considered in the current step.
- `changes` _List[Change]_ - a list of 0 or more changes applied in the current step.

#### \_\_init\_\_

```python
 | __init__(position: int, changes: List[Change] = None)
```

Constructor for Step class.

**Arguments**:

- `position` _int_ - the index of the value being considered.
- `changes` _List[Change]_ - a list of 0 or more changes applied.

### GifStrategy

```python
class GifStrategy(ABC)
```

Interface that declares contract for concrete gif strategy classes.

#### generate\_steps

```python
 | @abstractmethod
 | generate_steps(values: List[int]) -> List[Step]
```

Sorts the values and returns a list of the steps used.

**Arguments**:

- `values` _List[int]_ - the values to be sorted.

**Modifies:**

- `values` - sorts the list in increasing order.

**Returns**:

- `steps(List[Step])` - the list of steps used.

### GifGenerator

```python
class GifGenerator()
```

Object containing a GifStrategy and a GrahIllustrator for GIF file generation

**Attributes**:

- `illustrator` _GraphIllustrator_ - GraphIllustrator used for frame drawing.
- `strategy` _GifStrategy_ - GifStrategy to be used for step generation.

#### \_\_init\_\_

```python
 | __init__(strategy: GifStrategy, illustrator=GraphIllustrator) -> None
```

Constructor for GifGenerator class.

**Arguments**:

- `strategy` _GifStrategy_ - concrete GifStrategy to be used.
- `illustrator` _GraphIllustrator_ - concrete GraphIllustrator to be used.

#### generate\_steps

```python
 | generate_steps(values: List[int]) -> List[Step]
```

Delegates work to the GifStrategy and returns the steps used in sorting.

**Arguments**:

- `values` _List[int]_ - the values to be sorted.
  

**Returns**:

- `steps` _List[Step]_ - the steps used in sorting.

#### generate\_gif

```python
 | generate_gif(values: List[int], file_path: str, speed: int) -> None
```

Generates a GIF with frames corresponding to the steps taken by the GifGenerator's sorting strategy.

**Arguments**:

- `values` _List[int]_ - the list of values in the bar graph.
- `file_path` _str_ - the location where the png that the gif will be based off of is stored,
  and where the gif willl be stored.
- `speed` _int_ - the duration of each frame in centiseconds.

**Modifies:**

- `values` - sorts the list in increasing order.
- `./file_path` - save a gif.
  

**Returns**:

  None.

#### generate\_frame

```python
 | generate_frame(values: List[int], step: Step, frame: Image) -> None
```

Edits the frame to display the changes in Step, performs any changes on values.

**Arguments**:

- `values` _List[int]_ - the list of values displayed in frame.
- `step` _Step_ - the new position for the cursor and 0 or more changes.
- `frame` _Image_ - the image to be edited.

**Modifies:**

- `frame` - updated with the changes in step.
- `values` - values may be changed or moved.
  

**Returns**:

  None.

#### change\_dispatch

```python
 | change_dispatch(change: Change, values: List[int], draw: ImageDraw) -> None
```

Calls the appropriate function for the given change code.

**Arguments**:

- `change` _Change_ - object containing the change identifier and involved values.
- `values` _List[int]_ - the list of values displayed in frame.
- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `values` - values may be changed or moved.
- `draw` - the image associated with the drawing object is updated with the appropriate changes.
  

**Returns**:

  None.

#### apply\_draw

```python
 | apply_draw(values: List[int], involved: List[int], draw: ImageDraw) -> None
```

Draws a bar on the image at involved[0] with value involved[1], updates values accordingly.

**Arguments**:

- `values` _List[int]_ - the list of values displayed in frame.
- `involved` _List[int]_ - the index and value for the bar to be drawn.
- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `values` - the value at index involved[0] is set to involved[1].
- `draw` - the bar at index involved[0] is erased and replaced with a bar of value involved[1] on image associated with the drawing object.
  

**Returns**:

  None.

#### apply\_overlay

```python
 | apply_overlay(values: List[int], involved: List[int], draw: ImageDraw) -> None
```

Draws a bar-outline on the image at involved[0] with value involved[1], updates values accordingly.

**Arguments**:

- `values` _List[int]_ - the list of values displayed in frame.
- `involved` _List[int]_ - the index and value for the bar-outline to be drawn.
- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `values` - the value at index involved[0] is set to involved[1].
- `draw` - a bar outline with value involved[1] is drawn over top of the bar at index involved[0] on image associated with the drawing object.
  

**Returns**:

  None.

#### apply\_exchange

```python
 | apply_exchange(values: List[int], involved: List[int], draw: ImageDraw) -> None
```

Swaps the bars on the image at involved[0] and involved[1], updates values accordingly.

**Arguments**:

- `values` _List[int]_ - the list of values displayed in frame.
- `involved` _List[int]_ - the indicies of the bars to be swapped.
- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `values` - the value at index involved[0] is swapped with the value at index invovled[1].
- `draw` - the bars at index involved[0]  and involved[1] are swapped on image associated with the drawing object.
  

**Returns**:

  None.

#### apply\_add\_cursor

```python
 | apply_add_cursor(values: List[int], involved: List[int], draw: ImageDraw) -> None
```

Draws a cursor on the image at every index listed in involved.

**Arguments**:

- `values` _List[int]_ - the list of values displayed in frame.
- `involved` _List[int]_ - the indicies of the cursors to be drawn.
- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `draw` - cursors are drawn on image associated with the drawing object at every index listed in involved.

**Returns**:

  None.

#### apply\_remove\_cursor

```python
 | apply_remove_cursor(values: List[int], involved: List[int], draw: ImageDraw) -> None
```

Erases a cursor on the image at every index listed in involved.

**Arguments**:

- `values` _List[int]_ - the list of values displayed in frame.
- `involved` _List[int]_ - the indicies of the cursors to be erased.
- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `draw` - cursors are erased on image associated with the drawing object at every index listed in involved.

**Returns**:

  None.

#### apply\_color

```python
 | apply_color(values: List[int], involved: List[int], draw: ImageDraw) -> None
```

Re-draws all bars at indicies in involved[1:] on the image with the color specified in involved[0].

**Arguments**:

- `values` _List[int]_ - the list of values displayed in frame.
- `involved` _List[int]_ - the color code and indicies of re-coloring bars.
- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `draw` - all bars at indicies in involved[1:] are erased and re-drawn with the selected color on image associated with the drawing object.

**Returns**:

  None.

#### select\_color

```python
 | select_color(code: str) -> (int, int, int)
```

Selects the correct color from the GraphIllustrator's ColorProfile based on the code.

**Arguments**:

- `code` _str_ - one of the color options (sorted, fade, or bar).
  

**Returns**:

- `color` _int, int, int_ - a RGBA color code.

## src.input\_handler

#### select\_color\_profile

```python
select_color_profile(color: str) -> ColorProfile
```

Selects the correct color profile.

**Arguments**:

- `color` _str_ - used to select a preset color profile (red, blue or green).
  

**Returns**:

- `colors` _ColorProfile_ - An instance of the correct ColorProfile.

#### select\_graph\_strategy

```python
select_graph_strategy(code: str) -> GraphStrategy
```

Instantiates the correct GraphStrategy.

**Arguments**:

- `code` _str_ - one of the preset strategy codes.
  

**Returns**:

- `strategy` _GraphStrategy_ - An instance of the correct GraphStrategy.

#### select\_gif\_strategy

```python
select_gif_strategy(code: str) -> GraphStrategy
```

Instantiates the correct GifStrategy.

**Arguments**:

- `code` _str_ - one of the preset strategy codes.
  

**Returns**:

- `strategy` _GifStrategy_ - An instance of the correct GifStrategy.

#### handle\_input

```python
handle_input(args) -> None
```

Transforms command line inputs into the specififed graph.

**Arguments**:

- `args` _Namespace_ - object holding parsed command line attributes.

**Modifies:**

- `./sorting_visualized` - saves a .png and a .gif to the filepath in args.

**Raises**:

  InputError


**Returns**:

  None.

## src.graph\_illustrator

### ColorProfile

```python
class ColorProfile()
```

Class for storing all the RGB color codes for drawing a bar graph.

**Attributes**:

- `background` _int, int, int_ - the RGB color code for the background.
- `border` _int, int, int_ - the RGB color code for the border.
- `bar` _int, int, int_ - the RGB color code for the bar.
- `fade` _int, int, int_ - the RGB color code for a faded bar.
- `finished` _int, int, int_ - the RGB color code for the sorted bars.
- `cursor` _int, int, int_ - the RGB color code for the cursor.

#### \_\_init\_\_

```python
 | __init__(background: (int, int, int), border: (int, int, int), bar: (int, int, int), fade: (int, int, int), finished: (int, int, int), cursor: (int, int, int))
```

Constructor for ColorProfile class.

background (int, int, int): RGB color for thebackground.
border (int, int, int): RGB color for the border.
bar (int, int, int): RGB color for bars.
fade (int, int, int): RGB color for faded bars.
finished (int, int, int): RGB color for sorted bars.
cursor (int, int, int): RGB color for cursors.

### GraphIllustrator

```python
class GraphIllustrator()
```

Class for drawing and editing bar graphs.

**Attributes**:

- `image_width` _int_ - the width of the image in pixels
- `image_height` _int_ - the  height of the image in pixels
- `border_size` _int_ - the width of the border in pixels
- `num_bars` _int_ - the number of bars in the graph
- `bar_width` _int_ - the width of a bar in pixels
- `padding` _int_ - the horizontal padding between the border and the first and last bars in pixels
- `colrs` _ColorProfile_ - the object used to select colors for drawing

#### \_\_init\_\_

```python
 | __init__(num_bars: int, image_size: (int, int), border_size: int, colors: ColorProfile) -> None
```

Constructor for GraphIllustrator class.

**Arguments**:

- `image_size` _int, int_ - the width and height of the image.
- `border_size` _int_ - the size of the border.
- `colors` _ColorProfile_ - RGB color profile for the GraphIllustrator.

#### draw\_cursor

```python
 | draw_cursor(position: int, draw: ImageDraw, color: (int, int, int)) -> None
```

draws a color cursor on the image at the position.

**Arguments**:

- `position` _int_ - the index of the cursor.
- `draw` _ImageDraw_ - the drawing object.
- `color` _int, int, int, int_ - RGB color code.

**Modifies:**

- `draw` - a color cursor is drawn onto the image associated with the drawing object.

**Returns**:

  None.

#### erase\_cursor

```python
 | erase_cursor(position: int, draw: ImageDraw) -> None
```

Erases the cursor on the image at the position.

**Arguments**:

- `position` _int_ - the index of the cursor.
- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `draw` - a cursor is erased from the image associated with the drawing object.

**Returns**:

  None.

#### draw\_bar

```python
 | draw_bar(position: int, value: int, draw: ImageDraw, color: (int, int, int)) -> None
```

Draws a color bar of the correct height on the image at the position.

**Arguments**:

- `position` _int_ - the index of the bar.
- `value` _int_ - the new bar value.
- `draw` _ImageDraw_ - the drawing object.
- `color` _int, int, int, int_ - RGB color code.

**Modifies:**

- `draw` - a bar is drawn onto the image associated with the drawing object.

**Raises**:

- `InputError` - number of values is too large for the image size.
  

**Returns**:

  None.

#### erase\_bar

```python
 | erase_bar(position: int, draw: ImageDraw) -> None
```

Erases the bar on the image at the position.

**Arguments**:

- `position` _int_ - the index of the bar.
- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `draw` - a bar is erased from the image associated with the drawing object.

**Returns**:

  None.

#### draw\_bars

```python
 | draw_bars(values: List[int], draw: ImageDraw) -> None
```

Draws a bar for each value onto the image.

**Arguments**:

- `values(List[int])` - the values to be drawn.
- `draw` _ImageDraw_ - the drawing object.
  

**Raises**:

- `InputError` - number of values is too large for the image size.

**Modifies:**

- `draw` - a bar is drawn onto the image associated with the drawing object for each value in values.

**Returns**:

  None.

#### draw\_border

```python
 | draw_border(draw: ImageDraw) -> None
```

Draws a half self.colors.border, half self.colors.background border onto the image.

**Arguments**:

- `draw` _ImageDraw_ - the drawing object.

**Modifies:**

- `draw` - a border is drawn onto the image associated with the drawing object.

**Returns**:

  None.

#### draw\_graph

```python
 | draw_graph(values: List[int], draw: ImageDraw) -> None
```

Draws a bar graph of the values in values

**Arguments**:

- `values(List[int])` - a list of values.
- `draw` _ImageDraw_ - the drawing object.
  

**Raises**:

  InputError:
  * number of values is too large for the image size.
  * no values are passed.

  **Modifies:**
- `draw` - a bar graph is drawn onto the image associated with the drawing object.

**Returns**:

  None.

## src.exceptions

From Python Documentation exceptions example

### InputError

```python
class InputError(Exception)
```

Exception raised for errors in the input.

**Attributes**:

- `expression` _any_ - input expression in which the error occurred.
- `message` _str_ - explanation of the error.

#### \_\_init\_\_

```python
 | __init__(expression, message: str)
```

Constructor for InputError class.

**Arguments**:

- `expression` - input expression in which the error occurred.
- `message` _str_ - explanation of the error.

## src.graph\_strategy

### GraphStrategy

```python
class GraphStrategy(ABC)
```

Interface that declares contract for concrete graph strategy classes.

#### generate\_values

```python
 | @abstractmethod
 | generate_values(quantity: int, maximum: int) -> List[int]
```

Generates a list of quantity integers between 0 and maximum inclusive.

**Arguments**:

- `quantity` _int_ - the number of values to be generated.
- `maximum` _int_ - the maximum permissible value size.
  

**Returns**:

- `values(List[int])` - a list of integers.

#### generate\_values

```python
 | generate_values(quantity: int, maximum: int) -> List[int]
```

Fufuills the GraphStrategy.generate_values contract.

**Arguments**:

- `quantity` _int_ - the number of values to be generated.
- `maximum` _int_ - the maximum permissible value size.
  

**Returns**:

- `values(List[int])` - a increasing list of integers.

#### generate\_values

```python
 | generate_values(quantity: int, maximum: int) -> List[int]
```

Fufuills the GraphStrategy.generate_values contract.

**Arguments**:

- `quantity` _int_ - the number of values to be generated.
- `maximum` _int_ - the maximum permissible value size.
  

**Returns**:

- `values(List[int])` - a decreasing list of integers.

#### generate\_values

```python
 | generate_values(quantity: int, maximum: int) -> List[int]
```

Fufuills the GraphStrategy.generate_values contract

**Arguments**:

- `quantity` _int_ - the number of values to be generated.
- `maximum` _int_ - the maximum permissible value size.
  

**Returns**:

- `values(List[int])` - a nearly sorted list of integers.

#### generate\_values

```python
 | generate_values(quantity: int, maximum: int) -> List[int]
```

Fufuills the GraphStrategy.generate_values contract

**Arguments**:

- `quantity` _int_ - the number of values to be generated.
- `maximum` _int_ - the maximum permissible value size.
  

**Returns**:

- `values(List[int])` - a list of integers with many repeated values.

#### generate\_values

```python
 | generate_values(quantity: int, maximum: int) -> List[int]
```

Fufuills the GraphStrategy.generate_values contract

**Arguments**:

- `quantity` _int_ - the number of values to be generated.
- `maximum` _int_ - the maximum permissible value size.
  

**Returns**:

- `values(List[int])` - a random list of integers.

## src.graph\_generator

### GraphGenerator

```python
class GraphGenerator()
```

Object containing a GraphStrategy for PNG graph generation

**Attributes**:

- `strategy` _GraphStrategy_ - GraphStrategy to be used for value generation.

#### \_\_init\_\_

```python
 | __init__(strategy: GraphStrategy) -> None
```

Constructor for GraphGenerator class.

**Arguments**:

- `strategy` _GraphStrategy_ - an instance of a concrete GraphStrategy.

#### generate\_graph

```python
 | generate_graph(quantity: int, illustrator: GraphIllustrator, file_path: str) -> List[int]
```

Generates and saves an image of a graph.

**Arguments**:

- `quantity` _int_ - the number of bars on the graph.
- `illustrator` _Illustrator_ - the illistrator instance for the graph generation.
- `file_path` _str_ - the path relative to ./sorting_visualized to save the graph to.

**Modifies:**
./sorting_visualized

**Raises**:

  InputError:
  - less than 1 value
  - negative maximum value
  - illustrator image size less than 1
  - number of values is too large for the image size


**Returns**:

- `values` _List[int]_ - the values in the generated graph.

#### create\_graph\_base

```python
create_graph_base(width: (int), height: (int), background_color: (int, int, int)) -> Image
```

Creates a base image to draw a graph on.

**Arguments**:

- `width` _int_ - the width of the image in pixels.
- `height` _int_ - the width of the image in pixels.
- `background_color` _str_ - the RGBA color code for the background.
  

**Raises**:

- `InputError` - image size less than 1.
  

**Returns**:

- `base` _Image_ - the base for the graph.

