import subprocess
import time

def create_subprocess():
    """Create a basic subprocess calling `echo`.

    Tip 52 in Effective Python.
    
    Raises:
        CalledProcessError: Exit code of error is non-zero
    """
    result = subprocess.run(['echo', 'hello from child'], capture_output=True,
                            encoding='utf-8')
    result.check_returncode()
    print(result.stdout)

def create_sleeping_subprocess(process_num: int):
    """Create sleeping subprocess.
    
    Tip 52 in Effective Python. Note that if this program was run concurrently,
    it would take 2*process_num seconds, as opposed to ~2 seconds that it does
    with using subprocess.Popen().
    """
    print('Beginning create_sleeping_subprocess()')
    start_time = time.time()
    sleep_procs: list[subprocess.Popen] = []
    for _ in range(process_num):
        proc = subprocess.Popen(['sleep', '2'])
        sleep_procs.append(proc)
    
    for proc in sleep_procs:
        proc.communicate()
    end_time = time.time()
    print(f'Finished create_sleeping_subprocess in {end_time-start_time:.3} seconds.')