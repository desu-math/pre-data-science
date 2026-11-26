# Part III: Measures of Central Tendency
---
## 1. Introduction

**How can we represent a large collection of observations using one meaningful value?**

Imagine that a school has recorded the examination scores of 100 students. Looking at every individual score may not give us a quick understanding of the overall performance of the students.

Instead, we may calculate a single value that represents the center or typical value of the observations.

This is the main purpose of **measures of central tendency**.

Measures of central tendency are statistical measures used to identify a central or representative value within a dataset. They help summarize data and make comparisons easier.

The three most commonly used measures are:

1. Arithmetic Mean
2. Median
3. Mode

Each measure describes the center of a dataset in a different way. Understanding their differences helps us select the most appropriate measure for a particular statistical problem.

---
## 2. Table of Contents

- [3. Learning Objectives](#3-learning-objectives)
- [4. Arithmetic Mean](#4-arithmetic-mean)
  - [4.1 Definition](#41-definition)
  - [4.2 Mean for Ungrouped Data](#42-mean-for-ungrouped-data)
  - [4.3 Mean for Frequency Distribution](#43-mean-for-frequency-distribution)
  - [4.4 Mean for Grouped Data](#44-mean-for-grouped-data)
  - [4.5 Important Properties of the Mean](#45-important-properties-of-the-mean)
- [5. Weighted Arithmetic Mean](#5-weighted-arithmetic-mean)
- [6. Median](#6-median)
  - [6.1 Median for Ungrouped Data](#61-median-for-ungrouped-data)
  - [6.2 Median for Discrete Frequency Distribution](#62-median-for-discrete-frequency-distribution)
  - [6.3 Median for Grouped Data](#63-median-for-grouped-data)
- [7. Mode](#7-mode)
  - [7.1 Mode for Ungrouped and Discrete Data](#71-mode-for-ungrouped-and-discrete-data)
  - [7.2 Mode for Grouped Data](#72-mode-for-grouped-data)
- [8. Relationship Between Mean, Median, and Mode](#8-relationship-between-mean-median-and-mode)
- [9. Choosing an Appropriate Measure](#9-choosing-an-appropriate-measure)
- [10. Applications in Data Science](#10-applications-in-data-science)
- [11. Common Mistakes](#11-common-mistakes)
- [12. Formula Summary](#12-formula-summary)
- [13. Practice Questions](#13-practice-questions)
- [14. Conclusion](#14-conclusion)

---
## 3. Learning Objectives

After studying this part, you should be able to:

- Explain the meaning and purpose of measures of central tendency.
- Calculate arithmetic means for different types of data.
- Understand and calculate weighted arithmetic means.
- Determine the median of ungrouped, discrete, and grouped data.
- Identify the mode and calculate it for grouped data.
- Explain the relationship between mean, median, and mode.
- Select an appropriate measure of central tendency for a given dataset.
- Understand how these measures are applied in data science.

---
## 4. Arithmetic Mean

### 4.1 Definition

The **arithmetic mean** is a measure of central tendency obtained by dividing the sum of all observations by the total number of observations.

In simple terms, it represents the equal share of the total value among all observations.

For example, suppose five students scored:

10, 20, 30, 40, 50

The total score is:

10 + 20 + 30 + 40 + 50 = 150

If the total score were distributed equally among the five students, each student would receive:

150 / 5 = 30

Therefore, the arithmetic mean is 30.

### 4.2 Mean for Ungrouped Data

For a population, the arithmetic mean is calculated using:

μ = Σx / N

For a sample, it is calculated using:

x̄ = Σx / n

Where:

- μ = population mean
- x̄ = sample mean
- Σx = sum of all observations
- N = population size
- n = sample size

**Worked Example**

Consider the following examination scores:

12, 15, 18, 20, 25

Find the arithmetic mean.

**Step 1: Calculate the sum of observations.**

Σx = 12 + 15 + 18 + 20 + 25 = 90

**Step 2: Determine the number of observations.**

n = 5

**Step 3: Apply the formula.**

x̄ = Σx / n

x̄ = 90 / 5 = 18

Therefore, the arithmetic mean is **18**.

### 4.3 Mean for Discrete Frequency Distribution

Sometimes, observations are presented together with their frequencies rather than as a raw dataset.

In this situation, each observation must be multiplied by its corresponding frequency.

The formula is:

x̄ = Σfx / Σf

Where:

- x = observed value
- f = frequency of the observation
- fx = product of the observation and its frequency
- Σf = total frequency

**Worked Example**

The following table shows the number of books read by students during a particular period.

| Number of Books (x) | Frequency (f) | fx |
|---:|---:|---:|
| 1 | 2 | 2 |
| 2 | 3 | 6 |
| 3 | 4 | 12 |
| 4 | 1 | 4 |
| **Total** | **10** | **24** |

Using the formula:

x̄ = Σfx / Σf

x̄ = 24 / 10 = 2.4

Therefore, the average number of books read is **2.4 books per student**.

### 4.4 Mean for Grouped Data

When continuous observations are organized into class intervals, individual observations are no longer available.

Therefore, we use the midpoint of each class interval as its representative value.

The midpoint is calculated as:

m = (Lower class limit + Upper class limit) / 2

The grouped arithmetic mean is:

x̄ = Σfm / Σf

Where:

- m = class midpoint
- f = class frequency
- fm = product of frequency and midpoint
- Σf = total frequency

**Worked Example**

Consider the following grouped frequency distribution:

| Class Interval | Frequency (f) | Midpoint (m) | fm |
|---|---:|---:|---:|
| 10–20 | 2 | 15 | 30 |
| 20–30 | 5 | 25 | 125 |
| 30–40 | 8 | 35 | 280 |
| 40–50 | 5 | 45 | 225 |
| **Total** | **20** | | **660** |

Using the formula:

x̄ = Σfm / Σf

x̄ = 660 / 20 = 33

Therefore, the estimated arithmetic mean is **33**.

**Important:** The mean calculated from grouped data is generally an estimate because the individual observations within each class are unknown. We use class midpoints to represent them.

### 4.5 Important Properties of the Mean

Understanding the properties of the arithmetic mean helps us understand how it behaves when observations change.

#### Property 1: The Sum of Deviations from the Mean Is Zero

The sum of the differences between individual observations and their arithmetic mean is always zero.

Σ(x − x̄) = 0

**Example**

Consider:

5, 10, 15, 20, 25

The mean is:

x̄ = 15

The deviations are:

| Observation (x) | Deviation (x − x̄) |
|---:|---:|
| 5 | -10 |
| 10 | -5 |
| 15 | 0 |
| 20 | 5 |
| 25 | 10 |
| **Total** | **0** |

The negative deviations balance the positive deviations.

This property explains why the mean represents a balancing point of the observations.

#### Property 2: Adding a Constant to Every Observation

If a constant c is added to every observation, the new mean increases by c.

New mean = Old mean + c

**Example**

Suppose the original observations are:

5, 10, 15, 20, 25

The original mean is 15.

If we add 5 to every observation, the new dataset becomes:

10, 15, 20, 25, 30

The new mean is:

100 / 5 = 20

Therefore:

New mean = 15 + 5 = 20

#### Property 3: Multiplying Every Observation by a Constant

If every observation is multiplied by a constant k, the new mean is also multiplied by k.

New mean = k × Old mean

For example, if every observation is multiplied by 3 and the original mean is 15:

New mean = 3 × 15 = 45

#### Property 4: The Mean Uses Every Observation

Every observation contributes to the calculation of the arithmetic mean.

This makes the mean useful when we want to represent the entire dataset.

However, because every observation contributes to its calculation, unusually large or small values can influence it. This is why the mean may not always represent a typical observation well.

#### Property 5: The Mean Minimizes the Sum of Squared Deviations

Among all possible single values a, the arithmetic mean minimizes the sum of squared differences between observations and that value.

In mathematical form:

Σ(x − x̄)² ≤ Σ(x − a)²

This means that the mean is the value around which the total squared deviations are smallest.

This property is particularly important in statistics and data science, where squared errors are frequently used.

---
## 5. Weighted Arithmetic Mean

### 5.1 Definition

In an ordinary arithmetic mean, every observation has equal importance.

However, some situations require observations to contribute differently to the final average.

The **weighted arithmetic mean** is a measure of central tendency in which each observation is assigned a weight according to its relative importance or contribution.

Its formula is:

x̄w = Σwx / Σw

Where:

- x = observation
- w = weight assigned to the observation
- wx = product of observation and its weight
- Σw = sum of all weights

### 5.2 Worked Example

Suppose a student's final grade is determined by three assessments:

| Assessment | Score (x) | Weight (w) | wx |
|---|---:|---:|---:|
| Assignment | 80 | 20 | 1600 |
| Midterm | 70 | 30 | 2100 |
| Final Exam | 90 | 50 | 4500 |
| **Total** | | **100** | **8200** |

The weighted mean is:

x̄w = Σwx / Σw

x̄w = 8200 / 100 = 82

Therefore, the student's weighted average is **82**.

Notice that the final examination contributes more because it has a greater weight.

**Important:** The ordinary arithmetic mean is a special case of the weighted mean when all observations have equal weights.

### 5.3 Applications of Weighted Mean

Weighted means are useful when observations do not contribute equally.

Examples include:

- Calculating students' cumulative grade point averages using credit hours.
- Calculating average prices when different quantities are purchased.
- Calculating portfolio returns when investments have different proportions.
- Calculating overall performance scores using different assessment weights.

---
## 6. Median

### 6.1 Definition

The **median** is the middle value of a dataset after the observations have been arranged in ascending or descending order.

Unlike the arithmetic mean, the median is determined by the position of observations rather than by adding all their values.

It divides an ordered dataset into two equal parts:

- Approximately half of the observations are at or below the median.
- Approximately half of the observations are at or above the median.

### 6.2 Median for Ungrouped Data

The calculation of the median depends on whether the number of observations is odd or even.

**Case 1: Odd Number of Observations**

When the number of observations is odd, the median is the observation at position:

Median position = (n + 1) / 2

**Example**

Find the median of:

8, 3, 12, 5, 10

**Step 1: Arrange the observations in ascending order.**

3, 5, 8, 10, 12

**Step 2: Determine the median position.**

Median position = (5 + 1) / 2 = 3

**Step 3: Identify the third observation.**

Median = 8

**Case 2: Even Number of Observations**

When the number of observations is even, the median is the arithmetic mean of the two middle observations.

Median = [Observation at position n/2 + Observation at position (n/2 + 1)] / 2

**Example**

Find the median of:

4, 8, 10, 12, 16, 20

The observations are already arranged in ascending order.

The two middle observations are:

10 and 12

Therefore:

Median = (10 + 12) / 2 = 11

### 6.3 Median for Discrete Frequency Distribution

For a discrete frequency distribution, we use cumulative frequency to identify the position of the middle observation.

**Worked Example**

| Number of Books (x) | Frequency (f) | Cumulative Frequency (CF) |
|---:|---:|---:|
| 1 | 2 | 2 |
| 2 | 3 | 5 |
| 3 | 4 | 9 |
| 4 | 1 | 10 |

Total frequency:

N = 10

The two middle positions are:

N/2 = 5

N/2 + 1 = 6

From the cumulative frequency column:

- The 5th observation has value 2.
- The 6th observation has value 3.

Therefore:

Median = (2 + 3) / 2 = 2.5

### 6.4 Median for Grouped Data

When observations are organized into continuous class intervals, we estimate the median using the grouped median formula.

Median = L + [(N/2 − CF) / f] × h

Where:

- L = lower class boundary of the median class
- N = total frequency
- CF = cumulative frequency before the median class
- f = frequency of the median class
- h = class width

**How to Identify the Median Class**

The median class is the class interval whose cumulative frequency first equals or exceeds N/2.

**Worked Example**

Consider the following distribution:

| Class Interval | Frequency (f) | Cumulative Frequency (CF) |
|---|---:|---:|
| 10–20 | 2 | 2 |
| 20–30 | 5 | 7 |
| 30–40 | 8 | 15 |
| 40–50 | 5 | 20 |
| **Total** | **20** | |

**Step 1: Calculate N/2.**

N/2 = 20/2 = 10

**Step 2: Identify the median class.**

The cumulative frequency first exceeds 10 in the class 30–40.

Therefore, the median class is 30–40.

**Step 3: Identify the required values.**

- L = 29.5
- N = 20
- CF = 7
- f = 8
- h = 10

**Step 4: Substitute into the formula.**

Median = 29.5 + [(10 − 7) / 8] × 10

Median = 29.5 + (3/8 × 10)

Median = 29.5 + 3.75

Median = 33.25

Therefore, the estimated median is **33.25**.

**Important:** The median for grouped data is an estimate because the exact individual observations are unavailable. The formula assumes that observations are distributed approximately uniformly within the median class.

### 6.5 Important Characteristics of the Median

- The median depends on the position of observations after ordering.
- It is less affected by extremely large or small observations than the arithmetic mean.
- It can be used for ordinal and quantitative data.
- It is particularly useful when a dataset contains extreme observations or is highly skewed.

---
## 7. Mode

### 7.1 Definition

The **mode** is the observation or category that occurs most frequently in a dataset.

In simple terms, it identifies the most common value.

Unlike the mean and median, the mode can also be used with nominal categorical data.

### 7.2 Mode for Ungrouped and Discrete Data

Consider the following observations:

2, 3, 3, 4, 5, 3, 6, 7

The value 3 appears three times, more frequently than any other value.

Therefore:

Mode = 3

A dataset can have different modal situations:

- **Unimodal:** One mode.
- **Bimodal:** Two modes.
- **Multimodal:** More than two modes.
- **No mode:** No observation occurs more frequently than the others.

**Example of Categorical Mode**

Suppose students are asked about their preferred learning methods:

Online, Face-to-face, Online, Hybrid, Online, Face-to-face

The frequency of each category is:

| Learning Method | Frequency |
|---|---:|
| Online | 3 |
| Face-to-face | 2 |
| Hybrid | 1 |

The mode is **Online** because it is the most frequently selected category.

### 7.3 Mode for Grouped Data

For grouped data, the class interval with the highest frequency is called the **modal class**.

The estimated mode can be calculated using:

Mode = L + [(f₁ − f₀) / (2f₁ − f₀ − f₂)] × h

Where:

- L = lower class boundary of the modal class
- f₁ = frequency of the modal class
- f₀ = frequency of the class preceding the modal class
- f₂ = frequency of the class following the modal class
- h = class width

**Worked Example**

Consider the following distribution:

| Class Interval | Frequency |
|---|---:|
| 10–20 | 2 |
| 20–30 | 5 |
| 30–40 | 8 |
| 40–50 | 5 |

**Step 1: Identify the modal class.**

The highest frequency is 8.

Therefore, the modal class is 30–40.

**Step 2: Identify the required values.**

- L = 29.5
- f₁ = 8
- f₀ = 5
- f₂ = 5
- h = 10

**Step 3: Substitute into the formula.**

Mode = 29.5 + [(8 − 5) / (2(8) − 5 − 5)] × 10

Mode = 29.5 + [3 / 6] × 10

Mode = 29.5 + 5

Mode = 34.5

Therefore, the estimated mode is **34.5**.

**Important:** The modal class is the class interval with the highest frequency, whereas the grouped mode formula estimates the most common value within that class.

---
## 8. Relationship Between Mean, Median, and Mode

Mean, median, and mode describe the center of a dataset from different perspectives.

Their relationship can help us understand the general shape of a distribution.

### 8.1 Symmetrical Distribution

In a perfectly symmetrical, unimodal distribution, the three measures coincide:

Mean = Median = Mode

This means that the center of the distribution is represented by the same value using all three measures.

### 8.2 Positively Skewed Distribution

In a positively skewed distribution, the longer tail extends toward larger values.

Typically:

Mode < Median < Mean

The mean is usually pulled toward the larger observations.

### 8.3 Negatively Skewed Distribution

In a negatively skewed distribution, the longer tail extends toward smaller values.

Typically:

Mean < Median < Mode

The mean is usually pulled toward the smaller observations.

### 8.4 Empirical Relationship

For moderately skewed distributions, an approximate empirical relationship is sometimes used:

Mode ≈ 3(Median) − 2(Mean)

This relationship is an approximation, not an exact mathematical identity. It should not be treated as universally valid.

---
## 9. Choosing an Appropriate Measure

The three measures are not interchangeable in every situation. Selecting an appropriate measure depends on the type of data and the purpose of the analysis.

| Measure | Suitable Data | Main Strength | Main Limitation |
|---|---|---|---|
| Mean | Quantitative | Uses every observation | Sensitive to extreme values |
| Weighted Mean | Quantitative with unequal contributions | Accounts for different weights | Requires appropriate weights |
| Median | Ordinal and quantitative | Resistant to extreme observations | Does not use the magnitude of every observation directly |
| Mode | Nominal, ordinal, and quantitative | Identifies the most common value | May have multiple modes or no clear mode |

**Example: Choosing Between Mean and Median**

Suppose the monthly salaries of ten employees are:

5,000; 5,500; 6,000; 6,500; 7,000; 7,500; 8,000; 8,500; 9,000; 100,000

The arithmetic mean is:

Mean = 163,000 / 10 = 16,300

The median is:

Median = (7,000 + 7,500) / 2 = 7,250

The mean is much higher than the salaries of most employees because one employee earns an unusually high salary.

If the objective is to describe the typical salary of an employee, the median is more representative in this example.

However, if the objective is to calculate the total salary expenditure per employee, the arithmetic mean is still relevant.

**The key lesson:** The appropriate measure depends not only on the dataset but also on the question we want to answer.

---
## 10. Applications in Data Science

Measures of central tendency are important in data analysis because they summarize large datasets into understandable values.

Some practical applications include:

### 10.1 Business Analytics

Businesses use average sales, average revenue, and average customer spending to understand performance and support decisions.

### 10.2 Finance

Financial analysts use average returns, median income, and other central measures to summarize financial information.

Weighted means are particularly useful when calculating portfolio returns from investments with different weights.

### 10.3 Education

Schools and universities use average examination scores and the most frequently occurring grades to evaluate academic performance.

### 10.4 Missing-Value Treatment

In some data preprocessing tasks, missing numerical values may be replaced using the mean or median.

For example:

- Mean imputation may be appropriate when the data is reasonably balanced and extreme observations are not a major concern.
- Median imputation may be more appropriate when the data contains extreme observations.

However, replacing missing values with a central measure is not always appropriate. The decision should consider the nature of the data and the reason values are missing.

### 10.5 Customer Analysis

Businesses can use average purchase amounts and the most common product categories to understand customer behavior.

---
## 11. Common Mistakes

1. **Calculating the median without arranging the observations.**  
   Always arrange the observations before identifying the middle value.

2. **Confusing frequency with observation.**  
   In a frequency distribution, the frequency indicates how many times an observation occurs.

3. **Using the ordinary mean when observations have different weights.**  
   Use the weighted mean when contributions or importance differ.

4. **Using class limits instead of class boundaries in grouped median and mode calculations.**  
   Identify the correct lower class boundary according to the class intervals.

5. **Confusing the modal class with the grouped mode.**  
   The modal class is an interval; the grouped mode is an estimated value.

6. **Assuming that the mean always represents a typical observation.**  
   Extreme values can influence the arithmetic mean.

7. **Treating the empirical mean-median-mode relationship as an exact formula.**  
   It is only an approximation for moderately skewed distributions.

8. **Choosing a measure without considering the objective of the analysis.**  
   A mathematically correct measure may still be unsuitable for the question being investigated.

---
## 12. Formula Summary

| Measure | Formula |
|---|---|
| Population Mean | μ = Σx / N |
| Sample Mean | x̄ = Σx / n |
| Mean for Discrete Frequency Data | x̄ = Σfx / Σf |
| Mean for Grouped Data | x̄ = Σfm / Σf |
| Class Midpoint | m = (Lower limit + Upper limit) / 2 |
| Weighted Mean | x̄w = Σwx / Σw |
| Median Position (Odd n) | (n + 1) / 2 |
| Median (Even n) | Average of the two middle observations |
| Grouped Median | L + [(N/2 − CF) / f] × h |
| Grouped Mode | L + [(f₁ − f₀) / (2f₁ − f₀ − f₂)] × h |
| Empirical Relationship | Mode ≈ 3(Median) − 2(Mean) |

---
## 13. Practice Questions

### Part A: Conceptual Questions

1. Why is the arithmetic mean called a balancing point of a dataset?

2. Explain why the median is generally more appropriate than the mean when a dataset contains an extremely large observation.

3. Can a dataset have more than one mode? Explain with an example.

4. Why is the weighted mean more appropriate than the ordinary mean when calculating a student's overall performance using assessments with different weights?

5. Under what circumstances would the mode be more useful than the mean and median?

### Part B: Calculation Questions

**Question 1: Arithmetic Mean**

Calculate the arithmetic mean of the following observations:

12, 15, 18, 20, 25, 30

**Question 2: Weighted Mean**

A student's assessment scores are:

| Assessment | Score | Weight |
|---|---:|---:|
| Assignment | 85 | 20 |
| Midterm | 75 | 30 |
| Final Exam | 90 | 50 |

Calculate the weighted mean.

**Question 3: Median**

Find the median of:

7, 12, 5, 18, 10, 15, 20

**Question 4: Grouped Mean, Median, and Mode**

Consider the following frequency distribution:

| Class Interval | Frequency |
|---|---:|
| 10–20 | 3 |
| 20–30 | 7 |
| 30–40 | 10 |
| 40–50 | 6 |
| 50–60 | 4 |

Calculate:

a. The arithmetic mean.

b. The median.

c. The mode.

d. Compare the three results.

### Solutions

**Solution 1**

x̄ = Σx / n

x̄ = (12 + 15 + 18 + 20 + 25 + 30) / 6

x̄ = 120 / 6 = 20

**Solution 2**

x̄w = Σwx / Σw

x̄w = [(85 × 20) + (75 × 30) + (90 × 50)] / 100

x̄w = (1700 + 2250 + 4500) / 100

x̄w = 8450 / 100 = 84.5

**Solution 3**

Arrange the observations:

5, 7, 10, 12, 15, 18, 20

Median position = (7 + 1) / 2 = 4

Median = 12

**Solution 4**

First, calculate the midpoints and cumulative frequencies.

| Class Interval | f | Midpoint (m) | fm | CF |
|---|---:|---:|---:|---:|
| 10–20 | 3 | 15 | 45 | 3 |
| 20–30 | 7 | 25 | 175 | 10 |
| 30–40 | 10 | 35 | 350 | 20 |
| 40–50 | 6 | 45 | 270 | 26 |
| 50–60 | 4 | 55 | 220 | 30 |
| **Total** | **30** | | **1060** | |

**a. Arithmetic Mean**

x̄ = Σfm / Σf

x̄ = 1060 / 30

x̄ ≈ 35.33

**b. Median**

N/2 = 30/2 = 15

The median class is 30–40.

L = 29.5, CF = 10, f = 10, h = 10

Median = 29.5 + [(15 − 10) / 10] × 10

Median = 29.5 + 5

Median = 34.5

**c. Mode**

The modal class is 30–40.

L = 29.5, f₁ = 10, f₀ = 7, f₂ = 6, h = 10

Mode = 29.5 + [(10 − 7) / (20 − 7 − 6)] × 10

Mode = 29.5 + (3/7 × 10)

Mode ≈ 33.79

**d. Comparison**

Mean ≈ 35.33

Median = 34.5

Mode ≈ 33.79

Therefore:

Mode < Median < Mean

This is the typical ordering associated with a positively skewed distribution. However, the ordering of grouped estimates alone does not establish the exact shape of a distribution.

---
## 14. Conclusion

Measures of central tendency help us summarize datasets using representative values.

The arithmetic mean represents the equal share of the total observations, the median identifies the middle position of ordered observations, and the mode identifies the most frequently occurring value.

Although these measures serve a common purpose, they are not equally appropriate for every dataset.

A good statistical analysis requires understanding how each measure works, recognizing its limitations, and selecting the measure that best answers the question under investigation.

These concepts provide an important foundation for further statistical analysis and data science.

---

**End of Part III: Measures of Central Tendency**
