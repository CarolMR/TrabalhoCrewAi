# 🌈 SensiCrew: Exploradores dos Sentidos

**SensiCrew** é um projeto interativo baseado em agentes inteligentes com personalidades distintas, cada um com uma missão sensorial única. Os agentes utilizam LLMs e APIs para coletar e transformar dados sobre frutas, cores, gatos e percepções em reflexões poéticas e criativas.

## 🚀 Objetivo

Criar uma experiência divertida e criativa que explora o mundo das frutas, cores e gatos — e os transforma em histórias, combinações, sugestões e reflexões filosóficas sensoriais.

---

## 🧠 Tecnologias Utilizadas

- **[CrewAI](https://github.com/joaomdmoura/crewAI)**: Estrutura para criar agentes com LLMs e múltiplas ferramentas.
- **[LiteLLM](https://github.com/BerriAI/litellm)**: Abstração para chamadas a diferentes provedores de LLM.
- **Python 3.11.5**

---

## 🌐 APIs Utilizadas

| API                  | Finalidade                                                   |
|----------------------|--------------------------------------------------------------|
| [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/)     | Fornecer curiosidades sobre gatos.                        |
| [Fruityvice API](https://www.fruityvice.com/)                    | Obter dados nutricionais e características de frutas.     |
| [Colormind API](http://colormind.io/api-access/)                | Gerar combinações de paletas de cores.                    |

---

## 🤖 Agentes

### 🍇 Nutricionista de Frutas
- **Objetivo**: Informar dados nutricionais detalhados de frutas.
- **Ferramenta**: Fruityvice API.

### 🐱 Curioso Felino
- **Objetivo**: Compartilhar fatos interessantes sobre gatos.
- **Ferramenta**: Cat Facts API.

### 🎨 Designer de Paletas
- **Objetivo**: Sugerir paletas de cores baseadas em inspiração aleatória ou temas.
- **Ferramenta**: Colormind API.

### 🧘 Filósofo Sensorial
- **Objetivo**: Usando somente o LLM, compõe reflexões poéticas e filosóficas baseadas nas respostas dos demais agentes.
- **Ferramenta**: Nenhuma — apenas o poder da linguagem.

---

## 🧩 Tarefas

- Obter informações nutricionais de frutas.
- Compartilhar curiosidades felinas.
- Sugerir uma paleta de cores harmoniosa.
- Criar uma reflexão filosófica sensorial que una todos os dados.