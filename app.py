# FLAST USER APP 
import os
from flask import Flask , request , jsonify , render_template
from flask_cors  import CORS , cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.predict import PredictionPipeline

os.putenv('LANG' , 'en_US.UTF-8')
os.putenv('LC_ALL' , 'en_US.UTF-8')


# initialize the flask
app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "InputImage.jpg"
        self.classifier = PredictionPipeline(filename = self.filename)
        

#create default route
@app.route("/" , methods = ['GET'])
@cross_origin()
def home():
    return render_template('index.html')



#train route
@app.route("/train" , methods = ['GET' , 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"


#predict route
@app.route("/predict" , methods = ['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image'] #recieveing the image
    decodeImage(image , clApp.filename) #image is base 64 , needs to decode it
    result = clApp.classifier.predict() #prdict the result for the uploaded image
    return jsonify(result)

   
#calling the class ClientApp 
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host = '0.0.0.0' , port = 8080 , debug = True)
    

    
