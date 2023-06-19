export WEBSITE_NAME=深度学习演示网站
export ICP=粤ICP备2022122081号-1

install:
	python3 -m pip install -r requirements.txt
run:
	python3 -m streamlit run app.py --server.port 80