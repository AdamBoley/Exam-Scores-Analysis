import streamlit as st


def project_summary():

    st.write("### Project Summary")

    st.info(
        f"#### Project Introduction\n"

        f"A local government wishes to improve the exam scores"
        f" of students its schools.\n"
        f"\n"
        f"Therefore, they have contracted me to perform an analysis"
        f" and determine what factors most strongly influence student"
        f" exam scores.\n"
        f"\n"
        f"The local government has provided the records of 1000 students.\n"
        f"\n"
        f"The dataset has 5 feature variables.\n"
        f" These are non-numerical categorical variables.\n"
        f" They are:\n"
        f"- Gender\n"
        f"- Ethnicity\n"
        f"- Parental Education\n"
        f"- Lunch Program\n"
        f"- Test Preparation Course\n"
        f"\n"
        f"I will discuss these in further detail below\n"
        f"\n"
        f"##### Gender\n"
        f"The Gender variable has two values:\n"
        f"- Male\n"
        f"- Female\n"
        f"\n"
        f"##### Ethnicity\n"
        f"The Ethnicity variable indicates the ethnic"
        f" background of the student"
        f"This variable has 5 values:\n"
        f"- A\n"
        f"- B\n"
        f"- C\n"
        f"- D\n"
        f"- E\n"
        f"\n"
        f"##### Parenntal Education\n"
        f"The Parental Education variable indicates the level of"
        f" education the parents of the student have.\n"
        f"This variable has 6 values:\n"
        f"- Some High School\n"
        f"- High School\n"
        f"- Some College\n"
        f"- Associate's Degree\n"
        f"- Bachelor's Degree\n"
        f"- Master's Degree\n"
        f"\n"
        f"##### Lunch Program\n"
        f"The Lunch Program variable indicates the lunch program that"
        f" the student participates in.\n"
        f"This variable has 2 values:\n"
        f"- Standard\n"
        f"- Free/Reduced\n"
        f"\n"
        f"##### Test Preparation Course\n"
        f"The Test Preparaton Course variable indicates whether a student"
        f" completed the school's test preparation course\n"
        f"This variable has 2 values:\n"
        f"- Completed\n"
        f"- None\n"
        f"\n"
        f"Note - 'None' means that the student has not completed the course\n"
        f"\n"
        f"The dataset also has 3 continuous numerical variables."
        f"These are the student's exam scores, and are the values we are"
        f" interested in trying to predict with Machine Learning\n"
        f"\n"
        f"These variables are:\n"
        f"- math score\n"
        f"- reading score\n"
        f"- writing score\n"
    )

    st.info(
        f"For more information, see the project's Github repository:\n"
        f"https://github.com/AdamBoley/Exam-Scores-Analysis"
    )

    st.info(
        f"#### Business Requirements\n"
        f"The local government has given me 3 requirements to fulfil"
        f" for them to consider the project a success:\n"
        f"\n"
        f"1 - First, they want a general data analysis, with the aim of"
        f" determining patterns and relationships within the data.\n"
        f"The local government wishes to know which of the variables affect"
        f" the student's test scores, and to what degree.\n"
        f"They will use the identified relationships to formulate educational"
        f" policy with the aim of improving exam scores\n"
        f"\n"
        f"2 - Second, the local government wants me to produce a Machine"
        f" Learning tool which they can then use to predict"
        f" a student's test scores. If a student is predicted to score poorly"
        f" , then the local government can intervene and offer support\n"
        f"\n"
        f"3 - Third, the local government wants the fulfilments to the first"
        f" 2 business requirement to be held within a deployed"
        f" Streamlit dashboard"
        f"\n"
    )
