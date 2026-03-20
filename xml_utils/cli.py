import typer
from .parse import parse_xml_to_json
from .validate import is_valid_xml
from lxml import etree

app = typer.Typer(help="XML validation and parsing tool",no_args_is_help=True)

@app.command()
def validate(xml:str,
             xsd:str,
             verbose: bool = typer.Option(False,'--verbose','-v',help="Show additional info about the operation")
             ):
    """Validate XML file against XSD (XML Schema)."""
    if verbose:
        typer.echo(f"Validating '{xml}' against '{xsd}'.")
    try:
        if is_valid_xml(xml,xsd):
            typer.secho(f"'{xml}' is valid.", fg=typer.colors.GREEN)
        else:
            typer.secho(f"'{xml}' is invalid.", fg=typer.colors.RED)
    except OSError:
        typer.secho("File not found.",fg = typer.colors.RED)
        raise typer.Exit(code = 1)
    except etree.XMLSyntaxError as e:
        typer.secho(f"Invalid XML syntax: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.secho(f"Unexpected error: {e}",fg=typer.colors.RED)
        raise typer.Exit(code=1)


@app.command()
def parse(xml:str,
          dest:str,
          verbose: bool = typer.Option(False,'--verbose','-v',help="Show additional info about the operation")
          ):
    """Parse XML file into JSON."""
    if verbose:
        typer.echo(f"Parsing '{xml}' into '{dest}'.")
    try:
        parse_xml_to_json(xml,dest)
        typer.secho(f"Saved '{xml}' to '{dest}'.",fg=typer.colors.BLUE)
    except OSError:
        typer.secho("File error.",fg = typer.colors.RED)
        raise typer.Exit(code = 1)
    except etree.XMLSyntaxError as e:
        typer.secho(f"Invalid XML syntax: {e}",fg = typer.colors.RED)
        raise typer.Exit(code = 1)
    except Exception as e:
        typer.secho(f"Unexpected error: {e}",fg = typer.colors.RED)
        raise typer.Exit(code = 1)
        


if __name__ == "__main__":
    app()
