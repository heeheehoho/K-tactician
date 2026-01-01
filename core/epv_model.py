import numpy as np

class WhatIfEngine:
    def __init__(self, df):
        self.df = df
        self.pass_data = self.df[self.df['type_name'] == 'Pass'].copy()

    def simulate_pass(self, sx, sy, tx, ty):
        # 1. 기하학적 가치 계산 (골대와의 거리)
        dist_to_goal = np.sqrt((100 - tx)**2 + (50 - ty)**2)
        
        # 2. [Transformer가 활약할 부분] 
        # 실제로는 여기서 '시퀀스 데이터'를 Transformer에 넣어 성공 확률을 예측합니다.
        # 지금은 MVP를 위해 거리 기반의 가상 확률을 반환합니다.
        base_prob = 0.85 if dist_to_goal > 40 else 0.45
        
        return {
            "situation": {"start": [sx, sy], "target": [tx, ty]},
            "success_probability": base_prob,
            "expected_value_gain": round(float(100 - dist_to_goal), 2),
            "ai_comment": "위험하지만 치명적인 패스입니다." if base_prob < 0.5 else "안정적인 연결입니다."
        }