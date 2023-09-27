import pandas as pd
import plotly.graph_objs as go


df = pd.read_csv("winequality-red.csv")
columns = df.columns.values.tolist()
first_bar = df.loc[df["quality"] == 8]
first_bar = first_bar.drop(columns=["quality", "chlorides", "citric acid", "volatile acidity"], inplace=False)
values = first_bar.mean()

fig = go.Figure(data=[go.Pie(labels=columns, values=values)])
fig.update_traces(
    marker=dict(colors=list(range(len(columns))), line=dict(color='#000000', width=2))
)
fig.update_layout(
    title="Диаграмма значений признаков вин разного качества", title_font_size=20, title_x=0.5,
    height=700,
    margin=dict(l=0, r=0, t=40)
)
print(first_bar.head())
fig.show()