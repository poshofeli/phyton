def readdata():
    with open("data.json","r") as file:
        config = json.load(file)
        return config