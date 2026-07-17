import json
import os
from datetime import datetime

REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def save_report(filename, analysis):

    report = {
        "filename": filename,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "analysis": analysis
    }

    output_file = os.path.join(
        REPORT_FOLDER,
        filename + ".json"
    )

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return output_file