import click

from osint_cli.modules.domain_recon import get_dns_records


@click.group()
def cli():
    """OSINT CLI - A command-line interface for Open Source Intelligence tools."""


@cli.command()
@click.argument("target")
def domain(target):
    results = get_dns_records(target)
    click.echo(f"DNS records for {target}:")
    for rtype, records in results.items():
        click.echo(f"{rtype} records: {', '.join(records) if records else 'None'}")


if __name__ == "__main__":
    cli()
