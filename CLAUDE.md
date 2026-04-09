# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

- Python 3.14 via Homebrew (`/opt/homebrew/bin/python3`)
- Virtual environment at `.venv/` — always run scripts with `.venv/bin/python3`
- AWS credentials in `~/.aws/credentials` (default profile, region `ap-southeast-1`)

## Running Scripts

```bash
.venv/bin/python3 query.py        # Query Juniper vSRX AMIs
.venv/bin/python3 query_kali.py   # Query Kali Linux AMIs
```

## Architecture

Each script is a single standalone file that queries the AWS EC2 Marketplace for AMIs in `ap-southeast-1`. The pattern is:

1. Create a boto3 EC2 client for the target region
2. Call `describe_images(Owners=['aws-marketplace'], Filters=[...])` with name glob patterns
3. Sort results by `CreationDate` descending
4. Print detailed fields per AMI: ID, description, dates, architecture, virtualization, root device/volume, ENA support, public flag

**Key naming quirk:** Juniper vSRX AMIs are published as `junos-vsrx3-*` (lowercase), not `*vSRX*` — the filters account for both patterns.

## Adding a New AMI Query Script

Follow the same structure as `query.py` or `query_kali.py`. Use `Owners=['aws-marketplace']` to restrict to marketplace images. If an expected AMI isn't found, probe with broader name patterns first to discover the actual naming convention used by the publisher.
