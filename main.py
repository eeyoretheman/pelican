import click
from PIL import Image


@click.command()
@click.option(
    "--width",
    "-w",
    default=5000,
    help="The width of the generated image, measured in pixels.",
)
@click.option(
    "--height",
    "-h",
    default=100,
    help="The height of the generated image, measured in pixels.",
)
@click.option(
    "--depth",
    "-d",
    default=2,
)
@click.option(
    "--marks",
    "-m",
    nargs=3,
    default=[[0.1, 5, 60], [0.05, 3, 45]],
    multiple=True,
)
@click.option(
    "--mark-height",
    "-H",
    default=30
)
@click.option(
    "--mark-width",
    "-W",
    default=1
)
@click.argument("scale")
@click.argument("filepath")
def main(width, height, depth, marks, mark_height, mark_width, scale, filepath):
    with (
        Image.new(mode="1", size=(width, height), color=1) as image,
        open(filepath, "wb") as file,
    ):
        for i in range(1, 10**depth):
            match scale:
                case "linear":
                    d = round((i / (10**depth)) * width)
                    
                    current_mark_width = mark_width
                    current_mark_height = mark_height
                    
                    for mark_modulo, custom_width, custom_height in marks:
                        if i % round(mark_modulo * (10**depth)) == 0:
                            current_mark_width = custom_width
                            current_mark_height = custom_height
                            
                            break
                            
                    
                    for x in range((-current_mark_width)//2 + 1, current_mark_width//2 + 1):
                        for y in range(current_mark_height):
                            image.putpixel((d + x, y), 0)

        image.save(file)

if __name__ == "__main__":
    main()
