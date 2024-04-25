import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='LINHA DE PRODUTOS: SEMIPESADOS',
                   page_icon='📶',
                   layout='wide')

st.markdown('# LINHA DE PRODUTOS: SEMIPESADOS 📶')
st.subheader('ANÁLISES E PREVISÕES')

col1, col2, col3 = st.columns([1, 1, 1])


with col1:
    st.header('PARTICIPAÇÃO LINHA SEMIPESADOS 📶')
    participação = {
        'Ano': [2019, 2020, 2021, 2022, 2023],
        'Percentual': [22.9, 25.8, 25.0, 25.9, 26.6]
    }
    semipesados = pd.DataFrame(participação)
    semipesados['Ano'] = pd.to_datetime(semipesados['Ano'], format='%Y')    
    

    import plotly.graph_objects as go

    fig_part = go.Figure()
    fig_part.add_trace(go.Box(y=semipesados['Percentual'], name="Média & Desvio Padrão", marker_color='#EA3F41', boxmean='sd'))
    fig_part.update_layout(title='2019 à 2023')
    fig_part.update_layout(height=400, width=500)
    st.plotly_chart(fig_part)
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
    st.header('PREVISÃO DE DEMANDA LINHA SEMIPESADOS ⛟')        
    previsao_semipesados = pd.read_excel('previsao_arima_36 meses.xlsx')
    percentual_medio = pd.Series({'Semipesados': 25.2})    
    
    for produto, percentual in percentual_medio.items():
        previsao_semipesados[produto] = percentual * previsao_semipesados['Previsão'] / 100      
        
    
    fig_prev = px.line(previsao_semipesados, x='Mês', y='Semipesados', color_discrete_sequence=['#B62686'])
    fig_prev.update_layout(title='PREVISÃO DE DEMANDA PARA LINHA SEMIPESADOS')
    fig_prev.update_layout(height=400, width=500)
    st.plotly_chart(fig_prev)
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
    st.header('PREVISÃO DE DEMANDA LINHA SEMIPESADOS ⛟')    
    st.dataframe(previsao_semipesados)
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
    
col1, col2, col3, col4 = st.columns([1,1,1,0.3])

with col1:   
    st.header('MAN')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Semipesados'")      

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    man = df_resultado.query("Fabricante == 'MAN'")  
 
    
    st.dataframe(man, height=365, width=500)
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
    st.header('REGRESSÃO MAN')   
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm
    X_m = sm.add_constant(man['Ano'])
    modelo = sm.OLS(man['% Participação'], X_m)
    resultado = modelo.fit()
    fig_man = px.scatter(man, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='blue')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_man.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_man.update_layout(height=400, width=535)
    st.plotly_chart(fig_man)
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
    st.header('MERCEDES-BENZ')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Semipesados'")          

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    mb = df_resultado.query("Fabricante == 'Mercedes-Benz'")   
    
    st.dataframe(mb, height=365, width=500)
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
    st.header('REGRESSÃO MERCEDES-BENZ')   
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm    
    X_mb = sm.add_constant(mb['Ano'])
    modelo = sm.OLS(mb['% Participação'], X_mb)
    resultado = modelo.fit()
    fig_mb = px.scatter(mb, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='#FF00FF')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_mb.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_mb.update_layout(height=400, width=535)
    st.plotly_chart(fig_mb)
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
    st.header('IVECO')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Semipesados'")          

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    iveco = df_resultado.query("Fabricante == 'Iveco'")      
    
    st.dataframe(iveco, height=365, width=500)
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
    st.header('REGRESSÃO IVECO')   
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm    
    X_iv = sm.add_constant(iveco['Ano'])
    modelo = sm.OLS(iveco['% Participação'], X_iv)
    resultado = modelo.fit()
    fig_iveco = px.scatter(iveco, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='cyan')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_iveco.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_iveco.update_layout(height=400, width=535)
    st.plotly_chart(fig_iveco)
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
    st.header('HIGHLIGHTS')
    st.subheader('2012 à 2023')
    st.metric(label='MAN', value='43.3%', delta='7.9 pt')
    st.metric(label='MERCEDES-BENZ', value='22.4%',delta='-2.1pt')
    st.metric(label='IVECO', value='14.5%', delta='8.0 pt')
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

col1, col2, col3, col4 = st.columns([1,1,1,0.3])

with col1:   
    st.header('VOLVO')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')        
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Semipesados'")      

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano')) 
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    volvo = df_resultado.query("Fabricante == 'VOLVO'")     
 
    
    st.dataframe(volvo, height=365, width=500)
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
    st.header('REGRESSÃO VOLVO')   
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm
    X_v = sm.add_constant(volvo['Ano'])
    modelo = sm.OLS(volvo['% Participação'], X_v)
    resultado = modelo.fit()
    fig_volvo = px.scatter(volvo, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='blue')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_volvo.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_volvo.update_layout(height=400, width=535)
    st.plotly_chart(fig_volvo)
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
    st.header('DAF')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Semipesados'")          

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    daf = df_resultado.query("Fabricante == 'DAF'")   
    
    st.dataframe(daf, height=365, width=500)    
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
    st.header('REGRESSÃO DAF')       
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm    
    X_d = sm.add_constant(daf['Ano'])
    modelo = sm.OLS(daf['% Participação'], X_d)
    resultado = modelo.fit()
    fig_daf = px.scatter(daf, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='orange')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_daf.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_daf.update_layout(height=400, width=535)
    st.plotly_chart(fig_daf)
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
    st.header('SCANIA')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Semipesados'")          

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    scania = df_resultado.query("Fabricante == 'SCANIA'")          
    
    st.dataframe(scania, height=365, width=500)
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
    st.header('REGRESSÃO SCANIA')   
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm    
    X_s = sm.add_constant(scania['Ano'])
    modelo = sm.OLS(scania['% Participação'], X_s)
    resultado = modelo.fit()
    fig_scania = px.scatter(scania, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='green')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_scania.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_scania.update_layout(height=400, width=535)
    st.plotly_chart(fig_scania)
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
    st.header('HIGHLIGHTS')
    st.subheader('2012 à 2023')
    st.metric(label='VOLVO', value='13.7%', delta='3.6 pt')
    st.metric(label='DAF', value='2.9%',delta='2.9 pt')
    st.metric(label='SCANIA', value='2.9%', delta='0.5 pt')
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

col1, col2, col3 =st.columns([1,1,1])

with col1:
    st.header('PREVISÃO SEMIPESADOS 2024')
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'MAN': 45.0,
        'Mercedes-Benz': 22,
        'IVECO': 14,
        'VOLVO': 13,
        'DAF': 3,
        'SCANIA': 3,    
    })

    df = pd.Series({
        'Abr/24': 2111,
        'Maio/24': 2294,
        'Jun/24': 2254,
        'Jul/24': 2359,
        'Ago/24': 2456,
        'Set/24': 2340,
        'Out/24': 2375,
        'Nov/24': 2303,
        'Dez/24': 2068,
    })

    previsão_2024 = pd.DataFrame(index=df.index)

    for produto, percentual in percentuais_medios.items():
        previsão_2024[produto] = round((percentual * df / 100), 0)
    previsão_2024.insert(0, "Mês", previsão_2024.index)    

    # Lista de cores para as linhas
    cores = ['blue', '#FF00FF', 'green', 'orange', 'purple', 'cyan']

    fig_2024 = go.Figure()

    # Adicionando uma linha para cada fabricante com uma cor diferente
    for i, fabricante in enumerate(previsão_2024.columns[1:]):
        fig_2024.add_trace(go.Scatter(x=previsão_2024['Mês'], y=previsão_2024[fabricante], mode='lines', name=fabricante, line=dict(color=cores[i])))

    # Criando os botões para cada fabricante
    buttons = [
        dict(label="Todos",
             method="update",
             args=[{"visible": [True] * len(previsão_2024.columns[1:])},
                   {"title": "Previsão de vendas de veículos por fabricante em 2024"}])
    ]

    for i, fabricante in enumerate(previsão_2024.columns[1:]):
        visible = [False] * len(previsão_2024.columns[1:])
        visible[i] = True
        buttons.append(
            dict(label=fabricante,
                 method="update",
                 args=[{"visible": visible},
                       {"title": f"Previsão de vendas de {fabricante} em 2024"}])
        )

    fig_2024.update_layout(
        title="Previsão de vendas de por fabricante em 2024",
        xaxis_title="Mês",
        yaxis_title="Quantidade",
        xaxis=dict(type='category'),
        updatemenus=[
            dict(
                buttons=buttons,
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.1,
                yanchor="top"
            ),
        ]
    )
    fig_2024.update_layout(height=445, width=600)
    st.plotly_chart(fig_2024)
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
    st.header('PREVISÃO SEMIPESADOS 2025')
    # Aqui vai o código para a previsão de 2025...
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'MAN': 43.7,
        'Mercedes-Benz': 22,
        'IVECO': 14.5,
        'VOLVO': 13.5,
        'DAF': 3.3,
        'SCANIA': 3,    
    })

    df = pd.Series({
        'Jan/25': 2068,
        'Fev/25': 1972,
        'Mar/25': 2243,
        'Abr/25': 2054,
        'Maio/25': 2168,
        'Jun/25': 2258,
        'Jul/25': 2361,
        'Ago/25': 2396,
        'Set/25': 2261,
        'Out/25': 2307,
        'Nov/25': 2283,
        'Dez/25': 2452,
    })

    previsão_2025 = pd.DataFrame(index=df.index)

    for produto, percentual in percentuais_medios.items():
        previsão_2025[produto] = round((percentual * df / 100), 0)
    previsão_2025.insert(0, "Mês", previsão_2025.index)

    # Lista de cores para as linhas
    cores = ['blue', '#FF00FF', 'green', 'orange', 'purple', 'cyan']

    fig_2025 = go.Figure()

    # Adicionando uma linha para cada fabricante com uma cor diferente
    for i, fabricante in enumerate(previsão_2025.columns[1:]):
        fig_2025.add_trace(go.Scatter(x=previsão_2025['Mês'], y=previsão_2025[fabricante], mode='lines', name=fabricante, line=dict(color=cores[i])))

    # Criando os botões para cada fabricante
    buttons = [
        dict(label="Todos",
             method="update",
             args=[{"visible": [True] * len(previsão_2025.columns[1:])},
                   {"title": "Previsão de vendas por fabricante em 2025"}])
    ]

    for i, fabricante in enumerate(previsão_2025.columns[1:]):
        visible = [False] * len(previsão_2025.columns[1:])
        visible[i] = True
        buttons.append(
            dict(label=fabricante,
                 method="update",
                 args=[{"visible": visible},
                       {"title": f"Previsão de vendas de {fabricante} em 2025"}])
        )

    fig_2025.update_layout(
        title="Previsão de vendas de veículos por fabricante em 2025",
        xaxis_title="Mês",
        yaxis_title="Quantidade",
        xaxis=dict(type='category'),
        updatemenus=[
            dict(
                buttons=buttons,
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.1,
                yanchor="top"
            ),
        ]
    )
    fig_2025.update_layout(height=445, width=600)
    st.plotly_chart(fig_2025)
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
    st.header('PREVISÃO SEMIPESADOS 2026')
    
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'MAN': 42.5,
        'Mercedes-Benz': 22,
        'IVECO': 15,
        'VOLVO': 14,
        'DAF': 3.5,
        'SCANIA': 3,    
    })

    df = pd.Series({
        'Jan/26': 2078,
        'Fev/26': 1930,
        'Mar/26': 2217,
        'Abr/26': 2048,
        'Maio/26': 2164,
        'Jun/26': 2162,
        'Jul/26': 2256,
        'Ago/26': 2325,
        'Set/26': 2218,
        'Out/26': 2248,
        'Nov/26': 2189,
        'Dez/26': 2344,
    })

    previsão_2026 = pd.DataFrame(index=df.index)

    for produto, percentual in percentuais_medios.items():
        previsão_2026[produto] = round((percentual * df / 100), 0)
    previsão_2026.insert(0, "Mês", previsão_2026.index)

    # Lista de cores para as linhas
    cores = ['blue', '#FF00FF', 'green', 'orange', 'purple', 'cyan']

    fig_2026 = go.Figure()

    # Adicionando uma linha para cada fabricante com uma cor diferente
    for i, fabricante in enumerate(previsão_2026.columns[1:]):
        fig_2026.add_trace(go.Scatter(x=previsão_2026['Mês'], y=previsão_2026[fabricante], mode='lines', name=fabricante, line=dict(color=cores[i])))

    # Criando os botões para cada fabricante
    buttons = [
        dict(label="Todos",
             method="update",
             args=[{"visible": [True] * len(previsão_2026.columns[1:])},
                   {"title": "Previsão de vendas por fabricante em 2026"}])
    ]

    for i, fabricante in enumerate(previsão_2026.columns[1:]):
        visible = [False] * len(previsão_2026.columns[1:])
        visible[i] = True
        buttons.append(
            dict(label=fabricante,
                 method="update",
                 args=[{"visible": visible},
                       {"title": f"Previsão de vendas de {fabricante} em 2026"}])
        )

    fig_2026.update_layout(
        title="Previsão de vendas de veículos por fabricante em 2026",
        xaxis_title="Mês",
        yaxis_title="Quantidade",
        xaxis=dict(type='category'),
        updatemenus=[
            dict(
                buttons=buttons,
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.1,
                yanchor="top"
            ),
        ]
    )
    fig_2026.update_layout(height=445, width=600)
    st.plotly_chart(fig_2026)
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