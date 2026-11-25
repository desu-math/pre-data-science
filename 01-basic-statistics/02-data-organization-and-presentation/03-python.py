# Part II: Data Organization and Presentation — Python Implementation

## 1. Importing Libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
```

## 2. Preparing the Datasets

```python
# Numerical dataset: examination scores
observations = [
    3, 4, 7, 14, 5, 6, 26, 17, 8,
    9, 17, 20, 22, 16, 12, 25, 23, 24
]

# Qualitative dataset: students' learning methods
learning_methods = [
    'Online', 'Hybrid', 'Face-to-face', 'Hybrid', 'Online', 'Online',
    'Face-to-face', 'Hybrid', 'Online', 'Hybrid', 'Online', 'Face-to-face',
    'Face-to-face', 'Online', 'Online', 'Hybrid', 'Online', 'Face-to-face',
    'Online', 'Online', 'Hybrid', 'Online', 'Online', 'Online', 'Face-to-face',
    'Online', 'Face-to-face', 'Hybrid', 'Online', 'Online', 'Hybrid'
]
```

## 3. Arranging Raw Data

```python
# Create an ordered copy of the original dataset.
remaining_data = observations.copy()

ordered_data = []

# Repeatedly select and remove the smallest observation.
while remaining_data:

    smallest_value = min(remaining_data)

    ordered_data.append(smallest_value)

    remaining_data.remove(smallest_value)

print("Ordered data:", ordered_data)
```

## 4. Constructing a Qualitative Frequency Distribution

```python
# Identify distinct learning methods.
distinct_values = []

for value in learning_methods:

    if value not in distinct_values:
        distinct_values.append(value)

# Count the frequency of each distinct method.
frequencies = []

for value in distinct_values:

    frequency = learning_methods.count(value)

    frequencies.append(frequency)

# Construct the frequency distribution table.
qualitative_frequency = pd.DataFrame({
    'Learning Method': distinct_values,
    'Frequency': frequencies
})

print(qualitative_frequency)

# Calculate and display the total frequency.
total_frequency = qualitative_frequency['Frequency'].sum()

print("\nTotal Frequency:", total_frequency)
```

## 5. Constructing a Discrete Frequency Distribution

```python
# Identify distinct numerical observations.
distinct_scores = sorted(set(observations))

# Count the frequency of each distinct score.
score_frequencies = []

for score in distinct_scores:

    frequency = observations.count(score)

    score_frequencies.append(frequency)

# Construct the discrete frequency distribution.
discrete_frequency = pd.DataFrame({
    'Score': distinct_scores,
    'Frequency': score_frequencies
})

print(discrete_frequency)

print("\nTotal Frequency:",
      discrete_frequency['Frequency'].sum())
```

## 6. Calculating the Range

```python
minimum_value = min(observations)

maximum_value = max(observations)

data_range = maximum_value - minimum_value

print("Minimum value:", minimum_value)
print("Maximum value:", maximum_value)
print("Range:", data_range)
```

## 7. Determining the Number of Classes

```python
# Count the number of observations.
n = len(observations)

# Apply Sturges' rule.
number_of_classes = round(1 + 3.322 * np.log10(n))

print("Number of observations:", n)

print("Number of classes:", number_of_classes)
```

## 8. Determining Class Width

```python
# Calculate the approximate class width.
approximate_width = data_range / number_of_classes

# Round upward to obtain an integer class width.
class_width = math.ceil(approximate_width)

print("Approximate class width:", approximate_width)

print("Actual class width:", class_width)
```

## 9. Constructing a Grouped Frequency Distribution

```python
# Determine the first and last class limits.
first_lower_limit = minimum_value

last_upper_limit = maximum_value

# Generate the class intervals automatically.
class_intervals = []

lower_limits = []
upper_limits = []

current_lower_limit = first_lower_limit

while current_lower_limit <= last_upper_limit:

    current_upper_limit = current_lower_limit + class_width - 1

    lower_limits.append(current_lower_limit)

    upper_limits.append(current_upper_limit)

    class_intervals.append(
        f"{current_lower_limit} - {current_upper_limit}"
    )

    current_lower_limit = current_upper_limit + 1

# Count observations belonging to each class.
class_frequencies = []

for lower_limit, upper_limit in zip(lower_limits, upper_limits):

    frequency = sum(
        1 for value in observations
        if lower_limit <= value <= upper_limit
    )

    class_frequencies.append(frequency)

# Construct the grouped frequency distribution.
grouped_frequency = pd.DataFrame({
    'Class Interval': class_intervals,
    'Frequency': class_frequencies
})

print(grouped_frequency)

print("\nTotal Frequency:",
      grouped_frequency['Frequency'].sum())
```

## 10. Calculating Class Boundaries and Midpoints

For observations recorded to the nearest whole number:

- Lower boundary = Lower class limit − 0.5
- Upper boundary = Upper class limit + 0.5
- Midpoint = (Lower boundary + Upper boundary) / 2

```python
# Calculate class boundaries.
lower_boundaries = [
    limit - 0.5 for limit in lower_limits
]

upper_boundaries = [
    limit + 0.5 for limit in upper_limits
]

# Calculate class midpoints.
midpoints = [
    (lower + upper) / 2
    for lower, upper in zip(
        lower_boundaries,
        upper_boundaries
    )
]

# Add the calculated values to the grouped table.
grouped_frequency['Lower Boundary'] = lower_boundaries

grouped_frequency['Upper Boundary'] = upper_boundaries

grouped_frequency['Midpoint'] = midpoints

print(grouped_frequency)
```

## 11. Calculating Relative and Percentage Frequencies

```python
# Calculate total frequency.
total_frequency = grouped_frequency['Frequency'].sum()

# Calculate relative frequency.
grouped_frequency['Relative Frequency'] = (
    grouped_frequency['Frequency'] / total_frequency
)

# Calculate percentage frequency.
grouped_frequency['Percentage Frequency'] = (
    grouped_frequency['Relative Frequency'] * 100
)

print(grouped_frequency)
```

## 12. Constructing a Less-than Cumulative Frequency Distribution

```python
# Calculate the running total of frequencies.
grouped_frequency['Less-than Cumulative Frequency'] = (
    grouped_frequency['Frequency'].cumsum()
)

print(grouped_frequency)
```

## 13. Constructing a More-than Cumulative Frequency Distribution

```python
# Calculate cumulative frequency from the last class backward.
grouped_frequency['More-than Cumulative Frequency'] = (
    grouped_frequency['Frequency']
    .iloc[::-1]
    .cumsum()
    .iloc[::-1]
    .to_numpy()
)

print(grouped_frequency)
```

## 14. Calculating Cumulative Relative Frequency

```python
# Calculate the running total of relative frequencies.
grouped_frequency['Cumulative Relative Frequency'] = (
    grouped_frequency['Relative Frequency'].cumsum()
)

print(grouped_frequency)
```

## 15. Calculating Frequency Density

```python
# Calculate the width of each class.
class_widths = [
    upper - lower
    for lower, upper in zip(
        lower_boundaries,
        upper_boundaries
    )
]

# Calculate frequency density.
grouped_frequency['Frequency Density'] = (
    grouped_frequency['Frequency'] / class_widths
)

print(grouped_frequency)
```

## 16. Calculating Pie Chart Sector Angles

```python
# Calculate the total frequency of learning methods.
total_learning_frequency = qualitative_frequency['Frequency'].sum()

# Calculate the sector angle of each learning method.
qualitative_frequency['Sector Angle'] = (
    qualitative_frequency['Frequency']
    / total_learning_frequency
    * 360
)

print(qualitative_frequency)

print("\nSum of sector angles:",
      qualitative_frequency['Sector Angle'].sum())
```

## 17. Constructing a Bar Chart

```python
plt.figure(figsize=(8, 5))

plt.bar(
    qualitative_frequency['Learning Method'],
    qualitative_frequency['Frequency']
)

plt.xlabel('Learning Method')

plt.ylabel('Frequency')

plt.title('Frequency Distribution of Learning Methods')

plt.show()
```

## 18. Constructing a Pie Chart

```python
plt.figure(figsize=(7, 7))

plt.pie(
    qualitative_frequency['Frequency'],
    labels=qualitative_frequency['Learning Method'],
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Distribution of Learning Methods')

plt.show()
```

## 19. Constructing a Histogram

```python
# Use class boundaries as histogram edges.
histogram_edges = (
    lower_boundaries + [upper_boundaries[-1]]
)

plt.figure(figsize=(9, 5))

# For equal-width classes, frequency can be used as height.
plt.bar(
    lower_boundaries,
    grouped_frequency['Frequency'],
    width=class_widths,
    align='edge',
    edgecolor='black'
)

plt.xlabel('Class Boundaries')

plt.ylabel('Frequency')

plt.title('Histogram of Examination Scores')

plt.xticks(histogram_edges)

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
```

## 20. Constructing a Frequency Polygon

```python
# Add zero-frequency points to close the polygon.
polygon_midpoints = (
    [midpoints[0] - class_width]
    + midpoints
    + [midpoints[-1] + class_width]
)

polygon_frequencies = (
    [0]
    + class_frequencies
    + [0]
)

plt.figure(figsize=(9, 5))

plt.plot(
    polygon_midpoints,
    polygon_frequencies,
    marker='o',
    linestyle='-'
)

plt.xlabel('Class Midpoints')

plt.ylabel('Frequency')

plt.title('Frequency Polygon of Examination Scores')

plt.grid(axis='both', linestyle='--', alpha=0.5)

plt.show()
```

## 21. Constructing a Less-than Ogive

```python
# Include the lower boundary of the first class
# with a cumulative frequency of zero.
less_than_x = [lower_boundaries[0]] + upper_boundaries

less_than_y = (
    [0]
    + grouped_frequency['Less-than Cumulative Frequency'].tolist()
)

plt.figure(figsize=(9, 5))

plt.plot(
    less_than_x,
    less_than_y,
    marker='o',
    linestyle='-'
)

plt.xlabel('Class Boundaries')

plt.ylabel('Less-than Cumulative Frequency')

plt.title('Less-than Ogive')

plt.grid(axis='both', linestyle='--', alpha=0.5)

plt.show()
```

## 22. Constructing a More-than Ogive

```python
# Include the upper boundary of the last class
# with a cumulative frequency of zero.
more_than_x = lower_boundaries + [upper_boundaries[-1]]

more_than_y = (
    grouped_frequency['More-than Cumulative Frequency'].tolist()
    + [0]
)

plt.figure(figsize=(9, 5))

plt.plot(
    more_than_x,
    more_than_y,
    marker='o',
    linestyle='-'
)

plt.xlabel('Class Boundaries')

plt.ylabel('More-than Cumulative Frequency')

plt.title('More-than Ogive')

plt.grid(axis='both', linestyle='--', alpha=0.5)

plt.show()
```

## 23. Displaying the Complete Grouped Frequency Table

```python
# Display the final grouped frequency distribution.
print("Complete Grouped Frequency Distribution:\n")

print(grouped_frequency.to_string(index=False))

# Verify the total frequency.
print("\nTotal number of observations:",
      grouped_frequency['Frequency'].sum())

# Verify the sum of relative frequencies.
print("Sum of relative frequencies:",
      grouped_frequency['Relative Frequency'].sum())

# Verify the sum of percentage frequencies.
print("Sum of percentage frequencies:",
      grouped_frequency['Percentage Frequency'].sum())
```
