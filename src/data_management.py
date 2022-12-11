import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_input_data():
    input_path = 'inputs/datasets/raw/exams.csv'
    df_input = pd.read_csv(input_path)
    return df_input


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_output_data():
    output_path = 'outputs/datasets/collection/student-exam-results.csv'
    df_output = pd.read_csv(output_path)
    return df_output


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
