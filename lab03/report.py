class ExperimentReport:
    def __init__(self, experiment_name : str, tp: int|float = 0, fp: int|float = 0, tn: int|float = 0, fn: int|float = 0) -> None:
        self.__experiment_name = experiment_name
        self.tp = tp
        self.fp = fp
        self.tn = tn
        self.fn = fn

    @property
    def tp(self):
        return self._tp

    @tp.setter
    def tp(self, value: int|float):
        if value < 0:
            raise ValueError('tp must be >= 0')
        self._tp = value

    @tp.deleter
    def tp(self):
        del self._tp

    @property
    def fp(self):
        return self._fp

    @fp.setter
    def fp(self, value: int|float):
        if value < 0:
            raise ValueError('fp must be >= 0')
        self._fp = value
    
    @fp.deleter
    def fp(self):
        del self._fp

    @property
    def tn(self):
        return self._tn

    @tn.setter
    def tn(self, value: int|float):
        if value < 0:
            raise ValueError('tn must be >= 0')
        self._tn = value

    @tn.deleter
    def tn(self):
        del self._tn
        
    @property
    def fn(self):
        return self._fn

    @fn.setter
    def fn(self, value: int|float):
        if value < 0:
            raise ValueError('fn must be >= 0')
        self._fn = value

    @fn.deleter
    def fn(self):
        del self._fn

    @property
    def experiment_name(self):
        return self.__experiment_name

    @experiment_name.setter
    def experiment_name(self, value):
        raise AttributeError('Experiment name cannot be set')

    @experiment_name.deleter
    def experiment_name(self):
        raise AttributeError('Experiment name cannot be deleted')

    def get_accuracy(self):
        total = self.tp + self.tn + self.fp + self.fn
        return (self.tp + self.tn) / total if total > 0 else 0

    def get_precision(self):
        return self.tp / (self.tp + self.fp) if (self.tp + self.fp) > 0 else 0

    def get_recall(self):
        return self.tp / (self.tp + self.fn) if (self.tp + self.fn) > 0 else 0

    def get_f1(self):
        p = self.get_precision()
        r = self.get_recall()
        return 2 * (p * r) / (p + r) if (p + r) > 0 else 0

    def __str__(self):
        return f"Raport: {self.__experiment_name} | F1-Score: {self.get_f1():.4f}"

    def __repr__(self):
        return f"ExperimentReport('{self.experiment_name}', {self.tp}, {self.fp}, {self.tn}, {self.fn})"

