
import pytest
from user import User

def test_user_under_18():
    user = User("Alice", 17)
    assert not user.can_vote(), "User under 18 should not be eligible to vote"

def test_user_exactly_18():
    user = User("Bob", 18)
    assert user.can_vote(), "User exactly 18 should be eligible to vote"

def test_user_over_18():
    user = User("Charlie", 25)
    assert user.can_vote(), "User over 18 should be eligible to vote"
