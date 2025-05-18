from setuptools import setup, find_packages

setup(
    name="django-auto-model-loader",
    version="1.0",  
    packages=find_packages(),  
    include_package_data=True, 
    install_requires=[
        "Django>=1.8",
        "inflection>=0.5.1",
    ],
    author="Dennis Tverdostup",
    author_email="denystverdostup@gmail.com",
    description="Middleware for auto-loading Django models from URL parameters",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Volbeck/django_auto_model_loader",
    classifiers=[
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
)
