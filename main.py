"""程序入口：只负责”配置+调用“，不写业务逻辑"""

import logging
from pathlib import Path

from biz_tool.cleaner import clean_csv
from biz_tool.stats import sum_by, avg_by

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"


def setup_logging():
    LOG_DIR.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(LOG_DIR / "app.log", encoding="utf-8"),
            logging.StreamHandler()
        ],
    )


def main():
    setup_logging()
    OUT_DIR.mkdir(exist_ok=True)
    logger = logging.getLogger("main")

    leaves, r1 = clean_csv(DATA_DIR / "leaves_raw.csv", "days")
    logger.info("各部门统计%s，异常%s条", sum_by(leaves, "dept", "days"), len(r1.bad_rows))
    r1.save(OUT_DIR / "leaves_report.json")
    orders, r1 = clean_csv(DATA_DIR / "order_raw.csv", "amount")
    paid = [o for o in orders if o["status"] == "paid"]
    logger.info("电商各城市已支付金额：%s", sum_by(paid, "city", "amount"))
    r1.save(OUT_DIR / "order_report.json")

    tickets, r2 = clean_csv(DATA_DIR / "ticket_raw.csv", "minutes")
    logger.info("Saas各客服平均处理时长：%s", avg_by(tickets, "agent", "minutes"))
    r2.save(OUT_DIR / "tickets_reports.json")


if __name__ == "__main__":
    main()
