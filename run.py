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

# ── Database init (safe — only creates tables, no filesystem ops) ─────────
init_db()
migrate_db()

# ── Entry point (local dev only) ──────────────────────────────────────────
if __name__ == '__main__':
    # Create uploads folder for local development only
    _local_uploads = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    os.makedirs(_local_uploads, exist_ok=True)

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
