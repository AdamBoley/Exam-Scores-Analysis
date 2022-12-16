import streamlit as st


def predict_maths(live_vars, math_features, math_pipeline, math_label_map):

    # subset feature variables
    math_live_vars = live_vars.filter(math_features)

    # Make prediction
    math_prediction = math_pipeline.predict(math_live_vars)
    math_prediction_probability = math_pipeline.predict_proba(math_live_vars)

    # display results
    probability = math_prediction_probability[0, math_prediction][0]*100
    math_classes = math_label_map[math_prediction[0]]

    if math_prediction != 1:
        statement = (
            f"There is a {probability.round(2)}% probability that the"
            f" student will score {math_classes} points in their math exam"
        )

    else:
        statement = (
            f"The model predicts that the student will score {math_classes}"
            f" points in their math exam."
        )

    st.write(statement)


def predict_reading(live_vars, reading_features, reading_pipeline, reading_label_map):

    # subset feature variables
    reading_live_vars = live_vars.filter(reading_features)

    # Make prediction
    reading_prediction = reading_pipeline.predict(reading_live_vars)
    reading_prediction_probability = reading_pipeline.predict_proba(reading_live_vars)

    # display results
    probability = reading_prediction_probability[0, reading_prediction][0]*100
    reading_classes = reading_label_map[reading_prediction[0]]

    if reading_prediction != 1:
        statement = (
            f"There is a {probability.round(2)}% probability that the"
            f" student will score {reading_classes} points in their"
            " reading exam"
        )

    else:
        statement = (
            f"The model predicts that the student will score {reading_classes}"
            f" points in their reading exam."
        )

    st.write(statement)


def predict_writing(live_vars, writing_features, writing_pipeline, writing_label_map):

    # subset feature variables
    writing_live_vars = live_vars.filter(writing_features)

    # Make prediction
    writing_prediction = writing_pipeline.predict(writing_live_vars)
    writing_prediction_probability = writing_pipeline.predict_proba(writing_live_vars)

    # display results
    probability = writing_prediction_probability[0, writing_prediction][0]*100
    writing_classes = writing_label_map[writing_prediction[0]]

    if writing_prediction != 1:
        statement = (
            f"There is a {probability.round(2)}% probability that the"
            f" student will score {writing_classes} points in their"
            " writing exam"
        )

    else:
        statement = (
            f"The model predicts that the student will score {writing_classes}"
            f" points in their writing exam."
        )

    st.write(statement)
