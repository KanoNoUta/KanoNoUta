# GitHub Profile Design

## Goal

Create a concise, bilingual GitHub profile for KANO that presents an AI-tool developer identity through a clean anime-inspired visual language. The profile should make the projects easy to understand before decorative elements draw attention.

## Audience

- Developers evaluating KANO's open-source work
- Users looking for AI gateways and agent tooling
- Readers arriving from the personal blog or anime-theme projects

## Visual Direction

- Style: clean Japanese character-card design
- Identity: AI tooling first, anime culture as the visual expression
- Character art: reuse the current GitHub avatar rather than introducing a new character
- Palette: mint `#DFF5F3`, sakura pink `#FF7B9C`, deep blue-gray `#17324A`
- Theme compatibility: the content must remain readable in GitHub light and dark modes
- Density: approximately two desktop screens, with no trophy wall, visitor counter, marquee, or dense badge collection

## Page Structure

1. Repository-hosted PNG banner using the current avatar, `KANO / かの`, and a bilingual AI-tool tagline
2. Short bilingual introduction
3. Compact technology badges for JavaScript, TypeScript, Node.js, and GitHub Actions
4. Featured projects: Thief Neko, Gensokyo, and Kano no Uta Blog
5. Two compact GitHub statistics images: overview and top languages
6. A short footer linking to the blog and describing the current development focus

## Content Rules

- Chinese and English should convey the same meaning without duplicating long paragraphs
- Thief Neko is the primary featured project
- Project descriptions should explain outcomes, not only implementation technologies
- External dynamic images must have stable URLs and descriptive alt text
- Repository-owned visual assets live under `assets/`
- All links use HTTPS and point to public destinations

## Responsive Behavior

GitHub README rendering controls the final layout. HTML tables may be used only where they degrade naturally on narrow screens. The banner must remain legible when scaled to a mobile viewport, and no essential text may exist only inside the image.

## Reliability And Fallbacks

- The banner is committed to the profile repository so it does not depend on an image host
- Dynamic statistics are optional enhancement; the surrounding text and project links remain complete if they fail to load
- No custom CSS, JavaScript, animated SVG, or unsupported GitHub markup is used

## Verification

- Preview the README through GitHub-compatible Markdown rendering
- Verify every repository and blog link
- Confirm the banner remains legible at desktop and mobile widths
- Confirm the public profile repository is named exactly `KanoNoUta/KanoNoUta`
- Inspect the published GitHub profile after push
