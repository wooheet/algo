# A REST API contains information about a collection of IoT devices. Given a string statusQuery, numberical threshold value, and date in format MM-YYYY, query the API to get a list of devices.
# Return the total number of devices that:
#
# 1. were added to the collection during the given month and year
# 2. have a root threshold > threshold
#
# Make an HTTP GET request to https://jsonmock.hackerrank.com/api/iot_devices/search?status=<statusQuery>&page=<pageNumber>. it will return all items with status Query as a substring of their status. Be sure to grab all the Pages.
#
# The Response is a JOSN with the follwing 5 fields:
#
# - pars: The current page
# - per_page: The maximum number of devices returned per page
# - total: The totla number of devices
# - total_pages: Thetotal number of pages
# - date: An array of objects containing information
#
# Each device object has the following schema:
#
# - id: The unique ID of the device
# - timestamp;: The timestamp when the device was added to the collection, in UTC milliseconds
# - status: The status of the device
# - operatingParams: an object containing operating parameters of the device
# - asset: an object containing information about the asset of the device
# - parent: Optional. The obeject containing information about the parent of the device
#
# The operating parameters object has the following schema:
#
# - rotorSpeed: The rotor speed of the device
# - slack: The slack in the device
# - rootThreshold: The root threshold for the device
#
# The asset object has the following schema:
#
# - id: the unuque ID of the asset
# - alias: The alias for the asset
#
# The parent object has the following schema:
#
# - id: The unuque ID of the parent of the asset
# - alias: The alias for the parent of the asset
#
#
# function description
# Complete the function numDevices in the editor below.
#
# numDevices has the following parameters:
# - String statusQuery: the status substring to query
# - int threshold: the threshold value
# - String dateStr: in format MM-YYYY, the month and the year to query for
#
# Returns
# - int: the number of matching devices
#
#
# sample input:
# STOPPED
# 45
# 04-2019
#
# sample output
# 3
#
#
# explanation
# The status query is "STOPPED", the threshold value is 45 and we are intersted in the devices added to the collection in April 2019. There are a total of 2
#
#





import requests
import json
from datetime import datetime

def numDevices(statusQuery, threshold, dateStr):
    # Convert date string to datetime object
    date = datetime.strptime(dateStr, '%m-%Y')

    # Initialize variables
    total_devices = 0
    num_matching_devices = 0

    # Make initial request to get total number of pages
    response = requests.get(f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page=1')
    data = json.loads(response.text)
    total_pages = data['total_pages']

    # Iterate through all pages of results
    for page in range(1, total_pages + 1):
        response = requests.get(f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={page}')
        data = json.loads(response.text)

        # Iterate through devices on current page
        for device in data['data']:
            # Check if device was added during the given month and year
            device_date = datetime.utcfromtimestamp(device['timestamp'] / 1000)
            if device_date.month == date.month and device_date.year == date.year:
                total_devices += 1

                # Check if device has rootThreshold greater than threshold
                if device['operatingParams']['rootThreshold'] > threshold:
                    num_matching_devices += 1

    return num_matching_devices

