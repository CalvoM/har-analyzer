from ninja import NinjaAPI

api = NinjaAPI()


@api.get("")
def home():
    return {"home": "nyumbani"}
