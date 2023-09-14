from setuptools import setup , find_packages

setup(
  name = 'CNNproject',
  author = 'iAmanSharan',
  author_email = 'www.araj232@gmail.com',
  version = "0.0.0",
  description =  "Image recgnition for autonomous vehuicles , deployed over cloud services like  azure",
  url = "https://github.com/iAmanSharan/Image-Recognition-For-Autonomous-Vehicles",
  package_dir={'':"src"},
  packages = find_packages(where = 'src')
)