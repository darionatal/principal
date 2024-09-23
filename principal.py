import streamlit as st

st.set_page_config(page_title='- Pagina de Dashboard -',layout='wide')

with st.container():
    st.subheader('Meu site de dashboard com streanlite')
    st.title('Dados lidos de arquivo CSV')
    st.write('Analise de dados de vendas')
    st.write('Aprendendo Python')