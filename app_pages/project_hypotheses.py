import streamlit as st


def project_hypotheses():

    st.write("## Project Hypotheses")

    st.info(
        f"After examining the dataset provided, I was able to formulate some"
        f" hypotheses. I have split these into 2 class, which I call\n"
        f" primary and secondary. The primary hypotheses are those that"
        f" suppose some relationship between each of the 5 categorical feature"
        f" variables and the students' test scores. The secondary hypotheses"
        f" are those that suppose that relationships exist between the"
        f" categorical variables\n"
        f"\n"
    )

    st.info(
        f"### Primary hypotheses\n"
        f"The primary hypotheses are below"
        f"I hypothesize that:\n"
        f"\n"
        f"1 - Students who attend the Test Preparation Course achieve"
        f" high exam scores\n"
        f"\n"
        f"2 - A students' lunch program affects their exam scores\n"
        f"\n"
        f"Note that I am not making a judgement here, just offering a neutral"
        f" observation - that there is some effect\n"
        f"\n"
        f"3 - Students of better educated parents achieve higher test scores\n"
        f"\n"
        f"4 - A student's gender has an effect on their test scores\n"
        f"\n"
        f"5 - A student's ethnicity has an effect on their test scores\n"
        f"\n"
    )

    st.info(
        f"### Secondary hypotheses\n"
        f"The secondary hypotheses are below. These suppose some link"
        f" between the categorical variables. They are below\n"
        f"I hypothesize that:\n"
        f"\n"
        f"6 - that increased levels of parental education correlate"
        f" with increased participation in the test preparation program\n"
        f"\n"
        f"7 - that increased levels of parental education correlate with"
        f" increased participation in the standard lunch program\n"
        f"\n"
        f"8 - that a student's ethnicity is linked to"
        f" their parent's educational level. In simpler terms, this"
        f" supposes that some ethnicities are better educated than others\n"
        f"\n"
        f" 9 - that a student's ethnicity has an effect on their"
        f" participation in the free/reduced school lunch program. In"
        f" simpler terms, this supposes that certain ethnicities participate"
        f" in the free/reduced lunch program at higher or lower rates\n"
        f"\n"
        "10 - that a student's ethnicity has an effect on their participation"
        " in the test preparation course, or more simply that certain"
        " ethnicities participate in the test preparation course at higher"
        f" rates than other ethnicities.\n"
        f"\n"
        f"11 - that a student's gender has an effect on their participation"
        f" in the test preparation course\n"
    )
