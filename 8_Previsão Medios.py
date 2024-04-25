import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='LINHA DE PRODUTOS: MÉDIOS',
                   page_icon='🚚',
                   layout='wide')

st.markdown('# LINHA DE PRODUTOS: MÉDIOS 🚚')
st.subheader('ANÁLISES E PREVISÕES')

col1, col2, col3 = st.columns([1, 1, 1])


with col1:
    st.header('PARTICIPAÇÃO LINHA MÉDIOS 🚚')
    participação = {
        'Ano': [2019, 2020, 2021, 2022, 2023],
        'Percentual': [9.9, 9.3, 8.7, 8.2, 7.7]
    }
    medios = pd.DataFrame(participação)
    medios['Ano'] = pd.to_datetime(medios['Ano'], format='%Y')    
    

    import plotly.graph_objects as go

    fig_part = go.Figure()
    fig_part.add_trace(go.Box(y=medios['Percentual'], name="Média & Desvio Padrão", marker_color='#E0F56D', boxmean='sd'))
    fig_part.update_layout(title='2019 à 2023')
    fig_part.update_layout(height=440, width=500)
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
    st.header('PREVISÃO DE DEMANDA LINHA MÉDIOS ⛟')        
    previsao_medios = pd.read_excel('previsao_arima_36 meses.xlsx')
    percentual_medio = pd.Series({'Medios': 8.0})    
    
    for produto, percentual in percentual_medio.items():
        previsao_medios[produto] = percentual * previsao_medios['Previsão'] / 100           
        
    
    fig_prev = px.line(previsao_medios, x='Mês', y='Medios', color_discrete_sequence=['#52B727'])
    fig_prev.update_layout(title='PREVISÃO DE DEMANDA PARA LINHA MÉDIOS')
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
    st.header('PREVISÃO DE DEMANDA LINHA MÉDIOS ⛟')    
    st.dataframe(previsao_medios)
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
    
    linha = df_ano.query("Linha == 'Médios'")          

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
    
    linha = df_ano.query("Linha == 'Médios'")          

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
    
    linha = df_ano.query("Linha == 'Médios'")          

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
    st.metric(label='MAN', value='69.3%', delta='15.7 pt')
    st.metric(label='MERCEDES-BENZ', value='14.1%',delta='-6.3pt')
    st.metric(label='IVECO', value='13.9%', delta='11.7 pt')
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

col1, col2, col3 = st.columns([1,1,0.3])

with col1:   
    st.header('FORD')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')        
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Médios'")      

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano')) 
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    ford = df_resultado.query("Fabricante == 'Ford'")     
 
    
    st.dataframe(ford, height=255, width=500)
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
    st.header('REGRESSÃO FORD')   
    from sklearn.linear_model import LinearRegression    
    import statsmodels.api as sm
    X_f= sm.add_constant(ford['Ano'])
    modelo = sm.OLS(ford['% Participação'], X_f)
    resultado = modelo.fit()
    fig_ford = px.scatter(ford, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='blue')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_ford.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_ford.update_layout(height=400, width=535)
    st.plotly_chart(fig_ford)
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
    st.header('OUTRAS EMPRESAS')    
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Médios'")         

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    op = df_resultado.query("Fabricante == 'Outras empresas'")       
    
    st.dataframe(op, height=255, width=500)    
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
    st.header('REGRESSÃO OUTRAS EMPRESAS')       
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm    
    X_o = sm.add_constant(op['Ano'])
    modelo = sm.OLS(op['% Participação'], X_o)
    resultado = modelo.fit()
    fig_op = px.scatter(op, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='orange')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_op.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_op.update_layout(height=400, width=535)
    st.plotly_chart(fig_op)
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
    st.header('HIGHLIGHTS')
    st.subheader('2012 à 2023')
    st.metric(label='FORD', value='0%', delta='-22.3 pt')
    st.metric(label='OUTRAS EMPRESAS', value='2.3%',delta='2.3 pt')    
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
    st.header('PREVISÃO MÉDIOS 2024')
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'MAN': 73.5,
        'Mercedes-Benz': 14.5,
        'IVECO': 10,
        'OUTRAS EMPRESAS': 2,    
    })

    df = pd.Series({
        'Abr/24': 670,
        'Maio/24': 728,
        'Jun/24': 716,
        'Jul/24': 748,
        'Ago/24': 780,
        'Set/24': 742,
        'Out/24': 754,
        'Nov/24': 731,
        'Dez/24': 657,
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
    st.header('PREVISÃO MÉDIOS 2025')
    # Aqui vai o código para a previsão de 2025...
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'MAN': 73,
        'Mercedes-Benz': 14,
        'IVECO': 11,
        'OUTRAS EMPRESAS': 2,    
    })

    df = pd.Series({
        'Jan/25': 656,
        'Fev/25': 626,
        'Mar/25': 712,
        'Abr/25': 652,
        'Maio/25': 688,
        'Jun/25':  717,
        'Jul/25': 750,
        'Ago/25': 760,
        'Set/25': 717,
        'Out/25': 732,
        'Nov/25': 724,
        'Dez/25': 778,
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
    st.header('PREVISÃO MÉDIOS 2026')
    
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'MAN': 72.8,
        'Mercedes-Benz': 13.5,
        'IVECO': 12,
        'OUTRAS EMPRESAS': 2,    
    })

    df = pd.Series({
        'Jan/26': 660,
        'Fev/26': 612,
        'Mar/26': 704,
        'Abr/26': 650,
        'Maio/26': 687,
        'Jun/26': 686,
        'Jul/26': 716,
        'Ago/26': 738,
        'Set/26': 704,
        'Out/26': 713,
        'Nov/26': 695,
        'Dez/26': 744,
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