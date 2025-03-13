import click

@click.command()
@click.argument("input", type=click.File("r"), nargs=-1)
def cli(input):
    cols = 0
    words = 0
    bs = 0
    for f in input:
        lines = []
        while True:
            l = f.readline()
            if not l:
                break
            lines.append(l)
        c = 0
        w = 0
        b = 0
        sz = len(lines)

        for i in range(sz):
            c += 1
            w += len(lines[i].split())
            b += len(lines[i].encode('utf-8'))
            
        cols += c
        words += w
        bs += b
        if f.name != '<stdin>':
            bs += (c - 1)
            b += (c - 1)
            cols -= 1
            c -= 1
            click.echo(f" {c} {w} {b} {f.name}")
        else:
            click.echo(f" {c} {w} {b}")
    if len(input) > 1:
        click.echo(f" {cols} {words} {bs} total")       
if __name__ == "__main__":
    cli()
