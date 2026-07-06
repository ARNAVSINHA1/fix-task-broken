# Task: Generate an Access Log Summary

An Apache-style access log is available at:

```
/app/access.log
```

Analyze the log and generate a JSON report.

## Success Criteria

1. Read the input file located at `/app/access.log`.

2. Create a JSON file at:

```
/app/report.json
```

3. The JSON object must contain exactly the following fields:

```json
{
  "total_requests": <integer>,
  "unique_ips": <integer>,
  "top_path": "<string>"
}
```

Where:

- `total_requests` is the total number of log entries.
- `unique_ips` is the number of distinct client IP addresses.
- `top_path` is the request path that appears most frequently in the log.

4. The values in `report.json` must accurately reflect the contents of the provided access log.

## Notes

- Do not modify the input file.
- The solution must work without internet access.
- Produce only the required output file.