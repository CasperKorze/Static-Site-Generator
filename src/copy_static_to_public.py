import os
import shutil


def copy_static_to_public(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)


        if os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)
        elif os.path.isdir(src_path):
                # REKURENCJA: Wywołujemy tę samą funkcję dla podfolderu
                copy_static_to_public(src_path, dest_path)


if os.path.exists("public"):
    shutil.rmtree("public")

copy_static_to_public("static", "public")

