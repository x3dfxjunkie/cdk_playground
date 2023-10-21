import aws_cdk


def Duration(unit: str, value: int) -> aws_cdk.Duration:
    """Duration: input number of UNIT as an int and return a Duration object

    Args:
        unit (str): Length of time for VALUE to apply to
        value (int): number of UNIT of retention

    Returns:
        aws_cdk.Duration:
    """
    if unit.lower() == "millis":
        return aws_cdk.Duration.millis(value)
    elif unit.lower() == "seconds":
        return aws_cdk.Duration.seconds(value)
    elif unit.lower() == "minutes":
        return aws_cdk.Duration.minutes(value)
    elif unit.lower() == "hours":
        return aws_cdk.Duration.hours(value)
    elif unit.lower() == "days":
        return aws_cdk.Duration.days(value)
    else:
        print("Bad unit passed")
        raise
