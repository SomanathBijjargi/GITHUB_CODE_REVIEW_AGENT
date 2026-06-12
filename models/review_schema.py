from pydantic import BaseModel
from typing import List


class Bug(BaseModel):
    line: str
    description: str
    severity: str


class SecurityIssue(BaseModel):
    issue: str
    recommendation: str


class PerformanceIssue(BaseModel):
    issue: str
    recommendation: str


class QualityIssue(BaseModel):
    issue: str
    recommendation: str


class Score(BaseModel):
    security: int
    quality: int
    performance: int


class ReviewResponse(BaseModel):
    summary: str
    bugs: List[Bug]
    security: List[SecurityIssue]
    performance: List[PerformanceIssue]
    quality: List[QualityIssue]
    score: Score