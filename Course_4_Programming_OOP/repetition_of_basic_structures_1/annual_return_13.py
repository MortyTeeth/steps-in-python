def annual_return(start, percent, years):
    for i in range(1, years + 1):
        yield start * ((100 + percent) / 100)
        start = start * ((100 + percent) / 100)
