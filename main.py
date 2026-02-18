import torch
from torchvision import models
from PIL import Image
import time
import requests


weights = models.EfficientNet_V2_L_Weights.DEFAULT
model = models.efficientnet_v2_l(weights=weights)
model.eval()
preprocess = weights.transforms()

print("Sistema de reconhecimento de imagem (SRI)")
print("Desenvolvido e programado por:")
print("José Pedro Felício Moura Castro")
print("18/02/2026")
resposta = str("a")
repeater = int(1)
while repeater==1:
    resposta = (input("Deseja ver o preprocess? (s/n) ").lower())
    if resposta == "s":
        print("PREPROCESS:")
        time.sleep(1)
        print(preprocess)

    img_url = input("insira um link (ex: https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg)").strip()
    img = Image.open(requests.get(img_url, stream=True).raw)


    batch = preprocess(img).unsqueeze(0)

    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]
    print("O programa acha que é: {} com {}% de certeza." .format(category_name, score*100))
    again = "a"
    while again!="s" and again != "n":
        again =input("quer repetir novamente? (s/n)").lower().strip()
        if again == "n":
            repeater=0
            again = "s"
        elif again == "s":
            break
        else:
            print("Escreva apenas sim (s) ou não (n) ")