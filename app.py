# Import necessary libraries
import pickle
import streamlit as st

# Load the trained model
pickle_in = open('Telco churn_XGB.pkl', 'rb')
classifier = pickle.load(pickle_in)

# Define the prediction function
def prediction(region,tenure,age,marital,address,income,ed,
       employ,retire,gender,reside,tollfree,voice,internet,
       ebill,custcat):
   
    # Making prediction
    prediction = classifier.predict([[region,tenure,age,marital,address,income,ed,employ,retire,gender,reside,tollfree,voice,internet,
       ebill,custcat]])

    if prediction == 0:
        pred = 'will not churn'
    else:
        pred = 'is likely to churn'
    return pred

# Main function for the Streamlit app
def main():
    # Front-end elements of the web page
    st.title("Churn Prediction of customers")

    # User input fields
    region = st.number_input('region')
    tenure = st.number_input('tenure')
    age = st.number_input('age')
    marital = st.number_input('marital')
    address = st.number_input('address')
    income = st.number_input('income')
    ed = st.number_input('Education')
    employ = st.number_input('employ')
    retire = st.number_input('retire')
    gender = st.number_input('Gender')
    reside = st.number_input('reside')
    tollfree = st.number_input('Toll free')
    voice = st.number_input('voice calls')
    internet = st.number_input('internet')
    ebill = st.number_input('ebill')
    custcat = st.number_input('custcat')
    result = ""

    # When predict button is clicked
    if st.button('Predict'):
        result = prediction(region,tenure,age,marital,address,income,ed,
       employ,retire,gender,reside,tollfree,voice,internet,
       ebill,custcat)
        st.success('Customer {}'.format(result))

if __name__ == '__main__':
    main()
