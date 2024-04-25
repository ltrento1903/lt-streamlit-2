import streamlit as st
import pandas as pd
import webbrowser 

st.set_page_config(page_title='Linhas de Produtos',
                   page_icon='🚛',
                   layout='wide')

st.markdown('# LINHAS DE PRODUTOS 🚛')
st.subheader('ANÁLISE DO COMPORTAMENTO DAS LINHAS DE PRODUTOS E FABRICANTES 🚛')

col1, col2, col3 = st.columns([2, 3, 1])


with col1:
    st.header('CAMINHÕES')
    st.subheader('LICENCIAMENTOS POR LINHAS E FABRICANTES: 2012 À 2024')
    btn=st.button('Acesse os dados no site da Anfavea')
    if btn: 
        webbrowser.open_new_tab('https://anfavea.com.br/site/edicoes-em-excel/')

    df = pd.read_excel(r'C:\Users\luizt\Caminhões\Pages\caminhões_dados_.xlsx')
    st.write(df)
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
    st.header('PARTICIPAÇÃO POR LINHA')
    st.subheader('2012 à 2024 YTD')
    df['Mês'] = pd.to_datetime(df['Mês'])    
    df_grouped = df.groupby(['Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    df['Ano'] = df['Mês'].dt.year
    df_ano = df.groupby(['Ano', 'Linha', 'Fabricante'])['Quantidade'].sum().reset_index()    
    df_ano_linha = df_ano.groupby(['Ano','Linha'])['Quantidade'].sum().reset_index()    
    df_ano_linha.columns = ['Ano', 'Linha', 'Quantidade']
    total_por_ano = df_ano_linha.groupby('Ano')['Quantidade'].sum().reset_index()
    total_por_ano.columns = ['Ano', 'Total']
    df_ano_linha_total = pd.merge(df_ano_linha, total_por_ano, on='Ano')
    df_ano_linha_total['% do Total'] = (df_ano_linha_total['Quantidade'] / df_ano_linha_total['Total']) * 100   
  
    import plotly.express as px
    colors = {'Leves': '#1f77b4', 'Médios': '#ff7f0e', 'Pesados': '#2ca02c', 'Semileves': '#d62728', 'Semipesados': '#9467bd'}
    fig_2 = px.bar(df_ano_linha_total, x="Ano", y="% do Total", color="Linha", hover_name="Linha",
               title="Participação % de cada linha ao longo dos anos",
               labels={"% do Total": "% do Total"},
               category_orders={"Linha": ['Leves', 'Médios', 'Pesados', 'Semileves', 'Semipesados']},
               color_discrete_map=colors, 
               barmode='relative', 
               text=df_ano_linha_total['% do Total'].apply(lambda x: f'{x:.1f}%'),  
               height=490, width=900) 
    st.plotly_chart(fig_2)
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
    st.subheader('2012 á 2024')
    st.metric(label='CAMINHÕES', value='2023 = 100.074', delta='-39.100 Licenciamentos')
    st.metric(label='LEVES', value='7.5%', delta='- 16.5 pt')
    st.metric(label='PESADOS', value='53.3%', delta='23.4 pt')
    st.markdown("""
Houve uma diminuição significativa de 39.174 licenciamentos em 11 anos, juntamente com uma queda de 16,5 pontos 
                percentuais nas vendas de caminhões leves. Pode-se deduzir que parte desse mercado migrou para
                 os fabricantes de veículos comerciais leves, que registraram crescimento durante o mesmo período.
""")

    
col1, col2, col3 = st.columns([2, 3, 1])

with col1:
    st.header('LICENCIAMENTOS POR FABRICANTE')
    st.subheader('2012 à 2024')
    df_ano_fab = df.groupby(['Ano','Fabricante'])['Quantidade'].sum().reset_index()
    df_ano_fab.columns = ['Ano', 'Fabricante', 'Quantidade']
    total_por_ano_fab = df_ano_fab.groupby('Ano')['Quantidade'].sum().reset_index()
    total_por_ano_fab.columns = ['Ano', 'Total']
    df_ano_fab_total = pd.merge(df_ano_fab, total_por_ano_fab, on='Ano')
    df_ano_fab_total['% do Total'] = (df_ano_fab_total['Quantidade'] / df_ano_fab_total['Total']) * 100
    df_ano_fab_total
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
    st.header('PARTICIPAÇÃO POR FABRICANTE')
    st.subheader('2012 à 2024')
    colors = {
    'Agrale': '#7CFC00',
    'DAF': '#00FF7F',
    'Ford': '#DAA520',
    'INTERNATIONAL': '#D2691E',
    'Iveco': '#006400',
    'MAN': '#4B0082',
    'Mercedes-Benz': '#FF00FF',
    'Outras empresas': '#DDA0DD',
    'SCANIA': '#DC143C',
    'Shacman': 'black',
    'VOLVO': '#8B0000',
    'FCA (Fiat/Dodge)': 'green',
    'Peugeot Citroën': '#800000',
    'Caoa - Hyundai': '#008080',
}
    fig_3 = px.bar(df_ano_fab_total, x="Ano", y="% do Total", color="Fabricante", hover_name="Fabricante",
               title="Participação % de cada fabricante ao longo dos anos",
               labels={"% do Total": "% do Total"},
               color_discrete_map=colors,
               barmode='relative',  
               text=df_ano_fab_total['% do Total'].apply(lambda x: f'{x:.1f}%'),  
               height=800, width=900)
    st.plotly_chart(fig_3)
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
    st.subheader('2012 á 2024')
    st.markdown('# DESTAQUES 📈')
    st.metric(label='DAF', value='2023 = 7.7%', delta='7.7 PT')
    st.metric(label='VOLVO', value='2023 = 18.25%', delta='6.8 pt')
    st.metric(label='SCANIA', value='2023 = 11.5%', delta='3.5 pt')
    st.markdown('# PERDEDORES 📉')
    st.metric(label='Ford', value='2023 = 0.2%', delta='-15.7%')
    st.metric(label='MAN', value= '2023 = 25%', delta= '-4.8%')
    st.metric(label='MERCEDES-BENZ', value= '2023 = 23.3%', delta= '-1.6%')
    st.markdown("""
O crescimento notável dos fabricantes DAF e VOLVO destaca-se, com a DAF aumentando sua participação 
                de 0% para 8,4% em 11 anos e a VOLVO mantendo crescimento desde 2018. Mercedes e MAN VOLKWAGEM 
                precisam estar atentos aos concorrentes ambiciosos no mercado.
""")