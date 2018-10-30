from toolchain import PythonRecipe

class Asn1cryptRecipe(PythonRecipe):
    version = "master"
    url = "https://github.com/wbond/asn1crypto/archive/{version}.zip"
    depends = ["openssl", "python"]

recipe = Asn1cryptRecipe()
