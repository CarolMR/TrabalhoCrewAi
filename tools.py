from crewai.tools import BaseTool
import requests
from typing import Optional
import os

class FetchCatFactTool(BaseTool):
    name: str = "Cat Fact Fetcher"
    description: str = "Busca um fato curioso sobre gatos."

    def _run(self) -> str:
        response = requests.get("https://catfact.ninja/fact")
        return response.json().get("fact", "Fato não encontrado.")


class FetchColorPaletteTool(BaseTool):
    name: str = "Color Palette Generator"
    description: str = "Gera uma paleta de cores baseada em um estilo."

    def _run(self) -> str:
        data = {"model": "default"}
        response = requests.post("http://colormind.io/api/", json=data)
        colors = response.json().get("result", [])
        return str(colors)


class FetchFruitInfoTool(BaseTool):
    name: str = "Fruit Info Fetcher"
    description: str = "Busca informações nutricionais sobre uma fruta."

    def _run(self, _: str='') -> str:
        response = requests.get(f"https://www.fruityvice.com/api/fruit/papaya")
        return response.json()