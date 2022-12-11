import streamlit as st
from src.data_management import load_output_data, load_input_data


def data_analysis():

    st.write("## Data Analysis")

    st.write("### Datasets")

    df_input = load_input_data()
    df_output = load_output_data()

    st.info(
        f"Before the plots on this page can make sense to a reader"
        f" they must see the actual dataset that was used to construct them.\n"
        f"\n"
        f"Below are 2 datasets - the input dataset I was provided with by"
        f" the local government, and a modified version I used for all"
        f" data analyses and subsequent work\n"
        f"\n"
        f"The modified dataset changes the format of the column headers"
        f" which makes data manipulation easier, and also adds a column"
        f" called **average_score**, which averages the 3 preceeding score"
        f" columns to provide an overall indication of a students'"
        f" performance\n"
        )

    st.write("#### Input dataset")

    st.write(df_input)

    st.write("#### Modfied dataset")

    st.write(df_output)

    st.write("### Distribution and QQ plots")

    st.info(
        "Before we can examine the relationships within the data,"
        f" it is necessary to first examine the data itself\n"
        f"\n"
        f"In particular, we want to see whether the numerical data is"
        f" normally distributed. This is because normally distributed data"
        f" is easier to work with.\n"
        f"\n"
        f"Below are histograms with KDE lines, which serve as good visual"
        f" indicators of normally distributed data. Building machine"
        f" learning models is easier if the dataset is normally distributed."
        )

    st.write("#### Distribution plots")

    st.info(
        "These 4 plots are histograms, which show counts of various"
        f" groupings of score, called bins. Histograms are generally used to"
        f" examine distribution. When looking for normally distribution, we"
        f" are looking for the KDE line to be in a bell shape"
    )

    st.write("**Math Score Distribution**")

    st.image(
        image='outputs/plots/distribution/math-score-distribution-plot.png'
        )

    st.info(
        f"Above is the distribution plot for the math_score variable\n"
        f"The KDE line shows a classic bell shape, indicating normal"
        f" distribution."
    )

    st.write("**Reading Score Distribution**")

    st.image(
        image='outputs/plots/distribution/reading-score-distribution-plot.png'
    )

    st.info(
        "For the reading_score, the bell shape is still present"
        f" but to a lesser degree, since the KDE line is not smooth."
        f" However, we can still say that the reading_score variable is"
        f" normall distributed."
        )

    st.write("**Writing Score Distribution**")

    st.image(
        "outputs/plots/distribution/writing-score-distribution-plot.png"
    )

    st.info(
        "For the writing_score variable, the bell shape is present"
        f" but again to a lesser degree, as ther KDE line is not smooth."
        f" However, the writing_score variable is still normally"
        f" distributed\n"
    )

    st.write("**Average Score Distribution**")

    st.image(
        "outputs/plots/distribution/average-score-distribution-plot.png"
    )

    st.info(
        "For the average_score variable, the bell shape is again present"
        f", but the KDE line is not smooth. This is to be expected, since"
        f" the average_score variable is constructed from the other"
        f" 3 variables, 2 of which have rougher KDE lines."
        f" Since the other 3 variables have been identified as normally"
        f" distributed, we can say that the average_score variable is also"
        f" normally distributed\n"
    )

    st.write("#### QQ Plots")

    st.info(
        "The next 4 plots are QQ Plots, which are another method of"
        " examining distribution. A QQ plot indicates that the data is"
        " normally distributed if the line is roughly straight, and hence"
        " has an R2 score of close to 1"
    )

    st.write('**Math Score QQ Plot**')

    st.image(
        'outputs/plots/distribution/math-score-qq-plot.png'
    )

    st.info(
        "The math_score QQ plot strongly indicates that the math_score"
        " variable is normally distributed. The line is exceptionally straight"
        " with very little deviation. This produces an R2 score that is very"
        " close to 1."
    )

    st.write('**Reading Score QQ Plot**')

    st.image(
        'outputs/plots/distribution/reading-score-qq-plot.png'
    )

    st.info(
        "The reading_score QQ plot strongly indicates that the math_score"
        " variable is normally distributed. The line is exceptionally straight"
        " with very little deviation. This produces an R2 score that is very"
        " close to 1."
    )

    st.write('**Writing Score QQ Plot**')

    st.image(
        'outputs/plots/distribution/writing-score-qq-plot.png'
    )

    st.info(
        "The writing_score QQ plot strongly indicates that the math_score"
        " variable is normally distributed. The line is exceptionally straight"
        " with very little deviation. This produces an R2 score that is very"
        " close to 1."
    )

    st.write('**Average Score QQ Plot**')

    st.image(
        'outputs/plots/distribution/average-score-qq-plot.png'
    )

    st.info(
        "The average_score QQ plot strongly indicates that the math_score"
        " variable is normally distributed. The line is exceptionally straight"
        " with very little deviation. This produces an R2 score that is very"
        " close to 1. This is unsurprising, given the high R2 scores of"
        " the QQ plots of the constituent variables."
    )

    st.write("#### Conclusions")

    st.info(
        "Given the evidence presented in the KDE-histograms and QQ plots,"
        " we can now be sure that the numerical variables are"
        " normally distributed."
    )

    # save and insert dataframe of Shapiro-Wilk test?

    # st.image(image='outputs/plots/ethnicity/ethnicity-math-plot.png')

    st.write("### Primary Data Analysis Plots")

    st.info(
        "We can now begin to identify which of the categorical feature"
        " variables affect the numerical target variables, and to what degree."
        " In so doing, we can validate our primary hypotheses"
    )

    st.write("#### Gender Plots")

    st.info(
        "We can now examine how a student's gender affects their test scores."
        " Below are 4 plots, which show how each of the numerical variables"
        " is affected by the gender variable"
    )

    st.write('**Math Score**')

    st.image(
        'outputs/plots/gender/gender-maths-plot.png'
    )

    st.write('**Reading Score**')

    st.image(
        'outputs/plots/gender/gender-reading-plot.png'
    )

    st.write('**writing Score**')

    st.image(
        'outputs/plots/gender/gender-writing-plot.png'
    )

    st.write('**Average Score**')

    st.image(
        'outputs/plots/gender/gender-average-plot.png'
    )

    st.info(
        "As we can see in the above plots, male students outperform"
        " female students in mathematics, whereas female students"
        " outperform male students in reading and writing."
        " This means that female students outperform on average slightly"
    )

    st.write("#### Ethnicity Plots")

    st.info(
        "We can now examine how a student's ethnicity affects their test"
        " scores."
        " Below are 4 plots, which show how each of the numerical variables"
        " is affected by the ethnicity variable."
        " These plots are more complex than the gender plots, due to"
        " the existence of 5 values for the ethnicity variable."
    )

    st.write('**Math Score**')

    st.image(
        'outputs/plots/ethnicity/ethnicity-math-plot.png'
    )

    st.write('**Reading Score**')

    st.image(
        'outputs/plots/ethnicity/ethnicity-reading-plot.png'
    )

    st.write('**writing Score**')

    st.image(
        'outputs/plots/ethnicity/ethnicity-writing-plot.png'
    )

    st.write('**Average Score**')

    st.image(
        'outputs/plots/ethnicity/ethnicity-average-plot.png'
    )

    st.info(
        "As we can see in the above plots, ethnicity does have an effect"
        " on test scores. As we have 5 ethnicities, describing every"
        " relationship would be exhaustive and redundant. Instead, we can"
        f" describe observations of general trends.\n"
        f"\n"
        f"In mathematics, ethnicity E has a outperforms the next highest"
        f" performing ethnicity, ethnicity D, by 5 points."
        f" Ethnicities B and C perform the worst.\n"
        f"\n"
        "In reading, the differences between the performance of the"
        " various ethnicities is smaller."
        " Ethnicities E and D perform roughly equally. Ethnicities B and C"
        f" again perform the worst\n"
        f"\n"
        "In writing, the differences between the performance of the"
        " various ethnicities is smaller than that of the math_score,"
        " but larger than that of the reading_score."
        " Interestingly, ethnicity D performs the best."
        f" Ethnicities B and C continue to perform the worst.\n"
        f"\n"
        f"On average, ethnicity E performs the best, and ethnicities"
        f" B and C perform the worst\n"
        f"\n"
        "In conclusion, ethnicities E and D perform the best,"
        " ethnicity A has middling performance, and ethnicities"
        f"B and C perform the worst.\n"
        f"\n"
        "Overall, we can say that ethnicity has an effect on test scores."
    )

    st.write("#### Parental Education Plots")

    st.info(
        "We can now examine how the education of a student's parents"
        " affects their test scores."
        " Below are 4 plots, which show how each of the numerical variables"
        " is affected by the parental_education variable."
        " These plots are more complex than the gender plots, due to"
        " the existence of 6 values for the parental_education variable."
    )

    st.write('**Math Score**')

    st.image(
        'outputs/plots/parental-education/parental-education-math-plot.png'
    )

    st.write('**Reading Score**')

    st.image(
        'outputs/plots/parental-education/parental-education-reading-plot.png'
    )

    st.write('**writing Score**')

    st.image(
        'outputs/plots/parental-education/parental-education-writing-plot.png'
    )

    st.write('**Average Score**')

    st.image(
        'outputs/plots/parental-education/parental-education-average-plot.png'
    )

    st.info(
        "As we can see in the above plots, parental education"
        " does have an effect on test scores."
        " As we have 6 values for parental_education, describing every"
        " relationship would be exhaustive and redundant. Instead, we can"
        f" describe observations of general trends.\n"
        f"\n"
        f"In mathematics, we see that students of parents who only"
        " have some high school education perform very poorly."
        " However, if the parents have completed high school, performance"
        " jumps dramatically by 5 points."
        " Interestingly, parents who have some college education"
        " do not see their children perform markedly better."
        " We also see that there is no appreciable difference in"
        " performance between students of parents who have"
        " bachleor's degrees, and those whose parents have master's"
        f" degrees.\n"
        f"\n"
        "In reading, we again see students of parents with only"
        " some high school education perform poorly."
        " However, the difference in performance between those students"
        " and those whose parents have completed high school is smaller"
        " than in mathematics."
        " We again see little difference between students whose whose"
        " parents have completed high school and students whose"
        " parents have some college education."
        " Interestingly, we do see some difference in performance between"
        " students whose parents have bachelor's degrees and students"
        f" whose parents have master's degrees.\n"
        f"\n"
        "In writing, we continue to see students of parents with only"
        " some high school education perform poorly."
        " However, the difference in performance between those students"
        " and those whose parents have completed high school is smaller"
        " than in mathematics."
        " However, we do see some difference between students whose whose"
        " parents have completed high school and students whose"
        " parents have some college education."
        " Interestingly, we do see some difference in performance between"
        " students whose parents have bachelor's degrees and students"
        f" whose parents have master's degrees.\n"
        f"\n"
        "On average, we see the pattern that we might normally"
        " expect - as parental education increases, student exam"
        " performance improves. There is a considerable jump in"
        f" performance if the parents have completed high school.\n"
        f"\n"
        " In conclusion, we can see that, generally speaking,"
        " as parental education increases, student exam scores increase."
        " We can see that there is a definite advantage to having parents"
        f" complete a high school education.\n"
        f"\n"
    )

    st.write("#### Lunch Program Plots")

    st.info(
        "We can now examine how a student's lunch"
        " program affects their test scores."
        " Below are 4 plots, which show how each of the numerical variables"
        " is affected by the lunch_program variable."
    )

    st.write('**Math Score**')

    st.image(
        'outputs/plots/lunch-program/lunch-program-math-plot.png'
    )

    st.write('**Reading Score**')

    st.image(
        'outputs/plots/lunch-program/lunch-program-reading-plot.png'
    )

    st.write('**writing Score**')

    st.image(
        'outputs/plots/lunch-program/lunch-program-writing-plot.png'
    )

    st.write('**Average Score**')

    st.image(
        'outputs/plots/lunch-program/lunch-program-average-plot.png'
    )

    st.info(
        "As we can see in the above plots, a student's lunch program"
        f" has a large effect on their exam performance.\n"
        f"\n"
        "In maths, a student's lunch program has a huge effect on"
        f" their performance - there is a difference of 12 points.\n"
        f"\n"
        " In reading, the difference is smaller, but still"
        f" pronounced, at 9 points\n"
        f"\n"
        f"In writing, the difference is similar, at 9 points\n"
        f"\n"
        f"On average, the difference is 10.5 points\n"
        f"\n"
    )

    st.write("#### Test Preparation Course Plots")

    st.info(
        "We can now examine how a student's participation"
        " in the test preparation course affects their test scores."
        " Below are 4 plots, which show how each of the numerical variables"
        " is affected by the test_preparation_course variable."
    )

    st.write('**Math Score**')

    st.image(
        'outputs/plots/test-prep-course/test-prep-course-math-plot.png'
    )

    st.write('**Reading Score**')

    st.image(
        'outputs/plots/test-prep-course/test-prep-course-reading-plot.png'
    )

    st.write('**writing Score**')

    st.image(
        'outputs/plots/test-prep-course/test-prep-course-writing-plot.png'
    )

    st.write('**Average Score**')

    st.image(
        'outputs/plots/test-prep-course/test-prep-course-average-plot.png'
    )

    st.info(
        "As we can see in the above plots, a student's participation"
        " in the test preparation course has a small but"
        f" noticeable effect on their exam performance.\n"
        f"\n"
        "In maths, a student's participation in the test preparation "
        " course has a small effect on"
        f" their performance - there is a difference of 5 points.\n"
        f"\n"
        "In reading, a student's participation in the test preparation "
        " course has a larger effect on"
        f" their performance - there is a difference of 7.5 points.\n"
        f"\n"
        "In writing, a student's participation in the test preparation "
        " course has a dramatic effect on"
        f" their performance - there is a difference of 10 points.\n"
        f"\n"
        f"On average, a student's participation in the test preparation "
        " course has a considerable effect on"
        f" their performance - there is a difference of 7.5 points.\n"
        f"\n"
        "Overall, we can say that students who have completed the test"
        " preparation course perform better overall than students who do not"
    )

    st.write("#### Conclusions")

    st.success(
        "We now have a clear picture of what affects student exam"
        f" performance.\n"
        f"\n"
        "Higher performing students tend to have highly educated"
        " parents, participate in the standard lunch program,"
        " complete the test preparation course, and belong to"
        " ethnicities D and E."
        f"\n"
        "Lower performing students tend to have parents who have"
        " only some high school education, participate in the"
        " free/reduced lunch program, do not complete the"
        " test preparation course, and belong to ethnicities"
        f" B and C.\n"
        f"\n"
        " Female students perform better in reading and writing,"
        f" whereas male students perform better in maths.\n"
        f"\n"
        "The test preparation course has a lesser effect on"
        " performance than might be expected. The real determiners"
        f" are ethnicity, parental education and the school lunch program\n"
        f"\n"
        " We are now in a position to validate our primary hypotheses."
        " We will do this on the next page."
    )

    st.write("### Secondary Data Analysis Plots")

    st.info(
        "Now that the primary hypotheses have been investigated,"
        f" we can investigate the secondary hypotheses.\n"
        f"\n"
        "During my investigation of these relationships, I"
        " determined that there were only 2 cases where the hypotheses"
        " were true and that a valid relationship existed. These were"
        " that parental education influences participation in the"
        " test preparation course, and that student ethnicity is linked to"
        " parental education."
        " When interpreting these plots, it should be noted that"
        " they should be considered together, with the insights"
        " revealed in the differences between the plots."
        " In no other case was a statistically significant relationship"
        " detected."
        )

    st.write("#### Parental Education - Test Preparation Course Plots")

    st.info(
        "Below are the plots that reveal that there is a relationship"
        " between parental education and a student's participation in"
        " the test preparation course."
        " We have 2 plots here, so they must be considered together, per"
        " the note above."
    )

    st.image(
        "outputs/plots/parental-education-test-prep-course/parental-education-test-prep-course-completed.png"
    )

    st.image(
        "outputs/plots/parental-education-test-prep-course/parental-education-test-prep-course-none.png"
    )

    st.info(
        "If we examine the plots above, we see that students of less"
        " educated parents participate in the test"
        " preparation course at a noticeably lower rate."
        " This is noted by the differences in the high school"
        " some college, and associates degree columns."
    )

    st.write("#### Student Ethnicity - Parental Education Plots")

    st.info(
        "Below are the plots that reveal that there is a relationship"
        " between a student's ethnicity and their parent's level of education."
        " We have 5 plots, so they must be considered together,"
        " per the note above."
    )

    st.image(
        "outputs/plots/parental-education-ethnicity/parental-education-ethnicity-a.png"
    )

    st.image(
        "outputs/plots/parental-education-ethnicity/parental-education-ethnicity-b.png"
    )

    st.image(
        "outputs/plots/parental-education-ethnicity/parental-education-ethnicity-c.png"
    )

    st.image(
        "outputs/plots/parental-education-ethnicity/parental-education-ethnicity-d.png"
    )

    st.image(
        "outputs/plots/parental-education-ethnicity/parental-education-ethnicity-e.png"
    )

    st.info(
        "If we examine the above plots, we can draw several"
        f" conclusions."
        " Students of ethnicity A have significantly better educated parents."
        " This is evidenced by the smaller 'some high school'"
        " and `associates degree`"
        " columns, and the larger `some college` and "
        f" `bachelor's degree` columns.\n"
        f"\n"
        "Students of ethnicity B have parents who are almost as well"
        " educated as those of ethnicity A. This is evidenced by"
        f" the larger `masters degree` column.\n"
        f"\n"
        "Students of ethnicities D and E have parents who are less well"
        " educated. This is evidenced by the larger `some high school`"
        " and `high school` columns, and the smaller `masters degree`"
        f" columns.\n"
        f"\n"
        " In general, we are looking at the relative sizes of the columns."
        " Larger columns on the left indicate less well educated parents,"
        " whereas larger columns on the right indicate better"
        " educated parents."
    )

    st.write("#### Conclusions")

    st.info(
        "Overall, we can safely conclude that the categorical"
        " feature variables are mostly independent, and that"
        " they do not influence or affect each other."
        " The exceptions are those relationships identified above."
        " Increased parental education leads to increased participation"
        " in the test preparation course. In addition, student ethnicity"
        " is connected to parental education. I am being careful with"
        " my words here, so I will simply say that it appears that"
        " students of certain ethnicities tend to have better"
        " educated parents, and students of other ethnicities tend"
        " to have less well educated parents."
    )

    st.success(
        "On the next page, I will sum up the relationships"
        " identified here, and validate the hypotheses outlined on the "
        " previous page, stating whether I have hypothesized correctly or"
        " incorrectly."
    )
