from fastapi import FastAPI
import pandas as pd
import os
import sys

# 경로 추가
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.dna_extractor import DNAExtractor
from core.epv_model import WhatIfEngine

app = FastAPI()

dna_tool = None
whatif_engine = None

@app.on_event("startup")
async def startup_event():
    global dna_tool, whatif_engine
    path = os.path.join(BASE_DIR, "data", "raw_data.csv")
    print(f"📡 로딩 중: {path}")
    
    # 57만건 데이터를 여기서 한 번만 읽습니다.
    full_df = pd.read_csv(path)
    
    # 생성자에 데이터프레임(full_df)을 직접 넘깁니다.
    dna_tool = DNAExtractor(full_df)
    whatif_engine = WhatIfEngine(full_df)
    print("✅ 데이터 로드 및 엔진 준비 완료!")

@app.get("/")
def home(): return {"msg": "K-Tactician API"}

@app.get("/teams")
def teams(): return {"teams": dna_tool.df['team_name_ko'].unique().tolist()}

@app.get("/simulate/pass")
def simulate(sx: float, sy: float, tx: float, ty: float):
    return whatif_engine.simulate_pass(sx, sy, tx, ty)