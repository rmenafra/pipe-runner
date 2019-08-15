from setuptools import setup

setup(
    name="pipe_runner",
    version="0.0.1",
    description="Simple utility for running Snakemake pipelines on the LUMC SGE cluster",
    autor="Guy Allard, LUMC",
    author_email="guyallard01 at gmail dot com",
    url="https://github.com/lumc-pgx/pipe-runner",
    license="MIT",
    platforms=['linux'],
    packages=["pipe_runner"],
    install_requires=[
        'click'
    ],
    entry_points={
        "console_scripts": ['pipe-runner=pipe_runner.command_line:runner']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'License :: MIT License',
    ],
    keywords = 'bioinformatics snakemake'
)
