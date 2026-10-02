# Review notes without AWS

First observations from the NFDIxCS AE platform trial (2026-10-01), made by
reading the unpacked Zenodo record. Nothing was executed, and the paper has
not yet been compared. These are notes for a review, not a review: some points
may be explained in the paper. Paths are relative to `artefact/hybrid/`.

- **Missing dependencies in the README:** the code imports `paramiko` (403
  files) and `psutil` (34) besides `boto3`; the README lists only `boto3` and
  `awscli`.

- **README vs content:** `./figures` (promised: "result figures used in the
  paper") is not in the zip. The README says `exp1` is the r5 family, but
  `1000genome/exp1/` holds `m5a.*` configurations.

- **Driver not portable:** `<workflow>/exp*/test.py` hard-codes the key
  `/home/rohan/rohan.pem`, region `us-east-2`, SSH user `ubuntu` (README:
  `ec2-user`), an `instance_ID`, and the bucket `app-bucket-rohan` (in the
  Lambda handlers). It invokes Lambda functions as `run_<task>`, while the
  README creates them as `<task>`.

- **Task binaries are two programs:** all 18 `build_ec2/*.exe` across the
  three workflows are copies of two executables (md5 `98a6a8ab…`, plain C++,
  called with `-s N`; md5 `02e762d5…`, OpenMP, called with `--niter N`). They
  are synthetic stand-ins, not the 1000Genome/SRAsearch/Epigenomics tools.

- **Some Lambda results are not measured:** in 385 of 403 drivers,
  `run_lam()` does not invoke Lambda for the tasks in `lam_red_list`
  (1000genome: `sifting`, `individual_merge`; SRAsearch: `bowtie2_build`,
  `merge1`, `merge2`; epigenomics: `fastqsplit`, `mapmerge`, `chr21`,
  `pileup`). It writes their responses from hard-coded times (`lam_red_exe`,
  `lam_red_read`, `lam_red_write`) plus up to 1 % `random.uniform` noise,
  sleeps for their sum, and counts them in the Lambda cost. Whether the paper
  explains this is open (paper not yet read).

- **Raw results are shipped:** `cost.txt` (Lambda, EC2 cost) and
  `runtime_per_phase.txt` for every workflow × experiment × instance type ×
  strategy (`only_ec2`, `only_lambda`, `hybrid`, `hybrid+`, `technique`,
  `technique+`). The paper's time and cost improvements can be recomputed
  from them without AWS.
