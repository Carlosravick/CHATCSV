from pandasai.llm.local_llm import LocalLLM 
import streamlit as st 
import pandas as pd 
from pandasai import SmartDataframe 




def chat_with_csv(df,query):
    
    llm = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3")
    
    pandas_ai = SmartDataframe(df, config={"llm": llm})
   
    result = pandas_ai.chat(query)
    return result


st.set_page_config(layout='wide')

st.title("Chat CSV")

input_csvs = st.sidebar.file_uploader("Carregue seus arquivos CSV", type=['csv'], accept_multiple_files=True)


if input_csvs:
  
    selected_file = st.selectbox("Selecione um arquivo CSV", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)

    st.info("CSV enviado com sucesso")
    data = pd.read_csv(input_csvs[selected_index])
    st.dataframe(data.head(3),use_container_width=True)

    
    st.info("Bate-papo abaixo")
    input_text = st.text_area("Insira a consulta")

    
    if input_text:
        if st.button("Conversar com csv"):
            st.info("Sua pergunta: "+ input_text)
            result = chat_with_csv(data,input_text)
            st.success(result)