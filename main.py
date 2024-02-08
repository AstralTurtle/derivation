import flask as fl
import numpy as np
# import builtins
import uuid

# import local module
import plot
# import tests


def generate_plot():
        plot_id = uuid.uuid4()
        # generate a random function
        # generate a random degree
        degree = np.random.randint(2, 10)
        #generate random coefficients
        arr = []
        for i in range(degree):
            arr.append(np.random.randint(-5, 10))
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






if __name__ == "__main__":
    flask_app = fl.Flask(__name__)
    @flask_app.route('/')
    def index():
        return
        

        




    # load image files to an array
    paths = generate_plot()

    images = []
    for path in paths:
        images.append(
            # testing, open the file and read it
            open(path, 'rb'))
    for image in images:
        print(image.read())
    for image in images:
        # close the file
        image.close()
        # images.append(fl.send_file(path, mimetype='image/png'))
    

