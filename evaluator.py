def evaluate_cases(tests, func):
  for test, expected_result in tests:
    try:
      assert (func(test) == expected_result)
    except AssertionError as e:
      print(f"Test {test} failed")
      print(e)
      break