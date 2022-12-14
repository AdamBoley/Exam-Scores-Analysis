import streamlit as st
from app_pages.multi_page import MultiPage

# load page files:
from app_pages.project_summary import project_summary
from app_pages.project_hypotheses import project_hypotheses
from app_pages.distribution_analysis import distribution_analysis
from app_pages.data_analysis_primary import data_analysis_primary
from app_pages.data_analysis_secondary import data_analysis_secondary
from app_pages.hypothesis_validation import hypothesis_validation
from app_pages.model_information import model_information
from app_pages.predict_exam_scores import predict_exam_scores

app = MultiPage(app_name="Exam Score Analysis")

# Add app pages - these strings appear as the sidebar options
app.add_page("Project Summary", project_summary)
app.add_page("Project Hypotheses", project_hypotheses)
app.add_page("Distribution Analysis", distribution_analysis)
app.add_page("Data Analysis Primary", data_analysis_primary)
app.add_page("Data Analysis Secondary", data_analysis_secondary)
app.add_page("Hypothesis Validation", hypothesis_validation)
app.add_page("Model Information", model_information)
app.add_page("Predict Exam Scores", predict_exam_scores)

app.run()
