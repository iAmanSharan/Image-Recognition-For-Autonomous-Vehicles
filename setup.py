from setuptools import setup , find_packages

setup(
  name = 'Image-Recogniton-For-Autonomous-Vehicles',
  author_name = 'iAmanSharan',
  author_email = 'www.araj232@gmail.com',
  version = "0.0.0",
  decription =  "Image recgnition for autonomous vehuicles , deployed over cloud services like  azure",
  url = "https://github.com/iAmanSharan/Image-Recognition-For-Autonomous-Vehicles",
  packages = setuptools.find_packages(where = 'src')
)