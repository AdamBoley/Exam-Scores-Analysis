# Exam Scores Analysis

Am I responsive image here

## Introduction

This is a Machine Learning project developed as part of my Predictive Analytics studies with Code Institute. This is my 5th Portfolio Project.

## Business Requirements

The local government wants to increase educational attainment in its schools, primarily by improving test scores in reading, writing and mathematics. They have access to data about past students' test scores, as well as information about those students' circumstances. The local government has contracted me to undertake 3 tasks:

- Firstly, they want me to study the student data to find patterns and relationships, with the goal of identifying the most relevant variables that correlate to high test scores. These correlations will then be used to formulate educational policy with the aim of improving student test scores generally

- Secondly, they want me to produce a Machine Learning tool that their teachers can use to input data about a particular student and get a predictions of that student's test scores. Then, if those test scores fall below the mean of the historical test scores, that student can be offered additional support

- Thirdly, the local government has indicated that both the test scores analysis and the Machine Learning tool be held within a dashboard for ease of use

## Dataset

The local government has uploaded the dataset to Kaggle. It is located [here](https://www.kaggle.com/datasets/whenamancodes/students-performance-in-exams).

Before any data analysis takes place, a quick inspection of the data indicates that it has value for a hybrid demographical-educational analysis of how student circumstances affect test scores.

## Hypotheses

After discussions with the local government, I have formulated several hypotheses. These hypotheses will guide the data analysis.

- I hypothesize that students who attend the test preparation course attain higher test scores

- I hypothesize that a student's lunch program has an effect on their test scores

- I hypothesize that increased levels of parental education negatively correlate to their children's participation in the free/reduced school lunch program. For this hypothesis, I have made the reasonable assumption that better educated parents earn higher wages, and that the free/reduced school lunch program is only available to poorer parents

- I hypothesize that increased levels of parental education correlate with higher test scores. For this hypothesis, I have made the reasonable assumption that better educated parents have a greater focus on education

- I hypothesize that increased levels of parental education correlate with increased participation in the test preparation program. As above, for this hypothesis, I have made the reasonable assumption that better educated parents have a greater focus on education

- I hypothesize that a student's gender has an effect on their individual and overall test scores. It is the opinion of my Mentor that girls tend to perform better in education than boys, and [this article](https://www.theguardian.com/education/2021/aug/10/a-level-results-top-5-data-takeaways) appears to support that opinion

- I hypothesize that a student's ethnicity has an effect on their test scores.

- I hypothesize that a student's ethnicity has an effect on their parent's educational level. For this hypothesis, I assume that both parents are of the same ethnicity as their child

- I hypothesize that, assuming that the hypothesis that parental educational level correlates with participation in the free/reduced school lunch program is true, 
then a student's ethnicity has an effect on their participation in the free/reduced school lunch program

- I hypothesize that, assuming that the hypothesis that parental educational level correlates with participation in the test preparation course is true, 
then a student's ethnicity has an effect on their participation in the test preparation course

- I hypothesize that a student's gender has an effect on their participation in the test preparation course

- I hypothesize that students who achieve high scores in reading also achieve high scores in writing

## Dashboard pages

This project will be deployed as a Streamlit dashboard. I plan on designing 5 pages:

- Page 1 - A project summary with explanations of each feature variable, any relevant jargon, and the findings of the data analysis
- Page 2 - The project's hypotheses, absent any validation, since the hypotheses will guide the data analysis on Page 3
- Page 3 - An in-depth analysis of the dataset, with various plots
- Page 4 - The validation of the Project's hypotheses, based on any relevant findings identified in the data analysis page
- Page 5 - A user interface that allows the user to use the Machine Learning model to make predictions of student scores

## Mapping Business Requirements to the Data Visualisation and Machine Learning tasks

Now that the business requirements and data hypotheses have been laid down, it is now necessary to determine how the business requirements will be achieved and how the hypotheses will be validated

### Business Requirement 1 - Data Visualisation and Correlation Study
- Firstly, I will generally inspect the student test score data, and construct various plots
- I will then conduct a correlation study using the Pearson and Spearman methods to better understand how the feature variables are correlated to the test scores

### Business Requirement 2 - Construction of an appropriate Machine Learning model
- The local government wants to be able to predict student test scores based on their circumstances
- As the test scores are continuous numerical variables, a regression based model will be used first
- As the feature variables are categorical, it may be that a regression model will fail to perform
- If a regression model fails, a multiple classification approach will be used, with student test scores converted to bins

### Business Requirement 3 - Construction of Streamlit dashboard
- Once all data analysis, data visualisation and machine learning tasks are completed, the focus of the project can switch to construction of the dashboard


## Development cycle log
In previous projects, I have found it useful to log my progress through the development cycle. Given that I am considering a dataset of significant size and complexity, I shall continue this practice, and I will note any particularly interesting insights.

8/11/22:
[Student exam scores dataset](https://www.kaggle.com/datasets/whenamancodes/students-performance-in-exams) located on Kaggle. Several other datasets were considered, but I considered that this since dataset contains data about a student's cirsumstances as well as their test scores, a project using this dataset could contain a demographic analysis as well as an analysis of test scores.

After deciding to use this dataset, I noted down some quick thoughts regarding hypotheses, business cases, data cleaning, visualisation, model construction and so on. I booked the first project planning call with my Mentor and he agreed with the general thrust of my analysis approach.

9/11/22:
Project repository started and workspace built. Necessary data analysis and machine learning packages installed. Business Requirements, hypotheses, dashboard layout, and approach documented in ReadMe.

10/11/22:
Generate Pandas Profile Report, distribution analysis using QQ plots and Shapiro Wilk tests. Numerical data may or may not be normally distributed. Begin correlation study

11/11/22:
I think I need to go back one step, and expand the data analysis more in line with the hypotheses, with more plots.

20/11/22:
Categorical variable relationships analyses, and relevant hypotheses validated. Parental education influences student participation in the test preparation course, and there is a parental education bias in the various ethnicities of the students. 

Correlation study and predictive power score study conducted. For maths, only lunch_program has any significant correlation and predictive power. For reading, lunch_program shows strong predictive power, and lunch_program and test_preparation_course show significant correlation. For writing, lunch_program and test_preparation_course show strong predictive power and significant correlation. 



## Credits

https://stackoverflow.com/questions/34734940/row-wise-average-for-a-subset-of-columns-with-missing-values - for average row values

https://stackoverflow.com/questions/40088585/turn-off-error-bars-in-seaborn-bar-plot - add values to barplots and remove confidence intervals

https://stackoverflow.com/questions/34615854/seaborn-countplot-with-normalized-y-axis-per-group - seaborn countplot with normalised y-axis counts
