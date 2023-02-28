import joblib


def load_model(model_type):
    try:
        if model_type == "grid":
            return joblib.load("src/model/grid.pkl")
    except:
        print(f"Incorrect model type: {model_type}")
        return
