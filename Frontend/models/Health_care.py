from typing import Literal
from pydantic import BaseModel, Field

class InputModel(BaseModel):
    성별: Literal['남성', '여성'] = Field(
        default='남성',
        description='사용자의 성별'
    )
    나이: int = Field(
        ge=20,
        description='사용자의 나이'
    )
    키_cm: float = Field(
        ge=175.0,
        description='사용자의 키 (cm)'
    )
    몸무게_kg: float = Field(
        ge=75.0,
        description='사용자의 몸무게 (kg)'
    )
    운동_부위: Literal[
        '전신', 
        '등', 
        '가슴', 
        '어깨', 
        '팔', 
        '하체'
    ] = Field(
        default='전신',
        description='운동 집중 부위'
    )
    운동_목표: Literal[
        '근성장', 
        '체력 증진', 
        '기분 전환'
    ] = Field(
        default='근성장',
        description='운동 목표'
    )

class OutputModel(BaseModel):
    추천_루틴: str = Field(
        description='추천 운동 루틴',
    )


