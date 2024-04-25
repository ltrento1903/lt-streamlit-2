import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='LINHA DE PRODUTOS: LEVES',
                   page_icon='🛻',
                   layout='wide')

st.markdown('# LINHA DE PRODUTOS: LEVES 🛻')
st.subheader('ANÁLISES E PREVISÕES')

col1, col2, col3 = st.columns([1, 1, 1])


with col1:
    st.header('PARTICIPAÇÃO LINHA LEVES 📈')
    participação = {
        'Ano': [2019, 2020, 2021, 2022, 2023],
        'Percentual': [11.1, 10.1, 9.8, 8.5, 8.4]
    }
    leves = pd.DataFrame(participação)
    leves['Ano'] = pd.to_datetime(leves['Ano'], format='%Y')    
    

    import plotly.graph_objects as go

    fig_part = go.Figure()
    fig_part.add_trace(go.Box(y=leves['Percentual'], name="Média & Desvio Padrão", marker_color='#E06234', boxmean='sd'))
    fig_part.update_layout(title='2019 à 2023')
    fig_part.update_layout(height=443, width=500)
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
    st.header('PREVISÃO DE DEMANDA LINHA LEVES ⛟')    
    previsao_leves = pd.read_excel('previsao_arima_36 meses.xlsx')
    percentual_medio = pd.Series({'Leves': 8.5})    
    
    for produto, percentual in percentual_medio.items():
        previsao_leves[produto] = percentual * previsao_leves['Previsão'] / 100           
        
    
    fig_prev = px.line(previsao_leves, x='Mês', y='Leves', color_discrete_sequence=['#B73027'])
    fig_prev.update_layout(title='PREVISÃO DE DEMANDA PARA LINHA LEVES')
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
    st.header('PREVISÃO DE DEMANDA LINHA LEVES ⛟')    
    st.dataframe(previsao_leves)
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
    st.header('MERCEDES-BENZ')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()        
    
    linha = df_ano.query("Linha == 'Leves'")          

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

    
with col2:
    st.header('MAN')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()        
    
    linha = df_ano.query("Linha == 'Leves'")          

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
    

with col3:
    st.header('IVECO')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()        
    
    linha = df_ano.query("Linha == 'Semileves'")          

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
    st.metric(label='MERCEDES-BENZ', value='54.0%',delta='23.3pt')
    st.metric(label='MAN', value='27.4%', delta='-11.1 pt')   
    st.metric(label='IVECO', value='10.7%', delta='4.3 pt')
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
    
col1, col2, col3 = st.columns([1,1,1,])

with col1:   
    st.header('FORD')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')        
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Leves'")      

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
    fig_ford = px.scatter(ford, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='black')
   
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
    
    linha = df_ano.query("Linha == 'Leves'")         

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
    fig_op = px.scatter(op, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='#200B0F')
   
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
    st.header('CAOA-HYUNDAY')    
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Leves'")             

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    ch = df_resultado.query("Fabricante == 'Caoa - Hyundai'")            
    
    st.dataframe(ch, height=255, width=500)    
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
    st.header('REGRESSÃO CAOA-HYUNDAY')       
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm    
    X_ch = sm.add_constant(ch['Ano'])
    modelo = sm.OLS(ch['% Participação'], X_ch)
    resultado = modelo.fit()
    fig_ch = px.scatter(ch, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='#3D5657')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_ch.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_ch.update_layout(height=400, width=535)
    st.plotly_chart(fig_ch)
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

col1, col2 = st.columns([1,1])
with col1:
    st.header('AGRALE')    
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Leves'")             

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    ag = df_resultado.query("Fabricante == 'Agrale'")             
    
    st.dataframe(ag, height=475, width=500)    
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
    st.header('REGRESSÃO AGRALE')       
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm    
    X_ag = sm.add_constant(ag['Ano'])
    modelo = sm.OLS(ag['% Participação'], X_ag)
    resultado = modelo.fit()
    fig_ag = px.scatter(ag, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='orange')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_ag.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='#6D2828'))
    fig_ag.update_layout(height=400, width=535)
    st.plotly_chart(fig_ag)
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
    st.header('HIGHLIGHTS')
    st.subheader('2012 à 2023')
    st.metric(label='FORD', value='0%', delta='-22.0 pt')
    st.metric(label='OUTRAS EMPRESAS', value='3.4%',delta='2.6 pt')   
    st.metric(label='CAOA-HYUNDAY', value='3.5%',delta='3.5 pt')  
    st.metric(label='AGRALE', value='0.7%',delta='-0.34 pt')
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
    st.header('PREVISÃO LEVES 2024')
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'Mercedes-Benz': 54.8,
        'MAN': 27.3,
        'IVECO': 10.7,
        'OUTRAS EMPRESAS': 3.3,    
        'CAOA-HYUNDAY': 3.2,
        'Agrale': 0.7,
    })

    df = pd.Series({
        'Abr/24': 712,
        'Maio/24': 774,
        'Jun/24': 760,
        'Jul/24': 795,
        'Ago/24': 828,
        'Set/24': 789,
        'Out/24': 801,
        'Nov/24': 776,
        'Dez/24': 836,
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
    st.header('PREVISÃO LEVES 2025')
    # Aqui vai o código para a previsão de 2025...
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'Mercedes-Benz': 54.6,
        'MAN': 27.3,
        'IVECO': 10.7,
        'OUTRAS EMPRESAS': 3.4,
        'CAOA-HYUNDAY': 3.2,
        'Agrale': 0.7,    
    })

    df = pd.Series({
        'Jan/25': 697,
        'Fev/25': 665,
        'Mar/25': 756,
        'Abr/25': 693,
        'Maio/25': 731,
        'Jun/25':  761,
        'Jul/25': 796,
        'Ago/25': 808,
        'Set/25': 762,
        'Out/25': 778,
        'Nov/25': 770,
        'Dez/25': 827,
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
    st.header('PREVISÃO LEVES 2026')
    
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'Mercedes-Benz': 53.9,
        'MAN': 27.3,
        'IVECO': 11,
        'OUTRAS EMPRESAS': 3.6,   
        'CAOA-HYUNDAY': 3.7,
        'AGRALE': 0.7, 
    })

    df = pd.Series({
        'Jan/26': 700,
        'Fev/26': 651,
        'Mar/26': 748,
        'Abr/26': 690,
        'Maio/26': 730,
        'Jun/26': 729,
        'Jul/26': 760,
        'Ago/26': 784,
        'Set/26': 748,
        'Out/26': 758,
        'Nov/26': 738,
        'Dez/26': 790,
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