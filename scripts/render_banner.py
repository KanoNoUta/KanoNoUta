from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


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

for x, y, radius in ((820, 52, 14), (868, 92, 8), (810, 298, 9), (1228, 64, 10)):
    draw.ellipse(
        (x - radius, y - radius, x + radius, y + radius), fill="#FFB5C5"
    )

draw.text((138, 98), "KANO / かの", font=load_font(58), fill="#17324A")
draw.text(
    (142, 184),
    "AI TOOLS / GATEWAYS / AGENT WORKFLOWS",
    font=load_font(22),
    fill="#1E8F87",
)
draw.text(
    (142, 229),
    "AI 工具 / 协议网关 / Agent 工作流",
    font=load_font(24),
    fill="#536B78",
)

avatar = Image.open(ASSETS / "avatar.png").convert("RGB")
avatar = ImageOps.fit(avatar, (250, 250), method=Image.Resampling.LANCZOS)
mask = Image.new("L", avatar.size, 0)
ImageDraw.Draw(mask).ellipse((0, 0, 249, 249), fill=255)
draw.ellipse((932, 42, 1218, 328), fill="#FFFFFF")
draw.ellipse((942, 52, 1208, 318), fill="#FF7B9C")
canvas.paste(avatar, (950, 60), mask)

draw.text(
    (142, 270),
    "BUILD  /  CONNECT  /  CREATE",
    font=load_font(13),
    fill="#FF7B9C",
)
canvas.save(ASSETS / "profile-banner.png", optimize=True)
