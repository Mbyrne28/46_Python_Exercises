def test_fun(a_func, expected_result):
	result = "Failed"
	if a_func == expected_result:
			result = "Passed"

	return a_func + ": " + result
