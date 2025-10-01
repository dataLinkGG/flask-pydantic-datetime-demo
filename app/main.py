from flask import Flask, jsonify
from flask.json.provider import DefaultJSONProvider
from pydantic import BaseModel
from datetime import datetime

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
    return jsonify(Task(id=1, name="demo", execute_at=datetime.utcnow()))

if __name__ == "__main__":
    app.run(debug=True)
