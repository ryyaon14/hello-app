import streamlit as st

st.write('hello world!')
st.write("""
simple iris flower prediction app
this app predicts the oris flower type!
""")




st.sidebar.header('user input parameters')

def user_input_features():
  sepal_length= st.sidebar.slider('sepal length' , 4.3 , 7.9,5.4)
  sepal_width= st.sidebar.slider('sepal width' , 2.0 , 4.4 , 3.4)
  petal_length= st.sidebar.slider('petal length' , 1.0, 6.9 , 1.3)
  petal_width = st.sidebar.slider('petal width' , 0.1 , 2.5 , 0.2)
  data = { 'sepal length' : sepal_length,
           'sepal width' : sepal_width,
           'petal length' :  petal_length,
            'petal width' : petal_width}
  features = pd.DataFrame(data, index=[0])
  return features
  
df = user_input_features()

st.subheader('User input parameters')
st.write(df)

iris=datasets.load_iris()
X= iris.data
Y=iris.target

clf=RandomForestClassifier()
clf.fit(X,Y)

prediction=clf.predict(df)
prediction_proba=clf.predict_proba(df)

st.subheader('Class lables and thier corresponding index number')
st.write(iris.target_names)

st.subheader('prediction')
st.write(iris.target_names[prediction])

st.subheader('prediction_probapilty')
st.write(iris.target_names[prediction_proba])
