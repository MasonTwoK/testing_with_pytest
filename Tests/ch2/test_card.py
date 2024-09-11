from cards import Card


def test_field_access():
    c = Card()

    assert c.summary is None
    assert c.owner is None
    assert c.state == 'todo'
    assert c.id is None


def test_equality():
    c1 = Card('something', 'will', 'todo', 123)
    c2 = Card('something', 'will', 'todo', 123)

    assert c1 == c2


def test_equality_with_diff_ids():
    c1 = Card('something', 'will', 'todo', 123)
    c2 = Card('something', 'will', 'todo', 4567)

    assert c1 == c2


def test_inequality():
    c1 = Card('something', 'will', 'todo', 123)
    c2 = Card('completely', 'different', 'card', 456)

    assert c1 != c2
