import pytest
from pytest_bdd import scenarios, parsers, given, when, then

from retirement import *


EXTRA_TYPES = {
    'Number': int,
}


CONVERTERS = {
    'initial_month': int,
    'initial_year': int,
    'years_to_ssa': int,
    'months_to_ssa': int,
    'ssa_month': int,
    'ssa_year': int
}


scenarios('../features/retirement.feature', example_converters=CONVERTERS)


@given(parsers.cfparse('the user wants to know date to start receiving full SSA benefits', extra_types=EXTRA_TYPES))
@given('the user wants to know date to start receiving full SSA benefits')
def test_user_inputs():
    pass


@when(parsers.cfparse('"{initial_year:Number}" year is entered', extra_types=EXTRA_TYPES))
@when('"<initial_year>" year is entered')
def calculate_retirement(initial_year):
    pass


@then(parsers.cfparse('the program will use "{initial_year}" so retirement age will be in "{age_years}" years and "{age_months}" months', extra_types=EXTRA_TYPES))
@then('the program will use "<initial_year>" so retirement age will be in "<age_years>" years and "<age_months>" months')
def calculate_full_date(initial_year, age_years, age_months):
    calc_age = calculate_retirement_age(initial_year)
    assert calc_age[0].__eq__(age_years)
    assert calc_age[1].__eq__(age_months)


@given("the user enters invalid info")
def step_impl():
    pass


@when('"<initial_year>" year is invalid')
def input_invalid_year(initial_year):
    pass


@then('the program will return an invalid message for the "<initial_year>"')
def invalid_year_error(initial_year):
    with pytest.raises(ValueError):
        calculate_retirement_age(initial_year)
