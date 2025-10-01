import os
import psycopg2
import psycopg2.extras
from flask import Flask, jsonify
from flask.json.provider import DefaultJSONProvider
from pydantic import BaseModel
from datetime import datetime

DATABASE_URL = os.getenv("DATABASE_URL")


class Task(BaseModel):
    id: int
    name: str
    execute_at: datetime


class PydanticJSONProvider(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, BaseModel):
            return obj.model_dump()
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


app = Flask(__name__)
app.json = PydanticJSONProvider(app)


@app.get("/task")
def get_task():
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT id, name, execute_at FROM tasks LIMIT 1;")
            row = cur.fetchone()
            if row:
                return jsonify(Task(**row))
            return jsonify({"error": "No tasks found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
