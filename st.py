import streamlit as st
import pandas as pd
import numpy as np
import warnings
import plotly.express as px

# 方法一：忽略所有来自'openpyxl.styles.stylesheet'模块的UserWarning
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl.styles.stylesheet')

df = pd.read_excel('datas.xlsx',index_col='Time')

# 将索引格式转换为日期时间格式
df.index = pd.to_datetime(df.index)

# 获取每天第一条数据
df_first_data = df.resample('D').first().T

# # 获取每天最后一条数据
# # df_last_data = df.resample('D').last()

# st.write("每天第一条数据")
# # st.line_chart(df_first_data, y_min=3.0)
# selected_columns = st.multiselect(
#     "选择要显示的列", df_first_data.columns.tolist(), default=df_first_data.columns.tolist()
# )
# df_first_data = df_first_data[selected_columns]
# st.line_chart(df_first_data, use_container_width=True)


# 设置页面配置：宽屏和深色主题
st.set_page_config(layout="wide")

# 假设df_first_data已经存在
# 如果不存在，我们需要加载数据，例如：
# df_first_data = pd.read_csv('voltage_data.csv')

# 获取列名（日期列）并尝试按日期排序
try:
    # 尝试将列名转换为日期对象并排序
    sorted_columns = sorted(df_first_data.columns, key=lambda x: pd.to_datetime(x))
except:
    # 如果转换失败，则按字符串排序
    sorted_columns = sorted(df_first_data.columns)

# # 创建多选组件，让用户选择要显示的日期列
# selected_dates = st.multiselect(
#     "选择要显示的日期",
#     sorted_columns,
#     default=sorted_columns   # 默认显示所有日期
# )

# 根据用户选择显示DataFrame的相应列
# if selected_dates:
#     fig = px.line(df_first_data[selected_dates])
#     fig.update_layout(yaxis_range=[3, 3.4])  # 设置y轴范围
#     st.plotly_chart(fig, use_container_width=True)
# else:
#     st.warning("请至少选择一个日期进行显示。")


fig = px.line(df_first_data, title="捷克箱间主动均衡效果-折线图", height=800)
fig.update_layout(xaxis_title="Cell Index", yaxis_title="Cell Voltage (V)", yaxis_range=[3, 3.4])  # 设置y轴范围
st.plotly_chart(fig, use_container_width=True)

fig_multi_box = px.box(
    df_first_data,
    # points="all",    
    title="捷克箱间主动均衡效果-箱型图",
    width=1200,
    height=600
)
fig_multi_box.update_layout(xaxis_title="Date", yaxis_title="Voltage (V)")
# fig_multi_box.show()
st.plotly_chart(fig_multi_box, use_container_width=True)


