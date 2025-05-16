from crewai import Task

def create_cat_fact_task(agent):
    return Task(
        description="Descubra uma curiosidade interessante sobre gatos.",
        expected_output="Um fato curioso sobre gatos, com até 280 caracteres.",
        agent=agent, 
        verbose=True,
        output_file="output/catfact.txt"
    )


def create_color_palette_task(agent):
    return Task(
        description="Gere uma paleta de cores que combine com o humor de um dia ensolarado.",
        expected_output="Uma lista de 5 cores em RGB.",
        agent=agent,
        verbose=True,
        output_file="output/colorpallete.txt"
    )


def create_fruit_info_task(agent):
    return Task(
        description="Forneça informações nutricionais sobre a papaya.",
        expected_output="Tabela com calorias, açúcar, proteína e fibras da papaya.",
        agent=agent,
        verbose=True,
        output_file="output/fruitinfo.txt"
    )


def create_reflexao_sensorial_task(agent):
    return Task(
        description="Escreva uma reflexão filosófica e poética sobre a combinação de uma fruta, uma paleta de cores e um fato sobre gatos.",
        expected_output="Um parágrafo curto (máx. 500 caracteres) que explore os sentidos, emoções e significados ocultos dos dados fornecidos.",
        agent=agent,
        verbose=True,
        output_file="output/reflexaosensorial.txt"
    )