from distutils.core import setup

setup(
    name = 'ohbotWin',
    packages = ['ohbotWin'],
    package_data={'': ['MotorDefinitionsv21.omd','Silence1.wav']},
    include_package_data=True,
    version = '1.14',  
    description = 'Python library for controlling Ohbot on Windows',
    author = 'ohbot',
    author_email = 'info@ohbot.co.uk',
    url = 'https://github.com/ohbot/ohbotWin-python',
    download_url = 'https://github.com/ohbot/ohbotWin-python/archive/1.14.tar.gz',
    keywords = ['ohbot', 'robot'],
    classifiers = [],
    install_requires=[
          'pyserial','comtypes','lxml',
      ],
)
