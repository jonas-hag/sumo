# command_line
__version__ = "0.1.2"
SUMO_COMMANDS = ["prepare", "run", "evaluate"]

# prepare
CORR_METHODS = ["pearson", "spearman"]
SIMILARITY_METHODS = ["euclidean", "cosine"] + CORR_METHODS
TXT_EXT = [".txt", '.txt.gz', '.txt.bz2']
TSV_EXT = [".tsv", '.tsv.gz', '.tsv.bz2']
TEXT_EXT = TXT_EXT + TSV_EXT
SUPPORTED_EXT = [".npz"] + TEXT_EXT

PREPARE_DEFAULTS = {
    "method": ["euclidean"],
    "k": 0.1,
    "alpha": 0.5,
    "missing": [0.1],
    "names": None,
    "sn": 0,
    "fn": 0,
    "df": 0.1,
    "ds": 0.1,
    "logfile": None,
    "log": "INFO",
    "plot": None,
    "atol": 1e-2
}
PREPARE_ARGS = ["infiles", "outfile"] + list(PREPARE_DEFAULTS.keys())  # 3 positional args

# run
CLUSTER_METHODS = ["max_value", "spectral"]
RUN_DEFAULTS = {
    "sparsity": [0.1],
    "n": 50,
    "method": "max_value",
    "max_iter": 500,
    "tol": 1e-5,
    "calc_cost": 20,
    "logfile": None,
    "log": "INFO",
    "h_init": None,
    "t": 1
}
RUN_ARGS = ["infile", "k", "outdir"] + list(RUN_DEFAULTS.keys())  # 3 positional args

# evaluate args
EVALUATE_DEFAULTS = {
    "metric": None,
    "logfile": None
}
EVALUATE_ARGS = ["infile", "labels_file"] + list(EVALUATE_DEFAULTS.keys())  # 2 positional args

# utils
LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING']
CLUSTER_METRICS = ['NMI', 'purity', 'ARI']
