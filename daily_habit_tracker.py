# -*- coding: utf-8 -*-
"""daily_habit_tracker
Custom CLI logger for daily health habit tracking (July 2025)
"""

import csv
from datetime import date

def write_daily_log():
  today = date.today().isoformat()
  entry = {
      'date' : today,
      'exercise' = input("운동 점수 (0~5): "),
      'study' = input("공부 점수 (0~5): "),
      'health' = input("건강관리 점수 (0~5): "),
      'self_care' = input("셀프케어 점수 (0~5): "),
      'diet' = input("식단 점수 (0~5): "),
      'wellness_score' = input("전체 웰빙 점수 (0~10): ")
  }

  with open('data/daily_habits.csv', mode = 'a', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames = entry.keys())
    writer.writerow(entry)
    print(f"[{today}] 기록이 저장되었습니다!")

if __name__ == "__main__":
  record_habit_entry()