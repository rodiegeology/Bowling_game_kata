import pytest

from GameClass import Game


@pytest.fixture
def game():
    game = Game()
    game.create_frame()
    yield game


def test_create_frame(game):
    frame_created = game.get_frame
    frame_expected = {1: [None, None], 2: [None, None], 3: [None, None], 4: [None, None], 5: [None, None],
                      6: [None, None],
                      7: [None, None], 8: [None, None], 9: [None, None], 10: [None, None, None]}
    assert frame_created == frame_expected


@pytest.mark.parametrize(
    'pins, frame_expected', [
        ([1, 2, 3, 4, 5],
         {1: [1, 2], 2: [3, 4], 3: [5, None], 4: [None, None], 5: [None, None], 6: [None, None], 7: [None, None],
          8: [None, None], 9: [None, None], 10: [None, None, None]}),
        ([2, 4, 3, 5, 2],
         {1: [2, 4], 2: [3, 5], 3: [2, None], 4: [None, None], 5: [None, None], 6: [None, None], 7: [None, None],
          8: [None, None], 9: [None, None], 10: [None, None, None]}),
        ([2, 3], {1: [2, 3], 2: [None, None], 3: [None, None], 4: [None, None], 5: [None, None], 6: [None, None],
                  7: [None, None], 8: [None, None], 9: [None, None], 10: [None, None, None]}),
        ([1], {1: [1, None], 2: [None, None], 3: [None, None], 4: [None, None], 5: [None, None], 6: [None, None],
               7: [None, None], 8: [None, None], 9: [None, None], 10: [None, None, None]}),
    ]
)
def test_frame(game, pins, frame_expected):
    game.roll_many(pins)
    frame_result = game.get_frame
    assert frame_result == frame_expected


@pytest.mark.parametrize(
    'rolls_list, score', [
        ([0] * 20, 0),
        ([1] * 20, 20),
        ([2] * 20, 40),
        ([3] * 20, 60),
        ([4] * 20, 80)
    ]
)
def test_score(game, rolls_list, score):
    game.roll_many(rolls_list)
    assert game.score == score


@pytest.mark.parametrize(
    "rolls, score", [
        ([5, 5, 6] + [0] * 17, 22),
        ([5, 5, 6] + [0] + [5, 5, 6] + [0] * 13, 44),
        ([5] * 21, 150)
    ]
)
def test_spare(game, rolls, score):
    game.roll_many(rolls)
    assert game.score == score


@pytest.mark.parametrize(
    'rolls, score', [
        ([10, 4, 3] + [0] * 16, 24),  # one strike
        ([10] * 12, 300)  # perfect game
    ]
)
def test_strike(game, rolls, score):
    game.roll_many(rolls)
    assert game.score == score
