"""统计函数：与行业无关，只认字段名"""


def count_by(records, field):
    """按某个字段计数，返回{字段值：条数}"""
    counts = {}
    for r in records:
        key = r[field]
        counts[key] = counts.get(key, 0) + 1
    return counts


def sum_by(records, group_field, value_field):
    """按group_field分组，对value_field求和"""
    total = {}
    for r in records:
        key = r[group_field]
        total[key] = total.get(key, 0) + r[value_field]
    return total


def avg_by(records, group_field, value_field):
    """返回每组的平均值"""
    count = count_by(records, group_field)
    total = sum_by(records, group_field, value_field)
    return {k: round(total[k] / count[k], 1) for k in count}
