from setuptools import setup, find_packages

setup(
    name='kcsf',  # Replace with your project's name
    version='5.0.4',  # Project version
    packages=find_packages(),  # Automatically find packages in the project
    include_package_data=True,
    description='A simple Django app',  # A short description of your project
    long_description=open('README.md').read(),  # Long description read from the README.md
    long_description_content_type='text/markdown',
    install_requires=[
        'Django>=3.2',  # Replace or add any additional packages with their versions here
        'gunicorn',  # WSGI HTTP Server for UNIX
        # Add other dependencies as needed
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
    classifiers=[
        'Development Status :: 3 - Alpha',  # Development status
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',  # The license as you choose
    ],
    author='Trey Hulse',  # Your name
    author_email='trey.hulse@kcstorefixtures.com',  # Your email
    keywords='django heroku webapp',  # Keywords for your project
    url='https://github.com/yourusername/kcsf',  # Link to your project's repository or website
)
