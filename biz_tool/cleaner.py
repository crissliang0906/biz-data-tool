"""清洗函数：读取CSV，效验数值字段"""

import csv
import logging

from biz_tool.report import CleanReport

logger =logging.getLogger(__name__)

def to_number(text):
    if text is None or text.strip()=="":
        raise ValueError("为空")
    try:
        return float(text)
    except ValueError:
        raise ValueError("不是数字")

def clean_csv(path,number_field,allow_negative=False):
    """返回（valid,report）"""
    valid =[]
    report = CleanReport(path.name)
    with open(path,encoding="utf-8-sig",newline="") as f:
        for row in csv.DictReader(f):
            try:
                value = to_number(row[number_field])
            except ValueError as e:
                reason =f"{number_field}{e}"
                report.add_bad(row,reason)
                logger.warning("跳过一行：%s，原因：%s",row,reason)
                continue
            if value <0 and not allow_negative:
                reason = f"{number_field}为负数"
                report.add_bad(row,reason)
                logger.warning("跳过一行,%s,原因：%s",row,reason)
                continue
            row[number_field] =value
            valid.append(row)
            report.add_ok()
    logger.info(report.summary())
    return valid,report