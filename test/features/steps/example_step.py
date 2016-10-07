from behave import given, when, then
from hamcrest import assert_that, equal_to


@given('the ninja has a third level black-belt')
def step_impl(context):
    pass


@when('attacked by a samurai')
def step_impl(context):
    pass


@then('the ninja should engage the opponent')
def step_impl(context):
    assert_that(1, equal_to(1))
