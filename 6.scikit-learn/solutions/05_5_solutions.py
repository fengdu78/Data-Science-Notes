from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import KBinsDiscretizer

pipe_cat = OneHotEncoder(handle_unknown='ignore')
pipe_num = KBinsDiscretizer()
