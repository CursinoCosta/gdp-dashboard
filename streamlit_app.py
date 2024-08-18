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

    st.write("GRUPO 1")
    st.write("INTEGRANTES:")
    st.write("Igor Novais- 2022423407")
    st.write("Julia Paes- 2021032137    ")
    st.write("Mateus Costa- 2022043191")

    st.title("Perguntas")

    st.write("INTRODUÇÃO AO TRABALHO")

    st.write("Link para o Colab completo [Clique aqui](https://colab.research.google.com/drive/15goBpe5qIkR6YMtf1wXbw7RQvcO6cHYN#scrollTo=PIIVBkMm-Qm4)")

    opcode = st.selectbox("Selecione a análise", ["Taxa Populacional", "Aulas Online", "Treineiros"])
if opcode == "Taxa Populacional":
    
    with st.container():
        st.subheader("A taxa de inscritos por região é proporcional a taxa populacional por região?")
        st.write("---")

        st.write("Primeiro plot, ele trás a análise comparativa entre a taxa populacional e a taxa de incrição em cada região do país, percebe-se diferença entre ambas. A diferêça se assentua especialmente após a pandemia.")

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


        st.write("Concluimos então que taxa populacional e de inscrição estão interligados, mas não, necessariamente, são proporcionais. Há fatores externos que influenciam nesses valores, uma possível hipótese são os fatores culturais como o histórico da importância dos vestibulares que existe no Nordeste ou a cultura de empreendedorismo e oportunidade de emprego no Sudeste, especialmente em São Paulo que pode levar a menos pessoas procurarem uma faculdade por lá.")





if opcode == "Aulas Online":
    with st.container():
        st.subheader("Como as aulas onlines afetaram as notas do ENEM para cada faixa de renda durante a pandemia?")
        st.write("---")

        st.subheader("Limpeza e organização dos dados\n\nAnteriormente, a base de dados possuia muitas colunas, mas, para fins de otimizações das operações feitas no dataframe, foram selecionados apenas as colunas:")
        st.write("- TP_ST_CONCLUSAO = 2: Conclusão do Ensino Médio no mesmo ano da aplicação do exame")
        st.write("- TP_PRESENCA_MT = 1: Presença na prova de Matemática")
        st.write("- TP_PRESENCA_CN = 1: Presença na prova de Ciências da Natureza")
        st.write("- TP_PRESENCA_LC = 1: Presença na prova de Linguagens")
        st.write("- TP_PRESENCA_CH = 1: Presença na prova de Ciências Humanas")
        st.write("Dessa forma, os resultados da base não serão influenciados por alunos que faltaram em alguma prova ou que já tiveram anteriormente a oportunidade de fazer o terceiro ano do Ensino Médio sem a pandemia.")
        st.write("Além disso, também foi feito o mapeamento das 18 faixas de renda existentes para apenas 5 classes sociais diferentes (A, B, C, D, E) em que a classe social A possui mais recursos financeiros.")
        st.write("### Classe E = 0 até 1 salário mínimo.")
        st.write("### Classe D = 1 até 3 salários mínimos.")
        st.write("### Classe C = 3 até 6 salários mínimos.")
        st.write("### CLasse B = 6 até 10 salários mínimos.")
        st.write("### Classe A = 10 até 20 salários mínimos.")
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


        st.subheader("Testes de Hipótese e Intervalo de Confiança utilizando Teste de Permutação")
        st.write("Testes de Hipótese e Intervalo de Confiança utilizando Teste de Permutação")
        st.write("Ha: Média total da Classe X em 2017-2019 !=  Média total da Classe X em 2020 (Durante a pandemia)")
        st.write("Com limiar de significância de 5%")
        st.write("H0: Média total da Classe X em 2017-2019  =  Média total da Classe X em 2022 (Após a pandemia)")
        st.write("Ha: Média total da Classe X em 2017-2019 !=  Média total da Classe X em 2022 (Após a pandemia)")
        st.write("Com limiar de significância de 5%")
        st.write("Também foi feito testes de permutações e em todas resultaram na rejeição das hipóteses nulas (de que as médias dos anos comparados foram iguais) a um nível de significância de 5%. Isso fornece fortes evidências estatísticas de que há diferenças significativas entre as médias dos períodos comparados para cada classe social.")

        st.write("Classe Social A:")
        st.write("  2017_2019_vs_2020: Rejeitar H0 = True")
        st.write("  2017_2019_vs_2022: Rejeitar H0 = True")
        st.write("--")
        st.write("Classe Social B:")
        st.write("  2017_2019_vs_2020: Rejeitar H0 = True")
        st.write("  2017_2019_vs_2022: Rejeitar H0 = True")
        st.write("--")
        st.write("Classe Social C:")
        st.write("  2017_2019_vs_2020: Rejeitar H0 = True")
        st.write("  2017_2019_vs_2022: Rejeitar H0 = True")
        st.write("Classe Social D:")
        st.write("  2017_2019_vs_2020: Rejeitar H0 = True")
        st.write("2017_2019_vs_2022: Rejeitar H0 = True")
        st.write("--")
        st.write("Classe Social E:")
        st.write("2017_2019_vs_2020: Rejeitar H0 = True")
        st.write(" 2017_2019_vs_2022: Rejeitar H0 = True")
        st.write("--")


    with st.container():
        st.write("---")

        st.subheader("Regressão Linear")

        st.write("Primeiro foi aplicado o One-Hot-Encondign para a variável categórica de Classe Social para ser possível fazer a regressão.")
        st.write("Para a regressão foi utilizado o algoritmo do RidgeRegression.")


        st.write("Resultados para 2017-2019:\n\nR2 (treino): 0.2399\n\nR2 (corpo): 0,2402\n\nMSE (treino): 0.0063\n\nMSE (caras): 0,0063\n\nMelhor valor de alpha encontrado na validação cruzada: 1.000000\n\nCoeficientes:\n\n  Classe Social A: 0.1687\n\n  Classe Social B: 0,1275\n\n  Classe Social C: 0,0894\n\n  Classe Social D: 0,0392\n\nInterceptação: 0,5340\n\n\n\n")
        st.write("---")
        st.write("Resultados para 2020:\n\nR2 (treino): 0.2434\n\nR2 (corpo): 0,2460\n\nMSE (treino): 0.0076\n\nMSE (caras): 0,0076\n\nMelhor valor de alpha encontrado na validação cruzada: 0.100000\n\nCoeficientes:\n\n  Classe Social A: 0.1713\n\n  Classe Social B: 0,1356\n\n  Classe Social C: 0,1013\n\n  Classe Social D: 0,0490\n\nInterceptação: 0,5387\n\n\n\n")
        st.write("---")
        st.write("Resultados para 2022:\n\nR2 (treino): 0.2255\n\nR2 (corpo): 0,2269\n\nMSE (treino): 0.0070\n\nMSE (caras): 0,0070\n\nMelhor valor de alpha encontrado na validação cruzada: 0.100000\n\nCoeficientes:\n\n  Classe Social A: 0.1557\n\n  Classe Social B: 0,1238\n\n  Classe Social C: 0,0915\n\n  Classe Social D: 0,0468\n\nInterceptação: 0,5490")

        st.write("O modelo teve um poder explicativo um pouco maior em 2020 (R² = 0.2460) comparado a 2017-2019 (R² = 0.2402) e 2022 (R² = 0.2269), ou seja, indica que a relação entre classe social e a nota média no ENEM foi um pouco maior durante o pico da pandemia (2020).")
        st.write("Mas, de qualquer forma, os valores R² não foram altos em todos os períodos analisados, ou seja, a classe social sozinha só explicou cerca de 22.69% - 24.60% da variação da nota do ENEM.")
        st.write("Ademais, o Erro-Quadrático-Médio foi muito pequeno para todos os nossos testes. Isso se deve ao fato de que, como dito anteriormente, a nossa amostra é a nossa própria população. Logo, a lei dos grande números atua para esse intervalo ser quase que insignificante.")
        
        
        st.image("imagens igor/11.png")

    with st.container():
        st.write("---")

        st.write("Além disso, os coeficientes das classes sociais mostram que as classes sociais mais alta estão associadas a notas medias mais altas no ENEM.")
        st.write("Ademais, para todas as classes sociais ocorreu um aumento nos coeficientes de 2020 em relação ao período de 2017-2019, mas esse aumento foi ainda mais relevante para as classes sociais mais baixas.")
        st.write("Uma possível explicação para isso ter acontecido é que, durante a pandemia, os alunos, principalmente de classes sociais mais baixas (que tinham um acesso de educação de menos qualidade) sabiam que não estavam preparados para a prova e, consequentemente, desistiram de ir fazer a prova. Dessa forma, as notas das classes sociais foi aumentada de forma artificial.")
        st.write("Ademais, em 2022 houve uma diminuição nos coeficientes para todas as classes sociais em comparação com 2020, voltando a um pouco mais próximos em relação ao período de 2017-2019.")

        st.image("imagens igor/12.png")

        st.write("Com base em todos esses resultados obtidos, podemos concluir que as aulas online durante a pandemia afetaram as notas do ENEM. No entanto, diferente do que era esperado, as notas do ENEM subiram durante a pandemia. Como dito anteriormente, uma possível explicação para isso ter ocorrido foi que mais alunos sabiam que não estavam preparados por conta da má qualidade do ensino remoto, logo preferiram se absterem de fazer a prova. Com isso,  as notas aumentaram de forma artificial.")
        




if opcode == "Treineiros":
    with st.container():
        st.subheader("Fazer o ENEM como treineiro ajuda a melhorar a nota?")
        st.write("---")

        st.subheader("Analisando notas dos treineiros e não treineiros para cada ano analisado")

        st.write("As curvas de probabilidade se diferiram mais nos anos antes da pandemia (2017-2019) do que nos anos durante e imediatamente após ela (2020 e 2022). Antes da pandemia, a curva dos treineiros era deslocada na direção de maiores notas. O teste de hipótese aclarará essa aparente observação.")

        st.image("imagens julia/1.png")


    with st.container():
        st.write("---")

        st.subheader("Teste de hipótese")

        st.write("Usando bootstrap vamos comparar a diferença das médias das notas entre treineiros e não treineiros a cada ano e concluir se temos dados para aceitar ou rejeitar a hipótese de que não faz diferença fazer o ENEM apenas como teste em termos de nota (hipótese nula).")

        st.image("imagens julia/2.png")

        st.write("Podemos observar que:")
        st.write("1. Antes da pandemia (2017 - 2019) a diferença das notas não incluiu o zero, apesar de muito pequena em 2019, contudo, surpreendentemente, os treineiros tiraram maiores notas do que os não treineiros, o que poderia ser explicado pelo fato de a população dos treineiros se inserir em um contexto de maior preparação do que a média da população dos não treineiros. A hipótese nula, pois, não pode ser aceita nesse caso.")
        st.write("2. Depois da pandemia (2020 e 2022), a diferença entre as médias das notas de treineiros e não treineiros foi irrisória. A hipótese nula é cabível, principalmente no caso de 2022 (cenário pós-pandêmico), em que o zero está no intervalo de confiança. Isso é diferente do esperado, mas provavelmente se dá, pois os universos de pessoas que fazem e não fazem o ENEM como treineiras são influenciados por outras variáveis essa. De fato, em todos os anos, como se pode ver no tamanho das populações, há uma considerável maior quantidade de pessoas que fazem o ENEM como não treineiras, e é provável que nem todas essas pessoas tenham feito o ENEM antes para testarem os seus conhecimentos.")

        st.write("Uma explicação plausível para isso, pensando em experiências pessoais e em conversas com amigos, é a de que as pessoas que costumam fazer o ENEM como treineiras tendem a ser aquelas que se preparam para a prova com maior dedicação, então a média de suas notas tende a ser 'mais alta' do que o esperado.")
        st.write("Já a grande população que faz o ENEM 'para valer' engloba tanto os que já se preparavam há mais tempo e, pois, tiram boa notas, quanto os que não havido sido tão bem preparados para a prova, o que não eleva muito a média geral.")
        st.write("Nesse caso, apenas com esses dados - e sem a possibilidade de identificar exatamente as pessoas que fizeram como treineiras antes e depois refizeram a prova no ano de seu vestibular, para de fato ter uma noção embasada da influência dessa variável -, a hipótese nula é aceita.")
        st.write("Assim, apenas com essa análise superficial (pelos motivos citados acima), não faz diferença fazer o ENEM antes do ano do vestibular no cenário pós pandemia. Contudo, veremos que essa conclusão continua incerta quando aplicamos a regressão linear.")


    with st.container():
        st.write("---")
        st.subheader("Regressão Linear")


        st.image("imagens julia/3.png")
        st.image("imagens julia/4.png")

        st.write("Os resultados da regressão corroboram as conclusões tiradas na sessão anterior. Os intervalos de confiança da constante e dos coeficientes de treino, que medem a influência de ser treineiro na média das notas, continuam indicando um discreto decréscimo de nota nos anos antes da pandemia e irrisório nos anos pós pandemia. Observa-se, ainda, que os MSEs são muito altos em todos os casos, o que frisa a ideia de que a relação entre essas variáveis não é bem prevista apenas com essa análise.")
        st.write("De fato, já tínhamos chegado à conclusão de que mais variáveis afetam as notas de treineiros e não treineiros, sendo essa visualização isoladamente insuficiente para caracterizar de fato a influência que existe na nota final que um aluno obtém no ENEM de seu vestibular se ele fez a prova antes como treineiro.")
