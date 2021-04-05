from difflib import Differ
from pathlib import Path
from typing import Optional

import typer
from entitykb import Config
from entitykb.cli import commands, services
from ontologykb import cli

from .config import default_config

code_path = Path(__file__).parent
cache_path = code_path.parent.parent / "iiq"


@cli.command()
def bootstrap(
    root: Optional[Path] = typer.Option(None),
    dry_run: bool = typer.Option(False, "--dry-run"),
    wipe: bool = typer.Option(False, "--wipe"),
):
    """ Load HopeIQ local data store. """
    root = Config.get_root(root)
    typer.echo(f"Initializing kb: `{root}`")
    services.init_kb(root=root, exist_ok=True, config=default_config)

    if wipe:
        typer.echo(f"Clearing kb: `{root}`")
        commands.clear(root=root, force=True)

    igniteiq_jsonl = Path(__file__).parent.parent.parent / "iiq/igniteiq.jsonl"
    if not igniteiq_jsonl.exists():
        igniteiq_jsonl = Path("/data/iiq/igniteiq.jsonl")
        assert igniteiq_jsonl.exists(), "Could not find igniteiq.jsonl"

    commands.load(
        in_file=igniteiq_jsonl,
        root=root,
        file_format="jsonl",
        dry_run=dry_run,
        skip_reindex=True,
    )

    commands.load(
        in_file=code_path / "hope_ontologies.xlsx",
        root=root,
        file_format="ontologies",
        dry_run=dry_run,
        skip_reindex=True,
        is_binary=True,
    )

    # reindex
    if not dry_run:
        commands.reindex(root=root)


@cli.command()
def sync_config(root: Optional[Path] = typer.Option(None)):
    """ Update configuration while keeping the current Secret Key. """

    root = Config.get_root(root)
    config = Config.create(root=root)
    old_json = config.json(indent=4)
    typer.echo(f"Getting current config: {config.file_path}")

    # retain the secret key
    default_config.secret_key = config.secret_key

    # write the new config
    with config.file_path.open(mode="w") as fp:
        new_json = default_config.json(indent=4)
        fp.write(new_json)
        fp.write("\n")

    typer.echo(f"Config updated: {config.file_path}")
    diff_gen = Differ().compare(old_json.splitlines(), new_json.splitlines())
    typer.echo("\n".join(diff_gen))


if __name__ == "__main__":
    cli()
