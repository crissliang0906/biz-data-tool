import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)  # 文件夹不存在就创建，已存在也不报错

leaves_raw ="""name,dept,days
张三,研发,2
李四,销售,5
王五,研发,
赵六,销售,三
钱七,财务,4"""

with open(DATA_DIR/ "leaves_raw.csv","w",encoding="utf-8") as f:
    f.write(leaves_raw)
# orders_text = """order_id,city,amount,status
# 01,南京,120.0,paid
# 02,上海,80.5,refunded
# 03,南京,abc,paid
# 04,杭州,45,paid
# 05,上海,,paid
# 06,南京,200,paid
# 07,杭州,-10,paid
# """
#
# with open(DATA_DIR / "order_raw.csv", "w", encoding="utf-8-sig") as f:
#     f.write(orders_text)
#
# tickets_text = """ticket_id,agent,priority,minutes
# T100,小王,high,40
# T101,小李,low,12
# T102,小王,high,
# T103,小张,mid,abc
# T104,小李,high,95
# """
# with open(DATA_DIR / "ticket_raw.csv", "w", encoding="utf-8-sig") as f:
#     f.write(tickets_text)
#
# statement = {
#     "account": "6222021231234567890123",
#     "mouth": "2026-10",
#     "item": [
#         {"date": "10-01", "category": "餐饮", "amount": -45.5},
#         {"date": "10-02", "category": "工资", "amount": 12000},
#         {"date": "10-03", "category": "餐饮", "amount": -88.0},
#         {"date": "10-04", "category": "购物", "amount": -2300},
#         {"date": "10-05", "category": "交通"},
#         {"date": "10-06", "category": "餐饮", "amount": "-32.0"},
#     ]
# }
# with open(DATA_DIR / "bank_statement.json", "w", encoding="utf-8") as f:
#     json.dump(statement, f, ensure_ascii=False, indent=2)
#
# with open(DATA_DIR / "broken.json", "w", encoding="utf-8") as f:
#     f.write('{"account":"622202","item":[{"amount":-10')  # 故意写一个坏掉的JSON
#
# print("示例数据已生成", [p.name for p in DATA_DIR.iterdir()])
