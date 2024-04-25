import streamlit as st
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Análises",
    page_icon="📶",
    layout="wide"
)

st.markdown('# MODELAGEM DE PREVISÃO DE DEMANDA: ARIMA  📊')

col1, col2, col3 = st.columns([7, 10, 10]) 

with col1:
    st.header('DATAFRAME')
    df = pd.read_excel(r'C:\Caminhões\LIC_CAMIN_NAC_MES_JULHO_2023.xlsx', index_col=0, parse_dates=True)
    st.dataframe(df)
    st.markdown("""
        <style>
            .frame {
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
        </style>
        <div class="frame">
        """, unsafe_allow_html=True)

with col2:
    st.header('PREVISÃO DE VENDAS 36 MESES')
    previsao = pd.read_excel('previsao_arima_36 meses.xlsx')
    fig_previsao = px.line(previsao, x="Mês", y="Previsão", title='Previsão de Licenciamentos Caminhões (36 Meses)')
    fig_previsao.update_traces(line=dict(color='red', dash='dash'))
    fig_previsao.update_layout(
        xaxis_title='Meses',
        yaxis_title='Licenciamentos',
        title='Modelagem Arima: Previsão de Licenciamentos Caminhões (36 meses)',
        title_font=dict(family='Arial', size=18),
        width=650,  # Defina a largura da figura
        height=400  # Defina a altura da figura
    )
    st.plotly_chart(fig_previsao)
    st.markdown("""
        <style>
            .frame {
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
        </style>
        <div class="frame">
        """, unsafe_allow_html=True)

with col3:
    st.header('PREVISÃO DE VENDAS 36 MESES')
    previsao = pd.read_excel('previsao_arima_36 meses.xlsx')
    st.dataframe(previsao)
    st.markdown("""
        <style>
            .frame {
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
        </style>
        <div class="frame">
        """, unsafe_allow_html=True)


col1, col2, col3 = st.columns([7, 10, 10])

with col1:
    st.header('PREVISÃO vs REAL')
    data2 = pd.read_excel('LIC_CAMIN_NAC_MES_JULHO_2023_Erro_arima.xlsx')
    st.dataframe(data2)
    st.markdown("""
        <style>
            .frame {
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
        </style>
        <div class="frame">
        """, unsafe_allow_html=True)

with col2:
    st.header("PREVISÃO vs REAL")
    fig_licprev = px.line(data2, x='mês', y=['Licenciamentos', 'Previsão'], title='Modelagem Arima: Licenciamentos e Previsão para Caminhões',
              labels={'value': 'Licenciamentos', 'variable': 'Variáveis'},
              line_shape='linear', color_discrete_map={'Licenciamentos': 'blue', 'Previsão': 'red'})
    fig_licprev.update_layout(xaxis_title='Meses', title_font=dict(family='Arial', size=15), width=650, height=400)
    st.plotly_chart(fig_licprev)
    st.markdown("""
        <style>
            .frame {
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
        </style>
        <div class="frame">
        """, unsafe_allow_html=True)

with col3:    
    st.header("PREVISÃO DE VENDAS ANUAL")
    prev_ano = pd.read_excel('Licenciamentos_Real_ Previsão_2023_ 2024_ 2025).xlsx')
    fig_line = px.line(prev_ano, x='Ano', y='Licenciamentos')
    fig_line.update_traces(line=dict(color='red', width=2))
    fig_line.update_layout(
        title="Licenciamentos Over Years",
        xaxis_title="Year",
        yaxis_title="Licenciamentos",
        font=dict(family="Arial", size=16, color="darkblue"),  
        title_font=dict(family="Arial", size=24, color="black"),  
        paper_bgcolor="lightgray",  
        plot_bgcolor="white", 
        width=650, height=400, 
    )
    st.plotly_chart(fig_line)
    st.markdown("""
        <style>
            .frame {
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
        </style>
        <div class="frame">
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([10, 10, 10])

    with col1:
        st.metric(label='Previsão Licenciamentos 2024', value='108.254', delta='8.1 %')
        st.markdown("""
        <style>
            .frame {
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
        </style>
        <div class="frame">
        """, unsafe_allow_html=True)

    with col2:
        st.metric(label='Previsão Licenciamentos 2025', value='106.453', delta='-1.7%')
        st.markdown("""
        <style>
            .frame {
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
        </style>
        <div class="frame">
        """, unsafe_allow_html=True)

    with col3:            
        st.metric(label='Previsão Licenciamentos 2026', value= '103.309', delta='-2.9%')
        st.markdown("""
        <style>
            .frame {
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
        </style>
        <div class="frame">
        """, unsafe_allow_html=True)
        