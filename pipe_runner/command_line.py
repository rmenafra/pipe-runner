import subprocess
import click

@click.command(short_help="Snakemake pipeline helper")
@click.option("--directory", "-d", type=click.Path(), default="output",
              help="Directory for pipeline output")
@click.option("--extraconfig", "-e", type=click.STRING, 
              help="string containing additional config parameters")
@click.option("--configfile", "-c", type=click.Path(exists=True),
              help="path to an additional config file containing run-specific parameters") 
def runner(directory, extraconfig, configfile):
    args = ["snakemake", "--directory", directory]
    
    if extraconfig is not None:
        args += ["--config", extraconfig]

    if configfile is not None:
        args += ["--configfile", configfile]

    args += [
        "--latency-wait", 90,
        "--drmaa", " -N preprocessor -pe BWA {cluster.threads} -l h_vmem={cluster.vmem} -q all.q -cwd -V -j Y",
        "--drmaa-log-dir", directory + "/cluster_logs",
        "--jobs", 100,
        "--max-jobs-per-second", 10,
        "--cluster-config", "cluster_settings.yaml",
        "--use-conda"
    ]

    subprocess.run([str(arg) for arg in args])
