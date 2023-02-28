from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    all_salaries = read(path)
    max_salary = 0

    for salary in all_salaries:
        try:
            if int(salary["max_salary"]) > max_salary:
                max_salary = int(salary["max_salary"])
            [
                salary["max_salary"]
                for salary in all_salaries
                if bool(salary["max_salary"])
            ]
        except ValueError:
            continue

    return max_salary


def get_min_salary(path: str) -> int:
    all_salaries = read(path)
    min_salary = 383416

    for salary in all_salaries:
        try:
            if int(salary["min_salary"]) < min_salary:
                min_salary = int(salary["min_salary"])
            [
                salary["min_salary"]
                for salary in all_salaries
                if bool(salary["min_salary"])
            ]
        except ValueError:
            continue

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    try:
        get_min_salary = int(job["min_salary"])
        get_max_salary = int(job["max_salary"])
        get_salary = int(salary)
    except (TypeError, ValueError):     # trecho de código encontrado por
        raise ValueError                # pesquisa na internet

    if get_min_salary > get_max_salary:
        raise ValueError

    print(get_max_salary >= get_salary >= get_min_salary)
    return get_max_salary >= get_salary >= get_min_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
