import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='- Pagina de Dashboard -',layout='wide')

with st.container():
    st.subheader('Meu site de dashboard com streanlite')
    st.title('Dados lidos de arquivo CSV')
    st.write('Analise de dados de vendas')
    st.write('Aprendendo Python')

@st.cache_data
def Carregar_dados():
    tabela =  pd.read_csv('supermarket_sales.csv',sep=";", decimal=",")
    return tabela

with st.container():
    df = Carregar_dados()

    df['Date']=pd.to_datetime(df['Date'])
    df=df.sort_values(['Date'])

    df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))
    month = st.sidebar.selectbox('Mês', df['Month'].unique())

    df_filtrado = df[df['Month'] == month]

    col1,col2=st.columns(2)
    col3,col4=st.columns(2)

    fig_1 = px.bar(df_filtrado,x='Date', y = 'Total',color='City', title='Venda por dia')
    col1.plotly_chart(fig_1, use_container_width=True)

    fig_2 = px.bar(df_filtrado,x='Date', y = 'Product line',color='City', title='Venda por Produto',orientation='h')
    col2.plotly_chart(fig_2, use_container_width=True)

    city_total = df_filtrado.groupby("City")[("Total")].sum().reset_index()
    fig_3 = px.bar(city_total,x='City', y = 'Total', title='por Filial')
    col3.plotly_chart(fig_3, use_container_width=True)

    fig_4 = px.pie(df_filtrado,values='Total', names= 'Payment', title='por Tipo Pgto')
    col4.plotly_chart(fig_4, use_container_width=True)




