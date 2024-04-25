import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go

st.set_page_config(
    page_title="Medidas de Performance",
    page_icon="🔎",
    layout="wide"
)

st.markdown("# Medidas de Performance: ERROS, MAPE, MAE, BIAS E PROBABILIDADES 🔎")

col1, col2, col3, col4 = st.columns([10, 10, 10, 10])

with col1:
    st.header('ERRO PREVISÃO MARÇO/2024')
    st.markdown("""
A previsão do modelo Arima acertou em cheio ao estimar 9080 licenciamentos
                 para março, mas a realidade surpreendeu com 9.385 licenciamentos. 
                O modelo arrasou na precisão!                 
""")
    st.metric(label='ERRO PREVISÃO MARÇO/2024', value='-305', delta='3.3%', delta_color='off')
    st.markdown("""
        <style>
            .frame .content {
                height: 800px; /* Ajuste a altura conforme necessário */
            }
        </style>
        <div class="frame">        
    """, unsafe_allow_html=True)


with col2:
    st.header('MEAN ABSOLUTE PERCENTAGE ERROR (MAPE)')
    st.markdown("""
O MAPE (Mean Absolute Percentage Error, Erro Percentual Absoluto Médio) aparece
                 como um super-herói para avaliar a precisão dos modelos de
                 previsão, totalizando esses erros percentuais absolutos.                 
""")
    st.metric(label='MAPE', value='11.9%', delta='0.2%', delta_color='inverse')
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
    st.header('MEAN ABSOLUTE ERROR (MAE)')
    st.markdown("""
O MAE (Erro Absoluto Médio) é tipo o detetive das previsões na análise de 
                previsão. Ele calcula a média dos pitacos errados,
                 é descolado e não se abala com os desajustes. 
                Esse camarada mede a distância média entre as previsões e
                 a realidade, dando uma espiada no quão bom é o
                 palpite do modelo.
""")
    st.metric(label='MAE', value= '693 licenciamentos', delta='3', delta_color='inverse')
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

with col4:
    st.header('BIAS')
    st.markdown("""
O "viés da previsão"  ou "BIAS" refere-se ao erro sistemático na previsão de um modelo, ou seja, 
uma tendência consistente do modelo de prever valores que são sistematicamente diferentes dos valores reais.
Um valor positivo indica que as previsões são consistentemente mais altas do que os valores reais, 
enquanto um valor negativo indica que as previsões são consistentemente mais baixas do que os valores reais.
o viés é baixo -53.975288468412145 licenciamentos no periodo. Pense comigo...são 411 meses,
então...-53.975288468412145 x 411 meses = -22.184 licenciamentos que o realizado 2.791.860 licenciamentos, 
razão do viés 0,79% do total...exclente modelo...
""")
    st.metric(label='BIAS', value='-53 licenciamentos', delta='41', delta_color='inverse')
    st.metric(label='BIAS_RATIO', value='-0.79%', delta='0.61%', delta_color='inverse')
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


col1, col2, col3, col4 = st.columns([15, 15, 15, 15])

with col1:
    st.header('KPI MAPE')
    data2 = pd.read_excel('LIC_CAMIN_NAC_MES_JULHO_2023_Erro_arima.xlsx')
    data2['mês'] = pd.to_datetime(data2['mês'])
    ultimos_24_meses = data2[data2['mês'] >= data2['mês'].max() - pd.DateOffset(months=23)]
    ultimos_24_meses['Erro Absoluto'] = abs(ultimos_24_meses['Previsão'] - ultimos_24_meses['Licenciamentos'])
    ultimos_24_meses['Erro Percentual'] = (ultimos_24_meses['Erro Absoluto'] / ultimos_24_meses['Licenciamentos']) * 100
    meta_percentual = 12  
    ultimos_24_meses['KPI'] = ultimos_24_meses['Erro Percentual'].apply(lambda x: 'Dentro da Meta' if abs(x) <= meta_percentual else 'Fora da Meta')
    df_plot = ultimos_24_meses[['mês', 'Licenciamentos', 'Previsão', 'Erro Percentual', 'KPI']]
    fig_errokpi_p = px.bar(df_plot, x='mês', y='Erro Percentual', color='KPI',
                         title='Erro Percentual e KPI ao longo do tempo',
                         labels={'Erro Percentual': 'Erro Percentual (%)', 'mês': 'Mês'},
                         color_discrete_map={'Dentro da Meta': 'green', 'Fora da Meta': 'red'})
    fig_errokpi_p.add_annotation(xref='paper', yref='y',
                               x=1, y=meta_percentual,
                               text=f'Meta: {meta_percentual}%',
                               showarrow=False,
                               font=dict(color='black', size=20),
                               align='center', ax=0, ay=-40,
                               width=100, height=100,)
    fig_errokpi_p.update_layout(
        width=450,  # Defina a largura da figura
        height=322 # Defina a altura da figura
    )
    st.plotly_chart(fig_errokpi_p)
    st.metric(label='ERRO MARÇO/2024', value='3.3%', delta='-8 pontos')
    st.markdown("""
            <style>
                .grafico-frame {
                    padding: 10px;
                    border: 2px solid black;
                    border-radius: 5px;
                    }
            </style>
            <div class="grafico-frame">
            """, unsafe_allow_html=True)



with col2:
    st.header('PROBABILIDADE 2024 >= 108.254 LICENCIAMENTOS')
    prev_ano = pd.read_excel('Licenciamentos_Real_ Previsão_2023_ 2024_ 2025).xlsx')
    media_licenciamentos = prev_ano['Licenciamentos'].mean()
    desviopadrão_licenciamentos = prev_ano['Licenciamentos'].std()
    valor_especifico = 108254
    x = np.linspace(media_licenciamentos - 3 * desviopadrão_licenciamentos, media_licenciamentos + 3 * desviopadrão_licenciamentos, 1000)
    y = norm.cdf(x, media_licenciamentos, desviopadrão_licenciamentos)
    probabilidade = norm.cdf(valor_especifico, media_licenciamentos, desviopadrão_licenciamentos)
    fig_prob2024 = go.Figure()
    fig_prob2024.add_trace(go.Scatter(x=x, y=y, mode='lines', name='CDF'))
    fig_prob2024.add_trace(go.Scatter(x=[valor_especifico, valor_especifico], y=[0, probabilidade],
                             mode='lines', name=f'Probabilidade: {probabilidade:.4f}',
                             line=dict(color='red', dash='dash')))
    fig_prob2024.update_layout(title=f'Probabilidade Cumulativa (CDF) - Valor Específico: {valor_especifico}',
                      xaxis_title='Licenciamentos',
                      yaxis_title='Probabilidade Cumulativa',
                      font=dict(family="Arial", size=12, color="darkblue"),  
                      title_font=dict(family="Arial", size=12, color="black"),  
                      paper_bgcolor="lightgray",  
                      plot_bgcolor="white",
                      width=400, height=300,  
                      showlegend=True)
    st.plotly_chart(fig_prob2024)
    st.metric(label='PROBABILIDADE', value='25.0%')
    st.markdown("""
            <style>
                .grafico-frame {
                    padding: 10px;
                    border: 2px solid black;
                    border-radius: 5px;
                    }
            </style>
            <div class="grafico-frame">
            """, unsafe_allow_html=True)

with col3:
    st.header('PROBABILIDADE 2025 >= 106453 LICENCIAMENTOS')
    prev_ano = pd.read_excel('Licenciamentos_Real_ Previsão_2023_ 2024_ 2025).xlsx')
    media_licenciamentos = prev_ano['Licenciamentos'].mean()
    desviopadrão_licenciamentos = prev_ano['Licenciamentos'].std()
    valor_especifico = 106453
    x = np.linspace(media_licenciamentos - 3 * desviopadrão_licenciamentos, media_licenciamentos + 3 * desviopadrão_licenciamentos, 1000)
    y = norm.cdf(x, media_licenciamentos, desviopadrão_licenciamentos)
    probabilidade = norm.cdf(valor_especifico, media_licenciamentos, desviopadrão_licenciamentos)
    fig_prob2025 = go.Figure()
    fig_prob2025.add_trace(go.Scatter(x=x, y=y, mode='lines', name='CDF'))
    fig_prob2025.add_trace(go.Scatter(x=[valor_especifico, valor_especifico], y=[0, probabilidade],
                             mode='lines', name=f'Probabilidade: {probabilidade:.4f}',
                             line=dict(color='red', dash='dash')))
    fig_prob2025.update_layout(title=f'Probabilidade Cumulativa (CDF) - Valor Específico: {valor_especifico}',
                      xaxis_title='Licenciamentos',
                      yaxis_title='Probabilidade Cumulativa',
                      font=dict(family="Arial", size=12, color="darkblue"),  
                      title_font=dict(family="Arial", size=12, color="black"),  
                      paper_bgcolor="lightgray",  
                      plot_bgcolor="white",  
                      width=400, height=300,
                      showlegend=True)
    st.plotly_chart(fig_prob2025)
    st.metric(label='PROBABILIDADE', value='26.6%')
    st.markdown("""
            <style>
                .grafico-frame {
                    padding: 10px;
                    border: 2px solid black;
                    border-radius: 5px;
                    }
            </style>
            <div class="grafico-frame">
            """, unsafe_allow_html=True)

with col4:
    st.header('PROBABILIDADE 2026 >= 103309 LICENCIAMENTOS')
    prev_ano = pd.read_excel('Licenciamentos_Real_ Previsão_2023_ 2024_ 2025).xlsx')
    media_licenciamentos = prev_ano['Licenciamentos'].mean()
    desviopadrão_licenciamentos = prev_ano['Licenciamentos'].std()
    valor_especifico = 103309
    x = np.linspace(media_licenciamentos - 3 * desviopadrão_licenciamentos, media_licenciamentos + 3 * desviopadrão_licenciamentos, 1000)
    y = norm.cdf(x, media_licenciamentos, desviopadrão_licenciamentos)
    probabilidade = norm.cdf(valor_especifico, media_licenciamentos, desviopadrão_licenciamentos)
    fig_prob2026 = go.Figure()
    fig_prob2026.add_trace(go.Scatter(x=x, y=y, mode='lines', name='CDF'))
    fig_prob2026.add_trace(go.Scatter(x=[valor_especifico, valor_especifico], y=[0, probabilidade],
                             mode='lines', name=f'Probabilidade: {probabilidade:.4f}',
                             line=dict(color='red', dash='dash')))
    fig_prob2026.update_layout(title=f'Probabilidade Cumulativa (CDF) - Valor Específico: {valor_especifico}',
                      xaxis_title='Licenciamentos',
                      yaxis_title='Probabilidade Cumulativa',
                      font=dict(family="Arial", size=12, color="darkblue"),  
                      title_font=dict(family="Arial", size=12, color="black"),  
                      paper_bgcolor="lightgray",  
                      plot_bgcolor="white", 
                      width=400, height=300, 
                      showlegend=True)
    st.plotly_chart(fig_prob2026)
    st.metric(label='PROBABILIDADE', value='29.5%')
    st.markdown("""
            <style>
                .grafico-frame {
                    padding: 10px;
                    border: 2px solid black;
                    border-radius: 5px;
                    }
            </style>
            <div class="grafico-frame">
            """, unsafe_allow_html=True)
