import streamlit as st


def hypothesis_validation():

    st.write("## Hypothesis Validation")

    st.info(
        "We can now validate the hypotheses presented on the project"
        "_hypotheses page."
    )

    st.write("### Primary Hypotheses")

    st.success(
        f"#### Hypothesis 1\n"
        "Students who participate in the test preparation course"
        f" achieve higher exam scores than students who do not\n"
        f"\n"
        "Success - we can validate this hypothesis as true."
        " Students who participate in the test preparation course"
        " do achieve higher exam scores. The effect varies by subject."
        " In maths, the increase in performance is only 5 points."
        " In reading, the increase is 7.5 points, and in writing"
        " the increase is 10 points, for an average of 7.5 points."
        " Overall, we can say that participation in the test preparation"
        " course does increase student exam performance."
        )

    st.success(
        f"#### Hypothesis 2\n"
        f"A student's lunch program affects their exam performance\n"
        f"\n"
        "Success - we can validate this hypothesis as true. Students"
        " who participate in the standard lunch program achieve significantly"
        " higher test scores than those who participate in the free/reduced"
        " lunch program. In maths, the effect is pronounced, with a"
        " difference of 12 points. In reading and writing, the difference"
        " is 9 points. This makes for an average of 10.5 points."
        " Therefore, we can say that a student's lunch program does"
        " affect their exam performance."
    )

    st.success(
        f"#### Hypothesis 3\n"
        f"Students of better educated parents achieve higher test scores\n"
        f"\n"
        "Success - we can valiate this hypothesis as true. Students"
        " of better educated parents do perform better. The difference"
        " is particularly notable between students of parents who have some"
        " high school education and students of parents who have completed"
        " high school. In each of the scores, we see a large jump in"
        " performance. There also appears to be little discernable"
        " difference between students of parents who have bachelors degrees"
        " and students of parents with masters degrees."
    )

    st.success(
        f"#### Hypothesis 4\n"
        f"A student's gender affects their test scores\n"
        f"\n"
        " Success - we can validate this hypothesis as true."
        " Male students perform better in maths, and female students"
        " perform better in reading and writing. Male students outperform"
        " female students in maths by 6.5 points. Female students outperform"
        " male students in reading by 5 points and writing by 7.5 points."
        " Since female students outperform in 2 of the 3 subjects, the"
        " female students perform slightly better on average."
    )

    st.success(
        f"#### Hypothesis 5\n"
        f"A student's ethnicity affects their test scores\n"
        f"\n"
        " Success - we can validate this hypothesis as true."
        " Certain ethnicities perform better in exams than"
        " others. In maths, ethnicity group E performs the best by a"
        " considerable margin. In reading, groups D and E perform roughly"
        " equally, and in writing group D outperforms slightly."
        " In all three subjects and hence on average, groups B and C"
        " perform the worst, and group A has middling performance."
    )

    st.write("### Secondary Hypotheses")

    st.info(
        "As a note to the reader, several of the secondary hypotheses"
        " were shown to have noticeble but small differences. I refer to"
        " these influences as *True but slight*, meaning that a"
        " relationship was identified, but that it is small enough"
        " that no real conclusions can be drawn from it, and hence that"
        " it would be irresponsible to base educational policy"
        " on these relationships. These hypotheses are marked with"
        " an orange background."
    )

    st.warning(
        f"#### Hypothesis 6\n"
        f"\n"
        f"Increased levels of student parental education"
        " correlate with increased participation in the test"
        f" preparation course\n"
        f"\n"
        "Partial success - we can validate this hypothesis as true"
        " but slight."
        "Students of better educated parents participate in the test"
        " preparation course at slightly higher levels."
        " The influence is not strong, but is noticeable"
        " by the differences in the plots."
    )

    st.warning(
        f"#### Hypothesis 7\n"
        f"\n"
        f"Increased levels of student parental education correlate"
        f" with increased participation in the standard lunch program\n"
        f"\n"
        " Partial success - we can validate this hypothesis as true,"
        " but slight."
        "Students of better educated parents participate in the standard"
        " lunch program at a slightly higher rate."
        " The influence is not strong, but is notable."
    )

    st.success(
        f"#### Hypothesis 8\n"
        f"\n"
        "Parental education is linked to ethnicity, or more simply"
        f" that some ethnicities are better educated than others\n"
        f"\n"
        "Success - we can validate this hypothesis as true."
        " Students of ethnicity groups A and B have parents who are"
        " noticably better educated, whereas students of ethnicity"
        " groups D and E are noticably less well educated."
    )

    st.warning(
        f"#### Hypothesis 9\n"
        f"\n"
        "Student ethnicity is linked to their lunch program, or more"
        " simply that certain ethnicities participate in the different"
        f" lunch programs at different rates\n"
        f"\n"
        "Partial success - we can validate this hypothesis as true"
        " but slight."
        "Students of ethnicity D participate in the standard lunch program"
        " at a higher rate, whereas students of ethnicity E participate in"
        " the free/reduced lunch program at a higher rate. Ethnicity"
        " groups A, B and C have no real difference in lunch"
        " program participation rates."
    )

    st.warning(
        f"#### Hypothesis 10\n"
        f"\n"
        "Student ethnicity is linked to their participation"
        " in the test preparation course, or more simply that"
        " certain ethnicities participate in the test preparation"
        f" course at a higher rate than other ethnicities\n"
        f"\n"
        "Partial success - we can validate this hypothesis as true"
        " but slight."
        "Ethnicity group C completes the test preparation course"
        " at a slightly lower rate, whereas ethnicity group A"
        " completes the test preparation course at a slightly higher rate."
    )

    st.error(
        f"#### Hypothesis 11\n"
        f"\n"
        "A student's gender affects their participation in the test"
        " preparation course, or more simply that one gender participates"
        f" in the test preparation course at a higher rate than the other\n"
        f"\n"
        " Failure - we have hypothesised incorrectly. There is no"
        " discernable link between a student's gender and their participation"
        " in the test preparation course."
    )
