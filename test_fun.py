def test_fun(a_func, expected_result):
	result = "Failed"
	if str(a_func) == str(expected_result):
			result = "Passed"

	return str(a_func) + ": " + str(result)
