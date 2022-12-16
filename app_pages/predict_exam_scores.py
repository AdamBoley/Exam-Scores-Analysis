import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_output_data, load_pkl_file
from src.machine_learning.predictive_analysis_interface import (
    predict_maths, predict_reading, predict_writing)


def predict_exam_scores():

    st.write("## Model Interface")

    st.info(
        "This page contains an interface that allows the user"
        " to interact with the 3 pipelines and use the models"
        " to make predictions."
    )

    # load files
    math_pipeline = load_pkl_file("outputs/ml_pipeline/predict_maths/v1/pipeline-clf-math.pkl")
    reading_pipeline = load_pkl_file("outputs/ml_pipeline/predict_reading/v1/pipeline-clf-reading.pkl")
    writing_pipeline = load_pkl_file("outputs/ml_pipeline/predict_writing/v1/pipeline-clf-writing.pkl")

    math_label_map = load_pkl_file("outputs/ml_pipeline/predict_maths/v1/label-map-math.pkl")
    reading_label_map = load_pkl_file("outputs/ml_pipeline/predict_reading/v1/label-map-reading.pkl")
    writing_label_map = load_pkl_file("outputs/ml_pipeline/predict_writing/v1/label-map-writing.pkl")

    math_features = pd.read_csv("outputs/ml_pipeline/predict_maths/v1/math-train-vars.csv").columns.to_list()
    reading_features = pd.read_csv("outputs/ml_pipeline/predict_reading/v1/reading-train-vars.csv").columns.to_list()
    writing_features = pd.read_csv("outputs/ml_pipeline/predict_writing/v1/writing-train-vars.csv").columns.to_list()

    # Acquire live data
    live_vars = AcquireInputs()

    if st.button("Make Predictions"):
        predict_maths(live_vars, math_features, math_pipeline, math_label_map)
        predict_reading(live_vars, reading_features, reading_pipeline, reading_label_map)
        predict_writing(live_vars, writing_features, writing_pipeline, writing_label_map)


def AcquireInputs():

    df = load_output_data()

    column1, column2, column3, column4 = st.beta_columns(4)

    live_vars = pd.DataFrame([], index=[0])

    with column1:
        feature = 'lunch_program'
        streamlit_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    live_vars[feature] = streamlit_widget

    with column2:
        feature = 'ethnicity'
        streamlit_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    live_vars[feature] = streamlit_widget

    with column3:
        feature = 'parental_education'
        streamlit_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    live_vars[feature] = streamlit_widget

    with column4:
        feature = 'test_preparation_course'
        streamlit_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    live_vars[feature] = streamlit_widget

    st.write(live_vars)

    return live_vars
