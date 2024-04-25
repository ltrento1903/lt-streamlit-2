import streamlit as st
import pandas as pd
import webbrowser


st.set_page_config(
    page_title="Caminhões",
    page_icon="🚘",
    layout="wide"  
)

st.markdown('# PREVISÃO DE DEMANDA PARA O MERCADO DE CAMINHÕES POR MEIO DA LINGUAGEM PROGRAMAÇÃO PYTHON 📈')
st.subheader('Atualização: Março/2024')

btn=st.button('Acesse os dados no site da Anfavea')
if btn:
    webbrowser.open_new_tab('https://anfavea.com.br/site/edicoes-em-excel/')

st.markdown("""
<span style="font-size: 30px">
Adivinhar o futuro das vendas é como prever se vai chover no 
fim de semana - uma arte maluca, mas necessária para
os negócios brilharem. Usando a mágica da programação
em Python, ferramenta como ***ARIMA*** entra em cena para decifrar os dados e jogar luz nas tendências
futuras. ***Arima*** com seus superpoderes estatísticos, se unem
             ao Python por meio do Statsmodels para previsões certeiras e
             análises minuciosas. Que a dança dos números comece!

""", unsafe_allow_html=True)

st.sidebar.markdown('Desenvolvido por [UP_SALES PLANNING]("https://www.youtube.com/channel/UCx2HD4jzDqjCZL79sKI6Qkw")')

