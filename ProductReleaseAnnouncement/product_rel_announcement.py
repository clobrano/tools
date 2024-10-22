#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set ft=python :
"""
Auto-generate social media posts for Medik8s release announcements by filling in the latest tags and
release information.

Usage:
    product_rel_announcement.py --markdown
    product_rel_announcement.py --html
    product_rel_announcement.py --html --markdown

Options:
    -m, --markdown  Write the release announcement file release.md, in Markdown format
    -w, --html      Write the release announcement file release.html, in HTML format
"""
import requests
import markdown
from docopt import docopt


def main():
    arguments = docopt(__doc__)
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

    if arguments['--markdown']:
        with open('release.md', 'w') as f:
            f.write(TEMPLATE)

    if arguments['--html']:
        with open('release.html', 'w') as f:
            html = markdown.markdown(TEMPLATE)
            f.write(html)


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



