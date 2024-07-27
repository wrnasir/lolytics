from django.test import TestCase
from views import run_player_linear_regression

# Create your tests here.

def test_fetch_player_data():
    run_player_linear_regression("Smib", "6751")

test_fetch_player_data()