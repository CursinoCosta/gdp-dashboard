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

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.image("imagens igor/1.png")


    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.image("imagens igor/3.png")

    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.image("imagens igor/4.png")


    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.image("imagens igor/5.png")


    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

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

        st.write("Resultados para 2017-2019:\nR2 (treino): 0.2399\nR2 (corpo): 0,2402\nMSE (treino): 0.0063\nMSE (caras): 0,0063\nMelhor valor de alpha encontrado na validação cruzada: 1.000000\nCoeficientes:\n  Classe Social A: 0.1687\n  Classe Social B: 0,1275\n  Classe Social C: 0,0894\n  Classe Social D: 0,0392\nInterceptação: 0,5340\n\nResultados para 2020:\nR2 (treino): 0.2434\nR2 (corpo): 0,2460\nMSE (treino): 0.0076\nMSE (caras): 0,0076\nMelhor valor de alpha encontrado na validação cruzada: 0.100000\nCoeficientes:\n  Classe Social A: 0.1713\n  Classe Social B: 0,1356\n  Classe Social C: 0,1013\n  Classe Social D: 0,0490\nInterceptação: 0,5387\n\nResultados para 2022:\nR2 (treino): 0.2255\nR2 (corpo): 0,2269\nMSE (treino): 0.0070\nMSE (caras): 0,0070\nMelhor valor de alpha encontrado na validação cruzada: 0.100000\nCoeficientes:\n  Classe Social A: 0.1557\n  Classe Social B: 0,1238\n  Classe Social C: 0,0915\n  Classe Social D: 0,0468\nInterceptação: 0,5490")



if opcode == "Treineiros":
    with st.container():
        st.write("---")

        st.write("Vemos inicialmente a comparação das taxas populacionais e taxas de inscrição por região.")

        st.image("imagens igor/1.png")
