class Asset():
    def __init__(self):
        pass
    def __abs__(self):
        pass

    def classify(self):
        return { "falttype": "mechanical", "severity": "high", "confidence": 8}
    

asset = Asset()
classify = asset.classify()
print(classify)