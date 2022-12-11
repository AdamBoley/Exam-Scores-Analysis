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

    # st.image(image='outputs/plots/ethnicity/ethnicity-math-plot.png')
