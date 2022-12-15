import streamlit as st
from src.data_management import load_output_data, load_input_data


def distribution_analysis():

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
