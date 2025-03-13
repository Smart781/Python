import click

@click.command()
@click.argument("input", type=click.File("r"), nargs=-1)
def cli(input):
    for f in input:
        pos_str = 0
        lines = []
        while True:
            l = f.readline()
            if not l:
                break
            pos_str += 1
            line = str(pos_str) + " " + l
            lines.append(line)
        for line in lines:
            click.echo(f"{line.strip()}")
            
if __name__ == "__main__":
    cli()
