import os
import streamlit as st
from footer import icp_footer
from content import main_page

website_title = os.environ.get("WEBSITE_NAME", "演示网站")
icp = os.environ.get("ICP", "粤ICP备xxxxxx号")

if __name__ == "__main__":

    st.set_page_config(
        page_title=website_title,
        # page_icon=favicon,
        # layout="wide",
        initial_sidebar_state="auto",
    )
    # st.title(website_title)

    main_page()

    icp_footer(icp)
