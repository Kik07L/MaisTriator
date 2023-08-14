import re
import os

# Récupère tous les calques du document actif
def get_layers():
    layers = []
    for i, layer in enumerate(app.activeDocument.layers):
        layers.append(layer)
    return layers

# Renomme les calques en ajoutant un numéro à la fin
def rename_layers(layers):
    for i, layer in enumerate(layers):
        new_name = f"Layer_{i + 1}"
        layer.name = new_name

# Fonction principale
def main():
    layers = get_layers()
    rename_layers(layers)

if __name__ == "__main__":
    import clr
    clr.AddReference("System")
    import System
    from System import Array
    from System.Windows.Forms import MessageBox
    from Autodesk.ClipStudio import *

    main()