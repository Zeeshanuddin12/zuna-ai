import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zuna.store import Store, validate

SAMPLE = {"building":"Demo Tower", "area":"Demo Marina", "bedrooms":1, "nightly_aed":450, "amenities":["Wi-Fi"]}
class StoreTests(unittest.TestCase):
    def test_persistent_decision_and_audit(self):
        with tempfile.TemporaryDirectory() as folder:
            db = str(Path(folder)/"desk.db")
            store = Store(db)
            item = store.create(SAMPLE)
            self.assertEqual(item["status"], "pending")
            self.assertIn("AED 450",item["draft"])
            store.close()
            store = Store(db)
            self.assertEqual(store.decide(item["id"],"approved")["status"],"approved")
            with self.assertRaises(ValueError): store.decide(item["id"],"rejected")
            self.assertEqual([x["event"] for x in store.events(item["id"])],["created","approved"])
            store.close()
    def test_rejection_and_missing(self):
        store = Store(":memory:")
        self.assertEqual(store.decide(store.create(SAMPLE)["id"],"rejected")["status"],"rejected")
        with self.assertRaises(ValueError): store.get(999)
        store.close()
    def test_invalid_inputs(self):
        for key,value in [("nightly_aed",float("nan")),("nightly_aed",float("inf")),("nightly_aed",True),("nightly_aed",-1),("bedrooms",True),("building","Unit 123"),("area","a@example.com"),("amenities",["invented"]),("amenities",[{}]),("amenities",["Wi-Fi","Wi-Fi"])]:
            data=copy.deepcopy(SAMPLE);data[key]=value
            with self.subTest(key=key,value=value),self.assertRaises(ValueError):validate(data)
        with self.assertRaises(ValueError):validate({**SAMPLE,"phone":"private"})
    def test_cli_full_flow(self):
        with tempfile.TemporaryDirectory() as folder:
            base=[sys.executable,"-m","zuna","--db",str(Path(folder)/"desk.db")]
            item=json.loads(subprocess.check_output(base+["create","examples/listing.json"]))
            result=json.loads(subprocess.check_output(base+["approve",str(item["id"])]))
            self.assertEqual(result["status"],"approved")
            bad=subprocess.run(base+["create","missing.json"],capture_output=True)
            self.assertEqual(bad.returncode,2)
            self.assertNotIn(b"Traceback",bad.stderr)
