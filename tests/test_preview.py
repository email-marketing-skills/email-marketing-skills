import copy
import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("preview",ROOT/"skills/email-marketing/scripts/preview.py")
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
class PreviewTests(unittest.TestCase):
    def setUp(self):
        self.fixture=json.loads((ROOT/"skills/email-marketing/assets/preview.json").read_text())
    def test_activation_and_unsubscribe_cancel_due_reminders(self):
        result=module.simulate(self.fixture)
        self.assertEqual(len(result["messages"]),2)
        self.assertTrue(all(m["step"]=="welcome" for m in result["messages"]))
        self.assertIn("Hi there",result["messages"][0]["body"])
        reasons={d["decision"] for d in result["decisions"]}
        self.assertTrue({"suppressed","state_mismatch","already_previewed"}<=reasons)
    def test_duplicate_signup_and_ticks_do_not_resend(self):
        self.fixture["events"]=[self.fixture["events"][0],self.fixture["events"][0],{"id":"new-signup","type":"signup","recipient":"new-user","hour":1},{"id":"t1","type":"tick","hour":24},{"id":"t2","type":"tick","hour":24}]
        result=module.simulate(self.fixture)
        self.assertEqual(len(result["messages"]),2)
    def test_any_reply_pauses_followups(self):
        self.fixture["events"]=[self.fixture["events"][0],{"id":"r","type":"reply","recipient":"new-user","hour":1},{"id":"t","type":"tick","hour":24}]
        result=module.simulate(self.fixture)
        self.assertEqual(result["messages"],[])
        self.assertEqual({d["decision"] for d in result["decisions"]},{"reply_pause"})
    def test_missing_eligibility_defaults_to_suppressed(self):
        del self.fixture["recipients"][0]["marketing_eligible"]
        self.assertFalse(any(m["recipient"]=="new-user" for m in module.simulate(self.fixture)["messages"]))
    def test_malformed_eligibility_is_suppressed(self):
        for value in ["false", "true", 1, [], None]:
            self.fixture["recipients"][0]["marketing_eligible"] = value
            self.assertFalse(any(m["recipient"] == "new-user" for m in module.simulate(self.fixture)["messages"]))
    def test_missing_or_invalid_destination_rejected(self):
        for cta in [{}, {"type":"link"}, {"type":"link", "destination":"javascript:alert(1)"}, {"type":"link", "destination":"https://{app_host}/reports/new"}]:
            self.fixture["steps"][0]["cta"] = cta
            with self.assertRaises(ValueError): module.simulate(self.fixture)
    def test_empty_inline_destination_rejected(self):
        self.fixture["steps"][0]["body"] = "Open [your report]()."
        with self.assertRaises(ValueError): module.simulate(self.fixture)
    def test_reply_cta_allowed(self):
        self.fixture["steps"][0]["cta"] = {"type":"reply"}
        self.assertEqual(module.simulate(self.fixture)["messages"][0]["cta"]["type"], "reply")
    def test_unresolved_template_rejected(self):
        self.fixture["steps"][0]["body"]="Go to {url}"
        with self.assertRaises(ValueError):module.simulate(self.fixture)
    def test_out_of_order_events_rejected(self):
        self.fixture["events"].reverse()
        with self.assertRaises(ValueError):module.simulate(self.fixture)
    def test_complaint_and_bounce_suppress(self):
        for kind in ["complaint","bounce"]:
            self.fixture["events"]=[self.fixture["events"][0],{"id":"block","type":kind,"recipient":"new-user","hour":1},{"id":"t","type":"tick","hour":24}]
            self.assertEqual(module.simulate(self.fixture)["messages"],[])
if __name__=="__main__":unittest.main()
