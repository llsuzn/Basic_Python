# %% [markdown]
# # 주피터 노트북 사용법 학습
# 
# ## 마크다운, 파이썬 셀을 추가
# - 현재 셀 앞에 셀 추가 : a
# - 현재 셀 뒤에 셀 추가 : b
# - 현재 셀을 마크다운으로 변경 : 포커스(커서가 깜빡거리지 않는)만 있는 상태 : m
# - 현재 코드를 셀으로 변경 : 포커스(커서가 깜빡거리지 않는)만 있는 상태 : y

# %%
# 최초 작성된 python 셀

# %% [markdown]
# ## 파이썬 셀 실행
# - 셀 실행 : Ctrl + Enter
# - 입력 셀 실행 후 아래 셀로 이동 (없으면 새로운 셀 추가) : Shift + Enter
# - 입력영역 실행 후 아래 새로운 영역 추가 : Alt + Enter
# - 주석 처리 : Ctrl + K + C or Ctrl + '/'

# %%
print('Hello, Jupyter')

# %% [markdown]
# ## 디버깅!
# 매우 중요
# - Ctrl + Alt + Shift + Enter : 디버깅 셀

# %%
arr = [1,'2',True,'Hello',3.1415926585]

for i in arr:
    print(i)

# %% [markdown]
# ### 함수 디버깅

# %%
def plus(x,y):
    val = x + y
    return val

def div(x,y):
    val = x / y
    return val

print('더하기')
print(plus(10,4))

# %%
print('나누기')
print(div(10,4))


print(arr)
arr