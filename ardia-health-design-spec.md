# ArdiA Health Labs - Investor Pitch Design Specification

## 1. Direction & Rationale

**Style:** Dark Mode (Clinical Intelligence Edition)
**Essence:** A sophisticated, tech-forward aesthetic combining the precision of medical imaging with the modern sleekness of AI software.

**Rationale:**
*   **Context:** Investor pitch for a Series A/Seed stage AI healthcare startup. Needs to signal "cutting-edge technology" and "clinical trust" simultaneously.
*   **Audience:** VCs and Healthcare executives who are inundated with "AI hype". The dark, focused design cuts through the noise, reducing eye strain and highlighting data luminosity.
*   **Objective:** To position ArdiA not just as another chatbot, but as a deep-tech "Reasoning Engine". The high-contrast dark theme emphasizes signal over noise.

**Key Characteristics:**
*   **Deep Backgrounds:** `#121212` backgrounds reduce glare and allow data visualizations to "glow" without cheap neon effects.
*   **Precision Typography:** Montserrat (Headings) and Inter (Body) provide highly legible, Swiss-style objectivity.
*   **Luminous Accents:** Professional Blue (`#8BAFD0`) guides the eye to key insights, mimicking the cool tones of medical displays.
*   **Focused Light:** White space is replaced by "negative space", creating a cinematic focus on the content.

**References:**
*   Stripe Dark Mode
*   Linear.app Interface
*   Advanced Medical Imaging (MRI/CT UI)

---

## 2. Slide Templates (Visual Patterns)

**Global Rules:**
*   **Content Density:** Max 7 lines of text per slide. If content exceeds this, split into "Overview + Detail" slides.
*   **Typography:** Title 54px (Bold), Body 24px (Regular), Data 80px (Bold).
*   **Margins:** 96px Horizontal, 64px Vertical.

### Template 1: Title Slide
**Purpose:** Brand introduction and hook.
*   **Layout:** Centered alignment with a subtle, abstract background pattern (geometric grid or waveform) at 10% opacity.
*   **Typography:**
    *   **Hero:** 96px Montserrat Bold, Center, `#E8E8E8`.
    *   **Sub-hero:** 32px Inter Regular, Center, `#B3B3B3`, max-width 800px.
*   **Visuals:** Logo top-center (48px height).
*   **Animation:** Slow fade-in of background pattern, followed by text slide-up.

### Template 2: Content - Split (60/40)
**Purpose:** Problem statement, Solution, Product Dashboard.
*   **Layout:** Asymmetric 2-column grid. Left (40%) for text, Right (60%) for visual media.
*   **Typography:**
    *   **Title:** 54px Left-aligned.
    *   **Body:** 24px Inter, line-height 1.75. Max 5 bullet points.
*   **Visuals:** Right side contains a large rounded container (16px radius, `#1E1E1E` bg) for product screenshots or diagrams.
*   **Pagination:** Use "Slide 1 of 2" indicator if text exceeds 7 lines.

### Template 3: Data - Key Metrics
**Purpose:** Market Opportunity, Pilot Results.
*   **Layout:** 3-column grid of "Data Cards".
*   **Card Style:** `#1E1E1E` background, 16px radius, subtle border `#2D2D2D`.
*   **Typography:**
    *   **Big Number:** 80px Montserrat Bold, Center, Accent Color (`#8BAFD0`).
    *   **Label:** 24px Inter Medium, Center, `#E8E8E8`.
    *   **Context:** 18px Inter Regular, Center, `#B3B3B3`.
*   **Visuals:** Optional circular progress ring or trend line behind the number.

### Template 4: Comparison Matrix
**Purpose:** Competitive Landscape.
*   **Layout:** 4-column table structure. First column = Features, Columns 2-4 = Competitors/Us.
*   **Styling:**
    *   **Header Row:** `#2D2D2D` background, 24px text.
    *   **"Us" Column:** Highlighted with `#1E1E1E` background and `#8BAFD0` top border (4px).
    *   **Icons:** 32px Check (Green) or X (Gray).
*   **Typography:** Body 20px (Compact) for table data to ensure fit.

### Template 5: Quote / Big Statement
**Purpose:** "Healthcare AI is broken", Founder Vision.
*   **Layout:** Centered, narrow container (900px max width).
*   **Typography:**
    *   **Quote:** 64px Montserrat Medium, Italic.
    *   **Attribution:** 24px Inter Bold, Accent Color.
*   **Visuals:** Large decorative quote marks (opacity 0.1) in background.

### Template 6: Section Break
**Purpose:** Transition between Problem, Solution, Business.
*   **Layout:** Left-aligned, high contrast.
*   **Typography:**
    *   **Number:** 200px Montserrat Bold, opacity 0.05, absolute positioned.
    *   **Title:** 72px Montserrat Bold, `#E8E8E8`.
*   **Visuals:** Horizontal accent line (`#8BAFD0`, 4px height) extending 200px from left.

### Template 7: Closing / Contact
**Purpose:** Call to action, Contact info.
*   **Layout:** Centered.
*   **Typography:**
    *   **Title:** 54px "Invest in the Future".
    *   **Contact Block:** 24px Inter, vertical stack (Name, Email, Phone).
*   **Visuals:** QR Code placeholder (160px square) with white border.

### Optional Template 8: Timeline / Roadmap
**Purpose:** Traction & Milestones.
*   **Layout:** Horizontal line across center.
*   **Visuals:**
    *   **Line:** 4px `#2D2D2D` solid line.
    *   **Nodes:** 24px circles, Active = Filled Accent, Future = Border Only.
*   **Typography:** Date above line (24px Bold), Milestone below line (20px Regular).

---

## 3. Visual Guidelines

**Images & Media:**
*   **Style:** Cinematic, high-contrast, professional.
*   **Screenshots:** Wrap in a "Device Frame" style container: `#1E1E1E` background, 16px radius, subtle inner border `#3D3D3D`.
*   **Sourcing:**
    *   *Hero/Bg:* Abstract data flows, network nodes, dark medical environments.
    *   *Product:* Clean interface mockups, no clutter.
    *   *People:* Authentic medical settings, diverse, low-key lighting.

**Icons:**
*   **Set:** Lucide or Heroicons (Outline style).
*   **Size:** 32px standard, 48px for feature highlights.
*   **Color:** `#E8E8E8` (Primary), `#8BAFD0` (Accent).
*   **Stroke:** 2px.

**Charts & Data:**
*   **Palette:**
    1.  `#8BAFD0` (Primary Data)
    2.  `#5374AC` (Secondary)
    3.  `#E89856` (Highlight/Alert)
*   **Style:** Minimal axes (`#2D2D2D`), direct labeling (no legends if possible).
*   **Donuts/Pies:** Thin rings (stroke width 20-30).

**Animation:**
*   **Entrance:** Staggered `fadeInUp` (300ms delay between elements).
*   **Emphasis:** Subtle pulse on key data numbers.
*   **Transition:** `Fade` (400ms).

---

## 4. Implementation Restrictions

**MANDATORY for Build Agent:**
*   ❌ **NO Emojis:** Use SVG icons only.
*   ❌ **NO Specific Content:** Do not insert real company data into the templates. Use placeholders like `{{metric_1}}`, `{{title_text}}`.
*   ❌ **NO Light Backgrounds:** Stick strictly to `#121212` and `#1E1E1E`.
*   ✅ **Token Usage:** All colors and spacings must reference `design-tokens.json`.
*   ✅ **Body Text:** Minimum 24px. If text is too long, use the split-slide strategy.
*   ✅ **Accessibility:** Maintain 7:1 contrast for text (`#E8E8E8` on `#121212`).

---

## 5. Content Pagination Strategy

**For Dense Slides (Product, Technology):**
If the content extraction yields more than 7 bullet points or 150 words:
1.  **Split Strategy:** Create "Part 1: Overview" and "Part 2: Deep Dive".
2.  **Layout:** Use **Template 2 (Split)** for Part 1 (Visual heavy) and **Template 2 (reversed)** for Part 2 (Text heavy).
3.  **Visual Cue:** Add a subtle "1/2" and "2/2" indicator in the bottom right corner (16px, opacity 0.5).
