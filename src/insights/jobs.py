from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        reader = csv.DictReader(file)

        print(list(reader))
        return list(reader)


def get_unique_job_types(path: str) -> List[str]:
    all_jobs = read(path)

    return list(set([job["job_type"] for job in all_jobs]))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
