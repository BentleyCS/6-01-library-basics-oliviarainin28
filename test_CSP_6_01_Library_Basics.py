import CSP_6_01_Library_Basics as HW

def test_process_expenses():
    prices = [100, 200]
    result = HW.process_expenses(prices)
    assert result == [115, 230]

def test_analyze_scores():
    highest, average = HW.analyze_scores(3, test_inputs = ["90","80","100"])
    assert highest == 100
    assert average == 90


def test_sanitize_usernames():
    names = ["Alice", "BOB", "cHArliE"]
    result = HW.sanitize_usernames(names)
    assert result == ["alice", "bob", "charlie"]


def test_identify_outliers():
    numbers = [50, 120, 300, 80]
    result = HW.identify_outliers(numbers)
    assert result == [120, 300]


def test_search_and_report():
    def fake_input(prompt):
        items = ["Apple","Banana","Cherry"]
        result = HW.search_and_report(items, test_input="banana")
        assert result == 1
