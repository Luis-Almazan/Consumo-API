#!/usr/bin/env python3
import json

inventory = {
    "all": {
        "hosts": ["192.168.0.10"],
        "vars": {
            "ansible_user": "admin"
        }
    }
}
print(json.dumps(inventory))
