"""
RECORD CHECK  -  my version
===========================

Name  : Raimi Thomas Eappen
Lane  :  AI 
Date  : 13-11-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line=raw_line.strip()
    survey,rest = line.split(",", 1)
    survey=survey.strip().lower()

    fields={}
    for piece in rest.split(","):
        key,value=piece.split("=")
        fields[key.strip().lower()]=float(value.strip())

    return {"Survey": survey, "Rating": fields["rating"], "Age": fields["age"]}

def status_of(record):
    """Return FLAGGED when below 3 and OK for the others."""
  
    if record["Rating"] < 3:
        return "FLAGGED"
    else :
      return "OK"

c1=0;c2=0;c3=0

with open("messy_survey_records.txt") as f:
    for raw_lines in f:
      if not raw_lines.strip():
        continue

      c1+=1
      try:
        record=parse_line(raw_lines)
      except ValueError:
        print("Could not parse:",raw_lines)
        continue

      status=status_of(record)
      c2+=1
      if status == "FLAGGED":
        c3+=1

      print(record,"-",status)
      
print(
    f"Summary: {c1} input records , {c2} valid,"
    f" {c3} flagged"
)




