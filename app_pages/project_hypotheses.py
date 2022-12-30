import streamlit as st


def project_hypotheses():

    st.write("## Project Hypotheses")

    st.info(
        "After examining the dataset provided, I was able to formulate some"
        " hypotheses. I have split these into 2 classes, which I call"
        " **primary** and **secondary**."
        " The primary hypotheses are those that"
        " suppose some relationship between each of the 5 categorical feature"
        " variables and the students' test scores. The secondary hypotheses"
        " are those that suppose that relationships exist between the"
        " categorical variables."
        f"\n\n"
    )

    st.info(
        "### Primary hypotheses"
        f"\n\n"
        "The primary hypotheses are below"
        f"\n\n"
        "I hypothesize that:"
        f"\n\n"
        "1 - A student's gender has an effect on their test scores"
        f"\n\n"
        "2 - A student's ethnicity has an effect on their test scores"
        f"\n\n"
        "3 - Students of better educated parents achieve higher test scores"
        f"\n\n"
        "4 - A students' lunch program affects their exam scores"
        f"\n\n"
        "5 - Students who attend the Test Preparation Course achieve"
        " high exam scores"
        f"\n\n"
    )

    st.info(
        "### Secondary hypotheses"
        f"\n\n"
        "The secondary hypotheses are below. These suppose some link"
        " between the categorical variables. They are below."
        f"\n\n"
        "I hypothesize that:"
        f"\n\n"
        "6 - that increased levels of parental education correlate"
        " with increased participation in the test preparation program."
        f"\n\n"
        "7 - that increased levels of parental education correlate with"
        " increased participation in the standard lunch program."
        f"\n\n"
        "8 - that a student's ethnicity is linked to"
        " their parent's educational level. In simpler terms, this"
        " supposes that some ethnicities are better educated than others."
        f"\n\n"
        " 9 - that a student's ethnicity has an effect on their"
        " participation in the free/reduced school lunch program. In"
        " simpler terms, this supposes that certain ethnicities participate"
        " in the free/reduced lunch program at higher or lower rates."
        f"\n\n"
        "10 - that a student's ethnicity has an effect on their participation"
        " in the test preparation course, or more simply that certain"
        " ethnicities participate in the test preparation course at higher"
        " rates than other ethnicities."
        f"\n\n"
        "11 - that a student's gender has an effect on their participation"
        " in the test preparation course."
        f"\n\n"
    )
