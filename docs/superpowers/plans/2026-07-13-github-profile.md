# GitHub Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a concise bilingual GitHub profile with a repository-owned anime-inspired banner, clear AI-tool positioning, featured projects, and resilient statistics.

**Architecture:** The special `KanoNoUta/KanoNoUta` repository supplies the public profile through its root `README.md`. A deterministic Pillow script combines the existing GitHub avatar with a mint-and-sakura banner committed under `assets/`; the README uses GitHub-compatible Markdown and limited HTML, while optional statistics come from GitHub Readme Stats with light and dark variants.

**Tech Stack:** GitHub Profile README, Markdown, GitHub-compatible HTML, Python 3, Pillow, Shields.io, GitHub Readme Stats

---

## File Map

- `README.md`: complete public profile content and all public links
- `assets/avatar.png`: source copy of the current GitHub avatar
- `assets/profile-banner.png`: generated repository-owned banner displayed at the top of the profile
- `scripts/render_banner.py`: deterministic banner renderer
- `docs/superpowers/specs/2026-07-13-github-profile-design.md`: approved visual and content requirements
- `docs/superpowers/plans/2026-07-13-github-profile.md`: implementation and verification checklist

### Task 1: Create The Banner Asset

**Files:**
- Create: `assets/avatar.png`
- Create: `assets/profile-banner.png`
- Create: `scripts/render_banner.py`

- [ ] **Step 1: Download the public GitHub avatar**

Run:

```powershell
New-Item -ItemType Directory -Force assets | Out-Null
Invoke-WebRequest "https://avatars.githubusercontent.com/u/30767480?v=4" -OutFile assets/avatar.png
```

Expected: `assets/avatar.png` is a valid PNG or JPEG image returned by GitHub.

- [ ] **Step 2: Create the deterministic banner renderer**

Create `scripts/render_banner.py` with Pillow. The script must:

```python
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
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill="#FFB5C5")

draw.text((138, 98), "KANO / かの", font=load_font(58), fill="#17324A")
draw.text((142, 184), "AI TOOLS / GATEWAYS / AGENT WORKFLOWS", font=load_font(22), fill="#1E8F87")
draw.text((142, 229), "AI 工具 / 协议网关 / Agent 工作流", font=load_font(24), fill="#536B78")

avatar = Image.open(ASSETS / "avatar.png").convert("RGB")
avatar = ImageOps.fit(avatar, (250, 250), method=Image.Resampling.LANCZOS)
mask = Image.new("L", avatar.size, 0)
ImageDraw.Draw(mask).ellipse((0, 0, 249, 249), fill=255)
draw.ellipse((932, 42, 1218, 328), fill="#FFFFFF")
draw.ellipse((942, 52, 1208, 318), fill="#FF7B9C")
canvas.paste(avatar, (950, 60), mask)

draw.text((1088, 306), "BUILD  /  CONNECT  /  CREATE", anchor="ms", font=load_font(13), fill="#17324A")
canvas.save(ASSETS / "profile-banner.png", optimize=True)
```

Use `C:/Windows/Fonts/msyhbd.ttc` for Japanese and Chinese glyphs when available, with `DejaVuSans-Bold.ttf` as fallback. Keep the avatar on the right third and all text inside the left 720 pixels so the banner remains legible when GitHub scales it down.

- [ ] **Step 3: Render the banner**

Run:

```powershell
python scripts/render_banner.py
```

Expected: the command exits with code 0 and creates `assets/profile-banner.png` at `1280x360`.

- [ ] **Step 4: Validate the generated image**

Run:

```powershell
python -c "from PIL import Image; p='assets/profile-banner.png'; im=Image.open(p); assert im.size==(1280,360); assert im.mode=='RGB'; print(p, im.size, im.mode)"
```

Expected: `assets/profile-banner.png (1280, 360) RGB`.

- [ ] **Step 5: Commit the banner source and output**

Run:

```powershell
git add assets scripts/render_banner.py
git commit -m "feat: add anime-inspired profile banner"
```

Expected: a commit containing the avatar, renderer, and generated banner.

### Task 2: Build The Bilingual Profile README

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write the profile content**

Create `README.md` with this exact section order:

```markdown
<p align="center">
  <img src="assets/profile-banner.png" alt="KANO - AI tools, gateways and anime-inspired experiments" width="100%">
</p>

## Hi, I'm KANO / 你好，我是 KANO

I build practical AI gateways and agent tools, then give them a little anime soul.

我专注于实用的 AI 网关与 Agent 工具，也喜欢为它们加入一点二次元灵魂。

### Stack / 技术栈

<p>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=111111" alt="JavaScript">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

## Featured work / 精选项目

<table>
  <tr>
    <td colspan="2">
      <h3><a href="https://github.com/KanoNoUta/thief-neko">Thief Neko</a></h3>
      <p>A local Catpaw gateway and desktop controller that connects Claude Code and Codex to GLM models.</p>
      <p>连接 Claude Code、Codex 与 GLM 模型的本地 Catpaw 网关及桌面控制器。</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3><a href="https://github.com/KanoNoUta/Gensokyo">Gensokyo</a></h3>
      <p>An anime-inspired theme full of Gensokyo.</p>
      <p>一款充满幻想乡气息的二次元主题。</p>
    </td>
    <td width="50%">
      <h3><a href="https://github.com/KanoNoUta/kanonouta-blog">Kano no Uta Blog</a></h3>
      <p>Development notes, experiments, and things worth remembering.</p>
      <p>记录开发、实验与值得留下的片段。</p>
    </td>
  </tr>
</table>

## GitHub at a glance / GitHub 一览

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=KanoNoUta&amp;show_icons=true&amp;hide_border=true&amp;bg_color=00000000&amp;title_color=ff7b9c&amp;text_color=c9d1d9&amp;icon_color=76c7c0">
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api?username=KanoNoUta&amp;show_icons=true&amp;hide_border=true&amp;bg_color=00000000&amp;title_color=17324a&amp;text_color=536b78&amp;icon_color=1e8f87">
    <img height="165" src="https://github-readme-stats.vercel.app/api?username=KanoNoUta&amp;show_icons=true&amp;hide_border=true" alt="KANO GitHub statistics">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=KanoNoUta&amp;layout=compact&amp;hide_border=true&amp;bg_color=00000000&amp;title_color=ff7b9c&amp;text_color=c9d1d9">
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=KanoNoUta&amp;layout=compact&amp;hide_border=true&amp;bg_color=00000000&amp;title_color=17324a&amp;text_color=536b78">
    <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=KanoNoUta&amp;layout=compact&amp;hide_border=true" alt="KANO most used languages">
  </picture>
</p>

## Now / 现在

Building reliable protocol adapters and tool loops for coding agents.

正在打磨更可靠的协议适配、工具调用循环与本地 AI 工作流。

<p align="center">
  <sub>Code with utility. Design with personality.<br>让工具真正有用，也让它保留一点自己的性格。</sub>
</p>
```

- [ ] **Step 2: Check markup and forbidden clutter**

Run:

```powershell
rg -n "visitor|trophy|marquee|javascript:" README.md
```

Expected: no matches.

- [ ] **Step 3: Validate every public link**

Run:

```powershell
$urls = Select-String -Path README.md -Pattern 'https://[^)" ]+' -AllMatches | ForEach-Object Matches | ForEach-Object Value | Sort-Object -Unique
foreach ($url in $urls) { $clean = $url -replace '&amp;', '&'; $status = (Invoke-WebRequest $clean -Method Head -SkipHttpErrorCheck).StatusCode; "$status $clean" }
```

Expected: repository, badge, and statistics URLs return HTTP 200 or a documented redirect response.

- [ ] **Step 4: Commit the README**

Run:

```powershell
git add README.md
git commit -m "feat: publish bilingual GitHub profile"
```

Expected: a commit containing the complete root profile README.

### Task 3: Publish And Inspect The Profile

**Files:**
- Verify: `README.md`
- Verify: `assets/profile-banner.png`

- [ ] **Step 1: Verify repository state**

Run:

```powershell
git status --short
git log --oneline -3
```

Expected: the worktree is clean and the three latest commits cover design, banner, and README.

- [ ] **Step 2: Push the profile repository**

Run:

```powershell
git push -u origin master
```

Expected: GitHub accepts the branch and activates the Profile README for `KanoNoUta`.

- [ ] **Step 3: Inspect the published profile**

Open `https://github.com/KanoNoUta` and verify:

- The banner loads and remains legible
- The bilingual introduction appears directly below it
- All three featured project links work
- Statistics appear without horizontal overflow
- The profile remains coherent if a statistics image is unavailable

- [ ] **Step 4: Record the final public URL**

Expected result:

```text
https://github.com/KanoNoUta
```
