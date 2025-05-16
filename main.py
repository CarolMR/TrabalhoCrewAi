from crewai import Crew
from agents import *
from tasks import *
from dotenv import load_dotenv

load_dotenv()
create_curador_agent=create_curador_felino_agent()
create_designer_agent=create_designer_paleta_agent()
create_nutricionista_agent=create_nutricionista_frutal_agent()
create_filosofo_agent=create_filosofo_sensorial_agent()

task1=create_cat_fact_task(create_curador_agent)
task2=create_color_palette_task(create_designer_agent)
task3=create_fruit_info_task(create_nutricionista_agent)
task4=create_reflexao_sensorial_task(create_filosofo_agent)

crew = Crew(
    agents=[create_curador_agent, create_designer_agent, create_nutricionista_agent, create_filosofo_agent],

    tasks=[task1, task2, task3, task4],

    verbose=True,
)

print("Iniciando")

resultado= crew.kickoff()

print(resultado)