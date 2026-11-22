# Part II: Data Organization and Presentation

## 1. Introduction

Imagine that a researcher collects the monthly income of 100 households in a particular town.

The collected information may look like this:

```text
12000, 15000, 10000, 18000, 12000, 20000, 15000,
10000, 14000, 18000, 12000, 16000, 15000, 20000, ...
```

This is called **raw data** because the observations have been collected but have not yet been systematically organized or summarized.

Although the information contains useful facts, understanding its overall pattern may be difficult.

For example:

- How many households earn less than 15,000 Birr?
- Which income level occurs most frequently?
- How are the observations distributed?
- What proportion of households earns between 15,000 and 20,000 Birr?

To answer these questions easily, we need to organize and present the collected data.

**Data organization and presentation** involve arranging raw data systematically and displaying it in a form that makes information easier to understand, compare, and interpret.

This is an important step in statistical analysis and Data Science because meaningful analysis begins with understanding the structure and characteristics of the available data.

---

## 2. Table of Contents

1. [Learning Objectives](#3-learning-objectives)
2. [Raw Data and Data Organization](#4-raw-data-and-data-organization)
3. [Frequency Distribution](#5-frequency-distribution)
4. [Frequency Distribution for Qualitative Data](#6-frequency-distribution-for-qualitative-data)
5. [Frequency Distribution for Quantitative Discrete Data](#7-frequency-distribution-for-quantitative-discrete-data)
6. [Frequency Distribution for Quantitative Continuous Data](#8-frequency-distribution-for-quantitative-continuous-data)
7. [Cumulative and Relative Frequency Distributions](#9-cumulative-and-relative-frequency-distributions)
8. [Tabular Presentation of Data](#10-tabular-presentation-of-data)
9. [Graphical Presentation of Data](#11-graphical-presentation-of-data)
10. [Choosing an Appropriate Presentation Method](#12-choosing-an-appropriate-presentation-method)
11. [Importance in Data Science](#13-importance-in-data-science)
12. [Common Mistakes](#14-common-mistakes)
13. [Formula and Concept Summary](#15-formula-and-concept-summary)
14. [Practice Questions with Solutions](#16-practice-questions-with-solutions)
15. [Conclusion](#17-conclusion)

---

## 3. Learning Objectives

After studying this part, you should be able to:

- Explain raw data and why data organization is necessary.
- Arrange raw observations systematically.
- Explain frequency and frequency distributions.
- Construct frequency distributions for qualitative and quantitative data.
- Distinguish between discrete and continuous frequency distributions.
- Understand class intervals, class limits, class boundaries, class width, and class midpoints.
- Calculate relative and cumulative frequencies.
- Present data using appropriate statistical tables.
- Understand bar charts, pie charts, histograms, frequency polygons, and ogives.
- Distinguish between different graphical presentation methods.
- Select suitable tables and graphs for different types of data.

---

# 4. Raw Data and Data Organization

## 4.1 What Is Raw Data?

Raw data is data collected from a statistical investigation before it has been systematically arranged, summarized, or analyzed.

For example, suppose a researcher records the number of children in 12 selected households:

```text
2, 3, 1, 2, 4, 2, 3, 1, 2, 5, 3, 2
```

These observations represent the original collected information.

Although the data are available, their pattern is not immediately clear.

For instance, we may want to know how many households have two children or how many households have more than three children.

Organizing the observations helps answer such questions.

## 4.2 What Is Data Organization?

Data organization is the process of arranging collected observations systematically so that their characteristics and patterns become easier to understand.

Common data organization techniques include:

- Arranging observations in ascending or descending order.
- Constructing frequency distributions.
- Grouping observations into class intervals.
- Presenting information using statistical tables.

### Example: Arranging Raw Data

Consider the following observations representing the number of children in 12 households:

```text
2, 3, 1, 2, 4, 2, 3, 1, 2, 5, 3, 2
```

We can arrange them in ascending order:

```text
1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5
```

This arrangement makes the distribution easier to observe.

We can immediately see that:

- The smallest observation is 1.
- The largest observation is 5.
- The value 2 appears frequently.
- There are no observations equal to 6 or greater.

Arranging data in ascending or descending order is a simple but useful way of organizing raw observations.

## 4.3 Why Is Data Organization Necessary?

Data organization is important because it:

1. Makes large datasets easier to understand.
2. Helps identify repeated values and patterns.
3. Makes comparisons easier.
4. Helps detect unusual or unexpected observations.
5. Provides a foundation for statistical analysis.
6. Makes data presentation more effective.

**Important:** Data organization does not necessarily change the information contained in the original observations. It changes how the information is arranged and displayed.

---

# 5. Frequency Distribution

## 5.1 What Is Frequency?

Frequency is the number of times a particular value or category appears in a dataset.

For example, consider the following observations:

```text
2, 3, 1, 2, 4, 2, 3, 1, 2, 5, 3, 2
```

The value 2 appears five times.

Therefore, the frequency of 2 is 5.

Similarly:

- Frequency of 1 = 2.
- Frequency of 2 = 5.
- Frequency of 3 = 3.
- Frequency of 4 = 1.
- Frequency of 5 = 1.

Frequency tells us how often a particular value or category occurs.

## 5.2 What Is a Frequency Distribution?

A **frequency distribution** is a systematic arrangement of data that shows the number of times each value, category, or class interval occurs.

It summarizes raw observations by displaying their corresponding frequencies.

Consider the previous example:

| Number of Children | Frequency |
|---:|---:|
| 1 | 2 |
| 2 | 5 |
| 3 | 3 |
| 4 | 1 |
| 5 | 1 |
| **Total** | **12** |

This table is called a frequency distribution.

Instead of examining all 12 observations individually, we can understand the distribution using only five distinct values and their frequencies.

## 5.3 General Properties of a Frequency Distribution

A frequency distribution should satisfy the following properties:

1. Each observation must be represented.
2. Every observation should belong to an appropriate value or category.
3. Frequencies must be non-negative.
4. The sum of all frequencies must equal the total number of observations.

Mathematically:

**Σf = n**

Where:

- f = frequency of a value, category, or class.
- n = total number of observations.
- Σf = sum of all frequencies.

For example, if a dataset contains 12 observations, the sum of its frequencies must be 12.

This is an important check when constructing frequency distributions.

## 5.4 Types of Frequency Distribution

Frequency distributions can be constructed differently depending on the nature of the data.

The major forms considered in this part are:

1. Frequency distribution for qualitative data.
2. Frequency distribution for quantitative discrete data.
3. Frequency distribution for quantitative continuous data.

---

# 6. Frequency Distribution for Qualitative Data

Qualitative data represent categories rather than numerical quantities.

Therefore, a frequency distribution for qualitative data shows the number of observations belonging to each category.

### Example

Suppose a researcher investigates the preferred payment methods of 20 customers.

The collected observations are:

```text
Cash, Mobile Money, Cash, Bank Transfer, Mobile Money,
Cash, Mobile Money, Cash, Bank Transfer, Cash,
Mobile Money, Cash, Bank Transfer, Mobile Money,
Cash, Cash, Bank Transfer, Mobile Money, Cash,
Mobile Money
```

We can organize the observations into the following frequency distribution:

| Payment Method | Frequency |
|---|---:|
| Cash | 8 |
| Mobile Money | 7 |
| Bank Transfer | 5 |
| **Total** | **20** |

The table tells us how many customers prefer each payment method.

Notice that the categories are not numerical values. We simply count the number of observations in each category.

### Important Considerations

When constructing a frequency distribution for qualitative data:

- Each category should be clearly identified.
- Categories should not overlap.
- Every observation should belong to an appropriate category.
- The total frequency should equal the total number of observations.

For example, if we classify customers according to their preferred payment method, each customer should be assigned to the appropriate category.

---

# 7. Frequency Distribution for Quantitative Discrete Data

Quantitative discrete variables take distinct, countable numerical values.

For discrete data, we can construct a frequency distribution by listing the distinct observed values and counting how frequently each occurs.

### Example

Suppose the number of children in 20 households is recorded as follows:

```text
0, 1, 2, 2, 3, 1, 2, 4, 0, 3,
2, 1, 3, 2, 4, 1, 2, 3, 0, 2
```

We identify the distinct observed values:

```text
0, 1, 2, 3, 4
```

Then we count how frequently each value occurs.

| Number of Children | Frequency |
|---:|---:|
| 0 | 3 |
| 1 | 4 |
| 2 | 7 |
| 3 | 4 |
| 4 | 2 |
| **Total** | **20** |

This frequency distribution shows how the number of children is distributed among the 20 households.

### Important Considerations

For discrete quantitative data:

- List the distinct values.
- Arrange them in ascending order.
- Count the number of occurrences of each value.
- Check that the total frequency equals the number of observations.

For datasets with a small number of distinct values, this method is usually straightforward.

However, when a quantitative dataset contains many distinct values, listing every value separately may produce a very long table.

In such cases, grouping observations into class intervals can make the distribution easier to understand.

This leads us to grouped frequency distributions.

---

# 8. Frequency Distribution for Quantitative Continuous Data

## 8.1 Why Do We Group Continuous Data?

Consider a researcher who records the heights of 100 students.

The measurements might be:

```text
150.2, 162.5, 170.1, 155.8, 168.4, 173.2, ...
```

Since height is a continuous variable, many different values may appear.

Listing every distinct height and its frequency may produce a large table.

Instead, we can group the observations into intervals.

For example:

| Height (cm) | Frequency |
|---|---:|
| 150–159 | 15 |
| 160–169 | 35 |
| 170–179 | 30 |
| 180–189 | 20 |
| **Total** | **100** |

This is called a **grouped frequency distribution**.

It summarizes observations by showing how many values fall within each class interval.

## 8.2 Class Interval

A class interval is a range of values used to group observations in a frequency distribution.

For example:

```text
150–159
160–169
170–179
180–189
```

Each interval represents a class.

The frequency of a class is the number of observations belonging to that interval.

## 8.3 Class Limits

Class limits are the smallest and largest stated values of a class interval.

For the interval:

```text
150–159
```

- Lower class limit = 150.
- Upper class limit = 159.

The lower class limit is the smallest stated value, while the upper class limit is the largest stated value of that class.

## 8.4 Class Boundaries

Class boundaries define the actual continuous limits separating adjacent classes.

They are particularly useful when recorded data are rounded to a particular measurement unit.

Consider these classes:

```text
150–159
160–169
170–179
180–189
```

If measurements are recorded to the nearest whole centimetre, their continuous class boundaries are:

```text
149.5–159.5
159.5–169.5
169.5–179.5
179.5–189.5
```

Notice that the upper boundary of one class equals the lower boundary of the next class.

This ensures that there are no gaps or overlaps between consecutive classes.

### How Are Class Boundaries Determined?

When consecutive classes are expressed using whole-number limits, the difference between the upper limit of one class and the lower limit of the next class is 1.

Half of this difference is:

**1 / 2 = 0.5**

Therefore:

- Lower boundary = Lower class limit − 0.5.
- Upper boundary = Upper class limit + 0.5.

This adjustment is appropriate for the stated whole-number measurement precision.

For measurements recorded to another precision, the boundary adjustment must reflect the actual recording unit.

## 8.5 Class Width

Class width is the difference between the upper and lower class boundaries of a class.

It can also be determined using consecutive lower class limits when the classes have equal widths.

**Class Width = Upper Class Boundary − Lower Class Boundary**

Example:

For the class 150–159, the boundaries are 149.5 and 159.5.

Therefore:

Class width = 159.5 − 149.5 = 10.

Each class has a width of 10 cm.

For equal-width classes, the difference between consecutive lower class limits also gives the class width.

**Important:** Class width should be distinguished from the difference between the stated upper and lower class limits.

For example, 159 − 150 = 9, but the class width is 10 because the continuous boundaries are 149.5 and 159.5.

## 8.6 Class Midpoint

The class midpoint is the value exactly halfway between the lower and upper class boundaries.

It is also called the class mark.

**Class Midpoint = (Lower Class Boundary + Upper Class Boundary) / 2**

Example:

For the class 149.5–159.5:

Class midpoint = (149.5 + 159.5) / 2

Class midpoint = 154.5.

The class midpoint represents the central value of the class.

It is useful when working with grouped data, especially in later statistical calculations.

## 8.7 Number of Classes

When constructing a grouped frequency distribution, we need to decide how many class intervals to use.

The number of classes depends on:

- The total number of observations.
- The range of the data.
- The nature of the variable.
- The level of detail required.

One commonly used guideline is Sturges' Rule:

**k = 1 + 3.322 log₁₀(n)**

Where:

- k = approximate number of classes.
- n = total number of observations.
- log₁₀ = logarithm to base 10.

The calculated value is normally rounded to a suitable whole number.

This rule provides a guideline rather than a strict requirement. Other choices may be more appropriate depending on the dataset.

## 8.8 Range of Data

The range is the difference between the largest and smallest observations.

**Range = Maximum Value − Minimum Value**

Example:

Suppose the smallest recorded height is 150 cm and the largest is 189 cm.

Range = 189 − 150 = 39 cm.

The range helps us understand the spread of the observations and can assist in constructing class intervals.

A common approach to choosing an approximate class width is:

**Class Width ≈ Range / Number of Classes**

The resulting width may be adjusted to a convenient value.

## 8.9 Constructing a Grouped Frequency Distribution

A grouped frequency distribution can be constructed using the following general procedure:

1. Identify the smallest and largest observations.
2. Calculate the range.
3. Choose an appropriate number of classes.
4. Determine a suitable class width.
5. Construct non-overlapping class intervals.
6. Identify the class limits and boundaries.
7. Count the observations belonging to each class.
8. Check that the sum of frequencies equals the total number of observations.

### Example

Suppose the following table summarizes the heights of 20 students:

| Height (cm) | Frequency |
|---|---:|
| 150–159 | 3 |
| 160–169 | 6 |
| 170–179 | 7 |
| 180–189 | 4 |
| **Total** | **20** |

The corresponding class boundaries and midpoints are:

| Class Limits | Class Boundaries | Midpoint | Frequency |
|---|---|---:|---:|
| 150–159 | 149.5–159.5 | 154.5 | 3 |
| 160–169 | 159.5–169.5 | 164.5 | 6 |
| 170–179 | 169.5–179.5 | 174.5 | 7 |
| 180–189 | 179.5–189.5 | 184.5 | 4 |
| **Total** | | | **20** |

The table provides more information than simply listing the original observations.

It shows the number of students within each height interval.

## 8.10 Important Properties of Class Intervals

A good grouped frequency distribution should satisfy the following conditions:

1. **Mutually exclusive classes:** An observation should not belong to two classes simultaneously.
2. **Exhaustive classes:** Every observation should belong to one of the classes.
3. **No gaps:** The intervals should cover the relevant range of observations.
4. **Suitable number of classes:** Too many classes make the table complicated, while too few may hide important patterns.
5. **Appropriate class width:** Equal widths are often useful, although unequal widths may sometimes be necessary.

---

# 9. Cumulative and Relative Frequency Distributions

A frequency distribution can provide more information when we calculate relative and cumulative frequencies.

## 9.1 Relative Frequency

Relative frequency represents the proportion of observations belonging to a particular value, category, or class.

It tells us how large a frequency is relative to the total number of observations.

The formula is:

**Relative Frequency = Class Frequency / Total Frequency**

Or:

**RF = f / n**

Where:

- RF = Relative frequency.
- f = Frequency of a particular class.
- n = Total number of observations.

Relative frequency can also be expressed as a percentage:

**Percentage Frequency = (f / n) × 100**

### Example

Consider the following grouped frequency distribution:

| Height (cm) | Frequency |
|---|---:|
| 150–159 | 3 |
| 160–169 | 6 |
| 170–179 | 7 |
| 180–189 | 4 |
| **Total** | **20** |

For the class 150–159:

Relative frequency = 3 / 20 = 0.15.

Percentage frequency = 0.15 × 100 = 15%.

We can calculate the relative frequencies of all classes:

| Height (cm) | Frequency | Relative Frequency | Percentage |
|---|---:|---:|---:|
| 150–159 | 3 | 0.15 | 15% |
| 160–169 | 6 | 0.30 | 30% |
| 170–179 | 7 | 0.35 | 35% |
| 180–189 | 4 | 0.20 | 20% |
| **Total** | **20** | **1.00** | **100%** |

### Important Property

The sum of all relative frequencies must equal 1.

**ΣRF = 1**

Similarly, the sum of percentage frequencies must equal 100%.

**ΣPercentage Frequency = 100%**

Relative frequencies are particularly useful when comparing datasets of different sizes.

For example, comparing 20 observations with 200 observations using raw frequencies alone may be misleading. Relative frequencies allow us to compare proportions.

## 9.2 Cumulative Frequency

Cumulative frequency is the running total of frequencies up to and including a particular value or class.

It tells us how many observations are less than or equal to a given value or class boundary.

The cumulative frequency of a class is obtained by adding its frequency to the cumulative frequency of the preceding class.

**Cumulative Frequency = Previous Cumulative Frequency + Current Frequency**

For the first class:

**CF = f**

### Example

Consider the previous height distribution:

| Height (cm) | Frequency |
|---|---:|
| 150–159 | 3 |
| 160–169 | 6 |
| 170–179 | 7 |
| 180–189 | 4 |
| **Total** | **20** |

The cumulative frequencies are:

First class:

CF = 3.

Second class:

CF = 3 + 6 = 9.

Third class:

CF = 9 + 7 = 16.

Fourth class:

CF = 16 + 4 = 20.

Therefore:

| Height (cm) | Frequency | Cumulative Frequency |
|---|---:|---:|
| 150–159 | 3 | 3 |
| 160–169 | 6 | 9 |
| 170–179 | 7 | 16 |
| 180–189 | 4 | 20 |

The cumulative frequency of the third class is 16.

This means that 16 students have heights below the upper boundary of that class, assuming the stated class arrangement.

### Important Property

The final cumulative frequency must equal the total number of observations.

**Final CF = n**

## 9.3 Types of Cumulative Frequency

There are two common ways to express cumulative frequency.

### A. Less-Than Cumulative Frequency

Less-than cumulative frequency counts observations up to and including the upper boundary of each class.

For example:

| Height Below Upper Boundary (cm) | Cumulative Frequency |
|---|---:|
| 159.5 | 3 |
| 169.5 | 9 |
| 179.5 | 16 |
| 189.5 | 20 |

It answers questions such as:

- How many students have heights below 169.5 cm?
- How many observations fall below a particular upper class boundary?

### B. More-Than Cumulative Frequency

More-than cumulative frequency counts observations at or above the lower boundary of each class.

For the same data:

| Height at or Above Lower Boundary (cm) | Cumulative Frequency |
|---|---:|
| 149.5 | 20 |
| 159.5 | 17 |
| 169.5 | 11 |
| 179.5 | 4 |

For example, 11 students have heights of at least 169.5 cm.

The more-than cumulative frequency decreases as we move through the classes.

## 9.4 Cumulative Relative Frequency

Cumulative relative frequency is the running total of relative frequencies.

It can also be calculated by dividing cumulative frequency by total frequency.

**Cumulative Relative Frequency = Cumulative Frequency / Total Frequency**

Its final value must equal 1, or 100% when expressed as a percentage.

It helps us understand the proportion of observations below or above a particular class boundary.

---

# 10. Tabular Presentation of Data

## 10.1 What Is Tabular Presentation?

Tabular presentation is the systematic arrangement of data in rows and columns.

It provides a structured way of displaying information and makes comparison and interpretation easier.

Frequency distribution tables are common examples of tabular presentation.

## 10.2 Components of a Statistical Table

A properly constructed statistical table may contain the following components:

1. **Table Number:** Identifies the table.
2. **Title:** Describes the information presented.
3. **Column Headings:** Identify the information contained in each column.
4. **Row Headings:** Identify the information contained in each row.
5. **Body:** Contains the actual data.
6. **Units:** Indicate the measurement units where necessary.
7. **Source:** Identifies where the data were obtained, when applicable.
8. **Footnotes:** Provide additional explanations when necessary.

### Example

**Table 1: Distribution of Employees by Department**

| Department | Number of Employees |
|---|---:|
| Finance | 25 |
| Marketing | 20 |
| Human Resources | 15 |
| Information Technology | 30 |
| Operations | 10 |
| **Total** | **100** |

The table has a clear title, meaningful column headings, organized rows, and a total.

## 10.3 Characteristics of a Good Statistical Table

A good statistical table should:

- Have a clear and meaningful title.
- Use understandable row and column headings.
- Include measurement units where necessary.
- Present information accurately.
- Avoid unnecessary complexity.
- Make comparisons easy.
- Include the data source when appropriate.

The purpose of a statistical table is not merely to display numbers but to communicate information clearly.

---

# 11. Graphical Presentation of Data

## 11.1 What Is Graphical Presentation?

Graphical presentation is the representation of data using visual forms such as bars, sectors, lines, and other graphical structures.

Graphs help us identify patterns, compare categories, and understand distributions more easily.

Different types of graphs are appropriate for different types of data.

The main graphical methods introduced in this part are:

1. Bar chart.
2. Pie chart.
3. Histogram.
4. Frequency polygon.
5. Ogive.

## 11.2 Bar Chart

A **bar chart** is a graphical representation of categorical or discrete data using rectangular bars.

The height or length of each bar represents the frequency or another numerical quantity associated with a category or value.

### Example

Consider the following information about customers' preferred payment methods:

| Payment Method | Frequency |
|---|---:|
| Cash | 8 |
| Mobile Money | 7 |
| Bank Transfer | 5 |

A bar chart represents the categories along one axis and their corresponding frequencies along the other axis.

### Main Characteristics

- Bars are separated by spaces.
- Each bar represents a category or distinct value.
- Bar height or length represents frequency.
- Bars can be vertical or horizontal.
- Categories can be arranged in a suitable order.

### When Is a Bar Chart Appropriate?

Bar charts are particularly useful for:

- Nominal data.
- Ordinal data.
- Discrete quantitative data.

For example, a business may use a bar chart to compare the number of customers using different payment methods.

## 11.3 Pie Chart

A **pie chart** is a circular graphical representation in which a circle is divided into sectors representing the proportions of different categories.

The entire circle represents the total observations, equivalent to 100%.

Each sector represents the proportion of the total belonging to a particular category.

### Calculating Sector Angles

A complete circle contains 360 degrees.

The angle of each sector is calculated using:

**Sector Angle = (Category Frequency / Total Frequency) × 360°**

Or:

**Sector Angle = Relative Frequency × 360°**

### Example

Suppose 100 customers use the following payment methods:

| Payment Method | Frequency |
|---|---:|
| Cash | 50 |
| Mobile Money | 30 |
| Bank Transfer | 20 |
| **Total** | **100** |

For cash:

Sector angle = (50 / 100) × 360°

Sector angle = 180°.

For mobile money:

Sector angle = (30 / 100) × 360°

Sector angle = 108°.

For bank transfer:

Sector angle = (20 / 100) × 360°

Sector angle = 72°.

The three sectors together form the complete circle:

180° + 108° + 72° = 360°.

### Main Characteristics

- Represents parts of a whole.
- Each sector represents a category.
- Sector sizes are proportional to category frequencies.
- All sectors together represent 100% of the observations.

### When Is a Pie Chart Appropriate?

A pie chart is useful when:

- The data represent categories.
- The objective is to show proportions of a whole.
- The number of categories is relatively small.

A pie chart becomes difficult to interpret when it contains too many categories or sectors with very similar sizes.

## 11.4 Histogram

A **histogram** is a graphical representation of the frequency distribution of quantitative numerical data using adjacent rectangular bars.

It is commonly used for grouped continuous data.

### Example

Consider the following distribution of students' heights:

| Height (cm) | Frequency |
|---|---:|
| 150–159 | 3 |
| 160–169 | 6 |
| 170–179 | 7 |
| 180–189 | 4 |

A histogram displays:

- Class intervals along the horizontal axis.
- Frequencies along the vertical axis.
- Adjacent rectangles representing the classes.

### Main Characteristics

- Bars touch each other.
- Each bar represents a class interval.
- The horizontal axis represents numerical intervals.
- The vertical axis represents frequency or frequency density.

When all class widths are equal, the heights of the bars can represent frequencies directly.

When class widths are unequal, frequency density is generally used so that the area of each rectangle remains proportional to the class frequency.

For unequal class widths:

**Frequency Density = Frequency / Class Width**

This distinction is important because the area of a histogram bar, rather than its height alone, must represent the frequency.

### When Is a Histogram Appropriate?

Histograms are particularly useful for:

- Continuous quantitative data.
- Grouped numerical data.
- Understanding the shape of a distribution.

They help us see where observations are concentrated and how frequencies vary across numerical intervals.

## 11.5 Difference Between Bar Chart and Histogram

Although bar charts and histograms look similar, they represent different types of data.

| Bar Chart | Histogram |
|---|---|
| Commonly represents categorical or discrete data. | Commonly represents continuous quantitative data. |
| Bars are separated by spaces. | Bars touch each other. |
| Each bar represents a category or distinct value. | Each bar represents a numerical class interval. |
| Categories can be rearranged when appropriate. | Numerical intervals follow their natural order. |
| Bar height or length represents frequency. | Bar area represents frequency. |

**Remember:** A bar chart compares categories, while a histogram displays the distribution of numerical observations across intervals.

## 11.6 Frequency Polygon

A **frequency polygon** is a graphical representation of a frequency distribution obtained by plotting class midpoints against their corresponding frequencies and connecting the plotted points using straight lines.

### How Is It Constructed?

For a grouped frequency distribution:

1. Calculate the midpoint of each class.
2. Represent class midpoints along the horizontal axis.
3. Represent frequencies along the vertical axis.
4. Plot each midpoint against its corresponding frequency.
5. Connect consecutive points using straight lines.

### Example

Consider:

| Height (cm) | Midpoint | Frequency |
|---|---:|---:|
| 150–159 | 154.5 | 3 |
| 160–169 | 164.5 | 6 |
| 170–179 | 174.5 | 7 |
| 180–189 | 184.5 | 4 |

The points are:

- (154.5, 3)
- (164.5, 6)
- (174.5, 7)
- (184.5, 4)

Connecting these points produces a frequency polygon.

To close the polygon, it is common to add zero-frequency points at the midpoints of imaginary classes immediately before and after the actual classes.

### When Is a Frequency Polygon Appropriate?

It is useful for:

- Displaying grouped frequency distributions.
- Understanding the general shape of a distribution.
- Comparing two or more frequency distributions on the same graph.

## 11.7 Ogive (Cumulative Frequency Curve)

An **ogive** is a graph representing cumulative frequencies.

It is constructed by plotting cumulative frequency values against appropriate class boundaries.

There are two common types:

### A. Less-Than Ogive

A less-than ogive is constructed using:

- Upper class boundaries along the horizontal axis.
- Less-than cumulative frequencies along the vertical axis.

The plotted points are connected to form a cumulative frequency curve.

The curve generally increases because cumulative frequency cannot decrease.

### B. More-Than Ogive

A more-than ogive is constructed using:

- Lower class boundaries along the horizontal axis.
- More-than cumulative frequencies along the vertical axis.

The curve generally decreases because the number of observations at or above successive lower class boundaries becomes smaller.

### When Is an Ogive Appropriate?

Ogives are useful for:

- Understanding cumulative frequency.
- Identifying the number of observations below or above a specified value.
- Comparing cumulative distributions.

They are also useful when studying measures of position in later statistical topics.

---

# 12. Choosing an Appropriate Presentation Method

Not every presentation method is suitable for every type of data.

The choice depends on the nature of the variable and the purpose of the presentation.

| Data Type or Objective | Suitable Presentation |
|---|---|
| Nominal data | Frequency table, bar chart, pie chart |
| Ordinal data | Frequency table, ordered bar chart |
| Discrete quantitative data | Frequency table, bar chart |
| Continuous quantitative data | Grouped frequency table, histogram, frequency polygon |
| Cumulative distribution | Cumulative frequency table, ogive |
| Comparison of categories | Bar chart |
| Proportions of a whole | Pie chart |
| Shape of a numerical distribution | Histogram, frequency polygon |

A researcher should select a presentation method that communicates the information accurately and clearly.

For example, using a histogram to represent blood groups would be inappropriate because blood groups are categories rather than continuous numerical intervals.

Similarly, a pie chart may be less useful when there are many categories.

---

# 13. Importance of Data Organization and Presentation in Data Science

Data organization and presentation are important steps in the Data Science workflow.

Before applying statistical models or machine learning algorithms, data scientists must understand the structure and characteristics of their datasets.

Some important applications include:

### 13.1 Exploratory Data Analysis

Exploratory Data Analysis (EDA) involves examining and understanding datasets using summaries and visualizations.

Frequency tables, histograms, and other graphical methods help identify patterns and possible problems in the data.

### 13.2 Understanding Data Distribution

Histograms and frequency distributions help data scientists understand how numerical observations are distributed.

For example, a data scientist studying customer income can use a histogram to understand where most income observations are concentrated.

### 13.3 Detecting Data Problems

Data organization and visualization can help identify:

- Missing values.
- Unexpected categories.
- Unusual observations.
- Inconsistent data.
- Possible data entry errors.

### 13.4 Communicating Results

Tables and graphs make analytical findings easier to communicate to decision-makers.

For example, a business analyst can use a bar chart to present the number of customers in different regions.

### 13.5 Supporting Further Analysis

Organized data provide a foundation for later statistical calculations and modeling.

**Important:** Data presentation is not merely about making information attractive. Its main purpose is to communicate the characteristics of data accurately.

---

# 14. Common Mistakes

| Common Mistake | Correct Understanding |
|---|---|
| Treating raw data as already organized information. | Raw data are observations before systematic arrangement. |
| Assuming frequency means the value itself. | Frequency is the number of times a value or category occurs. |
| Forgetting to check total frequency. | The sum of frequencies must equal the number of observations. |
| Using overlapping class intervals. | Each observation should belong to exactly one class. |
| Confusing class limits and class boundaries. | Limits are stated class endpoints; boundaries define the continuous class edges. |
| Confusing class width with the difference between class limits. | Class width is determined by the class boundaries. |
| Treating relative frequency as a raw count. | Relative frequency is the proportion of observations in a class. |
| Confusing cumulative frequency with ordinary frequency. | Cumulative frequency is the running total of frequencies. |
| Using a histogram for categorical data. | Histograms are primarily used for numerical class intervals. |
| Leaving spaces between histogram bars. | Histogram bars normally touch because the intervals are continuous. |
| Using a bar chart with adjacent bars without justification. | Bar charts normally have spaces between categories. |
| Forgetting that a pie chart represents a whole. | All sectors together must represent 100% or 360°. |
| Using frequency instead of cumulative frequency in an ogive. | An ogive represents cumulative frequencies. |

---

# 15. Formula and Concept Summary

## 15.1 Frequency Distribution

**Total Frequency:**

Σf = n

Where:
- f = Frequency.
- n = Total number of observations.

## 15.2 Range

Range = Maximum Value − Minimum Value

## 15.3 Number of Classes

Sturges' Rule:

k = 1 + 3.322 log₁₀(n)

## 15.4 Class Width

Class Width = Upper Class Boundary − Lower Class Boundary

For equal-width classes:

Class Width ≈ Range / Number of Classes

## 15.5 Class Midpoint

Class Midpoint = (Lower Class Boundary + Upper Class Boundary) / 2

## 15.6 Relative Frequency

Relative Frequency = f / n

## 15.7 Percentage Frequency

Percentage Frequency = (f / n) × 100

## 15.8 Cumulative Frequency

Current Cumulative Frequency = Previous Cumulative Frequency + Current Frequency

## 15.9 Cumulative Relative Frequency

Cumulative Relative Frequency = Cumulative Frequency / Total Frequency

## 15.10 Pie Chart Sector Angle

Sector Angle = (Category Frequency / Total Frequency) × 360°

## 15.11 Histogram with Unequal Class Widths

Frequency Density = Frequency / Class Width

### Important Properties

- Sum of frequencies = Total number of observations.
- Sum of relative frequencies = 1.
- Sum of percentage frequencies = 100%.
- Final cumulative frequency = Total number of observations.
- Final cumulative relative frequency = 1.
- Sum of pie chart sector angles = 360°.

---

# 16. Practice Questions with Solutions

These questions test the concepts introduced in Part II. They focus on data organization, frequency distributions, and graphical presentation rather than measures of central tendency or dispersion, which will be studied in later parts.

## Question 1: Raw Data and Organization

A researcher records the number of customers visiting a bank during 10 consecutive days:

```text
25, 30, 25, 40, 35, 30, 25, 45, 35, 30
```

a) What is raw data?

b) Arrange the observations in ascending order.

c) Explain why arranging the observations is useful.

**Solution:**

a) Raw data are the original observations before systematic organization.

b)

```text
25, 25, 25, 30, 30, 30, 35, 35, 40, 45
```

c) Arranging observations makes repeated values, minimum and maximum observations, and general patterns easier to identify.

## Question 2: Frequency Distribution

Using the observations in Question 1, construct a frequency distribution.

**Solution:**

| Number of Customers | Frequency |
|---:|---:|
| 25 | 3 |
| 30 | 3 |
| 35 | 2 |
| 40 | 1 |
| 45 | 1 |
| **Total** | **10** |

The sum of frequencies is 10, which equals the number of observations.

## Question 3: Relative Frequency

Using Question 2, calculate the relative frequency and percentage frequency of each value.

**Solution:**

| Customers | Frequency | Relative Frequency | Percentage |
|---:|---:|---:|---:|
| 25 | 3 | 0.30 | 30% |
| 30 | 3 | 0.30 | 30% |
| 35 | 2 | 0.20 | 20% |
| 40 | 1 | 0.10 | 10% |
| 45 | 1 | 0.10 | 10% |
| **Total** | **10** | **1.00** | **100%** |

## Question 4: Cumulative Frequency

Using the frequency distribution in Question 2, construct a cumulative frequency distribution.

**Solution:**

| Customers | Frequency | Cumulative Frequency |
|---:|---:|---:|
| 25 | 3 | 3 |
| 30 | 3 | 6 |
| 35 | 2 | 8 |
| 40 | 1 | 9 |
| 45 | 1 | 10 |

The final cumulative frequency equals 10, the total number of observations.

## Question 5: Grouped Frequency Distribution

A researcher records the examination scores of students and groups them into the following classes:

| Score | Frequency |
|---|---:|
| 40–49 | 4 |
| 50–59 | 6 |
| 60–69 | 10 |
| 70–79 | 7 |
| 80–89 | 3 |

Identify:

a) The number of classes.

b) The total number of observations.

c) The lower and upper class limits of the third class.

d) The class boundaries of the third class, assuming scores are recorded to the nearest whole number.

e) The class width.

f) The midpoint of the third class.

**Solution:**

a) Number of classes = 5.

b) Total observations = 4 + 6 + 10 + 7 + 3 = 30.

c) Third class = 60–69.

- Lower class limit = 60.
- Upper class limit = 69.

d) Class boundaries = 59.5–69.5.

e) Class width = 69.5 − 59.5 = 10.

f) Midpoint = (59.5 + 69.5) / 2 = 64.5.

## Question 6: Graph Selection

Choose an appropriate graphical presentation method for each situation.

a) Comparing the number of customers using different payment methods.

b) Presenting the distribution of students' heights.

c) Showing the proportion of employees working in different departments.

d) Presenting the cumulative frequency of examination scores.

**Solution:**

a) Bar chart.

b) Histogram.

c) Pie chart.

d) Ogive.

## Question 7: Bar Chart vs. Histogram

Explain two differences between a bar chart and a histogram.

**Solution:**

1. Bar charts commonly represent categorical or discrete data, while histograms represent grouped numerical data, especially continuous data.
2. Bar charts normally have spaces between bars, while histogram bars touch because the intervals are continuous.

## Question 8: Pie Chart

A company has 200 employees distributed among three departments:

| Department | Employees |
|---|---:|
| Finance | 50 |
| Marketing | 70 |
| Operations | 80 |

Calculate the sector angle for each department.

**Solution:**

Finance:

(50 / 200) × 360° = 90°.

Marketing:

(70 / 200) × 360° = 126°.

Operations:

(80 / 200) × 360° = 144°.

Total:

90° + 126° + 144° = 360°.

## Question 9: Understanding Cumulative Frequency

A grouped frequency distribution has the following cumulative frequencies:

| Score | Cumulative Frequency |
|---|---:|
| Below 50 | 5 |
| Below 60 | 12 |
| Below 70 | 22 |
| Below 80 | 30 |

a) How many observations are below 70?

b) How many observations are below 80?

c) Explain why cumulative frequency cannot decrease as we move through successive upper class boundaries.

**Solution:**

a) 22 observations.

b) 30 observations.

c) Because each cumulative frequency includes all observations counted in the preceding classes plus the observations in the current class. Therefore, the running total can only increase or remain unchanged.

## Question 10: Integrated Understanding

A researcher collects the monthly household incomes of 40 households.

a) Explain why the original observations are called raw data.

b) Explain why a frequency distribution may be more useful than listing all 40 observations.

c) If the researcher groups the observations into income intervals, what type of frequency distribution is being constructed?

d) Which graph would be suitable for presenting the grouped income distribution?

e) If the researcher wants to show the percentage of households in each income interval, which frequency measure should be used?

**Solution:**

a) They are raw data because they are the original observations before systematic arrangement.

b) A frequency distribution summarizes repeated values or intervals, making patterns easier to understand.

c) A grouped frequency distribution.

d) A histogram.

e) Relative frequency or percentage frequency.

---

# 17. Conclusion

Data organization and presentation are essential steps in statistical analysis.

Raw observations may contain valuable information, but understanding their characteristics becomes easier when they are systematically arranged and presented.

In this part, we studied:

- Raw data and data organization.
- Frequency and frequency distributions.
- Frequency distributions for qualitative, discrete, and continuous data.
- Class intervals, limits, boundaries, widths, and midpoints.
- Relative and cumulative frequencies.
- Statistical tables.
- Bar charts, pie charts, histograms, frequency polygons, and ogives.

These concepts provide the foundation for exploring and understanding datasets before applying more advanced statistical techniques.

In Data Science, this knowledge is particularly useful during Exploratory Data Analysis (EDA), where we examine datasets to understand their structure, identify patterns, and detect possible problems.

**Remember: Organized data are easier to understand, compare, communicate, and analyze.**
