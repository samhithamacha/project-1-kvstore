import os

DATA_FILE = "data.db"

class KVStore:
    def __init__(self):
        self.store = []  # In-memory index
        self.load()

    def load(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(" ", 2)
                if parts[0] == "SET":
                    self._set_memory(parts[1], parts[2])

    def _set_memory(self, key, val):
        for i, (k, v) in enumerate(self.store):
            if k == key:
                self.store[i] = (key, val)
                return
        self.store.append((key, val))

    def set(self, key, val):
        with open(DATA_FILE, "a") as f:
            f.write(f"SET {key} {val}\n")
        self._set_memory(key, val)

    def get(self, key):
        for k, v in self.store:
            if k == key:
                return v
        return "NULL"

def main():
    kv = KVStore()
    while True:
        cmd = input("> ").split(" ", 2)
        if cmd[0].upper() == "SET" and len(cmd) == 3:
            kv.set(cmd[1], cmd[2])
        elif cmd[0].upper() == "GET" and len(cmd) == 2:
            print(kv.get(cmd[1]))
        elif cmd[0].upper() == "EXIT":
            break
        else:
            print("ERROR")

if __name__ == "__main__":
    main()
