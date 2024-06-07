from flask import Flask, render_template, request
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics import classification_report


import pickle

app = Flask(__name__)

print("Flask server started")

# Load the models once when the app starts
MODEL_PATH1 = 'website/model/predictor.pickle'
MODEL_PATH2 = 'website/model/rfcpredictor3.pickle'

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


model1 = load_model(MODEL_PATH1)
model2 = load_model(MODEL_PATH2)

def prediction(model, features):
    return model.predict([features])

@app.route('/', methods=['POST', 'GET'])
def index_model1():
    pred_value = None

    print("******** open home page ************")


    #model_path = '/static/models/avatar.glb'  # Default model
    if request.method == 'POST':
        try:
            Chest = float(request.form['Chest'])
            Shoulder = float(request.form['Shoulder'])
            Length = float(request.form['Length'])
            Brand = request.form['brandname']
            Type = request.form['Type']
            
            feature_list1 = [Chest, Shoulder, Length]
            
            feature_list1.append(1 if Brand == 'Brand Name_Robato' else 0)
            feature_list1.append(1 if Type == 'Type_slim fit' else 0)
            feature_list1.append(1 if Type == 'Type_trim fit' else 0)

            
            print("Feature list:", feature_list1)

           

            pred_value = prediction(model1, feature_list1)
            print(f"Prediction from model 1: {pred_value[0]}")

            


        except ValueError as e:
            print(f"Error in input conversion: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    return render_template("index_model1.html", pred_value=pred_value)

@app.route('/model2', methods=['POST', 'GET'])
def index_model2():
    pred_value = None
    print("******** Try Fittone page ************")
    model_path = '/static/models/avatar.glb'  # Default model

    if request.method == 'POST':
        try:
            Factory_CS = float(request.form['Factory CS'])
            Chest = float(request.form['Chest'])
            Shoulder = float(request.form['Shoulder'])
            Length = float(request.form['Length'])
            Brand = request.form['brandname']
            Type = request.form['Type']
            
            feature_list2 = [Factory_CS,Chest, Shoulder, Length ] 
            
            feature_list2.append(1 if Brand == 'Brand Name_Robato' else 0)
            feature_list2.append(1 if Type == 'Type_slim fit' else 0)
            feature_list2.append(1 if Type == 'Type_trim fit' else 0)

            print("Feature list:", feature_list2)

            pred_value = prediction(model2, feature_list2)
            print(f"Prediction from model 2: {pred_value[0]}")
            
            if pred_value[0] == "thight_chest":
                model_path = '/static/models/chestthight.glb'

            elif pred_value[0] == "thight_chest , sholder":
                model_path = '/static/models/Allthight.glb'

            elif pred_value[0] == "thight_sholder":
                model_path = '/static/models/Sholderthight.glb'

            elif pred_value[0] == "loose_chest":
                model_path = '/static/models/chestloose.glb'

            elif pred_value[0] == "loose_chest,shoulder":
                model_path = '/static/models/alllose1.glb'

            elif pred_value[0] == "loose_shoulder":
                model_path = '/static/models/sholderlose.glb'

            elif pred_value[0] == "fit_perfect":
                model_path = '/static/models/perfect.glb'

            elif pred_value[0] == "thight_chest_loose_shoulder":
                model_path = '/static/models/alllose1.glb'

            elif pred_value[0] == "loose_chest_thight_sholder":
                model_path = '/static/models/alllose1.glb'
                
            print(f"Uploded Avatar path:",model_path)


            # Add more conditions as necessary
            
        
        except ValueError as e:
            print(f"Error in input conversion: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    return render_template('index_model2.html', pred_value=pred_value, model_path=model_path)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6001)


"""from flask import Flask, render_template, request
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics import classification_report


import pickle

app = Flask(__name__)

# Load the models once when the app starts
MODEL_PATH1 = 'website/model/predictor.pickle'
MODEL_PATH2 = 'website/model/rfcpredictor3.pickle'

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


model1 = load_model(MODEL_PATH1)
model2 = load_model(MODEL_PATH2)

def prediction(model, features):
    return model.predict([features])

@app.route('/', methods=['POST', 'GET'])
def index_model1():
    pred_value = None
    if request.method == 'POST':
        try:
            Chest = float(request.form['Chest'])
            Shoulder = float(request.form['Shoulder'])
            Length = float(request.form['Length'])
            Brand = request.form['brandname']
            Type = request.form['Type']
            
            feature_list1 = [Chest, Shoulder, Length]
            
            feature_list1.append(1 if Brand == 'Brand Name_Robato' else 0)
            feature_list1.append(1 if Type == 'Type_slim fit' else 0)
            feature_list1.append(1 if Type == 'Type_trim fit' else 0)

            print("Feature list:", feature_list1)

            pred_value = prediction(model1, feature_list1)
            print(f"Prediction from model 1: {pred_value[0]}")
        except ValueError as e:
            print(f"Error in input conversion: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    return render_template("index_model1.html", pred_value=pred_value)

@app.route('/model2', methods=['POST', 'GET'])
def index_model2():
    pred_value = None
    model_path = '/static/models/avatar.glb'  # Default model

    if request.method == 'POST':
        try:
            Factory_CS = float(request.form['Factory CS'])
            Chest = float(request.form['Chest'])
            Shoulder = float(request.form['Shoulder'])
            Length = float(request.form['Length'])
            Brand = request.form['brandname']
            Type = request.form['Type']
            
            feature_list2 = [Factory_CS,Chest, Shoulder, Length ] 
            
            feature_list2.append(1 if Brand == 'Brand Name_Robato' else 0)
            feature_list2.append(1 if Type == 'Type_slim fit' else 0)
            feature_list2.append(1 if Type == 'Type_trim fit' else 0)

            print("Feature list:", feature_list2)

            pred_value = prediction(model2, feature_list2)
            print(f"Prediction from model 2: {pred_value[0]}")
            
            if pred_value[0] == "thight_chest":
                model_path = '/static/models/avatar.glb'
            elif pred_value[0] == "thight_chest , sholder":
                model_path = '/static/models/avatar2.glb'

            # Add more conditions as necessary
            
        except ValueError as e:
            print(f"Error in input conversion: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    return render_template('index_model2.html', pred_value=pred_value, model_path=model_path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6001)"""


"""app = Flask(__name__)

# Load the models once when the app starts
MODEL_PATH1 = 'website/model/predictor.pickle'
MODEL_PATH2 = 'website/model/rfcpredictor3.pickle'

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


model1 = load_model(MODEL_PATH1)
model2 = load_model(MODEL_PATH2)

def prediction(model, features):
    return model.predict([features])

@app.route('/', methods=['POST', 'GET'])
def index_model1():
    pred_value = None
    if request.method == 'POST':
        try:
            Chest = float(request.form['Chest'])
            Shoulder = float(request.form['Shoulder'])
            Length = float(request.form['Length'])
            Brand = request.form['brandname']
            Type = request.form['Type']
            
            feature_list1 = [Chest, Shoulder, Length]
            
            Brand_list = ['Brand Name_Robato']
            Type_list = ['Type_slim fit', 'Type_trim fit']

            feature_list1.append(1 if Brand == 'Brand Name_Robato' else 0)
            feature_list1.append(1 if Type == 'Type_slim fit' else 0)
            feature_list1.append(1 if Type == 'Type_trim fit' else 0)

            print("Feature list:", feature_list1)

            pred_value = prediction(model1, feature_list1)
            print(f"Prediction from model 1: {pred_value[0]}")
            pass
        except ValueError as e:
            print(f"Error in input conversion: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    return render_template("index_model1.html", pred_value=pred_value)

@app.route('/model2', methods=['POST', 'GET'])
def index_model2():
    pred_value = None
    model_path = '/static/models/avatar.glb'  # Default model

    if request.method == 'POST':
        try:
            Factory_CS = float(request.form['Factory CS'])
            Chest = float(request.form['Chest'])
            Shoulder = float(request.form['Shoulder'])
            Length = float(request.form['Length'])
            Brand = request.form['brandname']
            Type = request.form['Type']
            
            feature_list2 = [Chest, Shoulder, Length]
            
            Brand_list = ['Brand Name_Robato']
            Type_list = ['Type_slim fit', 'Type_trim fit']

            feature_list2.append(1 if Brand == 'Brand Name_Robato' else 0)
            feature_list2.append(1 if Type == 'Type_slim fit' else 0)
            feature_list2.append(1 if Type == 'Type_trim fit' else 0)

            print("Feature list:", feature_list2)

            
            
            pred_value = index_model2(request.form)

            if pred_value == "thight_chest":
                model_path = '/static/models/avatar.glb'
            elif pred_value == "thight_chest , sholder":
                model_path = '/static/models/avatar2.glb'

            # Add more conditions as necessary



            pred_value = prediction(index_model2, feature_list2)
            print(f"Prediction from model 2: {pred_value[0]}")
            pass
        except ValueError as e:
            print(f"Error in input conversion: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    #return render_template("index_model2.html", pred_value=pred_value)
            
    return render_template('index_model2.html', pred_value=pred_value, model_path=model_path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6001) """






""" def prediction(lst):
    filename = '/Users/dilshan/Desktop/project/model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value
 
@app.route('/', methods=['POST','GET'])
def index():
  pred_value = 0
  if request.method == 'POST':
    Chest = request.form ['Chest']
    Shoulder = request.form['Shoulder']
    Length = request.form['Length']
    Brand = request.form['brandname']
    Type = request.form['Type']
    
    
    
    #print(Chest,Shoulder,Length,Brand,Type)

    feature_list =[]
    feature_list.append(float(Chest))
    feature_list.append(float(Shoulder))
    feature_list.append(float(Length))
    
    Brand_list = ['Brand Name_Robato']
    Type_list = ['Type_slim fit','Type_trim fit']

    for item in Brand_list:
      if item == Brand:
        feature_list.append(1)
      else:
        feature_list.append(0)

    for item in Type_list:
      if item == Type:
        feature_list.append(1)
      else:
        feature_list.append(0)    

    print(feature_list)
     
    pred_value = prediction(feature_list)
    print(f"Prediction: {pred_value[0]}")
   
  return render_template("index.html",pred_value =pred_value)
  

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6001) """
