#!/usr/bin/env python
import warnings
from datetime import datetime

from lab01.crew import Lab01

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "Observabilidade e análise de incidentes com AIOps",
        "incidente": """
        API de pagamentos apresentou aumento de latência entre 10h05 e 10h40.
        Houve crescimento de erros HTTP 500.
        A ferramenta de observabilidade indicou degradação no serviço de autenticação.
        """,
        "current_year": str(datetime.now().year)
    }

    try:
        result = Lab01().crew().kickoff(inputs=inputs)
        print(result)

        with open("relatorio_rca.md", "w", encoding="utf-8") as file:
        file.write(str(result))

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()
