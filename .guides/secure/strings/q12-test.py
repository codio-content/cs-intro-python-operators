import ast, requests, os, random

print("<html>")
print("<style>error{color:red;font-weight:bold}success{color:darkgreen;font-weight:bold}hint{color:blue}*[stacktrace]{font-size:9px;color:darkgray;line-height:11px}inline-code{font-family:monospace}</style>")

def report_score(score, maxp):
  score = max(0, score)
  if score == maxp:
    print("<success>Good job</success>")
  url = "{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], score)
  requests.get(url)
  print("\n<b>Score:</b> %d out of %d" % (score, maxp))
  
with open('strings/Q12_Vowels.py') as subfile:
  subtext = subfile.read()
  
max_score = 5
score = max_score

NOT_SV = 'MAKE mud not war was a PROJECT by the US military yay'.split(' ')
IS_SV = 'Each audible either AEsop eulogy Feud dIAmond louise SWeat Main Street Tanzania reVeNuE please assignee chOO Codio Poughkeepsie eVentuAl'.split(' ')

exec(subtext)
for word in NOT_SV:
  if is_sv_present(word):
    print("<error>[FAIL] word=<inline-code>{}</inline-code> does not have subsequent vowels, but your function returned <inline-code>True</inline-code></error>".format(repr(word)))
    score -= 0.4
  else:
    print("<success>[PASS]</success>")
    

for word in IS_SV:
  if not is_sv_present(word):
    print("<error>[FAIL] word=<inline-code>{}</inline-code> has subsequent vowels, but your function returned <inline-code>False</inline-code></error>".format(repr(word)))
    score -= 0.4
  else:
    print("<success>[PASS]</success>")

report_score(max(0, score), max_score)

print("</html>")