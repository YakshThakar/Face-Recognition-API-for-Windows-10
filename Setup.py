from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'face_recognition_models>=0.3.0',
    'Click>=6.0',
    'dlib>=19.7',
    'numpy',
    'Pillow',
    'scipy>=0.17.0'
]

test_requirements = [
    'tox',
    'flake8==2.6.0'
]

setup(
    name='face_recognition',
    version='1.1.0',
    description="Recognize faces from Python or from the command line",
    long_description=readme + '\n\n' + history,
    author="Adam Geitgey",
    Updated_by="Yaksh Thakar"
    author_email='yakshthkar264@gmail.com',
    url='https://github.com/ageitgey/face_recognition',
    This is For Windows 7,8,10 User 
    packages=[
        'face_recognition',
    ],
    package_dir={'face_recognition': 'face_recognition'},
    package_data={
        'face_recognition': ['models/*.dat']
    },
    entry_points={
        'console_scripts': [
            'face_recognition=face_recognition.cli:main'
        ]
    },
    install_requires=requirements,
    license="YBlog",
    zip_safe=False,
    keywords='face_recognition',
    classifiers=[
        'Development Status ::Fresh
        'Intended Audience :: Developers
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
