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
    model_path = '/static/models/welcomeavatar.glb'  # Default model

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
            
            if pred_value[0] == "Thight in your chest area.":
                model_path = '/static/models/chestthight.glb'

            elif pred_value[0] == "Thight in your chest and shoulder area.":
                model_path = '/static/models/Allthight.glb'

            elif pred_value[0] == "Thight in your shoulder area.":
                model_path = '/static/models/Sholderthight.glb'

            elif pred_value[0] == "Loose in your chest area.":
                model_path = '/static/models/chestloose.glb'

            elif pred_value[0] == "Loose in your chest and shoulder area.":
                model_path = '/static/models/alllose1.glb'

            elif pred_value[0] == "Loose in your shoulder area.":
                model_path = '/static/models/sholderlose.glb'

            elif pred_value[0] == "Fits you perfectly":
                model_path = '/static/models/perfect.glb'

            elif pred_value[0] == "Thight in your chest area and loose in your shoulder area.":
                model_path = '/static/models/tchestlshoulder.glb'

            elif pred_value[0] == "Loose in your chest area and thight in your shoulder area.":
                model_path = '/static/models/lchesttshoulder.glb'
                
            print(f"Uploded Avatar path:",model_path)


            # Add more conditions as necessary
            
        
        except ValueError as e:
            print(f"Error in input conversion: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    return render_template('index_model2.html', pred_value=pred_value, model_path=model_path)

@app.route('/help', methods=['GET'])
def help():
    print("******** Open Help page ************")
    return render_template('help.html')

@app.route('/aboutus', methods=['GET'])
def aboutus():
    print("******** Open About Us page ************")
    
    return render_template('aboutus.html')
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6001)

