from toolchain import CythonRecipe

class BotoRecipe(CythonRecipe):  
    version = "master"
    url = "https://github.com/boto/boto/archive/{version}.zip"
    depends = ["python"]

recipe = BotoRecipe()
