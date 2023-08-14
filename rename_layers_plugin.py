import re
import os

# Récupère tous les calques du document actif
def get_layers():
    layers = []
    for i, layer in enumerate(app.activeDocument.layers):
        layers.append(layer)
    return layers

# Trie les calques par nom en utilisant la fonction sorted() et renomme
def sort_and_rename_layers(layers):
    sorted_layers = sorted(layers, key=lambda layer: layer.name)
    for i, layer in enumerate(sorted_layers):
        new_name = f"Layer_{chr(65 + i)}"  # Utilise les lettres de l'alphabet (A, B, C, ...)
        layer.name = new_name

# Fonction principale
def main():
    layers = get_layers()
    sort_and_rename_layers(layers)

if __name__ == "__main__":
    import clr
    clr.AddReference("System")
    import System
    from System import Array
    from System.Windows.Forms import MessageBox
    from Autodesk.ClipStudio import *

    main()