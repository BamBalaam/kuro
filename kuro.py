import click
import os
import subprocess
from typing import Union


@click.command()
@click.option(
    "--diff",
    is_flag=True,
    help=(
        "Create a diff of the changes, in a 'kuro.diff' file. If"
        " you approve the changes, run kuro with --apply_diff."
    ),
)
@click.option(
    "--apply_diff",
    is_flag=True,
    help=("Consume (and delete) an existing 'kuro.diff' file."),
)
@click.option(
    "--project_options",
    is_flag=True,
    help=("Setup options for Kuro/Black on a directory level."),
)
@click.pass_context
def main(
    ctx: click.Context, diff: bool, apply_diff: bool, project_options: bool
) -> None:

    if project_options:
        create_kuro_config()
        ctx.exit(0)

    if diff and apply_diff:
        click.echo("\nYou can't use both --diff and --apply_diff")
        ctx.exit(1)

    if apply_diff:
        consume_diff()
        click.echo("\nDone!")
        ctx.exit(0)

    git_ls_files = (
        subprocess.check_output("git ls-files --modified --other *[.py]".split())
        .decode("utf-8")
        .replace("\n", " ")
    )

    click.echo("\nApplying Black to the following files: \n" + git_ls_files)

    BLACK_OPTIONS = check_setup()

    kuro_run_command = f"black {git_ls_files} -q"

    if BLACK_OPTIONS is not None:
        kuro_run_command += f" {BLACK_OPTIONS}"

    kuro_diff_command = kuro_run_command + " --diff"

    diff_text = subprocess.check_output(kuro_diff_command.split())

    if len(diff_text) == 0:
        click.echo("\nBlack returned no changes. Good for you!")
        ctx.exit(0)

    if diff:
        with open("kuro.diff", "w") as kuro_diff:
            kuro_diff.write(diff_text.decode("utf-8"))
        click.echo("\nWrote 'kuro.diff' file.")
        ctx.exit(0)

    subprocess.run(kuro_run_command.split())
    click.echo("\nDone!")
    ctx.exit(0)


def check_setup() -> Union[str, None]:
    exists = os.path.isfile(".kuro_config")
    if exists:
        # Use configuration file values
        click.echo("\nUsing the local configuration file...")
        with open(".kuro_config") as kuro_config:
            BLACK_OPTIONS = kuro_config.readline().strip()
            return BLACK_OPTIONS
    else:
        BLACK_OPTIONS = os.getenv("KURO_BLACK_OPTIONS")
        if BLACK_OPTIONS is not None:
            # Use global configuration values
            click.echo("\nUsing the global configuration settings...\n")
            return BLACK_OPTIONS
        else:
            # Run Black with no extra options
            return None


def create_kuro_config() -> None:
    options = click.prompt("Please enter the Black/Kuro options you desire to set")
    with open(".kuro_config", "w") as kuro_config:
        kuro_config.write(options)
    click.echo("\nLocal options for Kuro/Black set.")


def consume_diff() -> None:
    """
    click.echo("\nApplying diff file...")
    subprocess.call("patch -p0 < kuro.diff".split())
    os.remove("kuro.diff")
    """
    click.echo("\nThis option is a bit buggy at the moment... Please ignore it!")


if __name__ == "__main__":
    main()
