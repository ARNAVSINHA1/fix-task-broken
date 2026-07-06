# Dynamo - Fix the Broken Terminal-Bench Task

This repository contains a fixed version of the Dynamo task for generating a JSON summary from an Apache-style access log.

## What the task does

The agent must read the provided log at `/app/access.log` and produce `/app/report.json` with:

- `total_requests`
- `unique_ips`
- `top_path`

## Files

- `log-report/instruction.md` — task instructions
- `log-report/task.toml` — Harbor task metadata
- `log-report/environment/Dockerfile` — container environment
- `log-report/solution/solve.py` — reference solution
- `log-report/tests/test_outputs.py` — verifier tests

## Verification

The verifier checks that the generated report contains the correct values for the sample log.
