import click

@click.command()
@click.argument("input", type=click.File("r"), nargs=-1)
def cli(input):
    for f in input:
        lines = []
        while True:
            l = f.readline()
            if not l:
                break
            lines.append(l)
        pos = 0
        sz = len(lines)
        if f.name == '<stdin>':
            pos = max(0, sz - 17)
        else:
            pos = max(0, sz - 10)
        if len(input) > 1:
            click.echo(f"==> {f.name} <==")
        for i in range(pos, sz):
            click.echo(f"{lines[i].strip()}")
            
if __name__ == "__main__":
    cli()
