import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='LINHA DE PRODUTOS: SEMILEVES',
                   page_icon='🚚',
                   layout='wide')

st.markdown('# LINHA DE PRODUTOS: SEMILEVES 🚚')
st.subheader('ANÁLISES E PREVISÕES')

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.header('PARTICIPAÇÃO LINHA SEMILEVES 📶')
    participação = {
        'Ano': [2019, 2020, 2021, 2022, 2023],
        'Percentual': [5.0, 5.4, 5.1, 6.0, 8.0]
    }
    sleves = pd.DataFrame(participação)
    sleves['Ano'] = pd.to_datetime(sleves['Ano'], format='%Y')  

    import plotly.graph_objects as go

    fig_part = go.Figure()    
    fig_part.add_trace(go.Box(y=sleves['Percentual'], name="Média & Desvio Padrão", marker_color='#AA2FCD', boxmean='sd'))
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
    st.header('PREVISÃO DE DEMANDA LINHA SEMILEVES 🚚')    
    previsao_sleves = pd.read_excel('previsao_arima_36 meses.xlsx')
    percentual_medio = pd.Series({'Semileves': 5.9})    
    
    for produto, percentual in percentual_medio.items():
        previsao_sleves[produto] = percentual * previsao_sleves['Previsão'] / 100               
        
    
    fig_prev = px.line(previsao_sleves, x='Mês', y='Semileves', color_discrete_sequence=['#E39825'])
    fig_prev.update_layout(title='PREVISÃO DE DEMANDA PARA LINHA SEMILEVES')
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
    st.header('PREVISÃO DE DEMANDA LINHA SEMILEVES ⛟')    
    st.dataframe(previsao_sleves)
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
    st.header('FCA FIAT (DODGE)')    
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Semileves'")         
    
    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    fca = df_resultado.query("Fabricante == 'FCA (Fiat/Dodge)'")           
    
    st.dataframe(fca, height=365, width=500)    
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
    st.header('REGRESSÃO FCA FIAT (DODGE)')       
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm    
    X_f = sm.add_constant(fca['Ano'])
    modelo = sm.OLS(fca['% Participação'], X_f)
    resultado = modelo.fit()
    fig_fca = px.scatter(fca, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='#0F0000')
   
    anos_futuros = [2024, 2025, 2026]      
    previsao_futuros = resultado.predict(sm.add_constant(anos_futuros))
    fig_fca.add_scatter(x=anos_futuros, y=previsao_futuros, mode='lines', name='Previsão', line=dict(color='red'))
    fig_fca.update_layout(height=400, width=535)
    st.plotly_chart(fig_fca)
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
    
    linha = df_ano.query("Linha == 'Semileves'")              

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
    st.header('MAN')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()        
    
    linha = df_ano.query("Linha == 'Semileves'")          

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

with col4:
    st.header('HIGHLIGHTS')
    st.subheader('2012 à 2023')
    st.metric(label='FCA FIAT (DODGE)', value='56.4%',delta='36.3 pt')   
    st.metric(label='MERCEDES-BENZ', value='27.5%',delta='14.4 pt')
    st.metric(label='MAN', value='6.9%', delta='-7.9 pt')       
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
    st.header('FORD')
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')        
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    
    linha = df_ano.query("Linha == 'Semileves'")      

    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano')) 
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    ford = df_resultado.query("Fabricante == 'Ford'")           
 
    
    st.dataframe(ford, height=365, width=500)
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
    
with col3:
    st.header('PEUGEUT CITRÖEN')    
    df=pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_s24.xlsx')    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    

    linha = df_ano.query("Linha == 'Semileves'")        
    
    df_total_ano = linha.groupby('Ano')['Quantidade'].sum()
    df = pd.merge(linha, df_total_ano, on='Ano', suffixes=('', '_Total_Ano'))      
    df['% Participação'] = (df['Quantidade'] / df['Quantidade_Total_Ano']) * 100   
    df_resultado = df[['Ano', 'Fabricante', '% Participação', 'Quantidade']]  

    op = df_resultado.query("Fabricante == 'Peugeot Citroën'")         
    
    
    st.dataframe(op, height=365, width=500)    
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
    st.header('REGRESSÃO PEUGEUT CITRÖEN')       
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm    
    X_op = sm.add_constant(op['Ano'])
    modelo = sm.OLS(op['% Participação'], X_op)
    resultado = modelo.fit()
    fig_op = px.scatter(op, x='Ano', y='% Participação', opacity=0.65, trendline='ols', trendline_color_override='#2D5B1A')
   
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

with col4:
    st.header('HIGHLIGHTS')
    st.subheader('2012 à 2023')
    st.metric(label='FORD', value='0%', delta='-19.6 pt')
    st.metric(label='IVECO', value='6.6%', delta='-24.6 pt')    
    st.metric(label='PEUGEUT CITRÖEN', value='1.4%',delta='1.4 pt')      
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
    st.header('PREVISÃO SEMILEVES 2024')
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'FCA FIAT (DODGE)': 56.7,
        'MERCEDES-BENZ': 28,
        'MAN': 8,
        'IVECO': 6,    
        'PEUGEUT CITRÖEN': 1.3,
    })

    df = pd.Series({
        'Abr/24': 494,
        'Maio/24': 537,
        'Jun/24': 528,
        'Jul/24': 552,
        'Ago/24': 575,
        'Set/24': 548,
        'Out/24': 556,
        'Nov/24': 530,
        'Dez/24': 580,
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
    st.header('PREVISÃO SEMILEVES 2025')
    # Aqui vai o código para a previsão de 2025...
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'FCA FIAT (DODGE)': 57.5,
        'MERCEDES-BENZ': 28,
        'MAN': 8,
        'IVECO': 5.2,    
        'PEUGEUT CITRÖEN': 1.3,
    })

    df = pd.Series({
        'Jan/25': 484,
        'Fev/25': 461,
        'Mar/25': 525,
        'Abr/25': 481,
        'Maio/25': 507,
        'Jun/25':  528,
        'Jul/25': 553,
        'Ago/25': 560,
        'Set/25': 529,
        'Out/25': 540,
        'Nov/25': 535,
        'Dez/25': 574,
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
    st.header('PREVISÃO SEMILEVES 2026')
    
    # Dados fornecidos
    percentuais_medios = pd.Series({
        'FCA FIAT (DODGE)': 58.7,
        'MERCEDES-BENZ': 28,
        'MAN': 7,
        'IVECO': 5,    
        'PEUGEUT CITRÖEN': 1.3,
    })

    df = pd.Series({
        'Jan/26': 486,
        'Fev/26': 452,
        'Mar/26': 519,
        'Abr/26': 479,
        'Maio/26': 507,
        'Jun/26': 506,
        'Jul/26': 528,
        'Ago/26': 544,
        'Set/26': 519,
        'Out/26': 526,
        'Nov/26': 512,
        'Dez/26': 548,
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