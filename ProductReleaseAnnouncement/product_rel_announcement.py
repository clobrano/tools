#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set ft=python :
import requests
import markdown

products_map = {
    "NMO": "node-maintenance-operator",
    "NHC": "node-healthcheck-operator",
    "SNR": "self-node-remediation",
    "FAR": "fence-agents-remediation",
    "MDR": "machine-deletion-remediation",
}
# print(requests.get(f'https://api.github.com/repos/medik8s/{products_map["MDR"]}/releases/latest').json())

def get_latest_version(op_shortname:str) -> dict[str,str]:
    response = requests.get(f'https://api.github.com/repos/medik8s/{products_map[op_shortname]}/releases/latest')
    return {"tag":response.json()["tag_name"], "link": response.json()["html_url"]}


NMO = get_latest_version("NMO")
NHC = get_latest_version("NHC")
SNR = get_latest_version("SNR")
FAR = get_latest_version("FAR")
MDR = get_latest_version("MDR")

TEMPLATE = f"""
Medik8s New Releases

The Medik8s team is thrilled to announce the new releases of ours operators

* Node Maintenance Operator (NMO)    {NMO['tag']} ([release note]({NMO['link']}))
* Node Healthcheck Operator (NHC)    {NHC['tag']} ([release note]({NHC['link']}))
* Self Node Remediation (SNR)        {SNR['tag']} ([release note]({SNR['link']}))
* Fence Agents Remediation (FAR)     {FAR['tag']} ([release note]({FAR['link']}))
* Machine Deletion Remediation (MDR) {MDR['tag']} ([release note]({MDR['link']}))

see our release notes for the complete list of changes.

Feel free to explore the new operators and contact us if you need any assistance.

Do not forget to visit [https://www.medik8s.io/](https://www.medik8s.io/) for the latest information on the team's operators,
Best regards from the Medik8s team.

"""

print("Raw version:")
print(TEMPLATE)

print("\nFormatted HTML version")
print(markdown.markdown(TEMPLATE))
