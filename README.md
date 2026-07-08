# Engenharia-de-Prompt

## Informações relevantes de Engenharia de Prompt:

- **Resumo (Summarizing):**<br>
Não peça apenas "resuma". Peça "resuma focado em [X] para o público [Y], limitando a [Z] palavras". Isso é o que a gestão espera de um relatório técnico.

- **Inferência (Inferring):**<br>
Use o modelo para extrair dados estruturados de textos não estruturados. Exemplo: **"Extraia o sentimento e os temas principais do log de erro abaixo e formate como JSON".** Isso é puro dia a dia de sustentação.

- **Transformação (Transforming):**<br>
O modelo é um tradutor universal de formatos. Use para mudar o tom de uma mensagem (de técnico para executivo) ou traduzir logs de formato cru para relatórios amigáveis.

- **Expansão (Expanding):**<br>
Use para gerar rascunhos de e-mails, documentação técnica ou respostas a clientes, sempre dando o contexto e o "tom de voz" desejado.

---
## A Regra de Ouro:

- **Seja Específico:** <br>
Defina o ângulo (ex: "foque nos aspectos científicos e no impacto do teste de Turing").

- **Delimitadores:** <br>
Use sinais para separar a instrução do conteúdo que será processado. Isso evita que o modelo se confunda.

- **Exemplos:** **""", ---, < >, ###.**

**Uso:** <br>
"Resuma o texto delimitado por triplas aspas: **""" {seu_texto} """".**

---

## O Processo Iterativo (O Método de Elite)
Ninguém acerta o prompt de primeira. O curso ensina que o prompt é código, e como todo código, precisa de refatoração.

## O Ciclo de Refatoração:

- **Escreva o primeiro prompt:** <br>
Tente ser claro e dar delimitadores.

- **Analise o resultado:** <br>
Onde ele falhou? Foi prolixo demais? Faltou dado técnico?

- **Refine a instrução:** <br>
Não mude o texto todo; adicione uma restrição ou clarifique o formato.

- **Repita:** <br>
Até que o output seja consistente.

---


