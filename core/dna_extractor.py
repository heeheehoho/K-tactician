import pandas as pd

class DNAExtractor:
    def __init__(self, df):
        # 이미 로드된 데이터프레임을 그대로 사용합니다.
        self.df = df
        
    def get_team_dna(self, team_name):
        team_events = self.df[self.df['team_name_ko'] == team_name]
        if team_events.empty:
            return {"error": "팀을 찾을 수 없습니다."}

        passes = team_events[team_events['type_name'] == 'Pass']
        
        # DNA 지표 계산
        forward_ratio = (passes['end_x'] > passes['start_x']).mean() if not passes.empty else 0
        success_rate = (passes['result_name'] == 'Successful').mean() if not passes.empty else 0
        
        return {
            "team": team_name,
            "dna_metrics": {
                "forward_attack_intensity": round(float(forward_ratio), 3),
                "pass_accuracy": round(float(success_rate) * 100, 2),
                "total_events": len(team_events)
            }
        }