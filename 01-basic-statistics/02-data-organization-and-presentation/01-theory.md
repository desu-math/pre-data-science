# Part II: Data Organization and Presentation

## 1. Introduction

After collecting data, we often obtain a collection of observations that may appear disorganized and difficult to understand. Before performing statistical analysis, we need to organize and present the data in a meaningful way.

For example, suppose we collect the examination scores of 100 students. Looking at all 100 scores individually may not immediately reveal the overall performance of the students. However, arranging the scores into a frequency distribution and presenting them graphically can help us understand the distribution more easily.

Data organization and presentation are therefore important steps in statistical analysis.

This part introduces the fundamental methods used to organize, summarize, and present statistical data.

## 2. Table of Contents

1. [Learning Objectives](#3-learning-objectives)
2. [Raw Data and Data Organization](#4-raw-data-and-data-organization)
3. [Frequency Distribution](#5-frequency-distribution)
4. [Grouped Frequency Distribution](#6-grouped-frequency-distribution)
5. [Relative and Cumulative Frequency](#7-relative-and-cumulative-frequency)
6. [Tabular Presentation](#8-tabular-presentation)
7. [Graphical Presentation](#9-graphical-presentation)
8. [Applications in Data Science](#10-applications-in-data-science)
9. [Common Mistakes](#11-common-mistakes)
10. [Formula Summary](#12-formula-summary)
11. [Practice Questions with Solutions](#13-practice-questions-with-solutions)
12. [Conclusion](#14-conclusion)

---

## 3. Learning Objectives

After studying this part, you should be able to:

- Explain why data organization is necessary in statistical analysis.
- Arrange raw data systematically.
- Construct frequency distributions for qualitative and quantitative data.
- Understand class intervals, class limits, class boundaries, class widths, and class midpoints.
- Calculate relative and cumulative frequencies.
- Present statistical information using appropriate tables.
- Construct and interpret common statistical graphs.
- Distinguish between bar charts, histograms, frequency polygons, and ogives.
- Select appropriate presentation methods depending on the nature of the data and the objective of the analysis.

---

## 4. Raw Data and Data Organization

### 4.1 What Is Raw Data?

Raw data refers to data collected from a population or sample before it has been systematically organized or summarized.

For example, suppose the examination scores of 10 students are:

45, 60, 55, 70, 45, 80, 65, 55, 90, 60

These observations represent raw data.

Although the information is available, identifying patterns and understanding the overall distribution may not be easy.

### 4.2 What Is Data Organization?

Data organization is the process of arranging collected observations into a systematic form to make them easier to understand, analyze, and interpret.

For example, we can arrange the previous scores in ascending order:

45, 45, 55, 55, 60, 60, 65, 70, 80, 90

This simple arrangement already makes some features of the data easier to observe.

### 4.3 Importance of Data Organization

Data organization helps us to:

1. Simplify large collections of observations.
2. Identify patterns and repeated values.
3. Understand the distribution of data.
4. Detect unusual observations and possible errors.
5. Prepare data for further statistical analysis.
6. Communicate information more effectively.

---

## 5. Frequency Distribution

### 5.1 What Is Frequency?

Frequency refers to the number of times a particular value or category occurs in a dataset.

For example, consider the examination scores:

40, 50, 40, 60, 50, 40, 70, 60, 50, 40

The value 40 occurs four times. Therefore, its frequency is 4.

### 5.2 What Is a Frequency Distribution?

A frequency distribution is a table that organizes data by showing the different values or categories and their corresponding frequencies.

For the previous examination scores:

| Score | Frequency |
|---|---:|
| 40 | 4 |
| 50 | 3 |
| 60 | 2 |
| 70 | 1 |
| **Total** | **10** |

The total frequency must equal the total number of observations.

In this example:

Total frequency = 4 + 3 + 2 + 1 = 10

Generally:

Σf = n

Where:

- f = frequency of a value or class.
- n = total number of observations.

### 5.3 Types of Frequency Distributions

Frequency distributions can be constructed for different types of data.

#### A. Qualitative Frequency Distribution

Used when observations belong to categories.

Example: Preferred learning method among students.

| Learning Method | Frequency |
|---|---:|
| Online | 30 |
| Face-to-face | 45 |
| Hybrid | 25 |
| **Total** | **100** |

Each observation should belong to one appropriate category, and all relevant categories should be represented.

#### B. Discrete Quantitative Frequency Distribution

Used when quantitative data consist of distinct countable values.

Example: Number of children in 20 households.

| Number of Children | Frequency |
|---|---:|
| 0 | 2 |
| 1 | 5 |
| 2 | 7 |
| 3 | 4 |
| 4 | 2 |
| **Total** | **20** |

#### C. Continuous Grouped Frequency Distribution

Used when continuous quantitative data are organized into class intervals.

For example, suppose we collect the examination scores of 40 students.

| Score Interval | Frequency |
|---|---:|
| 20–29 | 4 |
| 30–39 | 8 |
| 40–49 | 12 |
| 50–59 | 10 |
| 60–69 | 6 |
| **Total** | **40** |

Instead of displaying every distinct observation, we group the values into intervals.

This makes large datasets easier to summarize and interpret.

---

## 6. Grouped Frequency Distribution

When the dataset contains many different numerical values, constructing a separate row for every value may not be convenient.

Grouping observations into class intervals provides a more compact representation.

To construct a grouped frequency distribution, we need to understand several important terms.

### 6.1 Class Interval

A class interval is a range of values used to group observations in a frequency distribution.

For example:

20–29, 30–39, 40–49, and 50–59.

Each interval represents a particular group of observations.

### 6.2 Class Limits

Class limits are the smallest and largest values that can belong to a class.

For the class interval 40–49:

- Lower class limit = 40
- Upper class limit = 49

### 6.3 Class Boundaries

Class boundaries are the actual endpoints that separate consecutive classes without gaps or overlaps.

Suppose examination scores are recorded to the nearest whole number.

Consider:

| Class Interval |
|---|
| 40–49 |
| 50–59 |
| 60–69 |

The upper limit of the first class is 49, while the lower limit of the second class is 50.

The difference is 1. To remove this gap, we use the midpoint between the two adjacent limits:

(49 + 50)/2 = 49.5

Therefore, the class boundaries become:

| Class Interval | Lower Boundary | Upper Boundary |
|---|---:|---:|
| 40–49 | 39.5 | 49.5 |
| 50–59 | 49.5 | 59.5 |
| 60–69 | 59.5 | 69.5 |

For values recorded to the nearest whole number, we subtract 0.5 from the lower class limit and add 0.5 to the upper class limit.

This adjustment depends on the precision at which observations are recorded.

### 6.4 Class Width

Class width is the difference between the upper and lower class boundaries.

Formula:

Class width = Upper class boundary − Lower class boundary

Example:

For the class interval 40–49:

Class width = 49.5 − 39.5 = 10

For equal-width classes, we can also find the width by subtracting consecutive lower class limits.

For example:

50 − 40 = 10

### 6.5 Class Midpoint

The class midpoint is the central value of a class interval.

It is calculated as the average of the lower and upper class boundaries.

Formula:

Class midpoint = (Lower boundary + Upper boundary)/2

Example:

For the class interval 40–49:

Midpoint = (39.5 + 49.5)/2 = 44.5

The midpoint represents the center of the class and is useful in constructing frequency polygons and performing certain statistical calculations.

### 6.6 Range

The range measures the difference between the largest and smallest observations.

Formula:

Range = Maximum value − Minimum value

Example:

Suppose the smallest examination score is 20 and the largest is 90.

Range = 90 − 20 = 70

The range gives us an idea of how widely the observations are spread.

### 6.7 Number of Classes

The number of classes determines how many intervals we use to organize the observations.

One commonly used guideline is Sturges' rule:

k = 1 + 3.322 log₁₀(n)

Where:

- k = approximate number of classes.
- n = number of observations.
- log₁₀ = logarithm to base 10.

The result is rounded to a suitable whole number.

Sturges' rule is a guideline rather than a strict requirement. The researcher may adjust the number of classes depending on the dataset and the purpose of the presentation.

### 6.8 Approximate Class Width

After selecting the number of classes, we can estimate the class width.

Formula:

Class width ≈ Range / Number of classes

Example:

Suppose:

- Range = 80
- Number of classes = 8

Then:

Class width ≈ 80/8 = 10

The width may be adjusted to a convenient value when constructing the final frequency distribution.

### 6.9 Characteristics of a Good Grouped Frequency Distribution

A good grouped frequency distribution should satisfy the following conditions:

1. Classes should not overlap.
2. Every observation should belong to an appropriate class.
3. Class intervals should cover the entire range of observations.
4. Class widths should be suitable for the dataset.
5. The number of classes should be reasonable.
6. Class intervals should be arranged in an understandable order.

---

## 7. Relative and Cumulative Frequency

Frequency tells us how many observations belong to a particular category or class.

However, sometimes we want to understand the proportion of observations belonging to a category or the number of observations accumulated up to a particular class.

This leads to relative and cumulative frequencies.

### 7.1 Relative Frequency

Relative frequency represents the proportion of the total observations belonging to a particular value or class.

Formula:

Relative frequency = Frequency / Total frequency

Or:

RF = f/n

Where:

- f = frequency of a particular class.
- n = total number of observations.

Example:

Suppose 40 students are classified according to their examination scores.

| Score | Frequency |
|---|---:|
| 20–29 | 4 |
| 30–39 | 8 |
| 40–49 | 12 |
| 50–59 | 10 |
| 60–69 | 6 |
| **Total** | **40** |

The relative frequency of the class 40–49 is:

RF = 12/40 = 0.30

Therefore, 30% of the students belong to this class.

### 7.2 Percentage Frequency

Percentage frequency expresses relative frequency as a percentage.

Formula:

Percentage frequency = Relative frequency × 100

Or:

Percentage frequency = (f/n) × 100%

For the class 40–49:

Percentage frequency = (12/40) × 100% = 30%

The sum of all relative frequencies must equal 1.

The sum of all percentage frequencies must equal 100%.

### 7.3 Cumulative Frequency

Cumulative frequency is the running total of frequencies up to a particular class.

It tells us how many observations have accumulated up to that class.

Consider:

| Score | Frequency | Less-than Cumulative Frequency |
|---|---:|---:|
| 20–29 | 4 | 4 |
| 30–39 | 8 | 12 |
| 40–49 | 12 | 24 |
| 50–59 | 10 | 34 |
| 60–69 | 6 | 40 |

The cumulative frequencies are obtained by adding each frequency to the previous cumulative total.

For example:

- First class: 4
- Second class: 4 + 8 = 12
- Third class: 12 + 12 = 24
- Fourth class: 24 + 10 = 34
- Fifth class: 34 + 6 = 40

The final cumulative frequency must equal the total number of observations.

### 7.4 Less-than Cumulative Frequency

Less-than cumulative frequency gives the number of observations below the upper boundary of a particular class.

It is calculated by adding frequencies from the first class to the current class.

The less-than cumulative frequency is non-decreasing.

For the previous example:

| Upper Class Boundary | Less-than Cumulative Frequency |
|---|---:|
| 29.5 | 4 |
| 39.5 | 12 |
| 49.5 | 24 |
| 59.5 | 34 |
| 69.5 | 40 |

### 7.5 More-than Cumulative Frequency

More-than cumulative frequency gives the number of observations at or above the lower boundary of a particular class.

It is calculated by adding frequencies from the current class to the final class.

For the same example:

| Lower Class Boundary | More-than Cumulative Frequency |
|---|---:|
| 19.5 | 40 |
| 29.5 | 36 |
| 39.5 | 28 |
| 49.5 | 16 |
| 59.5 | 6 |

The more-than cumulative frequency is non-increasing.

### 7.6 Cumulative Relative Frequency

Cumulative relative frequency represents the proportion of observations accumulated up to a particular class.

Formula:

Cumulative relative frequency = Cumulative frequency / Total frequency

The final cumulative relative frequency must equal 1.

---

## 8. Tabular Presentation

### 8.1 What Is Tabular Presentation?

Tabular presentation is the method of organizing statistical information into rows and columns.

Tables allow readers to understand, compare, and interpret information systematically.

### 8.2 Components of a Statistical Table

A well-constructed statistical table generally contains:

1. **Table number:** Identifies the table.
2. **Title:** Describes the information presented.
3. **Column headings:** Identify the information in each column.
4. **Row headings:** Identify the categories or groups represented in rows.
5. **Body:** Contains the actual data.
6. **Units:** Indicate the measurement units, where necessary.
7. **Source:** Identifies where the data originated.
8. **Footnotes:** Provide additional explanations when necessary.

### 8.3 Characteristics of a Good Statistical Table

A good table should be:

- Clear and understandable.
- Properly titled.
- Correctly labeled.
- Organized systematically.
- Accurate and consistent.
- Easy to compare and interpret.
- Free from unnecessary information.

---

## 9. Graphical Presentation

### 9.1 What Is Graphical Presentation?

Graphical presentation is the use of visual representations to communicate statistical information.

Graphs help us identify patterns, compare groups, understand distributions, and communicate findings effectively.

Different types of data and analytical objectives require different graphical methods.

### 9.2 Bar Chart

A bar chart represents categorical or discrete data using rectangular bars.

The height or length of each bar represents the corresponding frequency or value.

Example:

Suppose students prefer the following learning methods:

| Learning Method | Frequency |
|---|---:|
| Online | 30 |
| Face-to-face | 45 |
| Hybrid | 25 |

A bar chart can visually compare the number of students preferring each learning method.

**Important characteristics:**

- Bars are separated by spaces.
- Bar height represents frequency or another measured quantity.
- Categories are displayed along one axis.
- Bar charts are useful for comparing categories.

### 9.3 Pie Chart

A pie chart represents the relative proportions of categories within a whole.

The entire circle represents 100% of the observations.

Each category is represented by a sector whose angle depends on its frequency.

Formula:

Sector angle = (Frequency / Total frequency) × 360°

Example:

Suppose 40 students prefer different learning methods:

| Learning Method | Frequency |
|---|---:|
| Online | 20 |
| Face-to-face | 12 |
| Hybrid | 8 |
| **Total** | **40** |

For online learning:

Sector angle = (20/40) × 360° = 180°

For face-to-face learning:

Sector angle = (12/40) × 360° = 108°

For hybrid learning:

Sector angle = (8/40) × 360° = 72°

The sum of all sector angles must equal 360°.

Pie charts are useful when the objective is to show how a whole is divided into different categories.

### 9.4 Histogram

A histogram represents the frequency distribution of continuous quantitative data using adjacent rectangles.

The horizontal axis represents class intervals, while the vertical axis represents frequencies or frequency densities.

**Important characteristics:**

- Rectangles are adjacent, without spaces between consecutive classes.
- The horizontal axis represents numerical intervals.
- The vertical axis represents frequency or frequency density.
- The area of each rectangle represents the frequency of the corresponding class.

#### Histogram with Equal Class Widths

When all class intervals have equal widths, frequencies can be represented directly by the heights of the rectangles.

#### Histogram with Unequal Class Widths

When class intervals have unequal widths, using frequencies directly as bar heights can produce misleading comparisons.

Instead, we use frequency density.

Formula:

Frequency density = Frequency / Class width

The area of each rectangle is:

Area = Class width × Frequency density

Therefore:

Area = Frequency

This ensures that the area of each rectangle remains proportional to the number of observations in its class.

**Example:**

Consider:

| Class Interval | Frequency | Class Width | Frequency Density |
|---|---:|---:|---:|
| 0–10 | 20 | 10 | 2 |
| 10–30 | 30 | 20 | 1.5 |
| 30–60 | 60 | 30 | 2 |

For the first class:

Frequency density = 20/10 = 2

Area = 10 × 2 = 20

For the second class:

Frequency density = 30/20 = 1.5

Area = 20 × 1.5 = 30

For the third class:

Frequency density = 60/30 = 2

Area = 30 × 2 = 60

Notice that the rectangle areas reproduce the original frequencies.

### 9.5 Frequency Polygon

A frequency polygon is a graphical representation of a frequency distribution constructed by plotting class midpoints against their corresponding frequencies and connecting the points with straight lines.

The horizontal axis represents class midpoints, while the vertical axis represents frequencies.

**Construction idea:**

1. Calculate the midpoint of each class.
2. Place the midpoints along the horizontal axis.
3. Place the corresponding frequencies along the vertical axis.
4. Plot the points.
5. Connect consecutive points using straight lines.

Frequency polygons are useful for:

- Understanding the shape of a frequency distribution.
- Comparing two or more distributions.
- Identifying patterns in numerical data.

For unequal class widths, frequency density should be considered when the polygon is intended to represent the histogram's shape.

### 9.6 Ogive (Cumulative Frequency Curve)

An ogive is a graph that represents cumulative frequency.

It is constructed by plotting cumulative frequencies against the corresponding class boundaries.

There are two main types.

#### A. Less-than Ogive

A less-than ogive is constructed by plotting less-than cumulative frequencies against the upper class boundaries.

It increases from left to right because cumulative frequency cannot decrease.

#### B. More-than Ogive

A more-than ogive is constructed by plotting more-than cumulative frequencies against the lower class boundaries.

It decreases from left to right because the number of observations at or above successive lower boundaries cannot increase.

Ogives are useful for:

- Understanding cumulative distributions.
- Estimating the number of observations below or above a particular value.
- Comparing cumulative distributions.
- Finding certain positional measures graphically.

### 9.7 Differences Between Common Graphical Methods

| Graph | Suitable Data | Main Purpose |
|---|---|---|
| Bar chart | Qualitative or discrete quantitative | Comparing categories or values |
| Pie chart | Categorical data | Showing proportions of a whole |
| Histogram | Continuous quantitative | Understanding the shape of a distribution |
| Frequency polygon | Quantitative frequency distributions | Understanding and comparing distributions |
| Ogive | Cumulative frequency distributions | Understanding accumulated frequencies |

### 9.8 Choosing an Appropriate Graph

The appropriate graphical method depends on the nature of the data and the purpose of the analysis.

For example:

- To compare the number of students in different departments, use a bar chart.
- To show the percentage of students in different departments, use a pie chart.
- To understand the distribution of examination scores, use a histogram.
- To compare two examination score distributions, use frequency polygons or comparable histograms.
- To determine how many students scored below a particular value, use a less-than ogive.

There is no single graph that is appropriate for every statistical situation.

---

## 10. Applications in Data Science

Data organization and presentation are essential in data science because they help transform raw observations into understandable information.

### 10.1 Exploratory Data Analysis

Exploratory Data Analysis (EDA) involves examining datasets to understand their main characteristics before conducting more advanced analysis.

Frequency distributions, tables, histograms, and other graphs are commonly used during this stage.

### 10.2 Understanding Data Distributions

Data visualization helps identify:

- Common values and categories.
- Concentrations of observations.
- Variability in the data.
- Possible unusual observations.
- Patterns that may require further investigation.

### 10.3 Detecting Data Problems

Organizing and visualizing data can reveal:

- Missing observations.
- Unexpected values.
- Incorrect categories.
- Unusual patterns.
- Possible data-entry errors.

### 10.4 Communicating Findings

Data scientists often communicate their findings to people who may not have a strong statistical background.

Well-designed tables and graphs make statistical information easier to understand and support better decision-making.

---

## 11. Common Mistakes

1. **Confusing frequency with relative frequency.**

   Frequency counts observations, while relative frequency represents their proportion of the total.

2. **Confusing class limits with class boundaries.**

   Class limits identify the smallest and largest recorded values in a class, while class boundaries define the actual endpoints separating consecutive classes.

3. **Calculating class width incorrectly.**

   Class width is the difference between the upper and lower class boundaries.

4. **Using frequencies directly as histogram heights for unequal class widths.**

   Frequency density should be used so that rectangle areas represent frequencies.

5. **Confusing bar charts with histograms.**

   Bar charts have spaces between bars, while histogram rectangles are adjacent because they represent continuous numerical intervals.

6. **Calculating cumulative frequency incorrectly.**

   Cumulative frequency is a running total, not simply the frequency of the current class.

7. **Confusing less-than and more-than cumulative frequencies.**

   Less-than cumulative frequency increases, while more-than cumulative frequency decreases.

8. **Using a graph without considering the data type.**

   The graphical method should be selected according to the nature of the data and the purpose of the analysis.

9. **Ignoring table labels and units.**

   Tables should clearly communicate what their values represent.

---

## 12. Formula Summary

| Concept | Formula |
|---|---|
| Total frequency | n = Σf |
| Range | Maximum − Minimum |
| Number of classes (Sturges' rule) | k = 1 + 3.322 log₁₀(n) |
| Approximate class width | Range / Number of classes |
| Class width | Upper boundary − Lower boundary |
| Class midpoint | (Lower boundary + Upper boundary) / 2 |
| Relative frequency | f/n |
| Percentage frequency | (f/n) × 100% |
| Cumulative relative frequency | Cumulative frequency / n |
| Frequency density | Frequency / Class width |
| Histogram rectangle area | Class width × Frequency density |
| Pie chart sector angle | (f/n) × 360° |

---

## 13. Practice Questions with Solutions

### Question 1: Frequency Distribution

The examination scores of 10 students are:

40, 50, 40, 60, 50, 40, 70, 60, 50, 40.

Construct a frequency distribution.

**Solution:**

| Score | Frequency |
|---|---:|
| 40 | 4 |
| 50 | 3 |
| 60 | 2 |
| 70 | 1 |
| **Total** | **10** |

### Question 2: Class Boundaries

Examination scores are recorded to the nearest whole number.

Determine the class boundaries of the interval 50–59.

**Solution:**

Lower boundary = 50 − 0.5 = 49.5

Upper boundary = 59 + 0.5 = 59.5

Therefore, the class boundaries are 49.5 and 59.5.

### Question 3: Class Midpoint and Width

For the class interval 40–49, determine its class midpoint and width.

**Solution:**

Class boundaries:

39.5 and 49.5

Class midpoint:

(39.5 + 49.5)/2 = 44.5

Class width:

49.5 − 39.5 = 10

### Question 4: Relative Frequency

A class contains 15 observations out of a total of 60 observations.

Calculate its relative and percentage frequencies.

**Solution:**

Relative frequency = 15/60 = 0.25

Percentage frequency = 0.25 × 100% = 25%

### Question 5: Cumulative Frequency

Consider:

| Class | Frequency |
|---|---:|
| 10–19 | 5 |
| 20–29 | 8 |
| 30–39 | 12 |
| 40–49 | 5 |

Construct the less-than cumulative frequency distribution.

**Solution:**

| Class | Frequency | Cumulative Frequency |
|---|---:|---:|
| 10–19 | 5 | 5 |
| 20–29 | 8 | 13 |
| 30–39 | 12 | 25 |
| 40–49 | 5 | 30 |

The final cumulative frequency is 30, equal to the total number of observations.

### Question 6: Histogram Frequency Density

Consider:

| Class Interval | Frequency |
|---|---:|
| 0–10 | 20 |
| 10–30 | 30 |
| 30–60 | 60 |

Calculate the frequency density of each class.

**Solution:**

First class:

20/10 = 2

Second class:

30/20 = 1.5

Third class:

60/30 = 2

The frequency densities are 2, 1.5, and 2, respectively.

### Question 7: Choosing a Graph

A researcher wants to show the number of students belonging to different departments.

Which graph is most appropriate?

**Solution:**

A bar chart is appropriate because department membership is categorical data, and the objective is to compare the number of students in each category.

### Question 8: Cumulative Distribution

A researcher wants to determine how many households earn less than a specified income level.

Which graphical method is appropriate?

**Solution:**

A less-than ogive is appropriate because it represents cumulative frequency against upper class boundaries.

---

## 14. Conclusion

Data organization and presentation transform raw observations into meaningful statistical information.

Frequency distributions help summarize data, relative frequencies describe proportions, and cumulative frequencies show how observations accumulate across classes.

Tables and graphs provide effective ways to communicate statistical information. Selecting the appropriate presentation method depends on the type of data and the objective of the analysis.

These concepts form an important foundation for further statistical topics, including measures of central tendency, measures of dispersion, and exploratory data analysis.

Understanding how to organize and present data is also an essential skill for anyone preparing to work in data science.
