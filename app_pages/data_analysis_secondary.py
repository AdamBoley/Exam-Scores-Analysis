import streamlit as st
from src.data_management import load_output_data, load_input_data
from feature_engine.discretisation import ArbitraryDiscretiser
import numpy as np
import plotly.express as px


def data_analysis_secondary():

    st.write("## Secondary Data Analysis")

    st.info(
        "On this page I will present the plots that I will use"
        " to validate the primary hypotheses."
        f"\n"
        "Before I do so, I will recap the modified dataset, as this was the"
        " dataset used to formulate these plots."
        )

    df_output = load_output_data()

    st.write("### Modfied dataset")

    st.write(df_output)

    st.write("### Secondary Data Analysis Plots")

    st.info(
        "Now that the primary hypotheses have been investigated,"
        f" we can investigate the secondary hypotheses.\n"
        f"\n"
        "Of the 6 secondary hypotheses that were initially made, only one"
        " was identified as absolutely false. Another was identified as"
        " absolutely true. The remaining 5 were identified as slightly true"
        ", which means that a relationship or influence was identified, but"
        " was considered slight enough that labelling it as"
        " true would be inaccurate. To illustrate this, those hypotheses"
        " are presented with an orange background, to show their"
        f" indeterminate status.\n"
        "It should also be noted that these plots mean little when considered"
        " in isolation. They are intended to be considered relative to each"
        " other, as that is where differences can be identified, and"
        " hence insights gleaned."
        )

    st.write(
        "#### Hypothesis 6 - Parental Education - Test Preparation Course"
        )

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
        " This is noted by the differences in the *high school*,"
        " *some college*, and *associates degree* columns."
    )

    st.write("#### Hypothesis 7 - Parental Education - Lunch Program")

    st.info(
        "Below are the plots that reveal the slight relationship"
        " between the parental education of a student and the lunch"
        " program that they participate in."
    )

    st.image(
        "outputs/plots/parental-education-lunch-program/parental-education-lunch-program-std.png"
    )

    st.image(
        "outputs/plots/parental-education-lunch-program/parental-education-lunch-program-fr.png"
    )

    st.info(
        "If we examine the above plots we can see differences in the"
        " *some college* and *bachelors degree* columns."
        " We see that students whose parents have some college"
        " education participate in the free/reduced lunch program"
        " at a higher rate, and also that students whose parents have"
        " bachelors degrees participate in the standard lunch program"
        " at a slightly higher rate. These differences are slight, and"
        " hence indicative of a weak correlation, but are large enough to"
        " be noted and remarked on"
    )

    st.write(
        "#### Hypothesis 8 - Student Ethnicity - Parental Education"
        )

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
        " This is evidenced by the smaller *some high school*"
        " and *associates degree*"
        " columns, and the larger *some college* and "
        f" *bachelor's degree* columns.\n"
        f"\n"
        "Students of ethnicity B have parents who are almost as well"
        " educated as those of ethnicity A. This is evidenced by"
        f" the larger *masters degree* column.\n"
        f"\n"
        "Students of ethnicities D and E have parents who are less well"
        " educated. This is evidenced by the larger *some high school*"
        " and *high school* columns, and the smaller *masters degree*"
        f" columns.\n"
        f"\n"
        " In general, we are looking at the relative sizes of the columns."
        " Larger columns on the left indicate less well educated parents,"
        " whereas larger columns on the right indicate better"
        " educated parents."
    )

    st.write("#### Hypothesis 9 - Ethnicity - Lunch Program")

    st.info(
        "Below are the plots that there is a slight relationship"
        " between a student's ethnicity and their lunch program."
        " As before, the plots must be considered together."
    )

    st.image(
        "outputs/plots/ethnicity-lunch-program/ethnicity-lunch-program-std.png"
    )

    st.image(
        "outputs/plots/ethnicity-lunch-program/ethnicity-lunch-program-fr.png"
    )

    st.info(
        "If we examine the above plots, we can see differences in the"
        " group D and group E columns. We can see that group D participates"
        " in the standard lunch program at a noticably higher rate, and that"
        " group E participates in the free/reduced lunch program at a"
        " noticably higher rate."
    )

    st.write("#### Hypothesis 10 - Ethnicity - Test Preparation Course")

    st.info(
        "Below are the plots that there is a slight relationship"
        " between a student's ethnicity and their participation."
        " in the test preparation course."
        " As before, the plots must be considered together."
    )

    st.image(
        "outputs/plots/ethnicity-test-prep-course/ethnicity-test-prep-course-comp.png"
    )

    st.image(
        "outputs/plots/ethnicity-test-prep-course/ethnicity-test-prep-course-none.png"
    )

    st.info(
        "If we examine the above plots, we can differences in the columns."
        " We can see that *group C* completes the test preparation"
        " at a slightly lower rate, and that *group A* does complete the test"
        " preparation course at a slightly higher rate."
    )

    st.write("#### Hypothesis 11 - Gender - Test Preparation Course")

    st.info(
        "Below are the plots that reveal that there is no relationship"
        " between student gender and their participation in the test"
        " preparation course."
    )

    st.image(
        "outputs/plots/gender-test-prep-course/gender-test-prep-course-comp.png"
    )

    st.image(
        "outputs/plots/gender-test-prep-course/gender-test-prep-course-none.png"
    )

    st.info(
        "If we examine the above plots, we can confirm that"
        "Both genders participate in the test"
        " preparation course at almost exactly same rate."
        " There is no discernable difference in column size."
    )

    st.write("### Parallel Plots")

    scores_map = [-np.Inf, 20, 40, 60, 80, 100, np.Inf]

    discretiser = ArbitraryDiscretiser(binning_dict={
        'math_score': scores_map,
        'reading_score': scores_map,
        'writing_score': scores_map
        })
    df_parallel = discretiser.fit_transform(df_output)

    n_classes = len(scores_map) - 1
    classes_ranges = discretiser.binner_dict_['math_score'][1:-1]

    labels_map = {}
    for n in range(0, n_classes):
        if n == 0:
            labels_map[n] = f"0 to {classes_ranges[0]}"
        elif n == n_classes-1:
            labels_map[n] = f"{classes_ranges[-1]}+"
        else:
            labels_map[n] = f"{classes_ranges[n-1] + 1} to {classes_ranges[n]}"

    df_parallel['math_score'] = df_parallel['math_score'].replace(labels_map)
    df_parallel['writing_score'] = df_parallel['writing_score'].replace(labels_map)
    df_parallel['reading_score'] = df_parallel['reading_score'].replace(labels_map)

    # math score parallel plot
    df_parallel_maths = df_parallel.drop(['reading_score', 'writing_score'], axis=1)

    fig_parallel_maths = px.parallel_categories(df_parallel_maths, width=900, height=600)

    st.plotly_chart(fig_parallel_maths)

    # reading score parallel plot
    df_parallel_reading = df_parallel.drop(['math_score', 'writing_score'], axis=1)

    fig_parallel_reading = px.parallel_categories(df_parallel_reading, width=900, height=600)

    st.plotly_chart(fig_parallel_reading)

    # writing score parallel plot
    df_parallel_writing = df_parallel.drop(['math_score', 'reading_score'], axis=1)

    fig_parallel_writing = px.parallel_categories(df_parallel_writing, width=900, height=600)

    st.plotly_chart(fig_parallel_writing)

    st.info(
        "Parallel plots reveal the mostly-independent nature"
        " of the categorical variables."
        " We cannot visually determine any patterns."
        " The categorical relationship plots show some"
        " small differences, but these are small enough that"
        " we should not expect to see them in the parallel plots."
    )

    st.write("### Conclusions")

    st.info(
        "Overall, we can safely conclude that the categorical"
        " feature variables are mostly independent, and that,"
        " while they do influence each other, this influence is slight"
        " in most cases, and is hence unnoticable in the parallel plots."
        f"\n"
        "A student's parental education is linked to their"
        " lunch program - better educated parents see their children"
        " participate in the standard lunch program at slightly higher rates"
        f"\n"
        "Increased parental education leads to increased participation"
        " in the test preparation course. This is the only case where the"
        " influence is not slight."
        f"\n"
        "Student ethnicity"
        " is connected to parental education. I am being careful with"
        " my words here, so I will simply say that it appears that"
        " students of certain ethnicities tend to have better"
        " educated parents, and students of other ethnicities tend"
        " to have less well educated parents."
        " This influence is nonetheless slight."
        f"\n"
        "A student's ethnicity slightly influences which lunch program"
        " they participate in."
        f"\n"
        "A student's ethnicity slightly influences their participation"
        " in the test preparation course."
        f"\n"
        "A student's gender has no real influence on their participation"
        " in the test preparation course."
    )

    st.success(
        "On the next page, I will sum up the relationships"
        " identified here, and validate the hypotheses outlined on the"
        " previous page, stating whether I have hypothesized correctly or"
        " incorrectly."
    )
