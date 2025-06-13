# 250613_pureba_codex
Primera prueba con Codex

## Uso

Se incluye el script `crew_scraper.py` que define un agente con [CrewAI](https://github.com/joaomdmoura/crewAI). Este agente utiliza la librería `BeautifulSoup` para extraer información de una página web. Para ejecutarlo:

```bash
python crew_scraper.py <url> <selector>
```

Por ejemplo, para obtener el título de `https://example.com`:

```bash
python crew_scraper.py https://example.com h1
```

Es posible que algunas URL no estén accesibles desde el entorno debido a restricciones de red.
