# Al-Rawasi Corporate Website

A professional, bilingual (Arabic/English) corporate website for Al-Rawasi Libyan Company for Engineering Consultations. Built with **Next.js 14**, **TypeScript**, and **Tailwind CSS**.

## Prerequisites

You must have **Node.js** installed on your system to run this project.
1. Download specific version (LTS recommended): [https://nodejs.org/](https://nodejs.org/)
2. Install it on your machine.
3. Verify installation by running `node -v` in your terminal.

## Getting Started

1. **Install Dependencies**:
   Open a terminal in this project folder (`al-rawasi-web`) and run:
   ```bash
   npm install
   ```

2. **Run the Development Server**:
   ```bash
   npm run dev
   ```

3. **Open the Website**:
   Visit [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

- `app/`: Next.js App Router pages and layouts.
- `app/[lang]/`: Localized routes (e.g. `/ar`, `/en`).
- `components/`: Reusable UI components.
- `dictionaries/`: Translation files (`ar.json`, `en.json`).
- `public/`: Static assets (images, fonts).

## Customization

- **Colors**: Edit `tailwind.config.ts` to change the `primary` (Blue) or `secondary` (Gold) colors.
- **Content**: Edit the files in `dictionaries/` to change the text for English or Arabic.
- **Images**: Place your images in `public/` and reference them in the code.
