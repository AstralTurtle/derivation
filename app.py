import flask as fl
from flask_cors import CORS
import numpy as np
import base64
# import builtins
import uuid

# import local module
import plot
# import tests
import os

def generate_plot():
        plot_id = uuid.uuid4()
        # generate a random function
        # generate a random degree
        degree = np.random.randint(3, 6)
        #generate random coefficients
        arr = []
        for i in range(degree):
            arr.append(np.random.randint(-5, 5))
        f = np.poly1d(arr)
        # test code
        # print(f)
        # print(f.deriv())
        # print(f.deriv().deriv())

        

        plot.makeImages(f,plot_id)
        # load images to an array
        images = []
        images.append(f'plots/{plot_id}.png')
        images.append(f'plots/{plot_id}_prime.png')
        images.append(f'plots/{plot_id}_double_prime.png')
        return images

def generate_response(imgs):
    return fl.jsonify(
        status = "ok",
        code=200,
        messages = ["done"],
        response = {
            "images": imgs
        }

    )



app = fl.Flask(__name__)
CORS(app)

#

@app.route('/')
def index():
    paths = generate_plot()
    image_data = []
    for path in paths:
        with open(path, 'rb') as f:
            image_base64 = base64.b64encode(f.read()).decode('utf-8')
            image_data.append(image_base64)
    return generate_response(image_data)
    # fl.jsonify(images=image_data,
    #     status=200
    # )    

@app.route('/clear')
def clear():
    # clear the plots directory
    folder = './plots'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
    return "cleared"
    
    
    




if __name__ == "__main__":
    app.run(debug=True)
    x
    

        

        




    
        # what am i doing!
        
    

