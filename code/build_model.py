import os
import numpy as np

from common.rune_file import RuneFile
from common.futhark_model import FutharkModel
from common.futhark_labels import FutharkLabels

model = FutharkModel()
labels = FutharkLabels()

X, y = [], []

for filename in os.listdir('data'):
  file = RuneFile.from_file(f'data/{filename}')
  X.append(file.rune_data)
  y.append(file.rune_name)

X = np.array(X)
y = np.array(y)

y = labels.encode(y)

score = model.build(X, y)
model.save()

print(score)