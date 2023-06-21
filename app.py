import os
import pandas as pd
import streamlit as st
import datetime
import base64
from footer import layout, link


def download_csv(name, df):
    csv = df.to_csv(index=False)
    base = base64.b64encode(csv.encode()).decode()
    file = (
        f'<a href="data:file/csv;base64,{base}" download="%s.csv">Download file</a>'
        % (name)
    )

    return file


def df_filter(message, df):
    slider_1, slider_2 = st.slider(
        "%s" % (message), 0, len(df) - 1, [0, len(df) - 1], 1
    )

    while len(str(df.iloc[slider_1][1]).replace(".0", "")) < 4:
        df.iloc[slider_1, 1] = "0" + str(df.iloc[slider_1][1]).replace(".0", "")

    while len(str(df.iloc[slider_2][1]).replace(".0", "")) < 4:
        df.iloc[slider_2, 1] = "0" + str(df.iloc[slider_1][1]).replace(".0", "")

    start_date = datetime.datetime.strptime(
        str(df.iloc[slider_1][0]).replace(".0", "")
        + str(df.iloc[slider_1][1]).replace(".0", ""),
        "%Y%m%d%H%M%S",
    )
    start_date = start_date.strftime("%d %b %Y, %I:%M%p")

    end_date = datetime.datetime.strptime(
        str(df.iloc[slider_2][0]).replace(".0", "")
        + str(df.iloc[slider_2][1]).replace(".0", ""),
        "%Y%m%d%H%M%S",
    )
    end_date = end_date.strftime("%d %b %Y, %I:%M%p")

    st.info("Start: **%s** End: **%s**" % (start_date, end_date))

    filtered_df = df.iloc[slider_1 : slider_2 + 1][:].reset_index(drop=True)

    return filtered_df


if __name__ == "__main__":
    df = pd.read_csv("data.csv")

    website_title = os.environ.get("WEBSITE_NAME", "演示网站")
    icp = os.environ.get("ICP", "粤ICP备xxxxxx号")

    st.set_page_config(
        page_title=website_title,
        # page_icon=favicon,
        # layout="wide",
        initial_sidebar_state="auto",
    )
    # favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)
    st.title(website_title)
    filtered_df = df_filter("滑动以过滤数据", df)

    column_1, column_2 = st.columns(2)

    with column_1:
        st.title("数据Data Frame")
        st.write(filtered_df)

    with column_2:
        st.title("表格Chart")
        st.line_chart(filtered_df["values"])

    st.markdown(
        download_csv("Filtered Data Frame", filtered_df), unsafe_allow_html=True
    )
    layout(
        link("https://beian.miit.gov.cn/", icp),
    )
