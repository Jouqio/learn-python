"""Mini Project 12: File-Based Database"""
import json
import os


class FileDB:
    def __init__(self, filepath="mini_db.json"):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            self._write({})

    def _read(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def set(self, key, value):
        data = self._read()
        data[key] = value
        self._write(data)

    def get(self, key, default=None):
        return self._read().get(key, default)

    def delete(self, key):
        data = self._read()
        data.pop(key, None)
        self._write(data)


def main():
    db = FileDB()
    db.set("username", "budi123")
    print(db.get("username"))
    db.delete("username")
    print(db.get("username", "not found"))


if __name__ == "__main__":
    main()
