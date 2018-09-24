# pipe-runner

This package contains a simple command line helper for running Snakemake workflows on the Shark cluster using sensible default values.  

## Installation

```
pip install git+git@git.lumc.nl:PharmacogenomicsPipe/pipe_runner.git
```

## Usage

```
Usage: pipe-runner [OPTIONS] [ADDITIONAL_ARGS]...

Options:
  -s, --snakefile PATH       path to the snakemake file to be run
  -d, --directory PATH       Directory for pipeline output
  -e, --extraconfig TEXT     string containing additional config parameters
  -c, --configfile PATH      path to an additional config file containing run-
                             specific parameters
  -cl, --clusterconfig PATH  path to the cluster configuration file
  -r, --retries INTEGER
  --help                     Show this message and exit.
```
