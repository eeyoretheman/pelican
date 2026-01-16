from PIL import Image, ImageFont, ImageDraw
from math import log10

def main():
    # 600 DPI
    # 6378 pixels ~ 270mm
    # 945 pixels ~ 40mm
    # 236 pixels ~ 10mm
    # 47 pixels ~ 2mm
    # 3 pixels ~ 0.125mm

    WIDTH = 2953
    HEIGHT = 473
    MARGIN = 118
    MARK_HEIGHT = 24
    MARK_WIDTH = 3

    FONT = ImageFont.truetype("/usr/share/fonts/truetype/hack/Hack-Regular.ttf", 32)

    with (
        Image.new("RGB", (WIDTH, HEIGHT), color="#FFFFFF") as mannheim_image,
        open("mannheim.png", "wb") as mannheim_file
    ):
        # Black border around scale

        for x in range(0, WIDTH):
            mannheim_image.putpixel((x, 0), (0, 0, 0))
            mannheim_image.putpixel((x, HEIGHT-1), (0, 0, 0))

        for y in range(0, HEIGHT):
            mannheim_image.putpixel((0, y), (0, 0, 0))
            mannheim_image.putpixel((WIDTH-1, y), (0, 0, 0))

        for n in range(0, 4):
            for x in range(0, WIDTH):
                mannheim_image.putpixel((x, n * MARGIN), (0, 0, 0))

        for y in range(0, HEIGHT):
            mannheim_image.putpixel((MARGIN, y), (0, 0, 0))
            mannheim_image.putpixel((WIDTH-1-MARGIN, y), (0, 0, 0))

        mannheim_drawable = ImageDraw.Draw(mannheim_image)

        for x in range(10, 1000):
            label_offset = 18
            mark_number = True

            if x == 10:
                mark_height = MARK_HEIGHT*3
                mark_width = MARK_WIDTH*2
                mark_number = True
                label_offset = -4
            elif x > 100:
                if x % 100 == 0:
                    mark_height = MARK_HEIGHT*3
                    mark_width = MARK_WIDTH
                elif x % 50 == 0:
                    mark_height = MARK_HEIGHT*2
                    mark_width = MARK_WIDTH
                elif x % 10 == 0:
                    mark_height = MARK_HEIGHT
                    mark_width = MARK_WIDTH // 2
                    mark_number = False
                else:
                    mark_height = 0
                    mark_width = 0
                    mark_number = False
            else:
                if x % 10 == 0:
                    mark_height = MARK_HEIGHT*3
                    mark_width = MARK_WIDTH
                elif x % 5 == 0:
                    mark_height = MARK_HEIGHT*2
                    mark_width = MARK_WIDTH
                    mark_number = False
                else:
                    mark_height = MARK_HEIGHT
                    mark_width = MARK_WIDTH // 2
                    mark_number = False

            print(mark_height, mark_width, x)

            x /= 10

            f = log10(x)/2

            d = MARGIN + round(f * (WIDTH - 2 * MARGIN))

            for y in range(mark_height):
                for w in range(-mark_width//2 + 1, mark_width//2 + 1):
                    if d + w >= WIDTH-MARGIN or d + w < MARGIN:
                        continue

                    mannheim_image.putpixel((d + w, MARGIN - y), (0, 0, 0))

            if mark_number:
                mannheim_drawable.text((d-label_offset, (MARGIN-mark_height-32)), f"{x:02.0f}", fill=(0, 0, 0), font=FONT)

        for x in range(10, 1000):
            label_offset = 18
            mark_number = True

            if x == 10:
                mark_height = MARK_HEIGHT*3
                mark_width = MARK_WIDTH*2
                mark_number = True
                label_offset = -4
            elif x > 100:
                if x % 100 == 0:
                    mark_height = MARK_HEIGHT*3
                    mark_width = MARK_WIDTH
                elif x % 50 == 0:
                    mark_height = MARK_HEIGHT*2
                    mark_width = MARK_WIDTH
                elif x % 10 == 0:
                    mark_height = MARK_HEIGHT
                    mark_width = MARK_WIDTH // 2
                    mark_number = False
                else:
                    mark_height = 0
                    mark_width = 0
                    mark_number = False
            else:
                if x % 10 == 0:
                    mark_height = MARK_HEIGHT*3
                    mark_width = MARK_WIDTH
                elif x % 5 == 0:
                    mark_height = MARK_HEIGHT*2
                    mark_width = MARK_WIDTH
                    mark_number = False
                else:
                    mark_height = MARK_HEIGHT
                    mark_width = MARK_WIDTH // 2
                    mark_number = False

            print(mark_height, mark_width, x)

            x /= 10

            f = log10(x)/2

            d = MARGIN + round(f * (WIDTH - 2 * MARGIN))

            for y in range(MARGIN, MARGIN+mark_height):
                for w in range(-mark_width//2 + 1, mark_width//2 + 1):
                    if d + w >= WIDTH-MARGIN or d + w < MARGIN:
                        continue

                    mannheim_image.putpixel((d + w, y), (0, 0, 0))

            if mark_number:
                mannheim_drawable.text((d-label_offset, (MARGIN+mark_height)), f"{x:02.0f}", fill=(0, 0, 0), font=FONT)

        for x in range(10, 100):
            label_offset = 18
            mark_number = True

            if x == 10:
                mark_height = MARK_HEIGHT*3
                mark_width = MARK_WIDTH*2
                mark_number = True
                label_offset = -4
            elif x > 100:
                if x % 100 == 0:
                    mark_height = MARK_HEIGHT*3
                    mark_width = MARK_WIDTH
                elif x % 50 == 0:
                    mark_height = MARK_HEIGHT*2
                    mark_width = MARK_WIDTH
                elif x % 10 == 0:
                    mark_height = MARK_HEIGHT
                    mark_width = MARK_WIDTH // 2
                    mark_number = False
                else:
                    mark_height = 0
                    mark_width = 0
                    mark_number = False
            else:
                if x % 10 == 0:
                    mark_height = MARK_HEIGHT*3
                    mark_width = MARK_WIDTH
                elif x % 5 == 0:
                    mark_height = MARK_HEIGHT*2
                    mark_width = MARK_WIDTH
                    mark_number = False
                else:
                    mark_height = MARK_HEIGHT
                    mark_width = MARK_WIDTH // 2
                    mark_number = False

            print(mark_height, mark_width, x)

            x /= 10

            f = log10(x)

            d = MARGIN + round(f * (WIDTH - 2 * MARGIN))

            for y in range(mark_height):
                for w in range(-mark_width//2 + 1, mark_width//2 + 1):
                    if d + w >= WIDTH-MARGIN or d + w < MARGIN:
                        continue

                    mannheim_image.putpixel((d + w, 3*MARGIN-y), (0, 0, 0))

            if mark_number:
                mannheim_drawable.text((d-label_offset, (3*MARGIN-mark_height-32)), f"{x:02.0f}", fill=(0, 0, 0), font=FONT)

        for x in range(10, 100):
            label_offset = 18
            mark_number = True

            if x == 10:
                mark_height = MARK_HEIGHT*3
                mark_width = MARK_WIDTH*2
                mark_number = True
                label_offset = -4
            elif x > 100:
                if x % 100 == 0:
                    mark_height = MARK_HEIGHT*3
                    mark_width = MARK_WIDTH
                elif x % 50 == 0:
                    mark_height = MARK_HEIGHT*2
                    mark_width = MARK_WIDTH
                elif x % 10 == 0:
                    mark_height = MARK_HEIGHT
                    mark_width = MARK_WIDTH // 2
                    mark_number = False
                else:
                    mark_height = 0
                    mark_width = 0
                    mark_number = False
            else:
                if x % 10 == 0:
                    mark_height = MARK_HEIGHT*3
                    mark_width = MARK_WIDTH
                elif x % 5 == 0:
                    mark_height = MARK_HEIGHT*2
                    mark_width = MARK_WIDTH
                    mark_number = False
                else:
                    mark_height = MARK_HEIGHT
                    mark_width = MARK_WIDTH // 2
                    mark_number = False

            print(mark_height, mark_width, x)

            x /= 10

            f = log10(x)

            d = MARGIN + round(f * (WIDTH - 2 * MARGIN))

            for y in range(mark_height):
                for w in range(-mark_width//2 + 1, mark_width//2 + 1):
                    if d + w >= WIDTH-MARGIN or d + w < MARGIN:
                        continue

                    mannheim_image.putpixel((d + w, 3*MARGIN+y), (0, 0, 0))

            if mark_number:
                mannheim_drawable.text((d-label_offset, (3*MARGIN+mark_height)), f"{x:02.0f}", fill=(0, 0, 0), font=FONT)

        FONT = ImageFont.truetype("/usr/share/fonts/truetype/hack/Hack-Regular.ttf", 96)

        mannheim_drawable.text((32, 8), f"A", fill=(0, 0, 0), font=FONT)
        mannheim_drawable.text((32, MARGIN+8), f"B", fill=(0, 0, 0), font=FONT)
        mannheim_drawable.text((32, 2*MARGIN+8), f"C", fill=(0, 0, 0), font=FONT)
        mannheim_drawable.text((32, 3*MARGIN+8), f"D", fill=(0, 0, 0), font=FONT)

        mannheim_drawable.text((WIDTH-96+8, 8), f"A", fill=(0, 0, 0), font=FONT)
        mannheim_drawable.text((WIDTH-96+8, MARGIN+8), f"B", fill=(0, 0, 0), font=FONT)
        mannheim_drawable.text((WIDTH-96+8, 2*MARGIN+8), f"C", fill=(0, 0, 0), font=FONT)
        mannheim_drawable.text((WIDTH-96+8, 3*MARGIN+8), f"D", fill=(0, 0, 0), font=FONT)

        mannheim_image.save(mannheim_file)

if __name__ == "__main__":
    main()
