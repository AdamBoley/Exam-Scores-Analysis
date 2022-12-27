import streamlit as st
from src.data_management import load_output_data, load_input_data


def data_analysis_primary():

    st.write("## Primary Data Analysis")

    st.info(
        "On this page I will present the plots that I will use"
        " to validate the primary hypotheses."
        f"\n"
        "Before I do so, I will recap the modified dataset, as this was the"
        " dataset used to formulate these plots"
        )

    df_output = load_output_data()

    st.write("### Modfied dataset")

    st.write(df_output)

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
    )
