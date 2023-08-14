import torch
import torchvision.models as models
from PIL import Image
from torchvision import transforms

# Charger le modèle ResNet pré-entraîné
def load_resnet_model():
    model = models.resnet50(pretrained=True)
    # Le modèle sera téléchargé automatiquement s'il n'est pas déjà enregistré localement
    return model

# Fonction pour prédire la classe d'une image à l'aide de ResNet
def predict_class_resnet(image, model, class_names):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    img = transform(image).unsqueeze(0)

    model.eval()
    with torch.no_grad():
        outputs = model(img)

    _, predicted = torch.max(outputs, 1)
    class_idx = predicted.item()
    class_name = class_names[class_idx]
    return class_name

# Fonction principale du plugin
def main():
    # Charger le modèle ResNet
    resnet_model = load_resnet_model()
    class_names = ["jambes", "corps", "visage"]  # Remplace par les noms de tes classes

    # Récupérer le document actif
    doc = app.ActiveDocument

    # Parcourir tous les calques du document
    for layer in doc.Layers:
        # Vérifier si le calque est visible
        if not layer.Visible:
            continue

        # Récupérer l'image du calque
        image = layer.GetContentAsImage()

        # Prédire la classe du contenu de l'image à l'aide de ResNet
        predicted_class = predict_class_resnet(image, resnet_model, class_names)

        # Renommer le calque en utilisant la classe prédite
        new_name = f"{layer.Name}_{predicted_class}"
        layer.Name = new_name

if __name__ == "__main__":
    import clr
    clr.AddReference("System")
    import System
    from System import Array
    from System.Windows.Forms import MessageBox
    from Autodesk.ClipStudio import *

    main()
