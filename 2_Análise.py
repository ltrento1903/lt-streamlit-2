import streamlit as st
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Análises",
    page_icon="📶",
    layout="wide"
)

st.markdown('# ESTATÍSTICAS DA SÉRIE TEMPORAL 📶')

col1, col2, col3, col4 = st.columns([2, 3, 3, 3])

# Coluna 1
with col1:
    st.header('DATAFRAME')
    df = pd.read_excel(r'C:\Caminhões\LIC_CAMIN_NAC_MES_JULHO_2023.xlsx', index_col=0, parse_dates=True)
    st.write(df)
    # Adicionando moldura
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

# Coluna 2
with col2:
    st.header('DECOMPOSIÇÃO SAZONAL')    
        
    result = seasonal_decompose(df['lic_cam_nac'], model='additive')
    fig_seasonal = go.Figure()
    fig_seasonal.add_trace(go.Scatter(x=df.index, y=df['lic_cam_nac'], mode='lines', name='Original',  line=dict(color='#54F513')))
    fig_seasonal.add_trace(go.Scatter(x=df.index, y=result.trend, mode='lines', name='Trend', line=dict(color='#902324')))
    fig_seasonal.add_trace(go.Scatter(x=df.index, y=result.seasonal, mode='lines', name='Seasonal'))
    fig_seasonal.update_layout(title='Seasonal Decomposition',
                               xaxis_title='Date',
                               yaxis_title='Licenciamentos',
                               width=480,
                               height=400)
    st.plotly_chart(fig_seasonal)
    # Adicionando moldura
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

# Coluna 3
with col3:
    st.header('BOX PLOT')    
    fig_box = px.box(df, y="lic_cam_nac")
    fig_box.update_layout(
        title="Licenciamentos Box Plot",
        xaxis_title="Ano",
        yaxis_title="Licenciamentos",
        font=dict(family="Arial", size=16, color="darkblue"),  
        title_font=dict(family="Arial", size=24, color="black"),  
        paper_bgcolor="lightgray",  
        plot_bgcolor="white",  
        width=480,
        height=400)
    st.plotly_chart(fig_box)
    # Adicionando moldura
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

# Coluna 4
with col4:
    st.header('HISTOGRAMA')
    fig_hist = px.histogram(df, x="lic_cam_nac")

    fig_hist.update_traces(
        marker_color="purple",  
        opacity=0.7
    )
    fig_hist.update_layout(
        title="Licenciamentos Histograma",
        xaxis_title="Licenciamentos",
        yaxis_title="Count",
        font=dict(family="Arial", size=16, color="darkblue"),  
        title_font=dict(family="Arial", size=24, color="black"),  
        paper_bgcolor="lightgray", 
        plot_bgcolor="white",  
        width=480,
        height=400)
    st.plotly_chart(fig_hist)
    # Adicionando moldura
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

