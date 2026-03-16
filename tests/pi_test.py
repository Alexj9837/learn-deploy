from first_step.pi import find__first_in_pi, find_all_pos_in_pi


class TestFindFirstInPi:
    def test_314_is_at_position_0(self):
        assert find__first_in_pi(314) == 0

    def test_known_position(self):
        # "1415" first appears at index 1
        assert find__first_in_pi(1415) == 1

    def test_not_found_returns_none(self):
        # No 7-digit sequence of all nines in the first 100k digits is guaranteed
        # absent, so use a value known not to appear
        assert find__first_in_pi(9999999999) is None

    def test_start_skips_earlier_match(self):
        # 314 is at 0; searching from position 1 should find the next occurrence
        first = find__first_in_pi(314)
        second = find__first_in_pi(314, start=1)
        assert second is not None
        assert second > first  # type: ignore[operator]

    def test_start_none_same_as_default(self):
        assert find__first_in_pi(314, start=None) == find__first_in_pi(314)


class TestFindAllPosInPi:
    def test_returns_list(self):
        assert isinstance(find_all_pos_in_pi(314), list)

    def test_314_first_position_is_0(self):
        positions = find_all_pos_in_pi(314)
        assert positions[0] == 0

    def test_314_has_many_occurrences(self):
        # From the live API response we know there are 95 occurrences
        assert len(find_all_pos_in_pi(314)) == 95

    def test_positions_are_sorted(self):
        positions = find_all_pos_in_pi(314)
        assert positions == sorted(positions)

    def test_not_found_returns_empty_list(self):
        assert find_all_pos_in_pi(9999999999) == []

    def test_all_positions_are_real_matches(self):
        # Each position should be re-findable as the first match from that offset
        for pos in find_all_pos_in_pi(314):
            assert find__first_in_pi(314, start=pos) == pos
