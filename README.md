# biz-data-tool

一个用python编写命令的命令行小工具，用来清洗不同行业导出的CSV数据，并按维度汇总统计
这是我学习企业数据交付的个人练习项目，【完成时间：2026年11月】

## 解决什么问题

客户从业务系统导出的数据常有空值、文字写在数字列、负数金额等问题，直接统计会出错或者报错。
本工具会：
- 逐行效验数值字段，不合规的记录跳过、并记录原因，不会因为一条坏数据中断
- 输出清洗报告（总条数、有效条数、各类异常原因及占比）
- 按任意字段分组求和、计数、求平均

## 设计思路
- `biz_tool/` 是与行业无关的工具包，只认字段名，不关心是订单还是工单
- `main.py`只负责配置：读哪个文件、效验哪个字段、按什么维度统计
- 接入新行业时只改`main.py`。已验证电商订单、SaaS工单、HR请假三类数据、工具包无需修改

## 项目结构

```
biz_tool/
  cleaner.py  读取CSV、读取数值字段
  stats.py    分组计数、求和、求平均
  report.py   清洗报告类CleanReport
data/         示例数据  
main.py       程序入口
make_data.py  生成示例数据
```

## 运行方法

需要Python 3.11,仅使用标准库，无需安装第三方包

```
python make_data.py    #生成示例数据
python main.py
```
运行后，`output/`中生成各数据源的清洗报告（JSON）,`logs/app.log`记录处理过程

## 示例输出

```
2026-11-06 19:31:32,851 [WARNING] biz_tool.cleaner: 跳过一行：{'order_id': '03', 'city': '南京', 'amount': 'abc', 'status': 'paid'}，原因：amount不是数字
2026-11-06 19:31:32,851 [WARNING] biz_tool.cleaner: 跳过一行：{'order_id': '05', 'city': '上海', 'amount': '', 'status': 'paid'}，原因：amount为空
2026-11-06 19:31:32,852 [WARNING] biz_tool.cleaner: 跳过一行,{'order_id': '07', 'city': '杭州', 'amount': '-10', 'status': 'paid'},原因：amount为负数
2026-11-06 19:31:32,852 [INFO] biz_tool.cleaner: <bound method CleanReport.summary of <biz_tool.report.CleanReport object at 0x000001694743E350>>
2026-11-06 19:31:32,852 [INFO] main: 电商各城市已支付金额：{'南京': 320.0, '杭州': 45.0}
```
## 后续计划

支持从数据库里读取数据