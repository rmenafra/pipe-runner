from setuptools import setup

setup(
    name="pipe_runner",
    version="0.0.1",
    description="Simple utility for running Snakemake pipelines on the cluster",
    autor="Guy Allard",
    author_email="w.g.allard AT lumc DOT nl",
    url="https://git.lumc.nl/wgallard/pipe_runner.git",
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
