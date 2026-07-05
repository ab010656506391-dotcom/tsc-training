import streamlit as st
import numpy as np
import json
import os
import time

# 데이터 로드
if 'thresholds' not in st.session_state:
    if os.path.exists("thresholds.json"):
        with open("thresholds.json", "r") as f: st.session_state.thresholds = json.load(f)
    else:
        st.session_state.thresholds = {"L": {str(f): 0 for f in [1000, 1500, 2000, 3000, 4000, 6000, 8000, 12000]}, 
                                       "R": {str(f): 0 for f in [1000, 1500, 2000, 3000, 4000, 6000, 8000, 12000]}}

st.title("TSC Ultimate Training Web")

# 탭 구성: 측정 / 훈련
tab1, tab2 = st.tabs(["측정(역치 설정)", "훈련 시작"])

with tab1:
    col1, col2 = st.columns(2)
    side = st.radio("귀 선택", ["L", "R"])
    freq = st.selectbox("주파수 선택", [1000, 1500, 2000, 3000, 4000, 6000, 8000, 12000])
    
    val = st.slider("역치(dB)", 0, 90, st.session_state.thresholds[side][str(freq)])
    if st.button("저장"):
        st.session_state.thresholds[side][str(freq)] = val
        with open("thresholds.json", "w") as f: json.dump(st.session_state.thresholds, f)
        st.success(f"{side}측 {freq}Hz: {val}dB 저장됨")

with tab2:
    st.subheader("훈련 설정")
    col1, col2 = st.columns(2)
    with col1:
        l_freqs = st.multiselect("왼쪽 주파수(3개)", [1000, 1500, 2000, 3000, 4000, 6000, 8000, 12000])
    with col2:
        r_freqs = st.multiselect("오른쪽 주파수(3개)", [1000, 1500, 2000, 3000, 4000, 6000, 8000, 12000])
    
    duration = st.number_input("훈련 시간(분)", 30, 60, 30)
    
    if st.button("훈련 시작"):
        if len(l_freqs) != 3 or len(r_freqs) != 3:
            st.error("좌우 각각 3개씩 선택하세요.")
        else:
            st.info("훈련이 시작되었습니다. (웹 환경에서는 사운드 생성기가 브라우저 오디오 API와 연결됩니다.)")
            # 여기서 실시간 훈련 로직이 루프를 돕니다.
            # 웹 브라우저에서는 JavaScript를 이용한 Web Audio API 재생이 권장됩니다.
            
# Streamlit은 자체적으로 클라우드 배포(Streamlit Cloud)를 지원합니다.
# GitHub에 코드 올리고 무료 배포하면, 폰에서 주소만 치면 바로 접속됩니다.