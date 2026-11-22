#
# SPDX-License-Identifier: Apache-2.0
import testtools

from bandit.core import constants
from bandit.core import issue
from bandit.core import metrics
from bandit.core import tester


class BanditTesterTests(testtools.TestCase):
    def test_invalid_severity_does_not_append_result(self):
        def invalid_severity_test(context):
            return issue.Issue(
                severity="SEVERE",
                confidence=constants.HIGH,
                text="test issue",
            )

        invalid_severity_test._test_id = "B999"

        class TestSet:
            @staticmethod
            def get_tests(checktype):
                return [invalid_severity_test]

        bandit_tester = tester.BanditTester(
            TestSet(), False, {}, metrics.Metrics()
        )
        context = {
            "filename": "code.py",
            "lineno": 1,
            "linerange": [1],
            "col_offset": 0,
        }

        scores = bandit_tester.run_tests(context, "Call")

        self.assertEqual([], bandit_tester.results)
        self.assertEqual([0] * len(constants.RANKING), scores["SEVERITY"])
