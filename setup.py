import setuptools


setuptools.setup(
    name="executor-image-foo-normalizer",
    version="2.0",
    author='Jina Dev Team',
    author_email='dev-team@jina.ai',
    description="Executor that normalizes images",
    url="https://github.com/nan-wang/executor-image-normalizer.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    py_modules=['jinahub.image.foo_normalizer'],
    package_dir={'jinahub.image': '.'},
    install_requires=open("requirements.txt").readlines(),
    python_requires=">=3.7",
)
