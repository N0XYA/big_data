import pandas as pd
import plotly.graph_objs as go


df = pd.read_csv("winequality-red.csv")
columns = df.columns.values.tolist()
first_bar = df.loc[df["quality"] == 3]
second_bar = df.loc[df["quality"] == 8]

fig = go.Figure(data=[go.Bar(x=columns, y=first_bar.mean(), marker=dict(color=list(range(len(columns))), coloraxis="coloraxis", line=dict(color="black",width=2)), showlegend=False),
                      go.Bar(x=columns, y=second_bar.mean(), marker=dict(color=list(range(len(columns))), coloraxis="coloraxis", line=dict(color="black",width=2)), showlegend=False)])

fig.update_layout(
    title="Диаграмма значений признаков вин разного качества", title_font_size=20, title_x=0.5,
    xaxis_title="Признаки", xaxis_title_font_size=16, xaxis_tickangle=315, xaxis_tickfont_size=14,
    yaxis_title="Значения", yaxis_title_font_size=16, yaxis_tickfont_size=14,
    height=700,
    margin=dict(l=0, r=0, t=40)
)
fig.update_xaxes(gridwidth=2, gridcolor="ivory")
fig.update_yaxes(gridwidth=2, gridcolor="ivory")
fig.show()