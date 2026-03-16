import pytest
from report import ExperimentReport


def test_metrics_calculation():
    """Testuje podstawowe obliczenia dla znanych wartości."""
    report = ExperimentReport("Test 1", tp=80, fp=10, tn=5, fn=5)

    assert report.get_accuracy() == 0.85  # (80+5)/100
    assert report.get_precision() == 0.8888888888888888  # 80/90
    assert report.get_recall() == 0.9411764705882353  # 80/85
    assert report.get_f1() > 0.9  # F1 to ok. 0.914


def test_negative_values_raise_error():
    """Testuje, czy setter blokuje wartości ujemne."""
    report = ExperimentReport("Test 2")

    with pytest.raises(ValueError, match="tp must be >= 0"):
        report.tp = -5

    with pytest.raises(ValueError):
        report.fn = -1


def test_zero_division_safety():
    """Testuje, czy klasa nie wywala się przy samych zerach."""
    report = ExperimentReport("Same zera", tp=0, fp=0, tn=0, fn=0)

    assert report.get_accuracy() == 0
    assert report.get_precision() == 0
    assert report.get_f1() == 0


def test_deleter():
    """Testuje, czy atrybut faktycznie znika po użyciu del."""
    report = ExperimentReport("Test Delete", tp=10)
    del report.tp

    with pytest.raises(AttributeError):
        print(report.tp)


def test_private_experiment_name():
    """Testuje, czy nazwa eksperymentu jest chroniona (name mangling)."""
    report = ExperimentReport("Tajny Projekt")

    with pytest.raises(AttributeError):
        print(report.__experiment_name)

    with pytest.raises(AttributeError, match="Experiment name cannot be set"):
        report.experiment_name = "Nietajny projekt"

    assert report._ExperimentReport__experiment_name == "Tajny Projekt"