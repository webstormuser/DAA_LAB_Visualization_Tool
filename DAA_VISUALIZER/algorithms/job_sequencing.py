algorithm = """
JOB SEQUENCING WITH DEADLINE

Input:
    Jobs with deadline and profit

Output:
    Maximum profit schedule

Procedure:

1. Sort jobs in decreasing order of profit.

2. Create empty schedule.

3. For each job:

       find latest free slot
       before deadline

       if slot available
            assign job

4. Return scheduled jobs.
"""

time_complexity = """
O(n log n)
"""

space_complexity = """
O(n)
"""