# -*- coding = utf-8 -*-
"""
# @Time : 2023/7/31 19:35
# @Author : CSDN:FriKlogff
# @File : PublicFunctions.py
# @Software: PyCharm
# @Function: 请输入项目功能
"""

import os
os.system("""python -m pip install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade pip setuptools
pip install -i https://mirrors.aliyun.com/pypi/simple/ websocket
pip install -i https://mirrors.aliyun.com/pypi/simple/ websocket-client
pip install -i https://mirrors.aliyun.com/pypi/simple/ gradio
pip install -i https://mirrors.aliyun.com/pypi/simple/ sxtwl
""")
import sxtwl
from XhApi import *
import XhApi

# print(XhApi.response_content)
Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
appid = ''
api_secret = ''
api_key = ''
gpt_url = ''


def generate_bazi(year, month, day, hour):
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)

    date = sxtwl.fromSolar(year, month, day)
    # 获取年柱
    yTG = date.getYearGZ()
    ganzhi_year = Gan[yTG.tg] + Zhi[yTG.dz]

    # 获取月柱
    mTG = date.getMonthGZ()
    ganzhi_month = Gan[mTG.tg] + Zhi[mTG.dz]

    # 获取日柱
    dTG = date.getDayGZ()
    ganzhi_day = Gan[dTG.tg] + Zhi[dTG.dz]

    # 获取时柱
    dayGan = dTG.tg
    hTG = sxtwl.getShiGz(dayGan, hour)
    ganzhi_hour = Gan[hTG.tg] + Zhi[hTG.dz]

    return f"{ganzhi_year}年{ganzhi_month}月{ganzhi_day}日{ganzhi_hour}时"


def xh_api( user_appid, user_api_secret, user_api_key, user_gpt_url):
    global appid, api_secret, api_key, gpt_url
    if user_appid == '' or user_api_secret == '' or user_api_key == '' or user_gpt_url == '':
        return "any api cannot be empty!"
    appid = str(user_appid)
    api_secret = str(user_api_secret)
    api_key = str(user_api_key)
    gpt_url = str(user_gpt_url)
    # print(type(appid), type(api_secret), type(api_key), type(gpt_url))
    # print(appid, api_secret, api_key, gpt_url)
    return "appid = "+appid+"\napi_secret = "+api_secret+"\napi_key = "+api_key+"\ngpt_url = "+gpt_url


def horoscope_reading(sex, name, birth_year, birth_month, birth_day, birth_hour, star):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url
    birth_year = str(int(birth_year))
    if sex is None:
        return "sex cannot be empty!"
    if name == '' or birth_year == '' or birth_month == '' or birth_day == '' or birth_hour == '' or star == '':
        return "Name or birth_year or birth_month or birth_day or star cannot be empty!"
    if birth_year == "0":
        return "0 is not a suitable value of birth_year!"
    template = "假设你是一位专业的星座运势分析师,根据客户提供的出生日期和时间,你需要进行以下几方面的详细分析工作:\n" \
               "1. 分析用户的星座及性格特点\n" \
               "2. 根据月球周期判断事业和学业趋势\n" \
               "3. 提供维持提升感情的建议\n" \
               "4. 预测财务收入和投资趋势\n" \
               "5. 提出健康保健建议\n" \
               "作为专业分析师,你需要用通俗语言解释理论,并提供专业建议\n"
    template += "客户信息:\n"
    template += "性别:{sex}\n"
    template += "姓名:{name}\n"
    template += "星座:{star}\n"
    template += "出生日期:{birth_year}-{birth_month}-{birth_day}-{birth_hour}"
    question = template.format(sex=sex, name=name, birth_year=birth_year, birth_month=birth_month, birth_day=birth_day,
                               birth_hour=birth_hour,
                               star=star)
    # print(appid, api_secret, api_key, gpt_url)
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)


def tarot_reading(question, num_cards):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url
    if question == '' or num_cards is None or num_cards == 0:
        return "question ornum_cards cannot be empty!"
    template = "假设你是一位专业的塔罗牌占卜师。用户提出的问题是:{question}。"
    template += "根据用户的问题,你需要为TA抽取{num_cards}张塔罗牌,"
    template += "解读每张塔罗牌的含义,"
    template += "综合牌面分析用户所问的问题,"
    template += "并根据占卜结果给予专业的建议。"
    template += "具体来说,你需要:\n"
    template += "1. 为用户抽取指定数量的塔罗牌\n"
    template += "2. 逐一解析每张塔罗牌的符号和含义\n"
    template += "3. 综合各牌面意义,对用户提问进行占卜分析\n"
    template += "4. 根据占卜结果,给出专业建议或预言"
    question = template.format(question=question, num_cards=int(num_cards))
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)


def marriage_bazi_analysis(name_husband, birth_year_husband, birth_month_husband, birth_day_husband, birth_hour_husband,
                           name_wife, birth_year_wife, birth_month_wife, birth_day_wife, birth_hour_wife):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url
    birth_year_husband = int(birth_year_husband)
    birth_year_wife = int(birth_year_wife)
    if name_husband == '' or birth_year_husband == '' or birth_month_husband == '' or birth_day_husband == '' or birth_hour_husband == '' \
            or name_wife == '' or birth_year_wife == '' or birth_month_wife == '' or birth_day_wife == '' or birth_hour_wife == '':
        return "Name or birth_year or birth_month or birth_day  cannot be empty!"
    if birth_year_husband == 0 or birth_year_wife == 0:
        return "0 is not a suitable value of birth_year!"
    bazi_husband = generate_bazi(birth_year_husband, birth_month_husband, birth_day_husband, birth_hour_husband)
    bazi_wife = generate_bazi(birth_year_wife, birth_month_wife, birth_day_wife, birth_hour_wife)
    # print(bazi_wife, bazi_husband)
    template = "假设你是一位专业的八字合婚分析师,你正在为一对新人进行八字合婚分析。" \
               "分析基于八字五行、十神、四柱的原理判断两人姻缘。重点看天格、年格五行相生相克。" \
               "以下是他们的基本信息\n"
    template += "新郎信息:\n"
    template += "姓名:{name_husband}\n"
    template += "出生日期:{birth_year_husband}-{birth_month_husband}-{birth_day_husband}\n"  # 根据用户的选择生成问题
    template += "八字:{bazi_husband}\n"
    template += "新娘信息:\n"
    template += "姓名:{name_wife}\n"
    template += "出生日期:{birth_year_wife}-{birth_month_wife}-{birth_day_wife}\n"  # 根据用户的选择生成问题
    template += "八字:{bazi_wife}\n"
    template += "作为资深的合婚分析师,你需要:\n"
    template += "1. 分析两人八字五行相生相克关系\n"
    template += "2. 比较两人十神是否匹配\n"
    template += "3. 检查四柱运势是否协调\n"
    template += "4. 给出姻缘匹配度及建议\n"
    question = template.format(name_husband=name_husband, name_wife=name_wife, bazi_husband=bazi_husband,
                               bazi_wife=bazi_wife, birth_year_husband=birth_year_husband,
                               birth_month_husband=birth_month_husband, birth_day_husband=birth_day_husband,
                               birth_year_wife=birth_year_wife, birth_month_wife=birth_month_wife,
                               birth_day_wife=birth_day_wife)
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)



# 兔年运程
def rabbit_year_prediction(sex, name, birth_year, birth_month, birth_day, birth_hour):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url

    birth_year = int(birth_year)
    bazi = generate_bazi(int(birth_year), int(birth_month), int(birth_day), int(birth_hour))
    if sex is None:
        return "sex cannot be empty!"
    if name == '' or birth_year == '' or birth_month == '' or birth_day == '' or birth_hour == '':
        return "Name or birth_year or birth_month or birth_day cannot be empty!"
    if birth_year == 0:
        return "0 is not a suitable value of birth_year!"
    template = "假设你是一位专业的命理师,仔细分析客户信息,结合通胜原理,考量客户的五行八字、天干合化等,对在兔年客户的事业、财富、姻缘等命局进行预测,并给出建议。"
    template += "\n客户信息:\n"
    template += "性别:{sex}\n"
    template += "姓名:{name}\n"
    template += "出生日期:{birth_year}-{birth_month}-{birth_day}-{birth_hour}\n"
    template += "八字:{bazi}\n"
    template += "具体来说,你需要:\n"
    template += "1. 检查客户八字和五行属性\n"
    template += "2. 分析天干合化对命局的影响\n"
    template += "3. 考量通胜原理对运势的作用\n"
    template += "4. 对事业、财富、姻缘等命局给出预测\n"
    template += "5. 提供专业建议"
    question = template.format(sex=sex, name=name, birth_year=birth_year, birth_month=birth_month, birth_day=birth_day,
                               birth_hour=birth_hour, bazi=bazi)
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)



# 公司测名
def company_name_analysis(sex, name, birth_year, birth_month, birth_day, birth_hour, company_name, industry):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url
    birth_year = int(birth_year)
    if sex is None:
        return "sex cannot be empty!"
    if name == '' or birth_year == '' or birth_month == '' or birth_day == '' or birth_hour == '' or company_name == '' or industry == '':
        return "Name or birth_year or birth_month or birth_day  or company_name  or industry cannot be empty!"
    if birth_year == 0:
        return "0 is not a suitable value of birth_year!"
    template = "假设你是一位公司命理专家,根据立命八字学说,姓名、公司名与行业之间存在相生相克的关系," \
               "需要综合考量五行、八卦、吉凶等理论,分析它们之间的互动对企业发展的影响," \
               "发掘其中蕴含的福禄文星,提出建议以改善财运。"
    template += "\n客户信息:\n"
    template += "性别:{sex}\n"
    template += "姓名:{name}\n"
    template += "出生日期:{birth_year}-{birth_month}-{birth_day}-{birth_hour}\n"
    template += "公司名:{company_name}\n"
    template += "行业:{industry}\n"
    template += "具体来说,你需要:\n"
    template += "1. 分析客户姓名五行属性\n"
    template += "2. 考量公司名五行与行业五行关系\n"
    template += "3. 判断相生相克对企业运势的影响\n"
    template += "4. 发掘姓名、公司名蕴含的福星\n"
    template += "5. 提出改善企业财运的专业建议"

    question = template.format(sex=sex, name=name, birth_year=birth_year, birth_month=birth_month, birth_day=birth_day,
                               birth_hour=birth_hour,
                               company_name=company_name, industry=industry)
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)



# 姓名配对
def name_compatibility(name1, name2):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url
    if name1 == '' or name2 == '':
        return "name1 or name2 cannot be empty!"
    template = "假设你是一位姓名学专家。用户提供了两人的姓名:{name1}和{name2}。"
    template += "作为专家,你需要分析他们两人姓名的五行、笔画等特征,"
    template += "判断姓名间的五行关系是否协调、笔画关系是否匹配,"
    template += "从姓名学角度出发,分析这两人的姓名是否配对。"
    template += "具体来说,你需要:\n"
    template += "1. 分析{name1}的五行属性和笔画数\n"
    template += "2. 分析{name2}的五行属性和笔画数\n"
    template += "3. 判断两人姓名的五行相生相克关系\n"
    template += "4. 判断两人姓名笔画数差是否合适\n"
    template += "5. 从姓名学角度给出配对建议\n"
    template += "最后要给出专业建议,说明这对姓名的搭配优劣势。"
    question = template.format(name1=name1, name2=name2)
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)



# 月老姻缘
def yue_lau_affinity(sex, name, birth_year, birth_month, birth_day, birth_hour):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url
    birth_year = int(birth_year)
    bazi = generate_bazi(int(birth_year), int(birth_month), int(birth_day), int(birth_hour))

    if sex is None:
        return "sex cannot be empty!"
    if name == '' or birth_year == '' or birth_month == '' or birth_day == '' or birth_hour == '':
        return "Name or birth_year or birth_month or birth_day cannot be empty!"
    if birth_year == 0:
        return "0 is not a suitable value of birth_year!"
    template = "假设你是一位月老姻缘专家。有客户需要你的帮助,其信息如下:\n"
    template += "性别:{sex}\n"
    template += "姓名:{name}\n"
    template += "出生日期:{birth_year}-{birth_month}-{birth_day}-{birth_hour}\n"
    template += "八字:{bazi}\n"
    template += "作为月老专家,你需要基于客户的姓名、性别、出生日期等信息,"
    template += "来分析其感情运势、最佳配对对象,"
    template += "给出专业的建议,帮助客户找到适合的另一半。"
    template += "具体来说,你需要:\n"
    template += "1. 分析客户八字姻缘格局\n"
    template += "2. 考量姓名数字对婚姻的影响\n"
    template += "3. 判断最佳配对对象的特征\n"
    template += "4. 提出改善感情运势的建议"
    question = template.format(sex=sex, name=name, birth_year=birth_year, birth_month=birth_month, birth_day=birth_day,
                               birth_hour=birth_hour, bazi=bazi)
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)



# 八字精批
def bazi_analysis(sex, name, birth_year, birth_month, birth_day, birth_hour):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url
    birth_year = int(birth_year)
    if sex is None:
        return "sex cannot be empty!"
    if name == '' or birth_year == '' or birth_month == '' or birth_day == '':
        return "Name or birth_year or birth_month or birth_day cannot be empty!"
    if birth_year == 0:
        return "0 is not a suitable value of birth_year!"
    bazi = generate_bazi(int(birth_year), int(birth_month), int(birth_day), int(birth_hour))
    template = "假设你是一位资深的八字命理师。有客户需要你对其八字进行专业精批,其信息如下:\n"

    template += "性别:{sex}\n"
    template += "姓名:{name}\n"
    template += "八字:{bazi}\n"

    template += "作为八字命理专家,你需要根据客户的八字,"
    template += "分析事业财运、健康等方面的运势趋势,"
    template += "具体来说,你需要:\n"
    template += "1. 检查天干五行对事业财运的影响\n"
    template += "2. 分析八字各宫协调性和局部格局\n"
    template += "3. 指出八字优势和劣势\n"
    template += "4. 提出合理的改善建议"

    question = template.format(sex=sex, name=name, bazi=bazi)
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)


def zhiwei_analysis(sex, name, birth_year, birth_month, birth_day, birth_hour):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url
    birth_year = int(birth_year)
    if sex is None:
        return "sex cannot be empty!"
    if name == '' or birth_year == '' or birth_month == '' or birth_day == '':
        return "Name or birth_year or birth_month or birth_day cannot be empty!"
    if birth_year == 0:
        return "0 is not a suitable value of birth_year!"
    # print(sex, name, birth_year, birth_month, birth_day)
    bazi = generate_bazi(int(birth_year), int(birth_month), int(birth_day), int(birth_hour))
    template = "假设你是一位紫薇斗数专家,接收到客户的出生八字后,你会依次完成以下步骤:\n" \
               "1. 计算该八字的紫微星位置,代表其总体运势\n" \
               "2. 分析年柱运程,判断事业财运\n" \
               "3. 分析月柱运程,判断感情运\n" \
               "4. 分析日柱运程,判断健康运\n" \
               "5. 综合四柱运势对该客户的综合运势做出详细的预言分析\n" \
               "客户信息：\n" \
               "性别：{sex}\n" \
               "姓名：{name}\n" \
               "八字为：{bazi}"

    question = template.format(sex=sex, name=name, bazi=bazi)
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)



# 姓名分析

def name_analysis(sex, name):
    XhApi.response_content = ''
    global appid, api_secret, api_key, gpt_url
    if sex is None:
        return "sex cannot be empty!"
    if name == '':
        return "Name cannot be empty!"
    template = "假设你是一位姓名学专家,请根据客户的姓名,分析其一生运势。\n"
    template += "要点包括:\n"
    template += "- 姓名的谐音是否吉利\n"
    template += "- 姓名笔画多寡对品性的影响\n"
    template += "- 单名双名优劣\n"
    template += "客户的姓名为 {name},性别为{sex},分析对其事业、婚姻、健康等方面的影响,并提出建议。"
    template += "具体来说,你需要\n"
    template += "1. 分析客户姓名谐音\n"
    template += "2. 判断姓名笔画数命理含义\n"
    template += "3. 讨论单名双名特点\n"
    template += "4. 分析姓名对运势各方面的影响\n"
    template += "5. 提出改善命运的专业建议"
    question = template.format(name=name, sex=sex)
    return main(
        appid=appid,
        api_secret=api_secret,
        api_key=api_key,
        gpt_url=gpt_url,
        question=question)

