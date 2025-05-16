from crewai import Agent
from config import get_llm
from tools import FetchCatFactTool, FetchColorPaletteTool, FetchFruitInfoTool


def create_curador_felino_agent():
    return Agent(
        role="Curador Felino",
        goal="Descobrir e compartilhar curiosidades fascinantes sobre gatos",
        backstory="Um amante de gatos que dedica sua vida a colecionar curiosidades sobre esses seres místicos.",
        tools=[FetchCatFactTool()],
        verbose=True,
        llm=get_llm(),
    )


def create_designer_paleta_agent():
    return Agent(
        role="Designer de Paleta",
        goal="Criar combinações de cores harmoniosas e visualmente impactantes",
        backstory="Um artista digital especializado em paletas de cores modernas para web e design.",
        tools=[FetchColorPaletteTool()],
        verbose=True,
        llm=get_llm(),
    )


def create_nutricionista_frutal_agent():
    return Agent(
        role="Nutricionista Frutal",
        goal="Fornecer dados nutricionais úteis e curiosos sobre frutas",
        backstory="Um entusiasta da alimentação saudável, apaixonado por frutas e seus benefícios.",
        tools=[FetchFruitInfoTool()],
        verbose=True,
        llm=get_llm(),
    )


def create_filosofo_sensorial_agent():
    return Agent(
        role="Filósofo Sensorial",
        goal="Refletir poeticamente e filosoficamente sobre os dados sensoriais (cores, sabores, sentimentos felinos) em até 500 caracteres.",
        backstory="Um pensador introspectivo treinado nas montanhas para transformar percepções sensoriais em sabedoria.",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )