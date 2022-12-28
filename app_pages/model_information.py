import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_output_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def model_information():

    st.write("## Model Information")

    st.info(
        "On this page, I will present the information regarding the"
        " Machine Learning part of this project."
        f"\n"
        "As we have seen, the dataset contains 3 numerical variables."
        "These are a student's exam scores, and are also the target"
        " variables, which the local government wants to predict, so"
        " that they can identify student who are likely to underperform."
        f"\n"
        "In total, 3 Machine Learning models were trained."
        " On the next page, 3 Machine Learning pipelines containing"
        " those models will be presented for the user to access and"
        " make predictions."
        f"\n"
        " As will be discussed in greater detail below, I trained"
        " classification models that sort students into 2 classes -"
        " passing or failing. Passing students are those predicted to"
        " achieve scores approximately above the mean score, whereas"
        " failing students are those predicted to achieve scores"
        " approximately below the mean. The word approximately is used"
        " here because the breakpoints (the divisions between classes) are"
        " not exactly on the mean scores."
    )

    st.write("### Math Score Pipeline")

    st.info(
        "When I first began training a Machine Learning model for predicting"
        " a student's math score, I considered that since math_score is a"
        " continuous numerical variable, I would be best served by a"
        " regression model that attempts to exactly predict the value of"
        " math_score. This approach failed. My studies identified 2"
        " machine learning algorithms that performed the best - the"
        f" LinearRegressor and the RandomForestRegressor.\n"
        f"\n"
        "The LinearRegressor algorithm gave R2 scores of 0.261 and 0.122"
        " on the train and test sets respectively."
        " The RandomForestRegressor gave slightly better R2 scores of"
        " 0.298 and 0.19 on the train and test sets respectively."
        " I immediately"
        " identified these scores as very poor. I briefly considered"
        " conducting a Principal Component Analysis in hopes of"
        " improving performance. I discarded this idea as I considered"
        " that it would be unlikely to measurably improve performance"
        f" as the dataset only has 5 categorical variables.\n"
        f"\n"
        "I therefore converted to training a classification model."
        " With this type of model, the goal is to be able to"
        " sort students into a number of categories."
        " These categories represent discrete ranges of scores, meaning"
        f" that students are likely to score within that range.\n"
        f"\n"
        "I initially used 2 approaches, one using 3 classes and another"
        " using 4 classes. The 3-class approach proved superior, giving"
        " Recall scores of 0.62 and 0.63 on the lowest performing classes"
        f" of the train and test sets respectively.\n"
        f"\n"
        " At the time, I considered these recall scores to be *decent*, a"
        " shorthand for not great and not poor. In hopes of improving these"
        " scores, I examined the 2-class approach, where students are sorted"
        " into either **below average** or **better than average** classes."
        " The **better than average** class is"
        " predicted to score greater than 66.5, whereas the"
        " **below average** class"
        " is predicted to score less than 66.5. Given that the mean value of"
        " the math_score variable is 66.4, I considered this to be a"
        " good outcome, since the **below average** class is predicted to"
        " score below the mean value."
        f"\n"
    )

    math_score_pipeline = load_pkl_file(
        "outputs/ml_pipeline/predict_maths/v1/pipeline-clf-math.pkl")

    math_train_vars = pd.read_csv(
        "outputs/ml_pipeline/predict_maths/v1/math-train-vars.csv")

    math_train_score = pd.read_csv(
        "outputs/ml_pipeline/predict_maths/v1/math-train-score.csv")

    math_test_vars = pd.read_csv(
        "outputs/ml_pipeline/predict_maths/v1/math-test-vars.csv")

    math_test_score = pd.read_csv(
        "outputs/ml_pipeline/predict_maths/v1/math-test-score.csv")

    math_feature_importance = plt.imread(
        "outputs/ml_pipeline/predict_maths/v1/feature-importance-plot-maths.png")

    st.write("#### Pipeline")

    st.info(
        "Below is the code for the math_score pipeline using the 2-class"
        " approach."
    )

    st.write(math_score_pipeline)

    st.info(
        "Since the feature variables are all categorical, there is no need"
        " for a StandardScaler step. All we need is an"
        " OrdinalCategoricalEncoder step to encode the categorical variables."
        " The model step uses the DecisionTreeClassifier algorithm,"
        " and that algorithm's default hyperparameters."
    )

    st.write("#### Feature Importance Plot")

    st.info(
        "Below is the plot of the feature variables the math_score pipeline"
        " was trained on, and how important those feature variables are."
    )

    st.image(math_feature_importance)

    st.info(
        "As we can see, the math score model was trained on the"
        " lunch_program, ethnicity and parental_education variables."
        " The lunch_program variable is the most important variable,"
        " which tallies with our previous studies, which show the large"
        " influence lunch_program has on the math_score variable."
    )

    st.write("#### Classification Report and Confusion Matrix")

    st.info(
        "Below is the classification report and confusion matrix"
    )

    clf_performance(
        x_train=math_train_vars,
        y_train=math_train_score,
        x_test=math_test_vars,
        y_test=math_test_score,
        pipeline=math_score_pipeline,
        label_map=["below average", "better than average"])

    st.info(
        "As we can see, the train set has a good recall score of 0.68"
        " on the train set, and a recall score of 0.51 on the test set."
        " The difference in performance is to be expected, though it may"
        " indicate some level of underfitting."
    )

    st.write("### Reading Score Pipeline")

    st.info(
        "When training a model for predicting the reading_score variable,"
        " I initially considered using the same approach as with the"
        " math_score pipeline, starting with a regression task with the"
        f" backup of a classification task.\n"
        f"\n"
        "However, given the problems in training a regression model,"
        " I decided to begin with a classification task."
        " As with the math_score pipeline, I initially began with"
        " a 3-class and a 4-class approach. The 3-class approach proved"
        " superior, with recall scores of 0.67 and 0.68 on the lowest"
        " performing class for the train and test sets respectively."
        " I considered these recall scores to be *decent*, but not"
        " particularly good. I then explored the 2-class approach, which had"
        " far better performance, as we will see below."
    )

    reading_score_pipeline = load_pkl_file(
        "outputs/ml_pipeline/predict_reading/v1/pipeline-clf-reading.pkl")

    reading_train_vars = pd.read_csv(
        "outputs/ml_pipeline/predict_reading/v1/reading-train-vars.csv")

    reading_train_score = pd.read_csv(
        "outputs/ml_pipeline/predict_reading/v1/reading-train-score.csv")

    reading_test_vars = pd.read_csv(
        "outputs/ml_pipeline/predict_reading/v1/reading-test-vars.csv")

    reading_test_score = pd.read_csv(
        "outputs/ml_pipeline/predict_reading/v1/reading-test-score.csv")

    reading_feature_importance = plt.imread(
        "outputs/ml_pipeline/predict_reading/v1/feature-importance-plot-reading.png")

    st.write("#### Pipeline")

    st.info(
        "Below is the code for the reading_score pipeline using the"
        " 2-class approach."
    )

    st.write(reading_score_pipeline)

    st.info(
        "Since the feature variables are all categorical, there is no need"
        " for a StandardScaler step. All we need is an"
        " OrdinalCategoricalEncoder step to encode the categorical variables."
        " The model step uses the XGBClassifier algorithm"
    )

    st.write("#### Feature Importance Plot")

    st.info(
        "Below is the plot of the feature variables the reading_score"
        " pipeline was trained on, and how important"
        " those feature variables are."
    )

    st.image(reading_feature_importance)

    st.info(
        "As we can see, the reading_score model was trained on the"
        " lunch_program and test_preparation_course variables."
        " This tallies with our data analysis, which indicates that"
        " these variables have a considerable influence on reading_score."
    )

    st.write("#### Classification Report and Confusion Matrix")

    st.info(
        "Below is the classification report and confusion matrix"
    )

    clf_performance(
        x_train=reading_train_vars,
        y_train=reading_train_score,
        x_test=reading_test_vars,
        y_test=reading_test_score,
        pipeline=reading_score_pipeline,
        label_map=["average or below", "better than average"])

    st.info(
        "As we can see, the reading_score model has fantastic recall"
        " scores on the failing class of 0.88 and 0.85 for the train and test"
        " sets respectively. This is brilliant performance, indicative"
        " of excellent predictive power."
    )

    st.write("### Writing Score Pipeline")

    st.info(
        "When training a model for predicting the writing_score variable,"
        " I began with a classification model, as with the reading_score"
        " pipeline. I initially considered 3-class and 4-class"
        " approaches, and as above, the 3-class approach proved superior,"
        " with recall scores on the lowest performing class of 0.68 and 0.71"
        " for the train and test sets respectively. Again, I considered this"
        " to be *decent* performance. I then considered the 2-class approach,"
        " which proved to have far better performance, as we shall see below."
    )

    writing_score_pipeline = load_pkl_file(
        "outputs/ml_pipeline/predict_writing/v1/pipeline-clf-writing.pkl")

    writing_train_vars = pd.read_csv(
        "outputs/ml_pipeline/predict_writing/v1/writing-train-vars.csv")

    writing_train_score = pd.read_csv(
        "outputs/ml_pipeline/predict_writing/v1/writing-train-score.csv")

    writing_test_vars = pd.read_csv(
        "outputs/ml_pipeline/predict_writing/v1/writing-test-vars.csv")

    writing_test_score = pd.read_csv(
        "outputs/ml_pipeline/predict_writing/v1/writing-test-score.csv")

    writing_feature_importance = plt.imread(
        "outputs/ml_pipeline/predict_writing/v1/feature-importance-plot-writing.png")

    st.write("#### Pipeline")

    st.info(
        "Below is the code for the writing_score pipeline using the"
        " 2-class approach."
    )

    st.write(writing_score_pipeline)

    st.info(
        "Since the feature variables are all categorical, there is no need"
        " for a StandardScaler step. All we need is an"
        " OrdinalCategoricalEncoder step to encode the categorical variables."
        " The model step uses the GradientBoostingClassifier algorithm."
    )

    st.write("#### Feature Importance Plot")

    st.info(
        "Below is the plot of the feature variables the writing_score"
        " pipeline was trained on, and how important"
        " those feature variables are."
    )

    st.image(writing_feature_importance)

    st.info(
        "As we can see, the writing_score model was trained on the"
        " lunch_program, test_preparation_course and parental_education"
        " variables. This tallies with our data analysis, which indicates that"
        " these variables have a considerable influence on writing_score."
    )

    st.write("#### Classification Report and Confusion Matrix")

    st.info(
        "Below is the classification report and confusion matrix"
    )

    clf_performance(
        x_train=writing_train_vars,
        y_train=writing_train_score,
        x_test=writing_test_vars,
        y_test=writing_test_score,
        pipeline=writing_score_pipeline,
        label_map=["below average", "better than average"])

    st.info(
        "As we can see, the reading_score model has fantastic recall"
        " scores on the failing class of 0.98 and 0.96 for the train and test"
        " sets respectively. This is brilliant performance, indicative"
        " of almost-perfect predictive power."
    )
