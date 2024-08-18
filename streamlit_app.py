#!/usr/bin/env python
# coding: utf-8

# #A taxa de inscritos por região é proporcional a taxa populacional por região?

# In[2]:

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


 

# In[3]:
st.set_page_config(page_title="Trabalho Prático ICD")

with st.container():
    st.subheader("Análise dos dados ENEM")

    st.title("Perguntas")

    st.write("INTRODUÇÃO AO TRABALHO")

    st.write("Link para o Colab completo [Clique aqui](https://colab.research.google.com/drive/15goBpe5qIkR6YMtf1wXbw7RQvcO6cHYN#scrollTo=PIIVBkMm-Qm4)")

    opcode = st.selectbox("Selecione a análise", ["Taxa Populacional", "Aulas Online", "Treineiros"])
if opcode == "Taxa Populacional":
    @st.cache_data
    def popData():
        dfpop = (pd.read_csv('./pop_ibge_18-22.csv',
                            sep=';',
                            encoding='latin1'))
        dfpop = dfpop.iloc[:, :6]
        dfpop.rename(columns={'Brasil, Grande Regiao e Unidade da Federativa': 'UF'}, inplace=True)
        dfpop.set_index('UF', inplace=True)
        return dfpop


    # In[4]:
    @st.cache_data
    def InscData():
        dfInscReg18 = pd.read_excel("Sinopse_ENEM_2018.xlsx", sheet_name="1_1", skiprows=[0, 1, 2, 3, 4, 6],
                                    usecols=[0, 1, 2])
        dfInscReg19 = pd.read_excel("Sinopse_ENEM_2019.xlsx", sheet_name="1_1", skiprows=[0, 1, 2, 3, 4, 6],
                                    usecols=[0, 1, 2])
        dfInscReg20 = pd.read_excel("Sinopse_ENEM_2020.xlsx", sheet_name="1_1", skiprows=[0, 1, 2, 3, 4, 6],
                                    usecols=[0, 1, 2])
        dfInscReg21 = pd.read_excel("Sinopse_ENEM_2021.xlsx", sheet_name="1_1", skiprows=[0, 1, 2, 3, 4, 6],
                                    usecols=[0, 1, 2])
        dfInscReg22 = pd.read_excel("Sinopse_ENEM_2022.xlsx", sheet_name="1_1", skiprows=[0, 1, 2, 3, 4, 6],
                                    usecols=[0, 1, 2])
        return [dfInscReg18, dfInscReg19, dfInscReg20, dfInscReg21, dfInscReg22]


    #

    # In[5]:
    ### CALCULO DE TAXAS

    dfpop = popData()

    InscReg = InscData()
    ano = 18
    for df in InscReg:
        df.rename(
            columns={'Unidade da Federação': 'UF', 'Região Geográfica': 'Região', 'Número de Inscritos': f'Inscritos{ano}'},
            inplace=True)
        df['UF'] = df['UF'].fillna(df['Região'])
        df.drop(columns=['Região'], inplace=True)
        df.set_index('UF', inplace=True)
        ano += 1
    dfInscRegALL = pd.concat(InscReg, axis=1, join="inner")
    # dfInscRegALL.rename(index={'Centro-Oeste ': 'Centro-Oeste'}, inplace=True)
    # dfInscRegALL

    # In[6]:


    dfALL = pd.concat([dfpop, dfInscRegALL], axis=1, join="inner")
    cols = ['2018', 'Inscritos18', '2019', 'Inscritos19', '2020',
            'Inscritos20', '2021', 'Inscritos21', '2022', 'Inscritos22']
    dfALL = dfALL[cols]
    # dfALL

    # In[7]:


    data = ({'2018': dfALL['Inscritos18'] / dfALL['2018'],
            '2019': dfALL['Inscritos19'] / dfALL['2019'],
            '2020': dfALL['Inscritos20'] / dfALL['2020'],
            '2021': dfALL['Inscritos21'] / dfALL['2021'],
            '2022': dfALL['Inscritos22'] / dfALL['2022']})
    dfInscPop = pd.DataFrame(data)
    # dfInscPop

    # In[8]:


    data = ({'2018': dfALL['2018'] / dfALL['2018'].loc['Brasil'],
            '2019': dfALL['2019'] / dfALL['2019'].loc['Brasil'],
            '2020': dfALL['2020'] / dfALL['2020'].loc['Brasil'],
            '2021': dfALL['2021'] / dfALL['2021'].loc['Brasil'],
            '2022': dfALL['2022'] / dfALL['2022'].loc['Brasil']})
    dfTaxaPop = pd.DataFrame(data)
    # dfTaxaPop

    # In[9]:


    data = ({'2018': dfALL['Inscritos18'] / dfALL['Inscritos18'].loc['Brasil'],
            '2019': dfALL['Inscritos19'] / dfALL['Inscritos19'].loc['Brasil'],
            '2020': dfALL['Inscritos20'] / dfALL['Inscritos20'].loc['Brasil'],
            '2021': dfALL['Inscritos21'] / dfALL['Inscritos21'].loc['Brasil'],
            '2022': dfALL['Inscritos22'] / dfALL['Inscritos22'].loc['Brasil']})
    dfTaxaInsc = pd.DataFrame(data)

    # dfTaxaInsc




    ### PLOT 1

    # Cria uma figura e um conjunto de subplots
    fig, axs = plt.subplots(3, 2, figsize=(10, 8))  # 5 subplots, um para cada ano

    # Define a largura das barras
    bar_width = 0.35

    # Define as posições das barras no eixo x para dfTaxaPop.iloc[1:6] e dfTaxaInsc.iloc[1:6]
    index_dfTaxaPop = np.arange(len(dfTaxaPop.iloc[1:6].index))
    index_dfTaxaInsc = index_dfTaxaPop + bar_width

    # Loop para criar um subplot para cada ano
    for i, ano in enumerate(range(2018, 2023)):
        if i == 0:
            ind = (0, 0)
        elif i == 1:
            ind = (1, 0)
        elif i == 2:
            ind = (2, 0)
        elif i == 3:
            ind = (0, 1)
        elif i == 4:
            ind = (1, 1)

        # Barras para o primeiro DataFrame
        axs[ind].bar(index_dfTaxaPop, dfTaxaPop.iloc[1:6].loc[:, str(ano)], bar_width, label=f'dfTaxaPop.iloc[1:6] - {ano}',
                edgecolor='k')

        # Barras para o segundo DataFrame, deslocadas pela largura da barra
        axs[ind].bar(index_dfTaxaInsc, dfTaxaInsc.iloc[1:6].loc[:, str(ano)], bar_width,
                label=f'dfTaxaInsc.iloc[1:6] - {ano}', edgecolor='k')

        # Definindo o título do subplot como o ano correspondente
        axs[ind].set_title(f'Dados do ano {ano}')

        # Adicionando as legendas das regiões no eixo x
        axs[ind].set_xticks(index_dfTaxaPop + bar_width / 2)
        axs[ind].set_xticklabels(dfTaxaPop.iloc[1:6].index)

        # Adicionando a legenda para diferenciar os DataFrames
        axs[ind].legend(['TaxaPop', 'TaxaInsc'])

    # Ajusta o layout para evitar sobreposição
    fig.delaxes(axs[2, 1])
    plt.tight_layout()

    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.pyplot(fig)

    # plt.show()
    #
    # # In[11]:


    dfInscRegALL = dfInscRegALL.reindex(
        index=['Brasil', 'Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste ', 'Rondônia', 'Acre', 'Amazonas', 'Roraima',
            'Pará',
            'Amapá', 'Tocantins', 'Maranhão', 'Piauí', 'Ceará',
            'Rio Grande do Norte', 'Paraíba', 'Pernambuco', 'Alagoas', 'Sergipe',
            'Bahia', 'Minas Gerais', 'Espírito Santo', 'Rio de Janeiro',
            'São Paulo', 'Paraná', 'Santa Catarina', 'Rio Grande do Sul',
            'Centro-Oeste ', 'Mato Grosso do Sul', 'Mato Grosso', 'Goiás',
            'Distrito Federal'])
    dfInscALLtime = pd.DataFrame({'Inscritos': dfInscRegALL.iloc[:6].sum(axis='columns')})
    dfTaxaInscALLtime = pd.DataFrame({'Taxa': dfInscALLtime['Inscritos'] / dfInscALLtime['Inscritos'].loc['Brasil']})
    # dfTaxaInscALLtime

    # In[12]:

    ###PLOT 2
    # Cria uma figura e um conjunto de subplots
    fig, axs = plt.subplots(3, 2, figsize=(10, 8))  # 5 subplots, um para cada ano

    # Define a largura das barras
    bar_width = 0.25

    # Define as posições das barras no eixo x para dfTaxaPop.iloc[1:6] e dfTaxaInsc.iloc[1:6]
    index_dfTaxaPop = np.arange(len(dfTaxaPop.iloc[1:6].index))
    index_dfTaxaInsc = index_dfTaxaPop + bar_width
    index_dfTaxaInscALLtime = index_dfTaxaInsc + bar_width

    # Loop para criar um subplot para cada ano
    for i, ano in enumerate(range(2018, 2023)):
        if i == 0:
            ind = (0, 0)
        elif i == 1:
            ind = (1, 0)
        elif i == 2:
            ind = (2, 0)
        elif i == 3:
            ind = (0, 1)
        elif i == 4:
            ind = (1, 1)

        # Barras para o primeiro DataFrame
        axs[ind].bar(index_dfTaxaPop, dfTaxaPop.iloc[1:6].loc[:, str(ano)], bar_width, label=f'dfTaxaPop.iloc[1:6] - {ano}',
                edgecolor='k')

        # Barras para o segundo DataFrame, deslocadas pela largura da barra
        axs[ind].bar(index_dfTaxaInsc, dfTaxaInsc.iloc[1:6].loc[:, str(ano)], bar_width,
                label=f'dfTaxaInsc.iloc[1:6] - {ano}', edgecolor='k')

        axs[ind].bar(index_dfTaxaInscALLtime, dfTaxaInscALLtime.iloc[1:6].loc[:, 'Taxa'], bar_width,
                label=f'dfTaxaInscAllTime', edgecolor='k')

        # Definindo o título do subplot como o ano correspondente
        axs[ind].set_title(f'Dados do ano {ano}')

        # Adicionando as legendas das regiões no eixo x
        axs[ind].set_xticks(index_dfTaxaPop + bar_width / 2)
        axs[ind].set_xticklabels(dfTaxaPop.iloc[1:6].index)

        # Adicionando a legenda para diferenciar os DataFrames
        axs[ind].legend(['TaxaPop', 'TaxaInsc', 'TaxaInscMedia'])

    # Ajusta o layout para evitar sobreposição
    fig.delaxes(axs[2, 1])
    plt.tight_layout()
    # plt.show()

    with st.container():
        st.write("---")

        st.write("Nesse segundo plot adicionamos uma taxa média de inscricões por região para incrementar a análise.")

        st.pyplot(fig)

    # In[13]:
    Inscritos = 10000
    insc_norte = 1177 / Inscritos
    insc_nordeste = 3395 / Inscritos
    insc_sudeste = 3483 / Inscritos
    insc_sul = 1079 / Inscritos
    insc_centro_oeste = 865 / Inscritos
    data = np.zeros(shape=Inscritos, dtype='str')
    data[:] = 'B'
    data[:int(len(data) * insc_norte)] = '1'
    data[int(len(data) * insc_norte): int(len(data) * (insc_norte + insc_nordeste))] = '2'
    data[int(len(data) * (insc_norte + insc_nordeste)):int(len(data) * (insc_norte + insc_nordeste + insc_sudeste))] = '3'
    data[int(len(data) * (insc_norte + insc_nordeste + insc_sudeste)):int(
        len(data) * (insc_norte + insc_nordeste + insc_sudeste + insc_sul))] = '4'
    data[int(len(data) * (insc_norte + insc_nordeste + insc_sudeste + insc_sul)):] = '5'

    # In[14]:


    sample_size = int(10000 * dfInscRegALL.loc['Brasil'].mean() / dfpop.loc['Brasil'].mean())
    simulations = np.zeros(1000)
    for i in range(1000):
        np.random.shuffle(data)
        amostra = data[:sample_size]
        num_norte = np.count_nonzero(amostra == '1')
        num_nordeste = np.count_nonzero(amostra == '2')
        num_sudeste = np.count_nonzero(amostra == '3')
        num_sul = np.count_nonzero(amostra == '4')
        num_centro_oeste = np.count_nonzero(amostra == '5')

        tvd = 0.5 * (abs((num_norte / sample_size) - dfTaxaInscALLtime.loc['Norte'].sum()) +
                    abs((num_nordeste / sample_size) - dfTaxaInscALLtime.loc['Nordeste'].sum()) +
                    abs((num_sudeste / sample_size) - dfTaxaInscALLtime.loc['Sudeste'].sum()) +
                    abs((num_sul / sample_size) - dfTaxaInscALLtime.loc['Sul'].sum()) +
                    abs((num_centro_oeste / sample_size) - dfTaxaInscALLtime.loc['Centro-Oeste '].sum()))
        simulations[i] = tvd

    # In[15]:


    tvd2018 = 0.5 * (abs(dfTaxaInsc.loc['Norte', '2018'].sum() - dfTaxaInscALLtime.loc['Norte'].sum()) +
                    abs(dfTaxaInsc.loc['Nordeste', '2018'].sum() - dfTaxaInscALLtime.loc['Nordeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sudeste', '2018'].sum() - dfTaxaInscALLtime.loc['Sudeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sul', '2018'].sum() - dfTaxaInscALLtime.loc['Sul']) +
                    abs(dfTaxaInsc.loc['Centro-Oeste ', '2018'].sum() - dfTaxaInscALLtime.loc['Centro-Oeste '].sum()))
    tvd2019 = 0.5 * (abs(dfTaxaInsc.loc['Norte', '2019'].sum() - dfTaxaInscALLtime.loc['Norte'].sum()) +
                    abs(dfTaxaInsc.loc['Nordeste', '2019'].sum() - dfTaxaInscALLtime.loc['Nordeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sudeste', '2019'].sum() - dfTaxaInscALLtime.loc['Sudeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sul', '2019'].sum() - dfTaxaInscALLtime.loc['Sul']) +
                    abs(dfTaxaInsc.loc['Centro-Oeste ', '2019'].sum() - dfTaxaInscALLtime.loc['Centro-Oeste '].sum()))

    tvd2020 = 0.5 * (abs(dfTaxaInsc.loc['Norte', '2020'].sum() - dfTaxaInscALLtime.loc['Norte'].sum()) +
                    abs(dfTaxaInsc.loc['Nordeste', '2020'].sum() - dfTaxaInscALLtime.loc['Nordeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sudeste', '2020'].sum() - dfTaxaInscALLtime.loc['Sudeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sul', '2020'].sum() - dfTaxaInscALLtime.loc['Sul']) +
                    abs(dfTaxaInsc.loc['Centro-Oeste ', '2020'].sum() - dfTaxaInscALLtime.loc['Centro-Oeste '].sum()))

    tvd2021 = 0.5 * (abs(dfTaxaInsc.loc['Norte', '2021'].sum() - dfTaxaInscALLtime.loc['Norte'].sum()) +
                    abs(dfTaxaInsc.loc['Nordeste', '2021'].sum() - dfTaxaInscALLtime.loc['Nordeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sudeste', '2021'].sum() - dfTaxaInscALLtime.loc['Sudeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sul', '2021'].sum() - dfTaxaInscALLtime.loc['Sul']) +
                    abs(dfTaxaInsc.loc['Centro-Oeste ', '2021'].sum() - dfTaxaInscALLtime.loc['Centro-Oeste '].sum()))

    tvd2022 = 0.5 * (abs(dfTaxaInsc.loc['Norte', '2022'].sum() - dfTaxaInscALLtime.loc['Norte'].sum()) +
                    abs(dfTaxaInsc.loc['Nordeste', '2022'].sum() - dfTaxaInscALLtime.loc['Nordeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sudeste', '2022'].sum() - dfTaxaInscALLtime.loc['Sudeste'].sum()) +
                    abs(dfTaxaInsc.loc['Sul', '2022'].sum() - dfTaxaInscALLtime.loc['Sul']) +
                    abs(dfTaxaInsc.loc['Centro-Oeste ', '2022'].sum() - dfTaxaInscALLtime.loc['Centro-Oeste '].sum()))

    ### PLOT 3

    fig = plt.figure(figsize=(10, 5))
    plt.hist(simulations, bins=20, edgecolor='black', color='powderblue')
    x_points = [tvd2018, tvd2019, tvd2020, tvd2021, tvd2022]
    y_points = [2, 2, 2, 7, 2]
    labels = ['2018', '2019', '2020', '2021', '2022']

    for x, y, label in zip(x_points, y_points, labels):
        plt.scatter(x, y, label=label)

    plt.axvline(x=np.percentile(simulations, 3), color='red', linestyle='--', label='3%')
    plt.axvline(x=np.percentile(simulations, 97), color='red', linestyle='--', label='97%')

    plt.title('TVD por permutação X observado')
    plt.legend()
    with st.container():
        st.write("---")

        (st.write("Aqui temos um teste de confiabilidade dos dados, foi utilizado um teste de permutação. Foi definido um intervalo de confiança de 94% e percebemos que os dados observados de fato não foram ao acaso."))

        st.pyplot(fig)
if opcode == "Aulas Online":
    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.pyplot(fig)

if opcode == "Treineiros":
    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.pyplot(fig)
