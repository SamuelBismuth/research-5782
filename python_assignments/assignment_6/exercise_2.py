from xmlrpc.client import boolean
import pandas as pd


def education_budget(year:int)->int():
    """
    We ask what is the education budget of the given year.

    >>> education_budget(2020)
    4343657
    >>> education_budget(1998)
    2184990
    >>> education_budget(2002)
    1492452
    """
    df = pd.read_csv('national-budget.csv')
    education_budget_sum = - df.loc[df['שנה'] == year].loc[df['שם רמה 2'] == 'חינוך'].loc[df['הוצאה/הכנסה'] == 'הכנסה']['הוצאה נטו'].sum()
    return int(education_budget_sum)


def security_budget_ratio(year:int)->float:
    """
    We ask for the ratio between the security budget of the year and the total budget of the year.
    There are some positive withdraws: how to deal with such a case?

    >>> security_budget_ratio(2020)
    4343657
    >>> security_budget_ratio(1998)
    2184990
    >>> security_budget_ratio(2002)
    1492452
    """
    df = pd.read_csv('national-budget.csv')
    year_lines = df.loc[df['שנה'] == year]
    year_budget_sum = - year_lines.loc[df['הוצאה/הכנסה'] == 'הכנסה']['הוצאה נטו'].sum()

    print(year_lines.loc[df['הוצאה/הכנסה'] == 'הכנסה'].loc[df['הוצאה נטו'] > 0]['הוצאה נטו'])


    security_budget_sum = - year_lines.loc[df['שם רמה 2'] == 'בטחון'].loc[df['הוצאה/הכנסה'] == 'הכנסה']['הוצאה נטו'].sum()
    print("year_budget_sum {0}".format(year_budget_sum))
    print("security_budget_sum {0}".format(security_budget_sum))
    return security_budget_sum / year_budget_sum


def largest_budget_year(office:str)->int:
    """
    We ask what year has the largest budget for a given office.
    
    >>> largest_budget_year('משרד הבטחון')
    2018
    >>> largest_budget_year('משטרה ובתי סוהר')
    1997
    >>> largest_budget_year('משרד החינוך והתרבות')
    2001
    """
    df = pd.read_csv('national-budget.csv')
    education_budget_sum = df.loc[df['שם סעיף'] == office].loc[df['הוצאה/הכנסה'] == 'הכנסה']['הוצאה נטו'].idxmin()
    return df.iloc[education_budget_sum]['שנה']


def is_education_year_budget_bigger_than_security(year:int)->boolean:
    """
    We ask if the education total budget of the year is bigger than the security total budget of the same year.

    After running the function with a lot of different example, we notice that the budget for the security is almost always 
    bigger than the budget for the education.
    This is a sad conclusion...

    >>> is_education_year_budget_bigger_than_security(2020)
    False
    >>> is_education_year_budget_bigger_than_security(1998)
    False
    >>> is_education_year_budget_bigger_than_security(2002)
    False
    >>> is_education_year_budget_bigger_than_security(2000)
    False
    >>> is_education_year_budget_bigger_than_security(1997)
    True
    >>> is_education_year_budget_bigger_than_security(1999)
    False
    >>> is_education_year_budget_bigger_than_security(2018)
    False
    """
    df = pd.read_csv('national-budget.csv')
    year_lines = df.loc[df['שנה'] == year]
    education_budget_sum = - year_lines.loc[df['שם רמה 2'] == 'חינוך'].loc[df['הוצאה/הכנסה'] == 'הכנסה']['הוצאה נטו'].sum()
    security_budget_sum = - year_lines.loc[df['שם רמה 2'] == 'בטחון'].loc[df['הוצאה/הכנסה'] == 'הכנסה']['הוצאה נטו'].sum()
    return education_budget_sum > security_budget_sum


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))