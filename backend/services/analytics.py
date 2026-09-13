from typing import List, Dict, Optional
from statistics import mean, stdev

from backend.models.metric import Metric


# ============================================================
# SUPPORTED METRICS
# ============================================================

METRIC_ATTRIBUTES = {
    "cpu",
    "ram",
    "disk",
    "network",
    "temperature",
}


# ============================================================
# BASIC STATISTICS
# ============================================================

def calculate_average(
    metrics: List[Metric],
    attribute: str
) -> float:
    """
    Calculate the average value of a metric attribute.
    """

    if attribute not in METRIC_ATTRIBUTES:
        raise ValueError(
            f"Invalid metric attribute: {attribute}"
        )

    values = [
        float(getattr(metric, attribute, 0.0))
        for metric in metrics
    ]

    return mean(values) if values else 0.0


def calculate_max(
    metrics: List[Metric],
    attribute: str
) -> float:
    """
    Calculate the maximum value of a metric attribute.
    """

    if attribute not in METRIC_ATTRIBUTES:
        raise ValueError(
            f"Invalid metric attribute: {attribute}"
        )

    values = [
        float(getattr(metric, attribute, 0.0))
        for metric in metrics
    ]

    return max(values) if values else 0.0


def calculate_min(
    metrics: List[Metric],
    attribute: str
) -> float:
    """
    Calculate the minimum value of a metric attribute.
    """

    if attribute not in METRIC_ATTRIBUTES:
        raise ValueError(
            f"Invalid metric attribute: {attribute}"
        )

    values = [
        float(getattr(metric, attribute, 0.0))
        for metric in metrics
    ]

    return min(values) if values else 0.0


def calculate_standard_deviation(
    metrics: List[Metric],
    attribute: str
) -> float:
    """
    Calculate the standard deviation of a metric attribute.
    """

    if attribute not in METRIC_ATTRIBUTES:
        raise ValueError(
            f"Invalid metric attribute: {attribute}"
        )

    values = [
        float(getattr(metric, attribute, 0.0))
        for metric in metrics
    ]

    return stdev(values) if len(values) > 1 else 0.0


# ============================================================
# ANOMALY DETECTION
# ============================================================

def detect_anomalies(
    metrics: List[Metric],
    attribute: Optional[str] = None,
    threshold: float = 2.0
) -> List[Metric]:
    """
    Detect anomalous metrics.

    If an attribute is provided, only that attribute is analyzed.

    Example:
        detect_anomalies(metrics, "cpu")

    If no attribute is provided, all supported attributes are
    analyzed.

    Example:
        detect_anomalies(metrics)
    """

    if not metrics:
        return []

    if attribute is not None:
        if attribute not in METRIC_ATTRIBUTES:
            raise ValueError(
                f"Invalid metric attribute: {attribute}"
            )

        return _detect_attribute_anomalies(
            metrics,
            attribute,
            threshold
        )

    anomaly_indexes = set()

    for metric_attribute in METRIC_ATTRIBUTES:
        anomalies = _detect_attribute_anomalies(
            metrics,
            metric_attribute,
            threshold
        )

        for anomaly in anomalies:
            for index, metric in enumerate(metrics):
                if metric is anomaly:
                    anomaly_indexes.add(index)
                    break

    return [
        metric
        for index, metric in enumerate(metrics)
        if index in anomaly_indexes
    ]


def _detect_attribute_anomalies(
    metrics: List[Metric],
    attribute: str,
    threshold: float
) -> List[Metric]:
    """
    Detect anomalies for a single metric attribute.

    Combines standard deviation, median deviation and relative
    distance to make the detection more reliable with small
    datasets.
    """

    values = [
        float(getattr(metric, attribute, 0.0))
        for metric in metrics
    ]

    if len(values) < 3:
        return []

    # All values are identical.
    if len(set(values)) == 1:
        return []

    average = mean(values)
    deviation = stdev(values)

    # --------------------------------------------------------
    # Median
    # --------------------------------------------------------

    sorted_values = sorted(values)

    middle = len(sorted_values) // 2

    if len(sorted_values) % 2 == 0:
        median = (
            sorted_values[middle - 1]
            + sorted_values[middle]
        ) / 2
    else:
        median = sorted_values[middle]

    # --------------------------------------------------------
    # Median Absolute Deviation (MAD)
    # --------------------------------------------------------

    absolute_deviations = [
        abs(value - median)
        for value in values
    ]

    sorted_deviations = sorted(absolute_deviations)

    middle_deviation = len(sorted_deviations) // 2

    if len(sorted_deviations) % 2 == 0:
        mad = (
            sorted_deviations[middle_deviation - 1]
            + sorted_deviations[middle_deviation]
        ) / 2
    else:
        mad = sorted_deviations[middle_deviation]

    anomalies = []

    for index, metric in enumerate(metrics):

        value = values[index]

        # ----------------------------------------------------
        # Z-score
        # ----------------------------------------------------

        z_score_anomaly = False

        if deviation > 0:
            z_score = abs(value - average) / deviation

            if z_score > threshold:
                z_score_anomaly = True

        # ----------------------------------------------------
        # Modified Z-score using MAD
        # ----------------------------------------------------

        mad_anomaly = False

        if mad > 0:
            modified_z_score = (
                0.6745
                * abs(value - median)
                / mad
            )

            if modified_z_score > 3.5:
                mad_anomaly = True

        # ----------------------------------------------------
        # Relative distance from remaining observations
        # ----------------------------------------------------

        other_values = [
            values[i]
            for i in range(len(values))
            if i != index
        ]

        other_average = mean(other_values)

        relative_anomaly = False

        if other_average != 0:
            relative_difference = (
                abs(value - other_average)
                / abs(other_average)
            )

            if relative_difference > 1.0:
                relative_anomaly = True

        # ----------------------------------------------------
        # Final decision
        # ----------------------------------------------------

        if (
            z_score_anomaly
            or mad_anomaly
            or relative_anomaly
        ):
            anomalies.append(metric)

    return anomalies


# ============================================================
# PREDICTION
# ============================================================

def predict_next_value(
    metrics: List[Metric],
    attribute: str
) -> float:
    """
    Predict the next value of a metric.

    The prediction is based on the average difference between
    consecutive observations.
    """

    if attribute not in METRIC_ATTRIBUTES:
        raise ValueError(
            f"Invalid metric attribute: {attribute}"
        )

    if not metrics:
        return 0.0

    last_value = float(
        getattr(metrics[-1], attribute, 0.0)
    )

    if len(metrics) < 2:
        return last_value

    differences = [
        float(
            getattr(
                metrics[index + 1],
                attribute,
                0.0
            )
        )
        - float(
            getattr(
                metrics[index],
                attribute,
                0.0
            )
        )
        for index in range(len(metrics) - 1)
    ]

    average_difference = mean(differences)

    return last_value + average_difference


def predict_usage(
    metrics: List[Metric]
) -> Dict[str, float]:
    """
    Predict the next value for all monitored resources.

    Returns:
        {
            "cpu": value,
            "ram": value,
            "disk": value,
            "network": value,
            "temperature": value
        }
    """

    if not metrics:
        return {
            "cpu": 0,
            "ram": 0,
            "disk": 0,
            "network": 0,
            "temperature": 0,
        }

    return {
        "cpu": predict_next_value(
            metrics,
            "cpu"
        ),
        "ram": predict_next_value(
            metrics,
            "ram"
        ),
        "disk": predict_next_value(
            metrics,
            "disk"
        ),
        "network": predict_next_value(
            metrics,
            "network"
        ),
        "temperature": predict_next_value(
            metrics,
            "temperature"
        ),
    }