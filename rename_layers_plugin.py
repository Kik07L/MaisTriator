import os
import torch
import torchvision.models as models
from PIL import Image
from torchvision import transforms

# load resnet
def load_resnet_model():
    model = models.resnet50()
    model.load_state_dict(torch.load(os.path.join(os.path.dirname(__file__), "resnet_weights/resnet50_weights.pth")))
    model.eval()
    return model

# tentative de prédi avec resnet ( pas sur que ca marche cette merde )
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

# F1
def main():
    # load resnet2
    resnet_model = load_resnet_model()
    class_names = ["jambes", "corps", "visage"]  # list des noms de classes

    # recup le projet actif ( pas sur que ce soit comme ca qu'on fait)
    doc = app.ActiveDocument

    # lister les calques
    for layer in doc.Layers:
        # Vérifier si le calque est visible
        if not layer.Visible:
            continue

        # Récupérer l'image du calque
        image = layer.GetContentAsImage()

        # prédi resnet
        predicted_class = predict_class_resnet(image, resnet_model, class_names)

        # rename le calque
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
# mais il a di : oublipa de fair une catégorie exprè line exprè colo et exprè sketch