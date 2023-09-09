# -*- coding = utf-8 -*-
"""
# @Time : 2023/7/31 19:33
# @Author : CSDN:FriKlogff
# @File : app.py
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
from PublicFunctions import *
import gradio as gr

# 定义星座选项
signs = ["白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
         "天秤座", "天蝎座", "射手座", "摩羯座", "水瓶座", "双鱼座"]
cards_num = [1, 2, 3, 4, 5]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
        13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
# 使用 Gradio 的模块化组件，构建包含五个选项卡的界面
with gr.Blocks() as demo:
    with gr.Tab("星火api配置"):
        xh_input = [
                    gr.components.Textbox(label="appid"),
                    gr.components.Textbox(label="api_secret"),
                    gr.components.Textbox(label="api_key"),
                    gr.components.Textbox(label="gpt_url")
                    ]
        xh_output = gr.components.Textbox(label="点击提交返回配置情况，请自行配置星火大模型API再使用后续功能")
        xh_button = gr.components.Button("提交")
        xh_button.click(xh_api, inputs=xh_input, outputs=xh_output
                        )
    with gr.Tab("AI星座解读"):
        horoscope_input = [gr.components.Radio(choices=["男", "女"], label="性别"),
                           gr.components.Textbox(label="姓名"),
                           gr.components.Number(label="出生年份"),
                           gr.components.Dropdown(months, label="出生月份"),
                           gr.components.Dropdown(days, label="出生日"),
                           gr.components.Dropdown(hours, label="出生时辰"),
                           gr.components.Dropdown(signs, label="选择您的星座")
                           ]
        horoscope_output = gr.components.Textbox(label="星座解读(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        horoscope_button = gr.components.Button("提交")
        horoscope_button.click(horoscope_reading, inputs=horoscope_input, outputs=horoscope_output
                               )

    with gr.Tab("AI塔罗牌解读"):
        tarot_input = [gr.components.Textbox(label="你想问的问题"),
                       gr.components.Dropdown(cards_num, label="你想抽几张牌"),
                       ]
        tarot_output = gr.components.Textbox(label="塔罗牌解析(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        upload_button = gr.components.Button("抽取")
        upload_button.click(tarot_reading, inputs=tarot_input, outputs=tarot_output)
    with gr.Tab("AI八字合婚分析"):
        marriage_input = [gr.components.Textbox(label="新郎姓名"),
                          gr.components.Number(label="出生年份"),
                          gr.components.Dropdown(months, label="出生月份"),
                          gr.components.Dropdown(days, label="出生日"),
                          gr.components.Dropdown(hours, label="出生时辰"),

                          gr.components.Textbox(label="新娘姓名"),
                          gr.components.Number(label="出生年份"),
                          gr.components.Dropdown(months, label="出生月份"),
                          gr.components.Dropdown(days, label="出生日"),
                          gr.components.Dropdown(hours, label="出生时辰"),
                          ]
        marriage_analysis_output = gr.components.Textbox(label="婚姻分析(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        analyze_button = gr.components.Button("马上测算")
        analyze_button.click(marriage_bazi_analysis,
                             inputs=marriage_input,
                             outputs=marriage_analysis_output)
    with gr.Tab("AI兔年运程预测"):
        birth_year_input = [gr.components.Radio(choices=["男", "女"], label="性别"),
                            gr.components.Textbox(label="姓名"),
                            gr.components.Number(label="出生年份"),
                            gr.components.Dropdown(months, label="出生月份"),
                            gr.components.Dropdown(days, label="出生日"),
                            gr.components.Dropdown(hours, label="出生时辰"),
                            ]
        prediction_output = gr.components.Textbox(label="运程预测(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        predict_button = gr.components.Button("预测运势")
        predict_button.click(rabbit_year_prediction,
                             inputs=birth_year_input,
                             outputs=prediction_output)
    with gr.Tab("AI公司命理解析"):
        company_name_input = [gr.components.Radio(choices=["男", "女"], label="性别"),
                              gr.components.Textbox(label="姓名"),
                              gr.components.Number(label="出生年份"),
                              gr.components.Dropdown(months, label="出生月份"),
                              gr.components.Dropdown(days, label="出生日"),
                              gr.components.Dropdown(hours, label="出生时辰"),
                              gr.components.Textbox(label="公司名称"),
                              gr.components.Textbox(label="所属行业")]
        name_analysis_output = gr.components.Textbox(label="命理分析(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        analyze_button = gr.components.Button("分析")
        analyze_button.click(company_name_analysis,
                             inputs=company_name_input,
                             outputs=name_analysis_output)
    with gr.Tab("AI姓名配对"):
        name1_input = [gr.components.Textbox(label="姓名1"),
                       gr.components.Textbox(label="姓名2"),
                       ]
        matching_output = gr.components.Textbox(label="配对结果(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        match_button = gr.components.Button("分析配对")
        match_button.click(name_compatibility,
                           inputs=name1_input,
                           outputs=matching_output)

    with gr.Tab("AI月老姻缘"):
        yue_lau_input = [gr.components.Radio(choices=["男", "女"], label="性别"),
                         gr.components.Textbox(label="姓名"),
                         gr.components.Number(label="出生年份"),
                         gr.components.Dropdown(months, label="出生月份"),
                         gr.components.Dropdown(days, label="出生日"),
                         gr.components.Dropdown(hours, label="出生时辰"),
                         ]
        affinity_output = gr.components.Textbox(label="姻缘分析(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        analyze_button = gr.components.Button("分析姻缘")
        analyze_button.click(yue_lau_affinity,
                             inputs=yue_lau_input,
                             outputs=affinity_output)

    with gr.Tab("AI八字精批"):
        bazi_input = [gr.components.Radio(choices=["男", "女"], label="性别"),
                      gr.components.Textbox(label="姓名"),
                      gr.components.Number(label="出生年份"),
                      gr.components.Dropdown(months, label="出生月份"),
                      gr.components.Dropdown(days, label="出生日"),
                      gr.components.Dropdown(hours, label="出生时辰"),
                      ]
        analysis_output = gr.components.Textbox(label="精批结果(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        batch_button = gr.components.Button("八字精批")
        batch_button.click(bazi_analysis,
                           inputs=bazi_input,
                           outputs=analysis_output)

    with gr.Tab("AI姓名分析"):
        name_input = [gr.components.Radio(choices=["男", "女"], label="性别"),
                      gr.components.Textbox(label="姓名")]
        name_output = gr.components.Textbox(label="命理分析(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        analyze_button = gr.components.Button("分析姓名")
        analyze_button.click(name_analysis,
                             inputs=name_input,
                             outputs=name_output)
    with gr.Tab("AI紫薇斗数解析"):
        zhiwei_input = [gr.components.Radio(choices=["男", "女"], label="性别"),
                        gr.components.Textbox(label="姓名"),
                        gr.components.Number(label="出生年份"),
                        gr.components.Dropdown(months, label="出生月份"),
                        gr.components.Dropdown(days, label="出生日"),
                        gr.components.Dropdown(hours, label="出生时辰"),
                        ]
        zhiwei_output = gr.components.Textbox(label="紫薇解读(由于我们的解析是由AI生成的，结果仅供娱乐，如果不成功请多试几次)")
        zhiwei_button = gr.components.Button("解读运势")
        zhiwei_button.click(zhiwei_analysis,
                            inputs=zhiwei_input,
                            outputs=zhiwei_output)
demo.launch()
# demo.launch(share=True)
