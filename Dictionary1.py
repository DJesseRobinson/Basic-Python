monthConversions = {
    0: "January",  # The keys (ie., "Jan") can also be numbers, such as 0: "January"
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions.get(0, "Not a Valid Key"))
