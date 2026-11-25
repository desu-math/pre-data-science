# Part II: Data Organization and Presentation — Algorithms

## Section A: Organizing Data and Constructing Frequency Distributions

### 1. Arranging Raw Data

**Input:** Unordered raw data  
**Output:** Ordered data

**Algorithm:**
1. Read the raw data.
2. Create an empty list for the ordered data.
3. Find the smallest value in the raw data.
4. Add the smallest value to the ordered data.
5. Remove that value from the original data.
6. Repeat Steps 3–5 until all observations have been arranged.
7. Display the ordered data.

### 2. Constructing a Qualitative Frequency Distribution

**Input:** Qualitative data  
**Output:** Qualitative frequency distribution table

**Algorithm:**
1. Read the qualitative data.
2. Identify all distinct categories.
3. Create an empty frequency list.
4. Count the occurrences of each distinct category.
5. Store each category and its corresponding frequency.
6. Calculate the total frequency.
7. Construct and display the frequency distribution table.

### 3. Constructing a Discrete Frequency Distribution

**Input:** Discrete quantitative data  
**Output:** Discrete frequency distribution table

**Algorithm:**
1. Read the discrete quantitative data.
2. Identify all distinct numerical values.
3. Arrange the distinct values in ascending order.
4. Count the occurrences of each value.
5. Store each value and its corresponding frequency.
6. Calculate the total frequency.
7. Construct and display the frequency distribution table.

### 4. Calculating the Range of a Dataset

**Input:** Numerical data  
**Output:** Range

**Algorithm:**
1. Read the dataset.
2. Find the maximum value.
3. Find the minimum value.
4. Calculate the range:

   Range = Maximum − Minimum

5. Display the range.

### 5. Determining the Number of Classes

**Input:** Numerical dataset  
**Output:** Number of classes

**Algorithm:**
1. Read the dataset.
2. Count the number of observations (n).
3. Apply Sturges' rule:

   k = 1 + 3.322 log₁₀(n)

4. Round k to the nearest suitable whole number.
5. Display the number of classes.

### 6. Determining Class Width

**Input:** Numerical dataset and number of classes  
**Output:** Class width

**Algorithm:**
1. Calculate the range of the dataset.
2. Determine the number of classes.
3. Calculate the approximate class width:

   Class width = Range / Number of classes

4. For integer-valued observations, round the class width upward to obtain a whole-number width.
5. Display the class width.

### 7. Constructing a Grouped Frequency Distribution

**Input:** Integer-valued numerical data  
**Output:** Grouped frequency distribution table

**Algorithm:**
1. Read the dataset.
2. Determine the minimum and maximum values.
3. Calculate the number of classes.
4. Calculate and round up the class width.
5. Construct consecutive class intervals beginning with the minimum value.
6. Count the observations belonging to each class.
7. Calculate the total frequency.
8. Construct and display the grouped frequency distribution table.

### 8. Calculating Class Boundaries and Midpoints

**Input:** Class limits  
**Output:** Lower boundaries, upper boundaries, and midpoints

**Algorithm:**
1. Read the class limits.
2. Determine the measurement precision.
3. Calculate the lower class boundary:

   Lower boundary = Lower class limit − 0.5

4. Calculate the upper class boundary:

   Upper boundary = Upper class limit + 0.5

5. Calculate the midpoint:

   Midpoint = (Lower boundary + Upper boundary) / 2

6. Repeat Steps 3–5 for every class.
7. Display the results.

*Note: The adjustment of 0.5 applies to measurements recorded to the nearest whole number.*

## Section B: Relative and Cumulative Frequencies

### 9. Calculating Relative and Percentage Frequencies

**Input:** Class frequencies and total frequency  
**Output:** Relative and percentage frequencies

**Algorithm:**
1. Read the class frequencies.
2. Calculate the total frequency.
3. Calculate the relative frequency of each class:

   Relative frequency = Class frequency / Total frequency

4. Calculate the percentage frequency:

   Percentage frequency = Relative frequency × 100

5. Display the results.

### 10. Constructing a Less-than Cumulative Frequency Distribution

**Input:** Class frequencies arranged in ascending order  
**Output:** Less-than cumulative frequencies

**Algorithm:**
1. Read the class frequencies.
2. Set the first cumulative frequency equal to the first class frequency.
3. Add each subsequent class frequency to the previous cumulative frequency.
4. Repeat until all classes have been processed.
5. Display the less-than cumulative frequency distribution.

### 11. Constructing a More-than Cumulative Frequency Distribution

**Input:** Class frequencies arranged in ascending order  
**Output:** More-than cumulative frequencies

**Algorithm:**
1. Read the class frequencies.
2. Calculate the total frequency.
3. Set the first more-than cumulative frequency equal to the total frequency.
4. Subtract the frequency of each preceding class to obtain the next cumulative frequency.
5. Repeat until all classes have been processed.
6. Display the more-than cumulative frequency distribution.

### 12. Calculating Cumulative Relative Frequency

**Input:** Relative frequencies arranged in ascending class order  
**Output:** Cumulative relative frequencies

**Algorithm:**
1. Read the relative frequencies.
2. Set the first cumulative relative frequency equal to the first relative frequency.
3. Add each subsequent relative frequency to the previous cumulative relative frequency.
4. Repeat until all classes have been processed.
5. Display the cumulative relative frequencies.

## Section C: Additional Frequency Calculations

### 13. Calculating Frequency Density

**Input:** Class frequencies and corresponding class widths  
**Output:** Frequency densities

**Algorithm:**
1. Read the class frequencies.
2. Read the corresponding class widths.
3. Calculate the frequency density of each class:

   Frequency density = Class frequency / Class width

4. Repeat for every class.
5. Display the frequency densities.

### 14. Calculating Pie Chart Sector Angles

**Input:** Category frequencies and total frequency  
**Output:** Sector angles

**Algorithm:**
1. Read the category frequencies.
2. Calculate the total frequency.
3. Calculate the sector angle of each category:

   Sector angle = (Category frequency / Total frequency) × 360°

4. Repeat for all categories.
5. Display the sector angles.

## Section D: Graphical Presentation

### 15. Constructing a Bar Chart

**Input:** Categories and their frequencies  
**Output:** Bar chart

**Algorithm:**
1. Read the categories and their corresponding frequencies.
2. Place the categories on the horizontal axis.
3. Place the frequencies on the vertical axis.
4. Draw separate bars for each category.
5. Label both axes.
6. Add an appropriate title.
7. Display the bar chart.

### 16. Constructing a Pie Chart

**Input:** Categories and their frequencies  
**Output:** Pie chart

**Algorithm:**
1. Read the categories and their frequencies.
2. Calculate the total frequency.
3. Determine the proportion of each category.
4. Convert the proportions into sector angles.
5. Draw a circular chart divided into sectors.
6. Label the sectors.
7. Display the pie chart.

### 17. Constructing a Histogram

**Input:** Class boundaries and class frequencies  
**Output:** Histogram

**Algorithm:**
1. Read the class boundaries and frequencies.
2. Calculate the class widths.
3. Calculate frequency density when class widths are unequal.
4. Place the class intervals on the horizontal axis.
5. Place frequency or frequency density on the vertical axis, depending on class widths.
6. Draw adjacent rectangles for the classes.
7. Label the axes and add a title.
8. Display the histogram.

### 18. Constructing a Frequency Polygon

**Input:** Class midpoints and class frequencies  
**Output:** Frequency polygon

**Algorithm:**
1. Read the class midpoints and frequencies.
2. Place the class midpoints on the horizontal axis.
3. Place the frequencies on the vertical axis.
4. Plot a point for each midpoint and its corresponding frequency.
5. Connect consecutive points using straight lines.
6. Add zero-frequency points at the ends when closing the polygon.
7. Label the axes and add a title.
8. Display the frequency polygon.

### 19. Constructing a Less-than Ogive

**Input:** Upper class boundaries and less-than cumulative frequencies  
**Output:** Less-than ogive

**Algorithm:**
1. Read the upper class boundaries.
2. Read the corresponding less-than cumulative frequencies.
3. Add the lower boundary of the first class with cumulative frequency zero.
4. Place class boundaries on the horizontal axis.
5. Place cumulative frequencies on the vertical axis.
6. Plot the corresponding points.
7. Connect the points using straight lines.
8. Label the axes and add a title.
9. Display the less-than ogive.

### 20. Constructing a More-than Ogive

**Input:** Lower class boundaries and more-than cumulative frequencies  
**Output:** More-than ogive

**Algorithm:**
1. Read the lower class boundaries.
2. Read the corresponding more-than cumulative frequencies.
3. Add the upper boundary of the last class with cumulative frequency zero.
4. Place class boundaries on the horizontal axis.
5. Place cumulative frequencies on the vertical axis.
6. Plot the corresponding points.
7. Connect the points using straight lines.
8. Label the axes and add a title.
9. Display the more-than ogive.
