# pipe-runner

This package contains a simple command line helper for running Snakemake workflows on the Shark cluster using sensible default values.  

## Installation

```
pip install git+https://github.com/lumc-pgx/pipe-runner.git
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
  -r, --retries INTEGER      Number of times to retry a failed pipeline stage
  -h, --help                 Show this message and exit.

Example:
pipe-runner -s Snakefile -d output_dir -c run_config.yaml -cl cluster_settings.yaml

Modify the run_config.yaml and cluster_settings.yaml according to the location of your data and run parameters.
```

## Outputs
The output of the pipeline includes the following folders

```
-	Annotation
-	Haplotyping
-	Phasing
-	Structural variation
-	Summary
-	Variant calling

```
