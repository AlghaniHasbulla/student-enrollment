# create_db.py
from enrollment.database import init_db

print("🔧 Creating database and tables...")
init_db()
print("✅ Database and tables created successfully.")