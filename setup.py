from setuptools import setup


setup(name='web3_app',
version='0.2.5',
description="""The source of Web3.""",
long_description_content_type="text/markdown",
include_package_data=True,
long_description="".join(open("README.md", encoding="utf-8").readlines()),
url='https://github.com/Naruno/Web3_App',
author="Naruno Developers",
author_email='onur.atakan.ulusoy@naruno.org',
license='MIT',
packages=["web3_app"],
package_dir={'':'src'},
install_requires=[
    "fire==0.5.0",
    "naruno_remote_app",
    "naruno",
    "kot==0.20.2",
    "flet==0.8.4"
],
entry_points = {
    'console_scripts': ['web3=web3_app.web3_app:main','web3_web=web3_app.web3_app:web_main'],
},
python_requires=">= 3",
zip_safe=False)
