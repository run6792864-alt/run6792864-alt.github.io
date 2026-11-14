"""회원 카톡 미리보기 그림(og.jpg) — 블랙+골드 테마
python3 _tools/make_og.py m/<주소>/og.jpg "홍길동" [M|F] [group]
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
FONT_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc"
TRAINER = "정현식"


def build(out, name, sex="M", group=False):
    W, H = 1200, 630
    bg = (20, 20, 20) if sex == "M" else (60, 14, 32)
    gold = (201, 162, 74)
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    # 은은한 금색 빛
    glow = Image.new("RGB", (W, H), bg)
    gd = ImageDraw.Draw(glow)
    for i in range(60):
        r = 520 - i * 8
        c = tuple(int(bg[k] + (gold[k] - bg[k]) * (i / 60) * 0.18) for k in range(3))
        gd.ellipse((W - 260 - r, -200 - r, W - 260 + r, -200 + r), fill=c)
    im = Image.blend(im, glow, 1.0)
    d = ImageDraw.Draw(im)
    logo = Image.open(os.path.join(HERE, "..", "assets", "logo.png")).convert("RGBA")
    lw = 300
    logo = logo.resize((lw, int(logo.height * lw / logo.width)))
    im.paste(logo, (80, 70), logo)
    f1 = ImageFont.truetype(FONT, 34)
    f2 = ImageFont.truetype(FONT_B, 96)
    f3 = ImageFont.truetype(FONT, 30)
    sub = "MY PT NOTE · 함께하는 그룹 PT 노트" if group else "MY PT NOTE · 나만의 운동 노트"
    d.text((82, 238), sub, font=f1, fill=gold)
    d.text((78, 300), name + " 회원님", font=f2, fill=(255, 255, 255))
    d.rectangle((0, 540, W, H), fill=(8, 8, 8))
    d.rectangle((0, 538, W, 541), fill=gold)
    d.text((82, 566), "GYMTOS 도당점 · 담당 %s 트레이너" % TRAINER, font=f3, fill=(225, 210, 170))
    im.save(out, quality=90)


if __name__ == "__main__":
    a = sys.argv
    build(a[1], a[2], a[3] if len(a) > 3 else "M", len(a) > 4 and a[4] == "group")
