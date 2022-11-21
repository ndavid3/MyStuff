bejar = ["alma", "körte", "meggy", 1, 2, 3, "alma", "alma", -10]

db = dict()
for elem in bejar:
    if type(elem) == int:
        db["egész_számok"] = db.get("egész_számok", 0) + 1
    else:
        db[elem] = db.get(elem, 0) + 1

print(db)