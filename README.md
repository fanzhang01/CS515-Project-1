# Test Harness

## Overview

Fan Zhang
<fzhang32@stevens.edu>
the URL of your public GitHub repo: <https://github.com/fanzhang01/CS515-Project-1>
an estimate of how many hours you spent on the project: 64hrs

any bugs or issues you could not resolve: No
an example of a difficult issue or bug and how you resolved it: Don't have any.

## Program3: CSV Sum Utility

One of the programs tested with this harness is a utility for loading CSV files and summing particular columns, demonstrating the harness's capability to handle data processing tasks.

## Extensions

1. **More Advanced `wc`: Multiple Files**
   - The harness supports testing scripts that process multiple files, providing total outputs across all files.
   - Write tests to utilize this feature in scenarios that are more complex than single-file processing.

2. **Expected Exit Status**
   - Each test can specify an expected exit status in `PROG.NAME.status`.
   - This extension allows for testing scripts under various conditions, including error states with non-zero exit statuses.

3. **Expected STDERR**
   - In addition to STDOUT, tests can define expected STDERR in `PROG.NAME.err` (or `PROG.NAME.arg.err` for argument mode).
   - Useful for validating error handling and messaging in scripts.

## How TO Test

- `PROG.NAME.in`: Input file for the test.
- `PROG.NAME.out`: Expected STDOUT for the test.
- `PROG.NAME.err`: Expected STDERR for the test.
- `PROG.NAME.status`: Expected exit status.
- For tests with arguments: `PROG.NAME.arg.in`, `PROG.NAME.arg.out`, and `PROG.NAME.arg.err`.
