import typer
from topwing import project_builder



def create_cli():
    cli = typer.Typer()

    project_builder_cli = typer.Typer()

    for command in project_builder.get_commands():
        project_builder_cli.command()(command)

    cli.add_typer(project_builder_cli, name='project')
    return cli


cli = create_cli()
