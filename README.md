# ml_demo
Simple Machine Learning deployment to localhost via flask and Jupyter Notebook

--------------------------------------
From the command Line:
- git clone https://github.com/jmeisele/ml_demo.git
- cd ml_demo
- conda create -n ml_demo python=3.7.0
- conda activate ml_demo
- pip install -r requirements.txt
- python jupyter-notebook

After pickling RandomForest model in notebook:
- python ml_flask_demo.py
