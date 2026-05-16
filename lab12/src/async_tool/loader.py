from pathlib import Path
import json
from typing import List, cast
from .models import TaskItem

# for JSON file:
def load_tasks(path: str) -> List[TaskItem]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return cast(List[TaskItem], data)