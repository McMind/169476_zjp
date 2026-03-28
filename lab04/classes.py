from typing import List, Optional, Any, Dict, Callable
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

class MLDataFrame:

    def __init__(self, data: pd.DataFrame) -> None:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")

        self._data = data.copy()

    def __getattr__(self, name: str) -> pd.Series:
        if name in self._data.columns:
            return self._data[name]
        raise AttributeError(f"Object {self.__class__.__name__} has no attribute '{name}'")

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "_data":
            super().__setattr__(name, value)
        elif name in self._data.columns:
            raise AttributeError(f"Column {name} is readonly")
        else:
            super().__setattr__(name, value)

    def add_feature(self, name: str, func: Callable[[pd.DataFrame], pd.Series]) -> None:
        self._data[name] = func(self._data)

    def mean(self, column: str) -> float:
        return float(self._data[column].mean())

    def variance(self, column: str) -> float:
        return float(self._data[column].var())

    def describe(self) -> pd.DataFrame:
        return self._data.describe()

    @classmethod
    def from_iris(cls) -> 'MLDataFrame':
        iris = load_iris(as_frame=True)
        df = iris.frame
        df['target_name'] = iris.target.map(dict(enumerate(iris.target_names)))
        return cls(df)

    def __repr__(self) -> str:
        shape = self._data.shape
        cols = ", ".join(self._data.columns)
        return f"MLDataFrame(rows={shape[0]}, cols={shape[1]}) -> [{cols}]"


class DataPreprocessor:
    def __init__(self, df: pd.DataFrame) -> None:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")

        self._df: pd.DataFrame = df.copy()
        self._history: List[pd.DataFrame] = []
        self._transformation_log: List[str] = []

    def _save_state(self, action_name: str) -> None:
        self._history.append(self._df.copy())
        self._transformation_log.append(action_name)

    def undo(self) -> None:
        if not self._history:
            print("History is empty")
            return

        self._df = self._history.pop()
        action = self._transformation_log.pop()
        print(f"Undone: {action}")

    def get_numeric_columns(self) -> List[str]:
        return self._df.select_dtypes(include=[np.number]).columns.tolist()

    def get_categorical_columns(self) -> List[str]:
        return self._df.select_dtypes(include=['object', 'category']).columns.tolist()

    def handle_missing(self, strategy: str = 'drop', columns: Optional[List[str]] = None) -> None:
        self._save_state(f"handle_missing(strategy={strategy})")
        cols = columns if columns else self._df.columns

        if strategy == 'drop':
            self._df.dropna(subset=cols, inplace=True)
        elif strategy in ['mean', 'median']:
            for col in cols:
                val = self._df[col].mean() if strategy == 'mean' else self._df[col].median()
                self._df[col] = self._df[col].fillna(val)
        elif strategy == 'mode':
            for col in cols:
                self._df[col] = self._df[col].fillna(self._df[col].mode()[0])
        else:
            raise ValueError("Unknown strategy.")

    def scale(self, columns: List[str], method: str = 'standard') -> None:
        self._save_state(f"scale(method={method})")

        scaler = StandardScaler() if method == 'standard' else MinMaxScaler()
        self._df[columns] = scaler.fit_transform(self._df[columns])

    def encode(self, columns: List[str], method: str = 'label') -> None:
        self._save_state(f"encode(method={method})")

        if method == 'label':
            le = LabelEncoder()
            for col in columns:
                self._df[col] = le.fit_transform(self._df[col].astype(str))
        elif method == 'onehot':
            self._df = pd.get_dummies(self._df, columns=columns)
        else:
            raise ValueError("Unknown coding method")

    @property
    def data(self) -> pd.DataFrame:
        return self._df

    @property
    def transformation_history(self) -> List[str]:
        return self._transformation_log


class DatasetSplitter:

    def __init__(self, data: pd.DataFrame, target_column: str) -> None:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")
        if target_column not in data.columns:
            raise ValueError(f"'{target_column}' doesn't exist in '{data.columns}'")

        self._data: pd.DataFrame = data.copy()
        self._target_column: str = target_column
        self._splits: Dict[str, pd.DataFrame] = {}

    def split_train_test(self, test_size: float = 0.2, random_state: int = 0) -> None:
        train, test = train_test_split(
            self._data,
            test_size=test_size,
            random_state=random_state,
            stratify=self._data[self._target_column]
        )
        self._splits = {'train': train, 'test': test}

    def split_train_val_test(self, train_size: float = 0.7, val_size: float = 0.15,
                             test_size: float = 0.15, random_state: int = 0) -> None:
        if not np.isclose(train_size + val_size + test_size, 1.0):
            raise ValueError("Proportion sum doesn't equal 1.0")

        train, temp = train_test_split(
            self._data,
            train_size=train_size,
            random_state=random_state,
            stratify=self._data[self._target_column]
        )

        relative_test_size = test_size / (val_size + test_size)
        val, test = train_test_split(
            temp,
            test_size=relative_test_size,
            random_state=random_state,
            stratify=temp[self._target_column]
        )

        self._splits = {'train': train, 'val': val, 'test': test}

    def get_split(self, name: str) -> pd.DataFrame:
        if name not in self._splits:
            raise KeyError(f"Dataset '{name}' hasn't been created yet")
        return self._splits[name]

    def get_statistics(self) -> pd.DataFrame:
        stats = []
        for name, df in self._splits.items():
            stats.append({
                'set': name,
                'rows': len(df),
                'unique_classes': df[self._target_column].nunique()
            })
        return pd.DataFrame(stats)

    def get_target_distribution(self, name: str) -> pd.Series:
        df = self.get_split(name)
        return df[self._target_column].value_counts(normalize=True)

    def __repr__(self) -> str:
        sets = ", ".join(self._splits.keys()) if self._splits else "None"
        return f"DatasetSplitter(target='{self._target_column}', active_sets=[{sets}])"

if __name__ == "__main__":
    iris = MLDataFrame.from_iris()
    print(iris)
    print(f"Sepal len mean: {iris.mean('sepal length (cm)')}")
    print(f"Sepal width variance: {iris.variance('sepal width (cm)')}")
    iris.add_feature('sepal ratio', lambda iris: getattr(iris,'sepal length (cm)') / getattr(iris,'sepal width (cm)'))
    print(getattr(iris,'sepal ratio'))
    print(iris.describe())
    try:
        setattr(iris, 'target', [1,2,3])
    except AttributeError as e:
        print(f"Error: {e}")

    print('---------')
    data_obj1 = pd.DataFrame({
        'age': [25, 30, np.nan, 45],
        'city': ['Warsaw', 'Krakow', 'Warsaw', None],
        'salary': [5000, 8000, 12000, 7000]
    })

    preprocessor = DataPreprocessor(data_obj1)
    preprocessor.handle_missing(strategy='median', columns=['age'])
    preprocessor.encode(columns=['city'], method='label')
    preprocessor.scale(columns=['salary'], method='minmax')

    print("After transformations:\n", preprocessor.data)
    print("History:", preprocessor.transformation_history)

    preprocessor.undo()
    print("\nAfter undoing:\n", preprocessor.data)

    print('---------')
    data_obj2 = pd.DataFrame({
        'feature1': np.random.rand(100),
        'feature2': np.random.rand(100),
        'label': np.random.choice(['A', 'B'], size=100)
    })

    splitter = DatasetSplitter(data_obj2, target_column='label')
    splitter.split_train_val_test(train_size=0.7, val_size=0.15, test_size=0.15)
    print(splitter.get_statistics())
    print(splitter.get_target_distribution('val'))

    train_df = splitter.get_split('train')
    print(f"\nTrain dataset shape: {train_df.shape}")

