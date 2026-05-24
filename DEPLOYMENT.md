# Deployment & Security Guide

## Deployment Options

### Option 1: Vercel (Recommended)
1. Push this code to a GitHub repository.
2. Go to [Vercel.com](https://vercel.com) and sign up/login.
3. Click "Add New Project" and import your GitHub repository.
4. Vercel will detect Next.js automatically. Click "Deploy".
5. Your site will be live on a generic URL (e.g. `al-rawasi.vercel.app`). You can add your custom domain later.

### Option 2: VPS (Ubuntu/Linux)
1. Install Node.js and PM2 on the server.
2. Upload the code.
3. Run `npm run build`.
4. Run `pm2 start npm --name "al-rawasi" -- start`.
5. Configure Nginx as a reverse proxy to port 3000.

## Security Best Practices

1. **SSL/TLS**: Always serve over HTTPS. Vercel provides this automatically. on VPS, use Certbot.
2. **Headers**: Next.js sets security headers by default. You can enhance them in `next.config.js`.
3. **Input Validation**: When you connect a real backend form, use libraries like `zod` to validate all user inputs.
4. **Admin Access**: Currently the Admin UI is a visual prototype. In production, you must implement Auth (e.g. NextAuth.js) to protect the `/admin` routes.

## SEO Optimization

1. **Meta Tags**: Edit the `metadata` object in `app/[lang]/layout.tsx` and specific pages.
2. **Sitemap**: Next.js can generate `sitemap.xml`. create `app/sitemap.ts`.
3. **Performance**: Use the `Next/Image` component (not executed in this prototype) for automatic image optimization.
