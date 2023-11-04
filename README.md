# Streamlit_Iris
Using the "iris classification" model I created, make it live with streamlit on AWS.

yum install git -y

yum install python3-pip -y

git clone https://github.com/M-Tnhn-Kr/Streamlit_Iris.git

cd Streamlit_Iris/

pip install -r requirements.txt --ignore-installed

streamlit run Iris_Classer_App.py --server.port 8080
