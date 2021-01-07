from behave import given, when, then
from SUM import SUM

@given('we have a list of values')
def step_impl(context):
    context.array = [4, 2, 8, 6]

@when('we SUM these values')
def step_impl(context):
    context.sum = SUM(context.array)

@then('we will get the SUM of the values')
def step_impl(context):
    print(context.sum)