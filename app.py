from pandasai.llm.local_llm import LocalLLM ## Importing LocalLLM for local Meta Llama 3 model
import streamlit as st 
import pandas as pd # Pandas for data manipulation
from pandasai import SmartDataframe # SmartDataframe for interacting with data using LLM



# Function to chat with CSV data
def chat_with_csv(df,query):
     # Initialize LocalLLM with Meta Llama 3 model
    llm = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3")
    # Initialize SmartDataframe with DataFrame and LLM configuration
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    # Chat with the DataFrame using the provided query
    result = pandas_ai.chat(query)
    return result

# Set layout configuration for the Streamlit page
st.set_page_config(layout='wide')
# Set title for the Streamlit application
st.title("Chat CSV")

# Upload multiple CSV files
input_csvs = st.sidebar.file_uploader("Carregue seus arquivos CSV", type=['csv'], accept_multiple_files=True)

# Check if CSV files are uploaded
if input_csvs:
    # Select a CSV file from the uploaded files using a dropdown menu
    selected_file = st.selectbox("Selecione um arquivo CSV", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)

    #load and display the selected csv file 
    st.info("CSV enviado com sucesso")
    data = pd.read_csv(input_csvs[selected_index])
    st.dataframe(data.head(3),use_container_width=True)

    #Enter the query for analysis
    st.info("Bate-papo abaixo")
    input_text = st.text_area("Insira a consulta")

    #Perform analysis
    if input_text:
        if st.button("Conversar com csv"):
            st.info("Sua pergunta: "+ input_text)
            result = chat_with_csv(data,input_text)
            st.success(result)