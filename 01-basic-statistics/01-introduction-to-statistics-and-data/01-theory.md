# Part I: Introduction to Statistics and Data

## 1. Introduction

Have you ever wondered how banks understand their customers, how researchers study thousands of people, or how businesses use information to make better decisions?

These activities rely on **Statistics**.

Statistics provides methods for collecting, organizing, presenting, analyzing, and interpreting data. It helps us transform raw data into meaningful information that can support decision-making.

In Data Science, statistics plays a fundamental role because data scientists use statistical concepts to understand datasets, identify patterns, make predictions, and draw conclusions.

This part introduces the fundamental concepts needed before studying statistical methods in greater detail.

## 2. Table of Contents

1. [Learning Objectives](#3-learning-objectives)
2. [Introduction to Statistics](#4-introduction-to-statistics)
3. [Population, Sample, Statistical Units, and Observations](#5-population-sample-statistical-units-and-observations)
4. [Types of Data and Variables](#6-types-of-data-and-variables)
5. [Levels of Measurement](#7-levels-of-measurement)
6. [Data Collection and Data Sources](#8-data-collection-and-data-sources)
7. [Importance of Statistics in Data Science](#9-importance-of-statistics-in-data-science)
8. [Common Mistakes and Important Distinctions](#10-common-mistakes-and-important-distinctions)
9. [Summary of Important Concepts](#11-summary-of-important-concepts)
10. [Practice Questions with Solutions](#12-practice-questions-with-solutions)
11. [Conclusion](#13-conclusion)

---

## 3. Learning Objectives

After studying this part, you should be able to:

- Define statistics and explain its major activities.
- Distinguish between descriptive and inferential statistics.
- Explain population, sample, statistical unit, and observation.
- Differentiate between a population parameter and a sample statistic.
- Identify different types of variables.
- Distinguish between discrete and continuous variables.
- Explain the four levels of measurement.
- Differentiate between primary and secondary data.
- Identify appropriate data collection approaches.
- Understand the importance of statistical concepts in Data Science.

---

## 4. Introduction to Statistics

### 4.1 What Is Statistics?

Statistics is the science of collecting, organizing, presenting, analyzing, and interpreting data to obtain meaningful information and support decision-making.

The five major activities of statistics are:

1. **Data Collection:** Obtaining relevant information from individuals, objects, or other sources.
2. **Data Organization:** Arranging collected data systematically.
3. **Data Presentation:** Displaying data using tables, graphs, charts, or other suitable methods.
4. **Data Analysis:** Applying statistical methods to discover patterns and relationships.
5. **Data Interpretation:** Explaining the meaning of analytical results and drawing appropriate conclusions.

These activities are connected. For example, a researcher first collects information, organizes it, presents it, analyzes it, and finally interprets the results.

### 4.2 Branches of Statistics

Statistics is commonly divided into two major branches:

#### A. Descriptive Statistics

Descriptive statistics deals with organizing, summarizing, and presenting the characteristics of a dataset.

It describes the data that have been collected without necessarily making conclusions about a larger population.

Common descriptive techniques include:

- Tables and frequency distributions.
- Graphical presentations.
- Measures of central tendency.
- Measures of dispersion.
- Measures of position.

**Example:**

Suppose a university has 8,000 students. A researcher randomly selects 500 students and calculates their average CGPA.

Calculating and describing the average CGPA of these 500 students is an application of descriptive statistics.

#### B. Inferential Statistics

Inferential statistics uses information obtained from a sample to make estimates, predictions, or conclusions about a larger population.

It helps us study a population without necessarily collecting information from every member.

Common inferential techniques include:

- Estimation.
- Confidence intervals.
- Hypothesis testing.
- Statistical prediction.

**Example:**

Suppose the researcher uses the average CGPA of the 500 selected students to estimate the average CGPA of all 8,000 university students.

This is an application of inferential statistics.

### 4.3 Difference Between Descriptive and Inferential Statistics

| Descriptive Statistics | Inferential Statistics |
|---|---|
| Summarizes collected data. | Draws conclusions about a population. |
| Describes the available dataset. | Uses sample information to study a larger population. |
| Uses tables, graphs, and descriptive measures. | Uses estimation, confidence intervals, and hypothesis testing. |
| Does not necessarily generalize beyond the observed data. | Generalizes from a sample to a population, accounting for uncertainty. |

**Important:** Descriptive statistics can describe either a sample or an entire population. The distinction between descriptive and inferential statistics is based on what we do with the data, not simply on whether the data come from a sample or population.

---

## 5. Population, Sample, Statistical Units, and Observations

When conducting a statistical investigation, we must first understand the group being studied and the information being collected.

### 5.1 Population

A **population** is the entire collection of individuals, objects, or elements about which a statistical investigation is conducted.

A population may consist of people, households, companies, products, transactions, or other elements.

**Example:**

Suppose a researcher wants to investigate the monthly income of employees working in Ethiopian commercial banks.

If there are 10,000 employees in the banks under consideration, all 10,000 employees form the population.

#### Types of Population

**Finite Population:**

A population containing a limited and countable number of elements.

Example: All 10,000 employees working in the selected commercial banks.

**Infinite Population:**

A population that is unlimited or theoretically infinite.

Example: All possible outcomes of repeatedly tossing a coin an unlimited number of times.

### 5.2 Sample

A **sample** is a subset of a population selected for statistical investigation.

Instead of studying every population member, researchers often select a smaller group to obtain information about the population.

**Example:**

From the 10,000 bank employees, suppose a researcher selects 300 employees.

The selected 300 employees form the sample.

A good sample should represent the population as closely as possible.

A sample that systematically excludes or overrepresents certain groups may produce biased conclusions.

### 5.3 Statistical Unit

A **statistical unit** is an individual element or member of a population about which information is collected.

It is the basic unit of a statistical investigation.

**Example:**

If a researcher studies the monthly income of 300 bank employees:

- One employee is a statistical unit.
- The 300 employees collectively form the sample.

A statistical unit can be a person, household, business, school, product, or any other element being investigated.

### 5.4 Variable

A **variable** is a characteristic or property of a statistical unit that can take different values.

Examples include:

- Age of an employee.
- Monthly income of an employee.
- Height of a student.
- Blood group of a patient.
- Number of customers visiting a bank.

A variable is what the researcher wants to investigate or record.

### 5.5 Observation

An **observation** is the recorded value of a variable for a particular statistical unit.

**Example:**

Suppose we record the monthly income of three employees:

| Employee | Monthly Income |
|---|---:|
| Employee A | 12,000 Birr |
| Employee B | 15,000 Birr |
| Employee C | 18,000 Birr |

In this example:

- Statistical unit: Each employee.
- Variable: Monthly income.
- Observations: 12,000 Birr, 15,000 Birr, and 18,000 Birr.

The distinction is important:

**A statistical unit is the element being studied, while an observation is the recorded information about that element.**

### 5.6 Census and Sample Survey

There are two common approaches to collecting information from a population.

#### A. Census

A **census** is a statistical investigation in which information is collected from every member of the population.

Example:

A university collects information about every student enrolled in the university.

Advantages:
- Provides information about every population member.
- Eliminates sampling error.
- Can provide detailed population information.

Limitations:
- Requires more time and resources.
- May be expensive.
- Can be difficult for very large populations.
- Does not eliminate non-sampling errors.

#### B. Sample Survey

A **sample survey** is a statistical investigation in which information is collected from a selected sample rather than the entire population.

Example:

A university selects 500 students from its 8,000 students and collects information about their study habits.

Advantages:
- Requires less time.
- Usually costs less.
- Suitable for large populations.
- Can provide reliable conclusions when the sample is appropriately selected.

Limitations:
- May produce sampling error.
- Can be biased if the sample is not representative.
- Results are subject to uncertainty.

**Important:** A census does not automatically guarantee perfect accuracy. Errors can still occur during data collection, measurement, recording, and processing.

### 5.7 Parameter and Statistic

These concepts describe numerical characteristics of populations and samples.

**Parameter:**

A parameter is a numerical measure that describes a characteristic of an entire population.

Example:

The actual average monthly income of all 10,000 bank employees is a population parameter.

**Statistic:**

A statistic is a numerical measure calculated from sample data.

Example:

The average monthly income calculated from the 300 selected employees is a sample statistic.

| Parameter | Statistic |
|---|---|
| Describes a population. | Describes a sample. |
| Calculated using population information. | Calculated using sample information. |
| Usually unknown when studying large populations. | Can be calculated from collected sample data. |
| Can be estimated using a sample statistic. | Often used to estimate a population parameter. |

The relationship can be summarized as:

**Population → Sample → Sample Statistic → Estimate of Population Parameter**

This relationship is fundamental to inferential statistics.

---

## 6. Types of Data and Variables

Data can be classified into different categories depending on the nature of the information they represent.

### 6.1 Qualitative Variables

A **qualitative variable** describes a category, characteristic, or quality rather than a numerical quantity.

Examples:

- Gender.
- Blood group.
- Nationality.
- Marital status.
- Educational level.

Qualitative variables are also called categorical variables.

Their values may be represented using words, symbols, or numerical codes.

For example, blood groups can be coded as:

- A = 1
- B = 2
- AB = 3
- O = 4

Even though numbers are used, blood group remains a qualitative variable because the numbers are only category labels.

### 6.2 Quantitative Variables

A **quantitative variable** represents a numerical quantity that can be counted or measured.

Examples:

- Age.
- Monthly income.
- Height.
- Weight.
- Number of children.
- Number of employees.

Quantitative variables are divided into two main categories.

#### A. Discrete Variables

A **discrete variable** takes distinct, countable values.

It commonly results from counting.

Examples:

- Number of students in a classroom.
- Number of customers visiting a bank.
- Number of children in a household.
- Number of employees in a company.

For example, the number of students in a classroom can be 30 or 31, but it cannot be 30.5 students.

#### B. Continuous Variables

A **continuous variable** can take any value within a given interval, depending on the precision of measurement.

It commonly results from measuring.

Examples:

- Height.
- Weight.
- Temperature.
- Time duration.
- Distance.

For example, a person's height may be 170 cm, 170.5 cm, or 170.55 cm.

### 6.3 Summary of Variable Classification

| Main Type | Subtype | Description | Examples |
|---|---|---|---|
| Qualitative | — | Represents categories or characteristics. | Blood group, nationality |
| Quantitative | Discrete | Takes distinct, countable values. | Number of children |
| Quantitative | Continuous | Takes measurable values within an interval. | Height, weight |

**Important distinction:** A number is not automatically a quantitative variable. Student identification numbers, telephone numbers, and postal codes are examples of numerical labels rather than numerical quantities.

---

## 7. Levels of Measurement

A measurement scale describes how the values of a variable are classified and what comparisons or mathematical operations are meaningful.

There are four major levels of measurement:

1. Nominal.
2. Ordinal.
3. Interval.
4. Ratio.

Understanding these levels helps researchers choose appropriate methods for analyzing data.

### 7.1 Nominal Scale

A **nominal scale** classifies data into different categories without any natural order or ranking.

Examples:

- Blood group.
- Nationality.
- Religion.
- Marital status.
- Type of business.

For example, blood groups A, B, AB, and O are different categories, but none is naturally greater or smaller than another.

Main characteristics:

- Categories are distinct.
- No meaningful order exists.
- Numerical differences between categories are meaningless.

### 7.2 Ordinal Scale

An **ordinal scale** classifies data into categories that have a meaningful order or ranking.

However, the differences between consecutive categories are not necessarily equal or measurable.

Examples:

- Educational level.
- Satisfaction level.
- Customer service ratings.
- Socioeconomic status.

For example:

Poor < Fair < Good < Very Good < Excellent

We know that Excellent is higher than Good, but we cannot assume that the difference between Good and Very Good is equal to the difference between Poor and Fair.

Main characteristics:

- Categories are distinct.
- A meaningful order exists.
- Differences between ranks are not necessarily equal.

### 7.3 Interval Scale

An **interval scale** is a numerical measurement scale in which values have equal and meaningful intervals, but there is no true or absolute zero.

Examples:

- Temperature measured in Celsius.
- Temperature measured in Fahrenheit.

Consider the following temperatures:

10°C, 20°C, and 30°C.

The difference between 10°C and 20°C is equal to the difference between 20°C and 30°C.

However, 20°C is not twice as hot as 10°C because 0°C does not represent the complete absence of temperature.

Main characteristics:

- Values have a meaningful order.
- Differences between values are equal.
- There is no true zero.
- Ratios between values are not meaningful.

### 7.4 Ratio Scale

A **ratio scale** is a numerical measurement scale with equal intervals and a meaningful absolute zero.

Examples:

- Height.
- Weight.
- Age.
- Monthly income.
- Distance.
- Time duration.

Consider two individuals:

- Person A weighs 40 kg.
- Person B weighs 80 kg.

We can meaningfully say that Person B weighs twice as much as Person A.

This is possible because zero represents the absence of the measured quantity.

Main characteristics:

- Values have a meaningful order.
- Differences between values are equal.
- A meaningful absolute zero exists.
- Ratios between values are meaningful.

### 7.5 Comparison of Measurement Scales

| Property | Nominal | Ordinal | Interval | Ratio |
|---|---|---|---|---|
| Classification | Yes | Yes | Yes | Yes |
| Meaningful order | No | Yes | Yes | Yes |
| Equal intervals | No | Not guaranteed | Yes | Yes |
| Absolute zero | No | No | No | Yes |
| Example | Blood group | Satisfaction level | Celsius temperature | Weight |

The four measurement scales can be understood as progressively adding more information:

**Nominal → Ordinal → Interval → Ratio**

Each level includes the properties of the preceding level and adds another measurement property.

---

## 8. Data Collection and Data Sources

Statistical analysis depends on the quality and relevance of collected data.

Before analyzing information, researchers must understand where the data come from and how they were obtained.

### 8.1 Primary Data

**Primary data** is data collected directly by a researcher for a particular investigation.

The researcher obtains the information from its original source.

Common primary data collection methods include:

- Questionnaires.
- Interviews.
- Direct observations.
- Experiments.
- Measurements.

Example:

A researcher wants to investigate the relationship between household income and internet access in Ethiopia.

The researcher prepares a questionnaire and collects information directly from selected households.

The collected information is primary data.

Advantages:

- Can be collected according to the research objectives.
- The researcher has control over the collection process.
- Information can be designed to meet specific requirements.

Limitations:

- Can be expensive.
- Requires time and effort.
- Poorly designed collection methods may produce unreliable information.

### 8.2 Secondary Data

**Secondary data** is data that has already been collected by another person or organization and is reused for a new investigation.

Examples of secondary data sources include:

- Government reports.
- Published research papers.
- Books and academic journals.
- World Bank datasets.
- International organization databases.
- Existing organizational records.

Example:

A researcher downloads Ethiopian population data from an existing government statistical report and uses it for a new study.

The researcher is using secondary data.

Advantages:

- Often less expensive.
- Saves time.
- Provides access to historical information.
- Can cover large populations or geographical areas.

Limitations:

- May not contain all the information required.
- May be outdated.
- Collection methods may be unknown.
- May not perfectly match the current research objectives.

### 8.3 Primary Data vs. Secondary Data

| Primary Data | Secondary Data |
|---|---|
| Collected directly by the researcher. | Previously collected by another person or organization. |
| Obtained from original sources. | Obtained from existing sources. |
| Designed for the current investigation. | May have been collected for another investigation. |
| Often requires more time and resources. | Often saves time and resources. |
| Example: Conducting interviews. | Example: Using an existing government report. |

### 8.4 Evaluating Secondary Data

Before using secondary data, a researcher should examine its quality and suitability.

Important considerations include:

1. **Source:** Who collected the data? Is the source trustworthy?
2. **Purpose:** Why was the data originally collected?
3. **Time:** Is the data recent enough for the current investigation?
4. **Collection Method:** How was the information collected?
5. **Relevance:** Does the information answer the current research question?
6. **Completeness:** Are important observations or variables missing?

Secondary data is not automatically unreliable. A well-documented government dataset or international database may be more reliable than poorly collected primary data.

---

## 9. Importance of Statistics in Data Science

Statistics is one of the fundamental foundations of Data Science.

Data Science involves extracting useful knowledge and insights from data. Statistics provides the mathematical principles and methods needed to perform this task responsibly.

Some important applications include:

### 9.1 Understanding Data

Statistical methods help data scientists summarize and understand datasets before applying more advanced techniques.

### 9.2 Identifying Patterns

Statistics helps identify trends, relationships, and variations in data.

### 9.3 Making Predictions

Inferential statistics provides a foundation for estimating unknown quantities and making predictions using available data.

### 9.4 Supporting Decision-Making

Organizations use statistical evidence to make decisions in business, finance, healthcare, education, and other fields.

### 9.5 Evaluating Models

Statistical thinking helps data scientists evaluate the performance and reliability of analytical models.

**Example:**

A bank may use customer information to investigate the relationship between income, repayment history, and loan default.

Statistical concepts help the bank understand its data, investigate relationships, and make evidence-based decisions.

---

## 10. Common Mistakes and Important Distinctions

The following distinctions are particularly important when working with statistical data.

| Common Mistake | Correct Understanding |
|---|---|
| Treating a sample as the entire population. | A sample is only a subset of the population. |
| Confusing a statistical unit with an observation. | A statistical unit is the element studied; an observation is the recorded value. |
| Calling average monthly income the variable. | Monthly income is the variable; its average is a statistical measure. |
| Confusing a parameter with a statistic. | A parameter describes a population; a statistic describes a sample. |
| Assuming every numerical value is quantitative. | Numerical identifiers may only be labels. |
| Confusing discrete and continuous variables. | Discrete variables are countable; continuous variables are measurable. |
| Treating ordinal categories as equally spaced. | Ordinal categories have order, but equal intervals are not guaranteed. |
| Assuming Celsius temperature has a true zero. | Celsius is an interval scale. |
| Assuming a census guarantees perfect accuracy. | A census eliminates sampling error, not all errors. |
| Assuming secondary data is always unreliable. | Its quality depends on its source, collection method, relevance, and other factors. |

---

## 11. Summary of Important Concepts

| Concept | Meaning |
|---|---|
| Statistics | Science of collecting, organizing, presenting, analyzing, and interpreting data. |
| Descriptive Statistics | Methods used to summarize and describe collected data. |
| Inferential Statistics | Methods used to draw conclusions about a population using sample information. |
| Population | Entire group under investigation. |
| Sample | Selected subset of a population. |
| Statistical Unit | Individual element about which information is collected. |
| Variable | Characteristic being investigated. |
| Observation | Recorded value of a variable for a statistical unit. |
| Census | Data collection from every population member. |
| Sample Survey | Data collection from a selected sample. |
| Parameter | Numerical measure describing a population. |
| Statistic | Numerical measure calculated from a sample. |
| Qualitative Variable | Variable representing categories or characteristics. |
| Quantitative Variable | Variable representing numerical quantities. |
| Discrete Variable | Quantitative variable with countable values. |
| Continuous Variable | Quantitative variable with measurable values within an interval. |
| Nominal Scale | Categories without a meaningful order. |
| Ordinal Scale | Ordered categories without guaranteed equal intervals. |
| Interval Scale | Equal intervals without an absolute zero. |
| Ratio Scale | Equal intervals with an absolute zero. |
| Primary Data | Data collected directly for an investigation. |
| Secondary Data | Previously collected data reused for an investigation. |

---

## 12. Practice Questions with Solutions

These questions are designed to test understanding of the fundamental concepts introduced in this part.

### Question 1: Descriptive and Inferential Statistics

A researcher selects 200 households from a town containing 5,000 households.

a) The researcher calculates the average monthly income of the 200 households. Which branch of statistics is being used?

b) The researcher uses the calculated average to estimate the average monthly income of all 5,000 households. Which branch is being used?

**Solution:**

a) Descriptive statistics, because the researcher is summarizing the collected sample data.

b) Inferential statistics, because the researcher is using sample information to estimate a population characteristic.

### Question 2: Population and Sample

A university has 12,000 students. A researcher selects 400 students to investigate their internet usage.

Identify:

a) Population.

b) Sample.

c) Statistical unit.

d) Variable.

**Solution:**

a) Population: All 12,000 university students.

b) Sample: The 400 selected students.

c) Statistical unit: One individual student.

d) Variable: Internet usage.

### Question 3: Parameter and Statistic

A researcher calculates the average monthly income of 150 selected employees to estimate the average monthly income of all employees in a company.

Identify the parameter and statistic.

**Solution:**

- Parameter: The actual average monthly income of all company employees.
- Statistic: The average monthly income calculated from the 150 selected employees.

### Question 4: Variable Classification

Classify the following variables as qualitative, quantitative discrete, or quantitative continuous.

a) Number of employees.

b) Monthly salary.

c) Blood group.

d) Height.

e) Number of children.

**Solution:**

| Variable | Classification |
|---|---|
| Number of employees | Quantitative discrete |
| Monthly salary | Quantitative continuous |
| Blood group | Qualitative |
| Height | Quantitative continuous |
| Number of children | Quantitative discrete |

### Question 5: Measurement Scales

Identify the appropriate measurement scale for each variable.

a) Nationality.

b) Educational level.

c) Temperature in Celsius.

d) Monthly income.

e) Weight.

**Solution:**

| Variable | Measurement Scale |
|---|---|
| Nationality | Nominal |
| Educational level | Ordinal |
| Temperature in Celsius | Interval |
| Monthly income | Ratio |
| Weight | Ratio |

### Question 6: Census and Sample Survey

Explain the difference between a census and a sample survey.

**Solution:**

A census collects information from every member of the population, while a sample survey collects information from a selected subset of the population.

A census eliminates sampling error but generally requires more resources. A sample survey is usually more economical but may introduce sampling error.

### Question 7: Primary and Secondary Data

Classify the following data sources as primary or secondary.

a) A researcher interviews 50 bank managers.

b) A researcher downloads an existing World Bank dataset.

c) A researcher distributes questionnaires to university students.

d) A researcher uses an existing government report.

**Solution:**

| Data Source | Classification |
|---|---|
| Interviews with bank managers | Primary |
| Existing World Bank dataset | Secondary |
| Questionnaires distributed to students | Primary |
| Existing government report | Secondary |

### Question 8: Integrated Research Scenario

A researcher wants to investigate the relationship between internet access and household income in a region containing 50,000 households.

The researcher selects 500 households and collects the following information:

- Household identification number.
- Monthly household income.
- Internet access (Yes/No).
- Number of household members.
- Educational level of the household head.

Identify:

a) Population.

b) Sample.

c) Statistical unit.

d) Variables being recorded.

e) Type of each variable.

f) Measurement scale of each variable.

g) Data collection approach if information is collected from the 500 households directly.

**Solution:**

a) Population: All 50,000 households.

b) Sample: The selected 500 households.

c) Statistical unit: One household.

d) Variables: Household identification number, monthly income, internet access, number of household members, and educational level of the household head.

e) Variable types:

| Variable | Type |
|---|---|
| Household identification number | Identifier (categorical label) |
| Monthly household income | Quantitative continuous |
| Internet access | Qualitative |
| Number of household members | Quantitative discrete |
| Educational level | Qualitative |

f) Measurement scales:

| Variable | Measurement Scale |
|---|---|
| Household identification number | Nominal (identifier) |
| Monthly household income | Ratio |
| Internet access | Nominal |
| Number of household members | Ratio |
| Educational level | Ordinal |

g) Data collection approach: Sample survey.

If the researcher collects the information directly from the selected households, the data are primary data.

---

## 13. Conclusion

Statistics provides the foundation for understanding and working with data.

Before performing statistical calculations or applying analytical methods, we must understand what data represent, whom or what we are studying, how information is collected, and how variables are measured.

The concepts introduced in this part establish the foundation for more advanced statistical topics.

In the next part, we will study **Data Organization and Presentation**, where we will learn how to transform raw data into organized and understandable information using tables, frequency distributions, and graphical presentations.

**Remember:** Good statistical analysis begins with understanding the data, not simply performing calculations.
