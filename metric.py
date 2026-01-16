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
        Image.new("RGB", (WIDTH, HEIGHT), color="#FFFFFF") as metric_image,
        open("metric.png", "wb") as metric_file
    ):
        # Black border around scale

        for x in range(0, WIDTH):
            metric_image.putpixel((x, 0), (0, 0, 0))
            metric_image.putpixel((x, HEIGHT-1), (0, 0, 0))

        for y in range(0, HEIGHT):
            metric_image.putpixel((0, y), (0, 0, 0))
            metric_image.putpixel((WIDTH-1, y), (0, 0, 0))

        for x in range(0, WIDTH):
            metric_image.putpixel((x, MARGIN), (0, 0, 0))

        for x in range(0, WIDTH):
            metric_image.putpixel((x, 3*MARGIN), (0, 0, 0))

        for y in range(0, HEIGHT):
            metric_image.putpixel((MARGIN, y), (0, 0, 0))
            metric_image.putpixel((WIDTH-1-MARGIN, y), (0, 0, 0))

        metric_drawable = ImageDraw.Draw(metric_image)

        for x in range(1, 230):
            label_offset = 18
            mark_number = True

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

            x /= 100

            f = x / 2.3

            print(f * (WIDTH - 2 * MARGIN), f)

            d = MARGIN + round(f * (WIDTH - 2 * MARGIN))

            for y in range(mark_height):
                for w in range(-mark_width//2 + 1, mark_width//2 + 1):
                    if d + w >= WIDTH-MARGIN or d + w < MARGIN:
                        continue

                    metric_image.putpixel((d + w, y), (0, 0, 0))

            if mark_number:
                metric_drawable.text((d-label_offset, (mark_height)), f"{x*10:02.0f}", fill=(0, 0, 0), font=FONT)

        for x in range(1, 230):
            label_offset = 18
            mark_number = True

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

            x /= 100

            f = x / 2.3

            print(f * (WIDTH - 2 * MARGIN), f)

            d = MARGIN + round(f * (WIDTH - 2 * MARGIN))

            for y in range(mark_height):
                for w in range(-mark_width//2 + 1, mark_width//2 + 1):
                    if d + w >= WIDTH-MARGIN or d + w < MARGIN:
                        continue

                    metric_image.putpixel((d + w, HEIGHT - 1 - y), (0, 0, 0))

            if mark_number:
                metric_drawable.text((d-label_offset, (HEIGHT-mark_height-32)), f"{x*10:02.0f}", fill=(0, 0, 0), font=FONT)

        metric_image.save(metric_file)

if __name__ == "__main__":
    main()
