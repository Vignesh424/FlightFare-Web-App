import streamlit as st
import pickle

model = pickle.load(open('flight.pkl', 'rb'), encoding='latin1')

def run():
    st.title("Flight Fare Predictions using Machine Learning")
    
    ## Airlines
    airline_display = ('SpiceJet','AirAsia', 'Vistara', 'GO_FIRST','Indigo','Air_India')
    airline_options = list(range(len(airline_display)))
    air_models = st.selectbox("Airlines",airline_options, format_func=lambda x: airline_display[x])

  ## Source City
    source_display = ('Delhi','Mumbai','Bangalore', 'Kolkata','Hyderabad','Chennai')
    source_options = list(range(len(source_display)))
    source_models = st.selectbox("Enter Source City ",source_options, format_func=lambda x: source_display[x])

    ## Departure
    departure_display = ('Evening', 'Early_Morning', 'Morning','Afternoon', 'Night','Late_Night')
    departure_options = list(range(len(departure_display)))
    departure_models= st.selectbox("Enter Departure Time",departure_options, format_func=lambda x: departure_display[x])

    ## Stops
    stops_display = ('zero','one','two_or_more')
    stops_options = list(range(len(stops_display)))
    stops_models = st.selectbox("Enter Stops", stops_options, format_func=lambda x: stops_display[x])

    ## Arrival
    arrival_display = ('Evening', 'Early_Morning', 'Morning','Afternoon', 'Night','Late_Night')
    arrival_options = list(range(len(arrival_display)))
    arrival_models= st.selectbox("Enter Arrival Time",arrival_options, format_func=lambda x: arrival_display[x])

    ## Destination City
    destination_display = ('Delhi','Mumbai','Bangalore', 'Kolkata','Hyderabad','Chennai')
    destination_options = list(range(len(destination_display)))
    destination_models = st.selectbox("Enter Destination City ",destination_options, format_func=lambda x: destination_display[x])

    ## Business Class
    class_display = ('Business', 'Economy')
    class_options = list(range(len(class_display)))
    class_models = st.selectbox("Enter Business Class",class_options, format_func=lambda x: class_display[x])

     ## Enter Duration
    duration= st.number_input('Enter Duration (Hours.Minutes)')

    ## Days Left
    days_left= st.slider('Enter Days Left')



    if st.button("Submit"):
        features = [[air_models,source_models,departure_models,stops_models, arrival_models,destination_models,class_models,duration,days_left]]
        print(features)
        prediction = model.predict(features)
        weight = [str(i) for i in prediction]
        ans = ', '.join(weight)
        if ans==0:
            st.error("Error in the Inputs: Please Try Again")

        else:
            st.success("The Predicted Price is:"+" "+ans)


            

run()