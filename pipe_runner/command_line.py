import subprocess
import click
import os

@click.command(context_settings=dict(
    ignore_unknown_options=True,
    help_option_names=["-h", "--help"]
    ),
    short_help="Snakemake pipeline helper"
)
@click.option("--snakefile", "-s", type=click.Path(exists=True),
              help="path to the snakemake file to be run")
@click.option("--directory", "-d", type=click.Path(), default="output",
              help="Directory for pipeline output")
@click.option("--extraconfig", "-e", type=click.STRING, multiple=True, 
              help="string containing additional config parameters")
@click.option("--configfile", "-c", type=click.Path(exists=True),
              help="path to an additional config file containing run-specific parameters")
@click.option("--clusterconfig", "-cl", type=click.Path(exists=True),
              help="path to the cluster configuration file")
@click.option("--retries", "-r", type=int, default=3,
              help="Number of times to retry a failed pipeline stage")
@click.argument('additional_args', nargs=-1, type=click.UNPROCESSED)
def runner(snakefile, directory, extraconfig, configfile, clusterconfig, retries, additional_args):
    args = ["snakemake", "-p", "--directory", directory]

    if snakefile is not None:
        args += ["--snakefile", snakefile]
    
    if configfile is not None:
        args += ["--configfile", configfile]

    if clusterconfig is None:
        cluster_file = os.path.join(os.getcwd(), "cluster_settings.yaml")
    else:
        cluster_file = clusterconfig

    args += ["--cluster-config", cluster_file]
    
    if len(extraconfig):
        args += ["--config"] + list(extraconfig)

    args += [
        "--latency-wait", 300,
        "--restart-times", retries,
        "--drmaa", " -N preprocessor -pe BWA {cluster.threads} -l h_vmem={cluster.vmem} -q all.q -cwd -V -j Y",
        "--drmaa-log-dir", os.path.join(directory, "cluster_logs"),
        "--jobs", 100,
        "--max-jobs-per-second", 10,
        "--use-conda",
        "--conda-prefix", os.path.join(os.getcwd(), ".conda")
    ]

    args += list(additional_args)

    subprocess.run([str(arg) for arg in args])
