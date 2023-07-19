import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st



sns.set(context='talk', style='ticks')
renda = pd.read_csv('previsao_de_renda.csv')

st.set_page_config(
     page_title="Previsão Renda",
     page_icon='2178261.png',
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')
st.markdown("---")


def plota(renda):
    fig, ax = plt.subplots(8,1,figsize=(10,70))
    renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
    st.write('## Gráficos ao longo do tempo')
    sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
    ax[1].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
    ax[2].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
    ax[3].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
    ax[4].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
    ax[5].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
    ax[6].tick_params(axis='x', rotation=45)
    sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
    ax[7].tick_params(axis='x', rotation=45)
    sns.despine()
    st.pyplot(plt)

    tabela = st.write('## Gráficos bivariada')
    fig, ax = plt.subplots(7,1,figsize=(10,50))
    sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
    sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
    sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
    sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
    sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
    sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
    sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
    sns.despine()
    st.pyplot(plt)

if st.checkbox('Apresentar mapa'):
    st.map(plota(renda) )

st.sidebar.write('# Informe seus dados para realizar uma previsão de renda ')


sexo = st.sidebar.selectbox('sexo',['M','F'])
estado_civil= st.sidebar.selectbox('estado civil',['Solteiro','Casado','Viúvo','União','Separado'])
tipo_renda = st.sidebar.selectbox('tipo_renda',['Empresário','Assalariado','Servidor público','Pensionista','Bolsista'])
educacao = st.sidebar.selectbox('educacao',['Secundário','Superior completo','Superior incompleto','Primário','Pós graduação'])
tipo_residencia = st.sidebar.selectbox('tipo_residencia',['Casa','Com os pais','Governamental','Aluguel','Estúdio','Comunitário'])
posse_de_veiculo = st.sidebar.selectbox('posse_de_veiculo',['False','True'])
posse_de_imovel = st.sidebar.selectbox('posse_de_imovel',['False','True'])
qtd_filhos = st.sidebar.selectbox('qtd_filhos',[0,1,2,3,4,5,6,7,8,9,10])
qt_pessoas_residencia = st.sidebar.selectbox('qt_pessoas_residencia',[1,2,3,4,5,6,7,9,10,15])
tempo_emprego = st.sidebar.number_input('Tempo Emprego', min_value=1, max_value=42)
idade = st.sidebar.number_input('idade', min_value=22, max_value=68)


data= {'sexo':sexo,
'estado_civil':estado_civil,
'tipo_renda':tipo_renda,
'educacao':educacao,
'tipo_residencia':tipo_residencia,
'posse_de_veiculo':posse_de_veiculo,
'posse_de_imovel':posse_de_imovel,
'qtd_filhos':qtd_filhos,
'qt_pessoas_residencia':qt_pessoas_residencia,
'tempo_emprego':tempo_emprego,
'idade':idade}

rent= pd.DataFrame(data,index=[0])
#renda.columns=['sexo','estado_civil','tipo_renda','educacao','tipo_residencia',
#'posse_de_veiculo','posse_de_imovel','qtd_filhos','qt_pessoas_residencia','tempo_emprego','idade']

st.sidebar.button('Buscar')


renda = pd.read_csv('previsao_de_renda.csv')

#plots






