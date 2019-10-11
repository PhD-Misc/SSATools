import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()


setuptools.setup(
        name="SSATools",
        version='0.1',        
        scripts=['parallax','rangeCal'],
        author="Steve Prabu",
        description="custom tools",
        packages=setuptools.find_packages(),
        author_email="",url="https://github.com/StevePrabu/SSATools.git",
)

