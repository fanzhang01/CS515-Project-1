import os
import subprocess

def run_test(prog, test_name, mode):
    input_file = f'test/{prog}.{test_name}.in'
    expected_output_file = f'test/{prog}.{test_name}{"." + mode if mode else ""}.out'
    expected_stderr_file = f'test/{prog}.{test_name}{"." + mode if mode else ""}.err'
    expected_status_file = f'test/{prog}.{test_name}.status'

    # Read the input file
    with open(input_file, 'r') as infile:
        input_data = infile.read()

    # Prepare the expected output and stderr
    expected_output, expected_stderr = '', ''
    if os.path.exists(expected_output_file):
        with open(expected_output_file, 'r') as outfile:
            expected_output = outfile.read()
    if os.path.exists(expected_stderr_file):
        with open(expected_stderr_file, 'r') as errfile:
            expected_stderr = errfile.read()

    # Read expected exit status, default is 0
    expected_status = 0
    if os.path.exists(expected_status_file):
        with open(expected_status_file, 'r') as statusfile:
            expected_status = int(statusfile.read().strip())

    # Run the program based on the mode
    script_path = f'prog/{prog}.py'
    if mode == 'arg':
        command = ['python', script_path, input_file]
    else:
        command = ['python', script_path]

    result = subprocess.run(command, input=input_data, capture_output=True, text=True)

    # Check for expected exit status
    actual_status = result.returncode
    if actual_status != expected_status:
        return 'TestResult.ExitStatusMismatch', result.stdout, expected_output

    # Compare outputs
    if result.stdout != expected_output:
        return 'TestResult.OutputMismatch', result.stdout, expected_output

    # Compare STDERR
    if result.stderr != expected_stderr:
        return 'TestResult.StderrMismatch', result.stderr, expected_stderr

    return 'TestResult.OK', result.stdout, expected_output

def print_test_result(prog, test_name, mode_desc, result, output, expected_output):
    if result == 'TestResult.StderrMismatch':
        print(f"FAIL: {prog} {test_name} failed{mode_desc} ({result})")
        print(f"      expected STDERR:\n{expected_output}")
        print(f"           got STDERR:\n{output}")
    elif result != 'TestResult.OK':
        print(f"FAIL: {prog} {test_name} failed{mode_desc} ({result})")
        print(f"      expected:\n{expected_output}")
        print(f"           got:\n{output}")
    else:
        print(f"OK: {prog} {test_name} passed{mode_desc}")

def discover_and_run_tests():
    test_results = {'TestResult.OK': 0, 'TestResult.OutputMismatch': 0, 'TestResult.StderrMismatch': 0, 'TestResult.ExitStatusMismatch': 0, 'TestResult.NonZeroExit': 0}
    total_tests = 0

    for file in os.listdir('test'):
        if file.endswith('.in'):
            parts = file.split('.')
            prog, test_name = parts[0], parts[1]

            # Determine the mode based on the test file name
            mode = 'arg' if 'arg' in file else ''

            # Run the test
            result, output, expected_output = run_test(prog, test_name, mode)
            mode_desc = ' in argument mode' if mode == 'arg' else ''
            print_test_result(prog, test_name, mode_desc, result, output, expected_output)
            test_results[result] += 1
            total_tests += 1

    # Print summary
    print("\nOK:", test_results['TestResult.OK'])
    print("output mismatch:", test_results['TestResult.OutputMismatch'])
    print("stderr mismatch:", test_results['TestResult.StderrMismatch'])
    print("exit status mismatch:", test_results['TestResult.ExitStatusMismatch'])
    print("non-zero exit:", test_results['TestResult.NonZeroExit'])
    print("total:", total_tests)
    return test_results

if __name__ == '__main__':
    results = discover_and_run_tests()
    if any(v > 0 for k, v in results.items() if k != 'TestResult.OK'):
        exit(1)
