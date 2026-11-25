import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  build: {
    // "build", not Vite's default "dist": PyInstaller writes to the repo's dist/ folder.
    outDir: 'build',
    emptyOutDir: true,
  },
  server: {
    // During `npm run dev`, forward API calls to a backend started with EA_PORT=8765.
    proxy: { '/api': 'http://127.0.0.1:8765' },
  },
})
