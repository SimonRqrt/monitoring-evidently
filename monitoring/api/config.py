import pickle


def load_model():
    with open('models/model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def prediction(model, data):
    predictions = model.predict(data)
    return predictions 