import functools

from numpy.core.fromnumeric import transpose
from numpy.core.numeric import cross
from numpy.lib.function_base import percentile


def compose2(func1, func2):
    return lambda x: func2(func1(x))


# 순서대로 적용될 함수 리스트
pipes = [lambda x: x + 1, lambda x: x * 2, lambda x: x * 10]

# reduce를 이용하여 func2와 함께 새로운 함수를 만드는 일을 반복
comp_func = functools.reduce(compose2, pipes)

for i, x in enumerate(range(5, 10)):
    print(f'{i}: {comp_func(x)}')


# 0: 120
# 1: 140
# 2: 160
# 3: 180
# 4: 200
# reduce에 대해서, 어떻게 사용하는지 등에 대하여 알 필요가 있음


#--------------------------------------------------------------

import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectPercentile, f_regression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge

cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, test_size=0.3, shuffle=True, random_state=42)

scaler = MinMaxScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
select = SelectPercentile(score_func=f_regression, percentile=5).fit(x_train_scaled, y_train)
x_selected = select.transform(x_test_scaled)
# print(f'x_train_scaled.shape: {x_train_scaled.shape}')
# print(f'x_test_scaled.shape: {x_test_scaled.shape}')
# print(f'x_test.shape: {x_test.shape}')
# print(f'x_selected.shape: {x_selected.shape}')
# print(f'y_test.shape: {y_test.shape}')

svc = SVC(gamma='auto')
svc.fit(x_train_scaled, y_train)

prd = svc.predict(x_test_scaled)
print(f'테스트 점수: {svc.score(x_test_scaled, y_test):.2f}')


"""
Object of pipelines:
To assemble several steps that can be cross-validated together while setting different parameters
(데이터변환(전처리) 과정과 모델을 연결하여 코드를 줄이고 재사용성을 높이기 위함)
"""
pipe = Pipeline([
    ('scaler', MinMaxScaler()),
    ('svm', SVC(gamma='auto'))
])
pipe.fit(x_train_scaled, y_train)
print(f'테스트 점수(파이프라인): {pipe.score(x_test_scaled, y_test):.2f}')
print(pipe.get_params)
