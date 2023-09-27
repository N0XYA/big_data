import uvicorn
from fastapi import FastAPI
import bars
app = FastAPI()

@app.get("bars")
def bars():
    bars.plot_bars()
    return "Done"

'''
in project folder:
uvicorn main:app --reload
'''
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
