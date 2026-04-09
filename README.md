# aws_query

A collection of Python scripts to query AWS Marketplace AMIs in the `ap-southeast-1` (Singapore) region using boto3.

## Scripts

| Script | Description |
|--------|-------------|
| `query.py` | Query Juniper vSRX AMIs from the AWS Marketplace |
| `query_kali.py` | Query Kali Linux AMIs from the AWS Marketplace |

## Prerequisites

- Python 3.10+
- AWS account with IAM access keys

## Setup

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install boto3
   ```

3. **Configure AWS credentials:**
   ```bash
   aws configure
   ```
   Or create `~/.aws/credentials` manually:
   ```ini
   [default]
   aws_access_key_id = YOUR_ACCESS_KEY_ID
   aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
   ```

## Usage

```bash
.venv/bin/python3 query.py        # List all vSRX AMIs
.venv/bin/python3 query_kali.py   # List all Kali Linux AMIs
```

### Example output

```
Searching for vSRX AMIs in ap-southeast-1...
Found 10 image(s).

[1] junos-vsrx3-x86-64-24.4R2-S3.5-appsec--prod-...
    AMI ID        : ami-095e0c907adfd8386
    Description   : junos-vsrx3-x86-64-24.4R2-S3.5-appsec--prod
    Creation Date : 2026-02-14T15:35:44.000Z
    Deprecation   : 2028-02-14T15:35:44.000Z
    Architecture  : x86_64
    Virtualization: hvm
    Root Device   : /dev/sda1 (gp2, 20 GB)
    ENA Support   : True
    Public        : True
```
