import streamlit as st

def get_user_input():
  dizziness = st.number_input("Do your experience dizziness? Enter 1 for yes, 0 for no.")
  sickness = st.number_input("Do you feel sick? Enter 1 for yes, 0 for no.")
  sex = st.number_input("Are you a male or a female? Enter 1 for male, 2 for female.")
  age = st.number_input("How old are you? Enter 1 if you are 50 and under, 2 for over 50.")

  input_features = [[dizziness, sickness]] # put your features in here!
  return input_features

