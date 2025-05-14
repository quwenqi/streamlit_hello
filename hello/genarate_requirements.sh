#pip3.11 install --upgrade streamlit
streamlit --version

pip3.11 install pipreqs
echo "生成requirements.txt"
pipreqs .. --savepath ./requirements.txt
