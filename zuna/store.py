"""Validated listing drafts and durable, explicit local decisions."""
import json
import math
import re
import sqlite3
from datetime import datetime, timezone

FIELDS = {"building", "area", "bedrooms", "nightly_aed", "amenities"}

def validate(data):
    if not isinstance(data, dict) or set(data) != FIELDS:
        raise ValueError("Provide exactly building, area, bedrooms, nightly_aed, amenities")
    for key in ("building", "area"):
        value = data[key]
        if not isinstance(value, str) or not 1 <= len(value.strip()) <= 80:
            raise ValueError(f"Invalid {key}")
        if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]*", value):
            raise ValueError(f"{key} must be a public place name without numbers/contact details")
    if type(data["bedrooms"]) is not int or not 0 <= data["bedrooms"] <= 10:
        raise ValueError("bedrooms must be an integer from 0 to 10")
    price = data["nightly_aed"]
    if type(price) not in (int, float) or not math.isfinite(price) or not 1 <= price <= 100000:
        raise ValueError("nightly_aed must be a finite positive amount up to 100000")
    allowed = {"Wi-Fi", "pool", "gym", "parking", "kitchen", "balcony"}
    amenities = data["amenities"]
    if not isinstance(amenities, list) or len(amenities) > len(allowed) or any(not isinstance(x, str) or x not in allowed for x in amenities) or len(set(amenities)) != len(amenities):
        raise ValueError("Use unique supported amenities: " + ", ".join(sorted(allowed)))
    return data

def render(data):
    validate(data)
    rooms = "Studio" if data["bedrooms"] == 0 else f"{data['bedrooms']}-bedroom holiday home"
    base = f"{rooms} at {data['building']}, {data['area']}. AED {data['nightly_aed']:g} per night."
    features = ", ".join(data["amenities"]) or "No amenities specified"
    return {"draft": base + " Amenities: " + features + ".",
            "alternative": "Where comfort begins. " + base + " Includes: " + features + ". Check availability and applicable fees before booking."}

class Store:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS drafts(id INTEGER PRIMARY KEY, content TEXT NOT NULL, status TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, draft_id INTEGER NOT NULL, event TEXT NOT NULL, timestamp TEXT NOT NULL);
        """)
    def close(self):
        self.db.close()
    def _event(self, draft_id, event):
        self.db.execute("INSERT INTO events(draft_id,event,timestamp) VALUES(?,?,?)", (draft_id,event,datetime.now(timezone.utc).isoformat()))
    def create(self, data):
        content = json.dumps(render(data), ensure_ascii=False)
        with self.db:
            draft_id = self.db.execute("INSERT INTO drafts(content,status) VALUES(?, 'pending')", (content,)).lastrowid
            self._event(draft_id, "created")
        return self.get(draft_id)
    def get(self, draft_id):
        row = self.db.execute("SELECT * FROM drafts WHERE id=?", (draft_id,)).fetchone()
        if row is None:
            raise ValueError("Draft not found")
        return {"id": row["id"], "status": row["status"], **json.loads(row["content"])}
    def decide(self, draft_id, decision):
        if decision not in {"approved", "rejected"}:
            raise ValueError("Decision must be approved or rejected")
        with self.db:
            cursor = self.db.execute("UPDATE drafts SET status=? WHERE id=? AND status='pending'", (decision,draft_id))
            if cursor.rowcount != 1:
                raise ValueError("Draft missing or already decided")
            self._event(draft_id, decision)
        return self.get(draft_id)
    def events(self, draft_id):
        self.get(draft_id)
        return [dict(row) for row in self.db.execute("SELECT event,timestamp FROM events WHERE draft_id=? ORDER BY id", (draft_id,))]
