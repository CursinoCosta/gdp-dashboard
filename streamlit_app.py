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
    
    with st.container():
        st.write("---")

        st.write("Primeiro plot, trás a análise comparativa entre a taxa populacional e a taxa de incrição em cada região do país, percebe-se diferença entre ambas. A diferêça se assentua especialmente após a pandemia.")

        st.image("imagens mateus/1.png")


    with st.container():
        st.write("---")

        st.write("Novo plot com a taxa média de inscrições para comparação. Houve mudanças muito pequenas ao longo dos anos em cada uma das taxas.")

        st.image("imagens mateus/2.png")

    
    with st.container():
        st.write("---")

        (st.write("Tomando como hipótese nula que essas diferenças entre percentil populacional e de inscrição por região seguem esse padrão ao acaso, foi realizado o teste da permutação de maneira proporcional aos valores reais observados."))

        st.write("Usando da métrica da Distância Total de Variação (TVD) da taxa média de inscrição e das taxas anuais, foi possivel realizar o teste da permutação e avaliar dentro de um intervalo de confiança de 94% que a hipotese nula era falsa maior parte das vezes para todos ou quase todos os anos analisados.")

        st.image("imagens mateus/3.png")


        st.warning("Concluimos então que taxa populacional e de inscrição estão interligados, mas não, necessariamente, são proporcionais. Há fatores externos que influenciam nesses valores, uma possível hipótese são os fatores culturais como o histórico da importância dos vestibulares que existe no Nordeste ou a cultura de empreendedorismo e oportunidade de emprego no Sudeste, especialmente em São Paulo que pode levar a menos pessoas procurarem uma faculdade por lá.")





if opcode == "Aulas Online":
    with st.container():
        st.write("---")

        st.write("Limpeza e organização dos dados\n\nAnteriormente, a base de dados possuia muitas colunas, mas, para fins de otimizações das operações feitas no dataframe, foram selecionados apenas as colunas:")
        st.write("- TP_ST_CONCLUSAO = 2: Conclusão do Ensino Médio no mesmo ano da aplicação do exame")
        st.write("- TP_PRESENCA_MT = 1: Presença na prova de Matemática")
        st.write("- TP_PRESENCA_CN = 1: Presença na prova de Ciências da Natureza")
        st.write("- TP_PRESENCA_LC = 1: Presença na prova de Linguagens")
        st.write("- TP_PRESENCA_CH = 1: Presença na prova de Ciências Humanas")
        st.write("Dessa forma, os resultados da base não serão influenciados por alunos que faltaram em alguma prova ou que já tiveram anteriormente a oportunidade de fazer o terceiro ano do Ensino Médio sem a pandemia.")
        st.write("Além disso, também foi feito o mapeamento das 18 faixas de renda existentes para apenas 5 classes sociais diferentes (A, B, C, D, E) em que a classe social A possui mais recursos financeiros.")
        st.write("##### Classe E = 0 até 1 salário mínimo.")
        st.write("##### Classe D = 1 até 3 salários mínimos.")
        st.write("##### Classe C = 3 até 6 salários mínimos.")
        st.write("##### CLasse B = 6 até 10 salários mínimos.")
        st.write("##### Classe A = 10 até 20 salários mínimos.")
        st.write("Também foi feito a normalização das notas já que para cada ano o ENEM possui uma nota máxima e mínima diferente. Dessa forma, um ano com nota máxima maior não teria vantagem em relação a um ano com nota máxima menor.")
        
        
        st.write("---")

        
        st.write("A partir da geração da frequências das medias totais para cada ano, percebe-se que todas elas seguem uma distribuição com uma leve assimetria à esquerda.\n\nAlém disso, é interessante observar que, para todas as classes sociais, o ano 2020 possui uma altura menor em relação ao ano de 2022. Isso provavelmente se deve ao fato de que no ano de 2022 ocorreu recorde de abstenção, ou seja, menos alunos foram fazer a prova.")


        st.image("imagens igor/1.png")


    with st.container():
        st.write("---")

        st.image("imagens igor/3.png")

        st.write("Nesse plot foi comparado a média total para cada classe social por ano.")
        st.write("E, como esperado, os alunos com classes sociais mais altas obtiveram uma nota média maior em relação as classes sociais mais baixas e essa tendência se manteve durante todos os anos.")
        st.write("Ademais, não parece existir um padrão claro, mas, em geral, as médias totais de 2020 e 2022 se mantiveram estáveis ou subiram em relação ao período de 2017-2019.")
        

    with st.container():
        st.write("---")
        st.image("imagens igor/4.png")

        st.write("Também foi gerado boxplots das notas de cada classe social. E também não foi possível")

        st.image("imagens igor/5.png")

        

    with st.container():
        st.write("---")

        st.subheader("Análise de Intervalos de Confiança utilizando Bootstrap\n\nCom limiar de significância de 5%")

        st.write("Foram gerados distribuições bootstrap das médias totais normalizadas para cada classe social em diferentes períodos (2017-2019, 2020 e 2022).")
        st.write("E, a partir deles, podemos inferir com 95% de certeza, a partir de sua análise visual, há diferenças estatisticamente significativas entre as médias dos períodos comparados (2017-2019 com 2020 e 2017-2019 com 2022), dado que nenhum intervalo de confiança se sobrepõe entre os períodos testados. Ou seja, posso dizer com 95% de confiança que essas médias são diferentes.")
        st.write("Além disso, é interessante observar que o intervalo de confiança é bem pequeno (4 casas decimais), isso se deve principalmente a nossa amostra ser a própria população e, consequentemnete, a lei dos grande números atua para esse intervalo ser quase que insignificante.")
        
        st.image("imagens igor/6.png")


    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.image("imagens igor/11.png")

    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.image("imagens igor/12.png")

    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.write("Resultados para 2017-2019:\n\nR2 (treino): 0.2399\n\nR2 (corpo): 0,2402\n\nMSE (treino): 0.0063\n\nMSE (caras): 0,0063\n\nMelhor valor de alpha encontrado na validação cruzada: 1.000000\n\nCoeficientes:\n\n  Classe Social A: 0.1687\n\n  Classe Social B: 0,1275\n\n  Classe Social C: 0,0894\n\n  Classe Social D: 0,0392\n\nInterceptação: 0,5340\n\n\n\n")
        st.write("---")
        st.write("Resultados para 2020:\n\nR2 (treino): 0.2434\n\nR2 (corpo): 0,2460\n\nMSE (treino): 0.0076\n\nMSE (caras): 0,0076\n\nMelhor valor de alpha encontrado na validação cruzada: 0.100000\n\nCoeficientes:\n\n  Classe Social A: 0.1713\n\n  Classe Social B: 0,1356\n\n  Classe Social C: 0,1013\n\n  Classe Social D: 0,0490\n\nInterceptação: 0,5387\n\n\n\n")
        st.write("---")
        st.write("Resultados para 2022:\n\nR2 (treino): 0.2255\n\nR2 (corpo): 0,2269\n\nMSE (treino): 0.0070\n\nMSE (caras): 0,0070\n\nMelhor valor de alpha encontrado na validação cruzada: 0.100000\n\nCoeficientes:\n\n  Classe Social A: 0.1557\n\n  Classe Social B: 0,1238\n\n  Classe Social C: 0,0915\n\n  Classe Social D: 0,0468\n\nInterceptação: 0,5490")

if opcode == "Treineiros":
    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.image("imagens igor/1.png")
