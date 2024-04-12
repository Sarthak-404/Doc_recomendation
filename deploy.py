import streamlit as st
import pandas as pd 

# Load the Excel file
df = pd.read_excel('Cancer.xlsx')

# Function to recommend hospitals based on disease
def recommend(disease):
    fil = df[df['disease'] == disease]
    hospitals = fil[['name', 'hospital', 'rate','fees']]
    hospital_sorted = hospitals.sort_values(by='rate', ascending=False)
    return hospital_sorted

# Streamlit app
def main():
    st.title('Hospital Recommendation')

    # Initialize selected_hospital in session state if not already initialized
    if 'selected_hospital' not in st.session_state:
        st.session_state.selected_hospital = None

    # Search bar for disease input
    disease_input = st.selectbox('Select disease', df['disease'])

    if st.button('Recommend'):
        if disease_input:
            # Display recommended hospitals
            st.write('Recommended doctors:')
            recommended_hospitals = recommend(disease_input)
            for index, row in recommended_hospitals.iterrows():
                unique_key = f"{index}-{row['hospital']}"
                button_label = f"{row['name']} - {row['hospital']} (Rate: {row['rate']}) (Fees:-{row['fees']})"#fees
                if st.button(label=button_label, key=unique_key):
                    selected_hospital = f"You have selected {row['hospital']} for the disease {disease_input}. Rate: {row['rate']}"
                    st.session_state.selected_hospital = selected_hospital

            # Display selected hospital message
            if st.session_state.selected_hospital:
                st.write(st.session_state.selected_hospital)

if __name__ == '__main__':
    main()
