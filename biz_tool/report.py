"""清洗报告：用一个类把”结果“和”操作结果的方法“放在一起"""

import json


class CleanReport:
    def __init__(self, source):
        self.source = source  # 数据来源，比如文件名
        self.ok = 0  # 有效条数
        self.bad_rows = []  # 异常记录

    def add_ok(self):
        self.ok += 1

    def add_bad(self, row, reason):
        self.bad_rows.append({"row": row, "reason": reason})

    def total(self):
        return self.ok + len(self.bad_rows)

    def summary(self):
        return f"{self.source}:共{self.total()}条，有效{self.ok}条，异常{len(self.bad_rows)}条"

    def save(self, path):
        data = {"source": self.source, "total": self.total(), "ok": self.ok, "bad_row": self.bad_rows, "reasons":self.reason_counts(), "bad_rate": self.bad_rate()}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def reason_counts(self):
        res = {}
        for i in self.bad_rows:
            key = i["reason"]
            res[key] = res.get(key, 0) + 1
        return res

    def bad_rate(self):
        if self.total() != 0:
            return f"{len(self.bad_rows) / self.total():.1%}"
        else:
            return f"0.0%"
