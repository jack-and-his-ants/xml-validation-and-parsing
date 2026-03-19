import typer
from .parse import parse_xml_to_json
from .validate import is_valid_xml

app = typer.Typer()

@app.command()
def validate(xml:str,xsd:str):
    """Validate XML file against XSD (XML Schema)."""
    if is_valid_xml(xml,xsd):
        typer.secho(f"{xml} is valid.", fg=typer.colors.GREEN)
    else:
        typer.secho(f"{xml} is invalid.", fg=typer.colors.RED)

@app.command()
def parse(xml:str,dest:str):
    """Parse XML file into JSON."""
    parse_xml_to_json(xml,dest)
    print(f"Saved {xml} to {dest}.")

if __name__ == "__main__":
    app()
