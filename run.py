"""
PS-CRM — Public Services CRM
Run this file to start the server.
"""
import os

if os.environ.get('FLASK_SECRET_KEY'):
    import app as _app_mod
    _app_mod.app.secret_key = os.environ['FLASK_SECRET_KEY']

from app import app
from database import init_db, migrate_db

# ── Startup init ───────────────────────────────────────────────────────────
# CRITICAL: On Render, /data is mounted by the PLATFORM before gunicorn runs.
# NEVER call os.makedirs('/data') — it causes PermissionError 13.
# ONLY create subfolders INSIDE /data — that is allowed.
_data_dir    = os.environ.get('RENDER_DATA_DIR',
                os.path.dirname(os.path.abspath(__file__)))
_uploads_dir = os.path.join(_data_dir, 'uploads')

# This is safe — /data exists (mounted by Render), we just add /data/uploads
os.makedirs(_uploads_dir, exist_ok=True)

# Initialise database — safe to call on every startup
init_db()
migrate_db()

# ── Entry point ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print()
    print("=" * 50)
    print("  PS-CRM Server Starting...")
    print("  Open:  http://127.0.0.1:5000")
    print()
    print("  Demo Logins:")
    print("  🔴 Admin   → admin@pscrm.in    / admin123")
    print("  🟡 Head    → head@pscrm.in     / head123")
    print("  🟢 Citizen → citizen@pscrm.in  / citizen123")
    print("=" * 50)
    print()
    is_prod = os.environ.get('FLASK_ENV') == 'production'
    port    = int(os.environ.get('PORT', 5000))
    app.run(debug=not is_prod, port=port, host='0.0.0.0')
