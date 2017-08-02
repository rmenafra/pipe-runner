import subprocess
import click
import os

@click.command(short_help="Snakemake pipeline helper")
@click.option("--directory", "-d", type=click.Path(), default="output",
              help="Directory for pipeline output")
@click.option("--extraconfig", "-e", type=click.STRING, 
              help="string containing additional config parameters")
@click.option("--configfile", "-c", type=click.Path(exists=True),
              help="path to an additional config file containing run-specific parameters") 
@click.argument("targets", nargs=-1)
def runner(directory, extraconfig, configfile, targets):
    args = ["snakemake", "--directory", directory]
    
    if extraconfig is not None:
        args += ["--config", extraconfig]

    if configfile is not None:
        args += ["--configfile", configfile]

    args += [
        "--latency-wait", 90,
        "--drmaa", " -N preprocessor -pe BWA {cluster.threads} -l h_vmem={cluster.vmem} -q all.q -cwd -V -j Y",
        "--drmaa-log-dir", os.path.join(directory, "cluster_logs"),
        "--jobs", 100,
        "--max-jobs-per-second", 10,
        "--cluster-config", os.path.join(os.getcwd(), "cluster_settings.yaml"),
        "--use-conda"
    ]

    if targets is not None and len(targets) > 0:
        for target in targets:
            args.append(target)

    subprocess.run([str(arg) for arg in args])
