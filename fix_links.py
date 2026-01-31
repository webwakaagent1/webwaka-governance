'''
import os

# Define the replacements to be made in the files
replacements = {
    "docs/architecture/ARCH_CS2_NOTIFICATION_SERVICE.md": [
        ("../../phases/CS-2_NOTIFICATION_SERVICE.md", "../phases/CS-2_NOTIFICATION_SERVICE.md"),
        ("../../governance/WEBWAKA_MASTER_CONTROL_BOARD.md#cs-2-notification-service", "../governance/WEBWAKA_MASTER_CONTROL_BOARD.md#cs-2-notification-service")
    ],
    "docs/architecture/ARCH_CB1_MLAS.md": [
        ("../runbooks/RUNBOOK_CB1_MLAS.md", "../../runbooks/RUNBOOK_CB1_MLAS.md"),
        ("../api/API_CB1_MLAS.md", "../../api/API_CB1_MLAS.md"),
        ("../adrs/ADR_COMMISSION_ENGINE.md", "")
    ],
    "docs/phases/CS-4_PRICING_BILLING_SERVICE.md": [
        ("(/docs/architecture/ARCH_CS4_PRICING_BILLING.md)", "(../../architecture/ARCH_CS4_PRICING_BILLING.md)")
    ]
}

# Iterate over the files and apply the replacements
for filepath, replacements_list in replacements.items():
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()
        
        for old, new in replacements_list:
            content = content.replace(old, new)
        
        with open(filepath, "w") as f:
            f.write(content)
'''
