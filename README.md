# MASHUP artefact, packaged for review in a cloud IDE

This repository packages the artefact of

> Rohan Basu Roy, Tirthak Patel, Devesh Tiwari. *MASHUP: Making Serverless
> Computing Useful for HPC Workflows via Hybrid Execution.* PPoPP '22.
> [doi:10.1145/3503221.3508407](https://doi.org/10.1145/3503221.3508407)

as a [devcontainer](https://containers.dev/), so that it opens in VS Code or in
the NFDIxCS Artifact Evaluation Platform's cloud IDE (Coder) with all software
installed. It is a test case for the platform. The original authors are not
involved, and this repository does not contain their artefact. The artefact is
downloaded from Zenodo when the container is created:
[doi:10.5281/zenodo.5733395](https://doi.org/10.5281/zenodo.5733395)
(`MashUP.zip`, md5 `b9e96748b36c7916b93c0df286b69499`, licence
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)).

## What the container provides

- Python 3.6, the language MASHUP is implemented in (`python:3.6-bullseye`).
- `boto3`, the AWS CLI (v1, from pip, as in the artefact's README), `paramiko`
  and `psutil`, pinned to their last Python 3.6 releases
  (`.devcontainer/requirements.txt`). The code imports `paramiko` and
  `psutil`, though the artefact's README does not list them.
- On creation, `.devcontainer/fetch-artefact.py` downloads `MashUP.zip`,
  checks size and md5, and unpacks it into `artefact/hybrid/`. The entry point
  is `artefact/hybrid/README.md`.

## Open it

- **VS Code:** install the Dev Containers extension, open this folder, run
  *Dev Containers: Reopen in Container*.
- **Coder (NFDIxCS AEP):** create a workspace from the template named by the
  AE chairs and give this repository's URL as the artefact source.

## What needs AWS and what does not

Running the experiments (`artefact/hybrid/<workflow>/<exp>/test.py`) needs an
AWS account: an EC2 cluster reachable by SSH, Lambda functions deployed from
`build_lambda/`, an S3 bucket, and `aws configure` with credentials. The
container contains the tools for that but no credentials.

Without AWS you can inspect the code, the deployment instructions, the
pre-compiled task binaries, and the raw results that the authors include for
every configuration (`cost.txt`, `runtime_per_phase.txt`,
`<task>_response.txt` and `<task>_output.txt` under `<workflow>/exp*/`).

First review observations made without AWS are in
[`REVIEW-NOTES.md`](REVIEW-NOTES.md).
