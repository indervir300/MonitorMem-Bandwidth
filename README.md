Network Bandwidth Monitor

This Python script monitors your network bandwidth usage and displays it in a user-friendly GUI window. It shows both cumulative and real-time upload and download speeds.

Features:

Shows cumulative upload and download traffic.
Displays real-time upload and download speeds.
Allows exporting data to an Excel spreadsheet.
Can be pinned on top of other windows.

Requirements:

Python 3.x
psutil library (pip install psutil)
openpyxl library (pip install openpyxl)
tkinter library (usually included with Python)

How to Use:

Save the script as network_bandwidth_monitor.py.
Run the script using python network_bandwidth_monitor.py.
The GUI window will appear. You can resize and move the window as needed.
Click the "Save" button to export current network usage data to a new Excel spreadsheet named "network_bandwidth_report.xlsx".
Use the "Pin" button to toggle whether the window stays on top of other windows.
Click the "X" button to close the application.

Notes:

The script saves cumulative traffic data (cumulative_stats.json) to track usage across sessions.
Exported data includes the date, time, upload traffic, and download traffic.
