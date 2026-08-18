<p align="center">
  <a href="https://cfgauss.com.br">
    <img src="assets/banner.svg" alt="CF Gauss · Applied AI Systems" width="100%" />
  </a>
</p>

<p align="center">
  <img src="assets/claude-partner.png" alt="Anthropic — Select Services Partner" height="48" style="vertical-align:middle" />
</p>

<p align="center">
  <strong>I build open-source marketing infrastructure: the landing-page engine, the email cockpit and the tracking layer — one contract, three skills, one funnel.</strong>
</p>

<p align="center">
  <a href="https://github.com/luisroquette"><img alt="Followers" src="https://img.shields.io/github/followers/luisroquette?style=for-the-badge&color=7B2FBE&labelColor=1A1524"></a>
  <a href="https://github.com/luisroquette?tab=repositories"><img alt="Stars" src="https://img.shields.io/github/stars/luisroquette?style=for-the-badge&color=C9A7FF&labelColor=1A1524"></a>
  <a href="https://github.com/luisroquette/My_UTMs_Make_Me_Proud/blob/main/LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-2E7D32?style=for-the-badge&labelColor=1A1524"></a>
  <img alt="Anthropic Select Services Partner" src="https://img.shields.io/badge/Anthropic-Select_Services_Partner-D5A62E?style=for-the-badge&labelColor=1A1524">
</p>

---

## About me

I am an **Anthropic Select Services Partner** and the builder behind the CF Gauss marketing stack. I spent years building production systems — landing pages that convert, email engines that follow up without becoming spam, tracking that attributes every sale to its channel — and then extracted each one into a portable, deterministic, MIT-licensed skill that any Claude Code or Codex user can clone and run.

The three skills form one funnel: the **LP engine** captures leads from evidence-backed pages, the **email cockpit** nurtures them under a shared throttle (one email per lead per day, guaranteed by a test suite), and the **tracking layer** attributes every CTA back to its channel. They interoperate through contracts — the tracking link owns the definition of a click; the others reference it. No vendor lock-in, no black box: every rule ships as Markdown contracts plus deterministic validators you can run in your terminal and your CI.

What I believe: marketing software should be **auditable** (the rules are prose you can read), **deterministic** (same input, same verdict, forever), and **honest** (absence is never zero, and anti-fabrication beats a pretty page). The repositories below are the reference implementations of that belief.

Previously: RocketLabs (applied AI systems and developer tools), Resuma, NotchAgent and other product experiments — the same discipline, different surfaces. Everything here follows one visual and engineering standard: auditable contracts, deterministic validators, honest metrics.

---

## Achievements

<p align="center">
  <img alt="Pull Shark x2" src="https://img.shields.io/badge/Pull_Shark-×2-7B2FBE?style=for-the-badge&labelColor=1A1524">
  <img alt="Pair Extraordinaire x2" src="https://img.shields.io/badge/Pair_Extraordinaire-×2-C9A7FF?style=for-the-badge&labelColor=1A1524">
  <img alt="YOLO" src="https://img.shields.io/badge/YOLO-×1-D5A62E?style=for-the-badge&labelColor=1A1524">
</p>

Earned the way achievements should be earned — by merging, reviewing and shipping.
---

## Quickstart

```bash
# The tracking layer — every marketing link, tracked and attributable
git clone https://github.com/luisroquette/My_UTMs_Make_Me_Proud.git

# The landing-page engine — brief, create, audit and publish
git clone https://github.com/luisroquette/My_LP_Makes_Neil_Proud.git

# The email cockpit — throttle, dispatcher, outbox and dashboard
git clone https://github.com/luisroquette/My_MailMKT_makes_Neil_Proud.git
```

All three are MIT, zero runtime dependencies, with deterministic validators and regression suites — clone one or clone all three.

---

## Flagship projects

| Project | What it is | Highlights |
|---|---|---|
| [**My_UTMs_Make_Me_Proud**](https://github.com/luisroquette/My_UTMs_Make_Me_Proud) | The tracking layer — creation, click, attribution, health and metrics as one auditable cycle | 13 regression cases · query-free destinations · SSRF-guarded health · first/last click attribution |
| [**My_LP_Makes_Neil_Proud**](https://github.com/luisroquette/My_LP_Makes_Neil_Proud) | The landing-page engine — six models, four gates, anti-fabrication above everything | 6 LP models · 12-criterion audit rubric · publication gate never bypassed |
| [**My_MailMKT_makes_Neil_Proud**](https://github.com/luisroquette/My_MailMKT_makes_Neil_Proud) | The email cockpit — shared throttle, single dispatcher, durable outbox, dashboard demo | 107 tests · 1 email/lead/day guaranteed · 5 motors, 1 cron · cockpit demo |
| [**RocketLabs**](https://github.com/luisroquette/RocketLabs) | Applied AI systems and developer tools — the earlier product era | Resuma, NotchAgent and content automation |

Deep dives: every repo's README documents the contracts in depth — the regression ledgers, the models, the gates, the fidelity rules. Start with the one that matches your layer of the funnel.

---

## Tech stack

### AI & Agents

[![Claude Code](https://img.shields.io/badge/Claude_Code-17131F?style=for-the-badge&logo=anthropic&logoColor=white&labelColor=1A1524)](https://claude.com/claude-code)
[![Codex](https://img.shields.io/badge/OpenAI_Codex-17131F?style=for-the-badge&logo=openai&logoColor=white&labelColor=1A1524)](https://openai.com/codex)
[![Claude API](https://img.shields.io/badge/Claude_API-7B2FBE?style=for-the-badge&logo=anthropic&logoColor=white&labelColor=1A1524)](https://docs.anthropic.com)
[![gpt-image](https://img.shields.io/badge/GPT_Image-7B2FBE?style=for-the-badge&logo=openai&logoColor=white&labelColor=1A1524)](https://openai.com)
[![Higgsfield](https://img.shields.io/badge/Higgsfield_Video-7B2FBE?style=for-the-badge&labelColor=1A1524)](https://higgsfield.ai)
[![MCP](https://img.shields.io/badge/MCP_Protocol-7B2FBE?style=for-the-badge&labelColor=1A1524)](https://modelcontextprotocol.io)

### Marketing & Data

[![DataForSEO](https://img.shields.io/badge/DataForSEO-C9A7FF?style=for-the-badge&labelColor=1A1524)](https://dataforseo.com)
[![Meta Graph API](https://img.shields.io/badge/Meta_Graph_API-C9A7FF?style=for-the-badge&labelColor=1A1524)](https://developers.facebook.com)
[![Instagram API](https://img.shields.io/badge/Instagram_API-C9A7FF?style=for-the-badge&labelColor=1A1524)](https://developers.facebook.com/docs/instagram-platform)
[![WhatsApp API](https://img.shields.io/badge/WhatsApp_API-C9A7FF?style=for-the-badge&labelColor=1A1524)](https://business.whatsapp.com)
[![Telegram Bot API](https://img.shields.io/badge/Telegram_Bot_API-C9A7FF?style=for-the-badge&labelColor=1A1524)](https://core.telegram.org/bots/api)
[![X API](https://img.shields.io/badge/X_API-C9A7FF?style=for-the-badge&labelColor=1A1524)](https://developer.x.com)

### Languages & Web

[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white&labelColor=1A1524)](https://www.typescriptlang.org)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=1A1524)](https://www.python.org)
[![Next.js](https://img.shields.io/badge/Next.js-17131F?style=for-the-badge&logo=nextdotjs&logoColor=white&labelColor=1A1524)](https://nextjs.org)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black&labelColor=1A1524)](https://react.dev)
[![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white&labelColor=1A1524)](https://tailwindcss.com)
[![shadcn/ui](https://img.shields.io/badge/shadcn/ui-17131F?style=for-the-badge&labelColor=1A1524)](https://ui.shadcn.com)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white&labelColor=1A1524)](https://vite.dev)

### Infrastructure & Quality

[![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=black&labelColor=1A1524)](https://supabase.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white&labelColor=1A1524)](https://www.postgresql.org)
[![Resend](https://img.shields.io/badge/Resend-17131F?style=for-the-badge&labelColor=1A1524)](https://resend.com)
[![Vercel](https://img.shields.io/badge/Vercel-17131F?style=for-the-badge&logo=vercel&logoColor=white&labelColor=1A1524)](https://vercel.com)
[![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=for-the-badge&logo=vitest&logoColor=white&labelColor=1A1524)](https://vitest.dev)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white&labelColor=1A1524)](https://playwright.dev)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white&labelColor=1A1524)](https://ffmpeg.org)

---

## Connect

[![Website](https://img.shields.io/badge/cfgauss.com.br-7B2FBE?style=for-the-badge&labelColor=1A1524)](https://cfgauss.com.br)
[![GitHub](https://img.shields.io/badge/GitHub-17131F?style=for-the-badge&logo=github&logoColor=white&labelColor=1A1524)](https://github.com/luisroquette)

<p align="center">
  <img src="assets/divider.svg" alt="" width="100%" />
</p>

<p align="center">
  <sub>CF Gauss · applied AI systems · open-source marketing infrastructure · MIT everywhere</sub>
</p>
