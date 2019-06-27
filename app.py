from flask import Flask , render_template
from webscraping import ed

app = Flask(__name__)
edi = ed()

@app.route('/')
def article():
  return render_template('index.html',e = edi)

if __name__=='__main__':
  app.run(debug = True)

# for e in edi:
#   print(e)