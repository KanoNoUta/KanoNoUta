from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SIZE = (1280, 360)
ASSETS = ROOT / "assets"
FONT_CJK = Path("C:/Windows/Fonts/msyhbd.ttc")


def load_font(size: int) -> ImageFont.FreeTypeFont:
    if FONT_CJK.exists():
        return ImageFont.truetype(str(FONT_CJK), size)
    return ImageFont.truetype("DejaVuSans-Bold.ttf", size)


canvas = Image.new("RGB", SIZE, "#DFF5F3")
draw = ImageDraw.Draw(canvas)

draw.rectangle((0, 0, 28, SIZE[1]), fill="#FF7B9C")
draw.rectangle((28, 0, 42, SIZE[1]), fill="#17324A")
draw.rounded_rectangle((92, 66, 770, 294), radius=20, fill="#F7FBFC")
draw.rectangle((92, 66, 102, 294), fill="#76C7C0")

for x in range(820, 1240, 40):
    draw.line((x, 44, x, 316), fill="#BBDDD9", width=1)
for y in range(44, 317, 40):
    draw.line((820, y, 1240, y), fill="#BBDDD9", width=1)

draw.text((138, 98), "KANO / かの", font=load_font(58), fill="#17324A")
draw.text(
    (142, 184),
    "DEVELOPER TOOLS / GATEWAYS / AUTOMATION",
    font=load_font(22),
    fill="#1E8F87",
)
draw.text(
    (142, 229),
    "开发工具 / 协议网关 / 自动化工作流",
    font=load_font(24),
    fill="#536B78",
)

draw.rounded_rectangle((874, 66, 1194, 294), radius=18, fill="#17324A")
draw.rectangle((874, 66, 884, 294), fill="#FF7B9C")
draw.text((924, 98), "LOCAL", font=load_font(38), fill="#F7FBFC")
draw.text((924, 158), "RELIABLE", font=load_font(38), fill="#76C7C0")
draw.text((924, 218), "OPEN", font=load_font(38), fill="#FF7B9C")

draw.text(
    (142, 270),
    "BUILD  /  CONNECT  /  CREATE",
    font=load_font(13),
    fill="#FF7B9C",
)
canvas.save(ASSETS / "profile-banner.png", optimize=True)
