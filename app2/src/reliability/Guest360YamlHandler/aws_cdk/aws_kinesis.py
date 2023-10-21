import aws_cdk

def days_retention(days: int) -> aws_cdk.Duration:
    """days_retention: input number of days as an int and return a Duration object

    Args:
        days (int): number of days of retention

    Returns:
        aws_cdk.Duration: Returns the number of days as a Duration
    """
    return aws_cdk.Duration.days(days)