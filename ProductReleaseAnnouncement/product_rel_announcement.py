#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set ft=python :
import requests
import markdown


def main():
    NMO = get_latest_version("node-maintenance-operator")
    NHC = get_latest_version("node-healthcheck-operator")
    SNR = get_latest_version("self-node-remediation")
    FAR = get_latest_version("fence-agents-remediation")
    MDR = get_latest_version("machine-deletion-remediation")

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


def get_latest_version(op_name:str) -> dict[str,str]:
    """
    Get the latest version of an Medik8s operator.

    :param op_name: The name of the operator to retrieve the latest version for.
    :return: A dictionary with the latest version tag and link to the release note.
    """
    response = requests.get(f'https://api.github.com/repos/medik8s/{op_name}/releases/latest')
    return {"tag":response.json()["tag_name"], "link": response.json()["html_url"]}


if __name__ == "__main__":
    main()



