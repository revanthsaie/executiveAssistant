import { useEffect, useState } from 'react'

/** Shape of GET /api/health. */
type Health = {
  status: string
  version: string
  python: string
  os: string
}

/** M0 hello screen: proves the window, the React build and the local API all work. */
export default function App() {
  const [health, setHealth] = useState<Health | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch('/api/health')
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`HTTP ${r.status}`))))
      .then(setHealth)
      .catch((e: Error) => setError(e.message))
  }, [])

  return (
    <main className="flex h-full items-center justify-center bg-slate-50 p-6 text-slate-900 dark:bg-slate-950 dark:text-slate-100">
      <div className="w-full max-w-md rounded-2xl border border-slate-200 bg-white p-8 shadow-sm dark:border-slate-800 dark:bg-slate-900">
        <p className="text-sm font-medium tracking-wide text-indigo-600 uppercase dark:text-indigo-400">
          Executive Assistant
        </p>
        <h1 className="mt-2 text-2xl font-semibold">Hello from your desktop app</h1>
        <p className="mt-2 text-sm text-slate-500 dark:text-slate-400">
          Milestone 0 check: window, UI and local backend.
        </p>

        <div className="mt-6 space-y-2 text-sm">
          <Row label="Window + React UI" ok />
          {health && <Row label={`Backend ${health.status} · v${health.version}`} ok />}
          {health && <Row label={`Python ${health.python} on ${health.os}`} ok />}
          {error && <Row label={`Backend unreachable: ${error}`} ok={false} />}
          {!health && !error && <p className="text-slate-500">Contacting backend…</p>}
        </div>
      </div>
    </main>
  )
}

/** One check line with a green or red dot. */
function Row({ label, ok }: { label: string; ok: boolean }) {
  return (
    <div className="flex items-center gap-3">
      <span className={`size-2.5 rounded-full ${ok ? 'bg-emerald-500' : 'bg-rose-500'}`} />
      <span>{label}</span>
    </div>
  )
}
