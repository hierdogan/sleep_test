import streamlit as st
import pandas as pd
import pickle


st.set_page_config(
    initial_sidebar_state="expanded",
    page_title="Sleep Quality",
    page_icon="💤",
    layout="wide"
)


st.sidebar.title("Zzz Factor 😴")
st.sidebar.divider()
st.sidebar.write("This app is prepared for insomniacs 😵‍💫")
st.sidebar.divider()
app_mode = st.sidebar.selectbox('Select Page', ["Sleep Well?", "Diagnosis", "About Project", "Presentation", "Team"])
if app_mode == 'Sleep Well?':
    st.title("Sleep Well?")
    st.image('./real_vis/babysleep.png')
    #st.write('This app is prepared for insomniacs 😵‍💫')
    st.divider()
    st.subheader('This project was prepared as a final project for Miuul&VBO Data Scientist Bootcamp, DSB13 semester.')


############## PREDICTION PAGE ##############

# TODO add an explanation and specify feature range and explain

elif app_mode == "Diagnosis":
    # st.balloons()

    container = st.container()
    col1, col2 = container.columns([1, 1])

    with col1:
        def main():
            style = """<div style='background-color:blue; padding:12px'>
                    <h1 style='color:black'>Sleep Disorder Analysis</h1>
            </div>"""
            st.markdown(style, unsafe_allow_html=True)
            st.header('How to make it?')
            st.write('You can make an approximate price estimate by updating the values you see below in accordance with the \
                    features of the house you are looking for - at the specified intervals. \
                    This will enable customers to make informed decisions when buying or selling properties.')

            st.divider()
            left, right = st.columns((2, 2))
            BLOOD_PRESSURE_SYSTOLIC = left.number_input('Blood Pressure Systolic', step=5.00, format='%2f', value=120.00, min_value=80.00, max_value=160.00)
            BLOOD_PRESSURE_DIASTOLIC = right.number_input('Blood Pressure Diastolic)', step=5.00, format='%2f', value=80.00, min_value=40.00, max_value=120.00)
            BMI_CATEGORY_Overweight = left.checkbox('The BMI category of the person = Overweight', value=False)
            # BP_CAT_Evre_2_HT = right.checkbox('BP Stage 2 HT', value=False)
            AGE = left.number_input('Age', step=1.00, format='%2f', value=18.00, max_value=65.00)
            SLEEP_DURATION = right.number_input('The number of hours the person sleeps per day.', step=0.10, format='%2f', value=0.00, min_value=0.00, max_value=24.00)
            # OCCUPATION_Nurse = left.checkbox('Occupation == Nurse', value=False)
            # DAILY_STEPS = left.number_input('The number of steps the person takes per day', step=1.00, format='%2f', value=0.00, max_value=30000.00)
            # NEW_STRESS_AGE = right.number_input('age-stress', step=0.01, format='%2f', value=0.00, min_value=0.00, max_value=0.30)
            button = st.button('Predict')
            # if button is pressed
            if button:
                # make prediction
                result = predict(BLOOD_PRESSURE_SYSTOLIC, BLOOD_PRESSURE_DIASTOLIC,BMI_CATEGORY_Overweight, AGE, SLEEP_DURATION)
                st.success(f'result {result}')
                # if result == 0:
                #     st.success(f'You are healthy {result}')
                #     st.balloons()
                # elif result == 2:
                #     st.warning(f'Patient is probably has Insomnia {result}')
                # else:
                #     st.warning(f'Patient is probably has Sleep Apnea {result}')

           # BP_CAT_Evre_2_HT = left.number_input('BP Stage 2 HT', step=1.00, format='%2f', value=0.00, max_value=1.00)


        # load the train model
        # with open('./xgb_model.pkl', 'rb') as rf:
        model = pickle.load(open('/Users/ibrahim/PycharmProjects/dsb_13/rf57_model.pkl', 'rb'))


        def predict(BLOOD_PRESSURE_SYSTOLIC, BLOOD_PRESSURE_DIASTOLIC,BMI_CATEGORY_Overweight, AGE, SLEEP_DURATION):
            lists = [BLOOD_PRESSURE_SYSTOLIC, BLOOD_PRESSURE_DIASTOLIC,BMI_CATEGORY_Overweight, AGE, SLEEP_DURATION]
            df = pd.DataFrame(lists).transpose()
            #     # scaling the data
            #    scaler.transform(df)
            # making predictions using the train model
            prediction = model.predict(df)
            result = int(prediction)
            return result


        if __name__ == '__main__':
            main()

    # Görsel
    with col2:
        image = st.image('./real_vis/sleeping_at_office.jpg', caption="Let's Calculate")

############## ABOUT  PROJECT ##############
elif app_mode == 'About Project':
    container = st.container()
    ap_col1, ap_col2 = container.columns([1, 1])

    with ap_col1:
        st.image('./vis/about_pro_sleep.jpg', caption="")

    with ap_col2:
        df = pd.read_csv("./Sleep_health_and_lifestyle_dataset.csv")
        st.dataframe(df, height=600)  # Same as st.write(df)

    st.header('Dataset Overview')
    st.write('The Sleep Health and Lifestyle Dataset comprises 400 rows and 13 columns, covering a wide range of variables related to sleep and daily habits. \
    It includes details such as gender, age, occupation, sleep duration, quality of sleep, physical activity level, stress levels, BMI category, blood pressure, heart rate, daily steps, and the presence or absence of sleep disorders.')

    st.header('Key Features of the Dataset')
    st.write('Comprehensive Sleep Metrics: Explore sleep duration, quality, and factors influencing sleep patterns. \
             Lifestyle Factors: Analyze physical activity levels, stress levels, and BMI categories. \
             Cardiovascular Health: Examine blood pressure and heart rate measurements. \
             Sleep Disorder Analysis: Identify the occurrence of sleep disorders such as Insomnia and Sleep Apnea.')

    st.header('Dataset Columns')
    st.markdown(
    """
    - **Person ID:** An identifier for each individual.
    - **Gender:** The gender of the person (Male/Female).
    - **Age:** The age of the person in years.
    - **Occupation:** The occupation or profession of the person.
    - **Sleep Duration (hours):** The number of hours the person sleeps per day.
    - **Quality of Sleep (scale: 1-10):** A subjective rating of the quality of sleep, ranging from 1 to 10.
    - **Physical Activity Level (minutes/day):** The number of minutes the person engages in physical activity daily.
    - **Stress Level (scale: 1-10):** A subjective rating of the stress level experienced by the person, ranging from 1 to 10.
    - **BMI Category:** The BMI category of the person (e.g., Underweight, Normal, Overweight).
    - **Blood Pressure (systolic/diastolic):** The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.
    - **Heart Rate (bpm):** The resting heart rate of the person in beats per minute.
    - **Daily Steps:** The number of steps the person takes per day.
    - **Sleep Disorder:** The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).
    """)

    st.subheader('Details about Sleep Disorder Column')
    st.write('None: The individual does not exhibit any specific sleep disorder.\
    Insomnia: The individual experiences difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep. \
    Sleep Apnea: The individual suffers from pauses in breathing during sleep, resulting in disrupted sleep patterns and potential health risks.')


############## TEAM ##############

elif app_mode == 'Team':

    st.header("Educators 👨‍🔬")
    educators = {
        "Educator : Vahit Keskin": "https://www.linkedin.com/in/vahitkeskin",
        "Mentor Teacher : Yasemin Arslan": "https://www.linkedin.com/in/yaseminarslann"
    }

    for isim, profil_linki in educators.items():
        # LinkedIn linki içeren butonu oluşturma
        st.subheader(f" {isim} | [LinkedIn]({profil_linki})")

    st.header(" ")
    st.divider()

    st.header("Team Members 👩‍💻‍👨‍💻")
    # Ekip üyelerinin isimleri ve LinkedIn profillerinin linkleri
    ekip_uyeleri = {

        "Halil İbrahim Erdoğan": "https://www.linkedin.com/in/hierdogan",
        "Nimet Karagöz": "https://www.linkedin.com/in/nimet-karag%C3%B6z-34238390",
        "Birkan Çanakçıoğlu": "https://www.linkedin.com/in/birkancanakcioglu",
        "Elif Mavili": "https://www.linkedin.com/in/elifmavili"
    }

    for isim, profil_linki in ekip_uyeleri.items():
        # LinkedIn linki içeren butonu oluşturma
        st.subheader(f" {isim} | [LinkedIn]({profil_linki})")

#####################################
    st.header(" ")
    st.divider()
    st.header("Education Platform 🏫")
    company = {

        "Miuul": "https://miuul.com",
        "Veri Bilimi Okulu": "https://www.veribilimiokulu.com"
    }

    for isim, profil_linki in company.items():
        # LinkedIn linki içeren butonu oluşturma
        st.subheader(f" {isim} | [Web Site]({profil_linki})")
