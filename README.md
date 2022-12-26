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

After discussions with the local government, I have formulated several hypotheses. These hypotheses will guide the data analysis. I have 11 hypotheses total, and I have split them into Primary Hypotheses and Secondary Hypotheses.

The Primary Hypotheses are those that generally suppose some link between each of the 5 categorical variables and the numerical exam score variables. These are somewhat simple hypotheses, and validating them will fulfil the first business requirement.

The Secondary Hypotheses are those that generally suppose that certain pairs of categorical variables are correlated, such as the hypothesis that students of better educated parents have increased participation in the test preparation course. These hypotheses are more complex, and validating them could reveal insights about the demographics of the student body. These insights could allow me to better fulfil the first business requirement.

### Primary

- I hypothesize that students who attend the test preparation course attain higher test scores

- I hypothesize that a student's lunch program has an effect on their test scores

- I hypothesize that increased levels of parental education correlate with higher test scores. For this hypothesis, I have made the reasonable assumption that better educated parents have a greater focus on education

- I hypothesize that a student's gender has an effect on their individual and overall test scores. It is the opinion of my Mentor that girls tend to perform better in education than boys, and [this article](https://www.theguardian.com/education/2021/aug/10/a-level-results-top-5-data-takeaways) appears to support that opinion

- I hypothesize that a student's ethnicity has an effect on their individual and overall test scores

### Secondary

- I hypothesize that increased levels of parental education correlate with increased participation in the test preparation course. As above, for this hypothesis, I have made the reasonable assumption that better educated parents have a greater focus on education

- I hypothesize that increased levels of parental education correlate with increased participation in the standard lunch program

- I hypothesize that a student's ethnicity has an effect on their parent's educational level. For this hypothesis, I assume that both parents are of the same ethnicity as their child. Put more simply, this hypothesis states that certain ethnicities are better educated that others

- I hypothesize that a student's ethnicity has an effect on their participation in the free/reduced school lunch program

- I hypothesize that a student's ethnicity has an effect on their participation in the test preparation course

- I hypothesize that a student's gender has an effect on their participation in the test preparation course

## Dashboard pages

This project will be deployed as a Streamlit dashboard. There will be 8 pages:

- Page 1 - A project summary page with an introduction, the project business requirements, and soem basic, surface-level information about the dataset and its variables
- Page 2 - The project's hypotheses, absent any validation
- Page 3 - A distribution analysis of the dataset, to determine whether the data is normally distributed
- Page 4 - Data Analysis as guided by the Primary Hypotheses, with plots that show the correlations between each of the categorical feature variables and the numerical target variables
- Page 5 - Data Analysis as guided by the Secondary Hypotheses, with plots that show the correlations and links between certain pairs of categorical variables
- Page 4 - The validation of the Project's hypotheses, based on any relevant findings identified in the data analysis pages
- Page 5 - Information about the predictive machine learning models that were trained 
- Page 6 - A user interface that allows the user to use the Machine Learning models to make predictions of student scores

## Mapping Business Requirements to the Data Visualisation and Machine Learning tasks

Now that the business requirements and data hypotheses have been laid down, it is now necessary to determine how the business requirements will be achieved and how the hypotheses will be validated

### Business Requirement 1 - Data Visualisation and Correlation Study
- Firstly, I will generally inspect the student test score data via a Pandas Profile Report
- Then I will conduct a distribution study, to determine if the data is normally distributed
- I will then conduct a data analysis guided by the project hypotheses. The Primary Hypotheses will be investigated first, followed by the Secondary Hypotheses
- I will then conduct a correlation study and Predictive Power Score analysis to determine which categorical variables have the greatest predictive power

### Business Requirement 2 - Construction of an appropriate Machine Learning model
- The local government wants to be able to predict student test scores based on their circumstances
- As the test scores are continuous numerical variables, a regression based model will be tried first
- As the feature variables are categorical, it may be that a regression model will fail to perform to an acceptable level
- If a regression model fails, a classification approach will be used, with student test scores converted to bins, with the best number to be determined through extensive testing

### Business Requirement 3 - Construction of Streamlit dashboard
- Once all data analysis, data visualisation and machine learning tasks are completed, the focus of the project can switch to construction of the dashboard
- All necessary data analysis plots must be saved and inserted into the dashboard pages
- Appropriate commentary on those plots must be supplied
- Users must be be able to ineterface with the machine learning models so that they may make predictions


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

25/11/22:
Fit math_score pipeline

27/11/22:
Fit reading_score pipeline

2/12/22:
Fit writing_score pipeline

5/12/22:
Round up performance of all machine learning pipelines



## Notebook discussions

In this section I will discuss the various notebooks created and populated in the course of the project. The notebooks themselves have appropriate commentary, but they are long and hence the commentary is spread out. All of the notebooks were initially constructed from a single template that contains the code cells to set the working directory, and the markdown cells to outline the purpose of the notebook. Each notebook is independent, and does not rely on any other notebook, though if you have forked this project or used it as a template, them you must run the first notebook before any others, so that you can download the data from Kaggle.

### Data Collection Notebook

Notebook `01-data-collection.ipynb` deals with the collection of the dataset from Kaggle. [It can be accessed here](https://www.kaggle.com/datasets/whenamancodes/students-performance-in-exams). 

This notebook also contains some basic, surface-level data inspection. The dataset has 8 columns and 1000 rows. The first 5 columns have the object datatype, meaning that they contain categorical data. The last 3 columns have the int64 datatype, meaning that they contain numerical data.

After this basic inspection, I found it necessary to rename the columns for increased clarity and ease of use:
- `race/ethnicity` column renamed to `ethnicity`
- `parental level of education` column renamed to `parental_education`
- `lunch` column renamed to `lunch_program`
- `test preparation course` column renamed to `test_preparation_course`
- `math score` column renamed to `math_score`
- `reading score` column renamed to `reading_score`
- `writing score` column renamed to `writing_score`

I then added a column of my own called `average_score`, which averages the values in each of the 3 numerical datatype columns. This was done to provide an overall picture of a student's performance.

The final step of this notebook is to save the downloaded and modified dataset as a CSV file in the outputs/datasets/collection directory. As this code cell saves a file, there is terminal command that deletes an extant file of the same name, in case the notebook is being re-run.

### Data Analysis 1 Notebook

Notebook `02-data-analysis-1.ipynb` deals with a distribution study of the dataset. As noted in that notebook, I began with a distribution study so that I could determine whether or not the dataset's numerical variables were normally distributed. Machine Learning theory generally, and the Code Institute learning material specifically, states that machine learning models are easier to construct and train if the dataset they are working with is normally distributed. I therefore determined early on that it was essential to determine the distribution status before any machine learning work could begin.

The first part of the notebook concerns the construction of a Pandas Profile Report. From this I noted several things:
- The `gender` column is evenly distributed, as there are roughly 500 records each for male and female students
- The `ethnicity` column is unevenly distributed, as some ethnicities are more numerous than others
- The `parental_education` column is somewhat evenly distributed. There are approximately 200 records for each of the `some high school`, `high school`, `some college` and `associates degree` values, whilst there are only 112 records for the `bachelor's degree` value and 70 for the `master's degree` value
- The `lunch_program` column has about twice as many counts of the `standard` value as the `free/reduced` value
- The `test_preparation_course` column has about twice as many counts of the `none` value as the `completed` value
- I also noted that the small histograms plotted for the 4 numerical variables appear to show a classic bell shape, indicating normal distribution

My first step was to plot larger histograms of the numerical variables, and annotate them with KDE lines. Though these KDE line were rough, and had tails in some cases, they still showed the classic bell shape, which I took as a sign of normal distribution.

I then used the Pingouin library's Shapiro-Wilk test, which mathematically checks for normal distribution. This returned a negative result for all 4 numerical variables, meaning that the data was not normally distributed.

I then began exploring methods that could correct for this lack of normal distribution. My initial approach was to transform the data using the Box-Cox and Yeo-Johnson Transformers. I then re-ran the Shapiro-Wilk test on these transformed datasets, and again got negative results, indicating that those transformers had failed to normally distributed the data. To confirm this, I constructed QQ Plots of each numerical variable for each of the datasets - the original and the 2 transformed datasets. As with the KDE-histograms, these superfically appeared to show normal distribution going by the straightness of the lines and the exceptionally good R2 scores. However, closer inspections revealed that the lines are somewhat rough and wobbly, and also have significant bends toward the lower-left and upper-right. At this point, I was confused. I personally lack any significant education in statistics outside my Predictive Analytics studies, so I turned to the Slack Community for assistance. Niel McEwan was kind enough to respond, and indictated that the outliers may be having an out-sized effect, given the relatively small size of the dataset - 1000 records is considered small in predictive analytics.

With this advice, I began exploring the effect of removing various outliers, to see if I could get the Shapiro-Wilk test to return positive results. Initially I filtered out records with scores below 40, but this failed to improve distribution. I then conducted extensive testing, setting the cut-off point at each integer value between 20 and 40. In all cases, the Shapiro-Wilk test failed to return positive results. I then widened the analysis, and began filtering out students who score very highly. This failed to return positive Shapiro-Wilk results as well, and I stopped this line of enquiry when I noted that this was excluding large amounts of data, which would impact any attempt to train a model.

I ultimately concluded that the data was not normally distributed, and that nothing could be done to more normally distribute it. Nonetheless, I took the rough bell-shapes of the KDE-histograms and the exceptional R2 scores of the QQ plots to mean that the data is close enough to being normally distributed to allow me to continue, though I do concede that there may be some issues with training machine learning models.

The final part of this notebook is concerned with studying the skewness and kurtosis of the data. The skewness study revealed that the `math_score` variable is heavily skewed. The kurtosis study reveals that the math_score variable has a very highly positive kurtosis, indicating that the central peaks are too tall relative to the surrounding peaks. The reading_score and writing_score variables have very highly negative kurtosis, indicating that the data is too flat. These findings reinforce the conclusion that the data is not normally distributed, as such data would not show high skewness and kurtosis values.

The remaining code cells in the notebook deal with saving the relevant plots for use within the streamlit dashboard.

### Data Analysis 2 Notebook

Notebook `03-data-analysis-2.ipynb` deals with validation of the project's primary hypotheses - those that suppose a correlative link between each of the categorical variables and the numerical variables. Each section deals with a particular categorical variable. 

The relationships are examined via 4 barplots in each section, for 20 barplots overall. These barplots essentially average the scores in each numerical variable for each value of the categorical variable. For example, in the plot that examines the relationship between the test preparation course and reading score, there are 2 bars in the plot, one which shows the average reading score of students who have completed the test preparation course and another which shows the average reading score of students who have not completed the test preparation course. No specific calculations are performed to do this, as the Seaborn barplot function handles this itself. 

The MatPlotLib `bar_label()` method is used to add the values of the bars, allowing for a direct numerical comparison. I also set the plots to remove the error bars for a cleaner look

#### Gender

I began my studies with the `gender` column. This section contains 4 Seaborn barplots, where gender is plotted against each of the numerical variables. These plots show that male students perform better than female students in maths, and that female students perform better than male students in reading and writing. Since female students perform better than male students in 2 subjects, then on average they perform slightly better overall.

#### Ethnicity

The next section studies the `ethnicity` column. The plots show that ethnicity E performs the best, scoring the highest performance in maths and reading. In writing, ethnicity D edges out ethnicity E. On average, ethnicity E performs the best, closely followed by ethnicity D. Ethnicities C and D perform the worst in all 3 subjects and hence also on average.

#### Parental Education

The third section studies the `parental_education` column. The plots show a clear trend that as a student's level of parental education increases, their exam scores improve. The plots also show that there is a considerable difference in test scores between students whose parents have completed a high school education versus students whose parents only have some high school education. 

#### Lunch Program

The fourth section studies the `lunch_program` column. The plots show clearly that a student's lunch program has a large influence on their test scores. Those students on the standard lunch program perform significantly better than those students in the free/reduced lunch program.

#### Test Preparation Course

The last section studies the `test_preparation_course` column. The plots show that a student's participation in the test preparation course has a large influence on their test scores. Those students who complete the test preparation course achieve significantly higher scores.


### Data Analysis 3 Notebook

Notebook `04-data-analysis-3.ipynb` deals with the validation of the project's secondary hypotheses - those that suppose some link between pairs of categorical variables. Each section deals with a particular hypothesis and the associated pair of variables.

The first part of the notebook deals with data preparation. In order to properly investigate these relationships, I determined that I had to arbitrarily encode the categorical variables, which was accomplished using dictionaries that map each value to a number. I then dropped the numerical variable columns, as these were immaterial to the analysis.

I determined that the first step in determining any relationships was a correlation study using the `corr()` method. I then plotted these on a heatmap. This showed no significant correlations between the categorical variables.

I then considered that perhaps a more targeted study of the pairs of categorical variables in the hypotheses might reveal some correlative link. Determining the correct method for this proved difficult. I began with examining the parental_education and test_preparation_course variables.

#### Parental education - test preparation course

First, I used the `filter()` method to exclude all but the parental_education and test_preparation_course variables. I then used the `query()` method to produce 2 dataframes. The first contains only those students who have completed the test preparation course, and the second contains those students who have not completed the test preparation course. I then used the `value_counts()` method to calculate the counts of each value of parental_education in each of the dataframes. This is where I first ran into difficulties. Since the test_preparation_course variable is not evenly distributed, the Pandas series constructed by the `value_counts()` method could not be directly compared. I constructed barplots with number labels on them, but again, these could not be compared.

To circumvent this issue, I used the `normalize` attribute of the `value_counts()` method, and sorted the series by index. This produced Series that contain relative counts, similar to percentages. I then translated these series into dataframes, appending a third column that multiplies the normalised value counts by 100, which produces a more user-friendly percentage value.

These dataframes were then used to construct Seaborn barplots. As I note in the notebook and in the Streamlit dashboard, these two plots must be viewed together. The differences between the two indicate differences in the parental education of students who have completed and who have not completed the test preparation course. Overall, it appears that students who complete the test preparation course appear to have slightly better educated parents on average, which can be seen by the differences in height of the `high school`, `some college` and `associates degree` bars. However, as I note in the Streamlit dashboard, this correlative link is slight. It exists, but is not large.

Once I had the above method nailed down, I proceeded to examine the other hypotheses and the associated pairs of variables.

#### Parental Education - School Lunch program

In this section, I showed that the hypothesis that supposes a link between a student's parental education and the school lunch program they participate in is true but slight. This is demonstrated by the differences in bar size in the `some college` and `bachelor's degree` columns. It is therefore possible to say that students who participate in the standard lunch lunch program have slightly better educated parents overall.

#### Parental Education - Ethnicity

This section is longer than the others, as both of the variables under examination have more than 2 values. However, some interesting insights were gleaned by comparing the plots. Students of Ethnicity A appear to have more highly educated parents, closely followed by students of ethnicity B. Students of ethnicities D and E appear to have parents who are less well educated. Students of ethnicity C appear to have parents who have average levels of education. It is therefore possible to say that student ethnicity and parental education are linked - certain ethnicities are better educated.

This hypothesis is the only one that I can validate as definitively true, and that there is a large, noticably influence. The other secondary hypotheses are either only slightly true or false.

This particular study is very interesting when combined with the studies into how parental_education and ethnicity affect affect test scores.

I have established that parents of students of ethnicity A are highly educated. However, students of ethnicity A appear to perform relatively poorly in their exams. The same is true of students of ethnicity C, whose parents have middling education levels, and yet perform poorly in their exams. Conversely, students of ethnicities D and E have parents who are less well educated overall, and yet these students perform very well in their exams.

This is a curious thing to identify, though we do not have the data to make further judgements.

#### Ethnicity - Lunch Program

In this section, I showed that student ethnicity has a slight influence on their lunch program. The differences in bar height for ethnicity D and ethnicity E show this. There are no meaningful differences for the other ethnicities, hence the validation of true but slight.

#### Ethnicity - Test Preparation Course

In this section I showed that the hypothesis that a student's ethnicity influences their participation in the test preparation course is true but slight. Ethnic group A appears to participate in the test preparation course at a slightly higher rate, and ethnic group C appears to participate at a slightly lower rate.

#### Gender - Test Preparation Course

In this section I showed that the hypothesis that a student's gender influences their participation in the test preparation course is false. There is no meaningful difference in participation rates for each of the2 genders.

#### Conclusions

Based on these studies, I showed that the categorical variables are mostly independent. There is evidence of slight relationships between certain pairs of variables, and definite evidence of a link between parental education and ethnicity.

### Correlation study

By this point, I had thoroughly investigated the dataset for correlations and relationships. Before moving onto the machine learning section of the project, I decided to conduct a general correlation study, so as to determine if any of the categorical variables had any particularly strong correlations with the numerical variables, as this may have influenced the model training process. 

To do this, I loaded the dataset and applied the One Hot Encoder, which is the normal way of preparing a dataset containing categorical variables for a correlation study.

I decided to use both the Pearson and Spearman correlation methods for each of the numerical variables. Unfortunately, the correlation studies only showed weak correlation levels (between 0.2 and 0.4) at maximum, and often considerably less than that.

For the math_score variable, both methods of the correlation study determined that the lunch_program variable has the highest correlation

For the reading_score variable, both methods of the correlation study determined that the lunch_program and test_preparation_course variables have the highest correlation

For the writing_score variable, both methods of the correlation study determined that the lunch_program and test_preparation_course variables have the highest correlation

I also conducted a Predictive Power Score study, so as to determine if any of the categorical variables had particularly strong predictive power over the numerical variables.

For the math_score variable, the Predictive Power Study indicated that the lunch_program variable has the greatest predictive power by far. This tallied with the second data analysis notebook, which indicated that lunch_program has a large effect on test scores.

For the reading_score variable, the Predictive Power Study indicated that the lunch_program variable has the greatest predictive power, though this technically under the threshold for strong predictive power.

For the writing_score variable, the Predictive Power Study indicated that the lunch_program and test_preparation_course variables had the strongest predictive power.

I determined that when training machine learning models that the lunch_program and test_preparation_course variables would probably feature heavily.

### Parallel plots

I determined that, before begining the process of training machine learning models, that it would be useful to generate Parallel Plots to see how the categorical variables connects to each of the numerical variables. The idea was to reinforce the conclusion that the categorical variables were mostly independent, with only slight relationships between them, as was identified when validating the secondary hypotheses, and also to determine if I had missed any such relationships, as Parallel Plots show the entire dataset on one interactive plot. If I had missed any relationships, they would be visible by noticably clumps of lines between each y-axis.

Before I could construct parallel plots, I first had to sort the numerical variables into bins. I easily appropriated the code from the Churnometer Walkthrough Project to do this. To improve user-friendliness, I also renamed the bins, again using code from the Churnometer project.

Once that had been done, I constructed the parallel plots. These prove that the identified relationships between the categorical variables are slight, as noted, since no patterns can be easily discerned in any of the three parallel plots.

### Feature engineering

Once the parallel plots had been constructed, I decided that there was nothing more that needed to be done regarding the data analysis portion of the project, and that I could move my focus to training machine learning models.

Prior to this, I decided to undertake some feature engineering work. Primarily, this involved the use of the `SmartCorrelatedSelection()` method to determine if any feature variables were correlated enough that they needed to be dropped prior to fitting a model. In a way, this served as a further reinforcement of the conclusion that the categorical feature variables were independent.

### Math score regression

### Math score classification

### Reading score classification

### Writing score classification

### Conclusions


## Hypothesis validation

## Screenshots

## Credits

https://stackoverflow.com/questions/34734940/row-wise-average-for-a-subset-of-columns-with-missing-values - for average row values

https://stackoverflow.com/questions/40088585/turn-off-error-bars-in-seaborn-bar-plot - add values to barplots and remove confidence intervals

https://stackoverflow.com/questions/34615854/seaborn-countplot-with-normalized-y-axis-per-group - seaborn countplot with normalised y-axis counts

https://www.hostinger.co.uk/tutorials/how-to-remove-files-and-folders-using-linux-command-line/#:~:text=To%20permanently%20remove%20a%20directory,use%20rm%20%2Dr%20%5Bdirname%5D - linux terminal commands

https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/936220/Retaining_the_current_grading_system_-_arguments_and_evidence_290419.pdf - ofsted ranking system for justifying number of classification bins

https://towardsdatascience.com/multi-class-metrics-made-simple-part-i-precision-and-recall-9250280bddc2

https://towardsdatascience.com/multi-class-metrics-made-simple-part-ii-the-f1-score-ebe8b2c2ca1

https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D - for adding lines to custom legends

https://towardsdatascience.com/how-to-use-your-own-color-palettes-with-seaborn-a45bf5175146 - custom colour palettes for seaborn plots

https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible
and 
https://stackoverflow.com/questions/39500265/how-to-manually-create-a-legend - for custom legends as well

https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/2 - for Streamlit bullet points

https://stackoverflow.com/questions/54735877/seaborn-countplot-series-doesnt-recognize-input - construct barplots from series


Performance:
`Warning: Your slug size (418 MB) exceeds our soft limit (300 MB) which may affect boot time.`
