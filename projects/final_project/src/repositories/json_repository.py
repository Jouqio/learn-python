"""Persists student records to a JSON file on disk."""
import json
import os


class JSONStudentRepository:
    def __init__(self, filepath="students.json"):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            self._write([])

    def _read(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, records):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)

    def load_all(self):
        return self._read()

    def save_all(self, records):
        self._write(records)
