"""
Teste dee Velocidade com expressões Geradores

# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num

gel = nums()
print(gel)
print(next(gel))
print(next(gel))

# Generator Expression
ge2 = (num for num in range(1, 10))

print(ge2)
print(next(ge2))
print(next(ge2))
"""
# Realizando o teste de velocidade
import time

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(1, 100000000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(1, 100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehesion levou {list_tempo}')




###########################


import streamlit as st
import streamlit.components.v1 as components

# ===============================
# CONFIGURAÇÃO
# ===============================
st.set_page_config(
    page_title="Cancelamento",
    layout="wide"
)

# ===============================
# FUNÇÕES AUXILIARES
# ===============================
def fmt_int_br(x):
    return f"{int(round(float(x))):,}".replace(",", ".")


def fmt_pct_br(x):
    return f"{float(x):.1f}".replace(".", ",") + "%"


def parse_num_or_pct(value):
    if isinstance(value, (int, float)):
        return "number", float(value)

    v = str(value).strip()
    is_percent = "%" in v or "pp" in v

    v = (
        v.replace("%", "")
         .replace("pp", "")
         .replace(".", "")
         .replace(",", ".")
    )

    return ("percent" if is_percent else "number"), float(v)


def format_value(value):
    tipo, num = parse_num_or_pct(value)
    return fmt_pct_br(num) if tipo == "percent" else fmt_int_br(num)


def calc_delta(atual, ref):
    tipo_a, num_a = parse_num_or_pct(atual)
    tipo_r, num_r = parse_num_or_pct(ref)

    diff = num_a - num_r

    if diff > 0:
        cls, arrow, sign = "up", "↑", "+"
    elif diff < 0:
        cls, arrow, sign = "down", "↓", "−"
    else:
        cls, arrow, sign = "flat", "↔", ""

    if tipo_a == "percent":
        diff_str = f"{abs(diff):.1f}".replace(".", ",") + " pp"
        ref_str = fmt_pct_br(num_r)
    else:
        diff_str = fmt_int_br(abs(diff))
        ref_str = fmt_int_br(num_r)

    return cls, arrow, sign, diff_str, ref_str


# ===============================
# CARD (HTML + CSS INLINE)
# ===============================
def render_card(
    title,
    value,
    mes_anterior,
    meses_12,
    ki_anterior,
    recorde,
    meta
):
    value_str = format_value(value)

    deltas = [
        ("Mês anterior", mes_anterior),
        ("12 meses", meses_12),
        ("KI anterior", ki_anterior),
        ("Recorde", recorde),
        ("Meta", meta),
    ]

    rows_html = ""

    for label, ref in deltas:
        cls, arrow, sign, diff_str, ref_str = calc_delta(value, ref)

        rows_html += f"""
        <div class="delta-row">
            <div class="delta-label">{label}</div>
            <div class="delta-content">
                <div class="delta-volume">{ref_str}</div>
                <div class="badge {cls}">{sign}{diff_str}</div>
                <div class="arrow">{arrow}</div>
            </div>
        </div>
        """

    html = f"""
    <html>
    <head>
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
        }}

        .card {{
            background: #ffffff;
            border-radius: 12px;
            padding: 16px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
            border: 1px solid #eaeaea;
        }}

        .title {{
            font-size: 20px;
            font-weight: 700;
            text-align: center;
            color: #333;
        }}

        .value {{
            font-size: 28px;
            font-weight: 800;
            text-align: center;
            margin: 8px 0 14px;
            color: #111;
        }}

        .delta-row {{
            display: flex;
            align-items: center;
            font-size: 14px;
            margin-top: 4px;
        }}

        .delta-label {{
            min-width: 110px;
            color: #666;
            font-weight: 600;
        }}

        .delta-content {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-left: -25px;
        }}

        .delta-volume {{
            font-weight: 600;
            color: #444;
        }}

        .badge {{
            padding: 2px 8px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 13px;
            border: 1px solid;
        }}

        .up {{
            color: #0f9d58;
            background: rgba(15,157,88,.1);
            border-color: rgba(15,157,88,.25);
        }}

        .down {{
            color: #d93025;
            background: rgba(217,48,37,.1);
            border-color: rgba(217,48,37,.25);
        }}

        .flat {{
            color: #b8860b;
            background: rgba(255,193,7,.15);
            border-color: rgba(255,193,7,.35);
        }}

        .arrow {{
            font-size: 16px;
            font-weight: 700;
            width: 18px;
            text-align: center;
        }}
    </style>
    </head>

    <body>
        <div class="card">
            <div class="title">{title}</div>
            <div class="value">{value_str}</div>
            {rows_html}
        </div>
    </body>
    </html>
    """

    components.html(html, height=360)


# ===============================
# EXEMPLO – 6 CARDS
# ===============================
cards_data = [
    ("Cancelamentos (Mês)", 245, 237, 198, 260, 180, 200),
    ("Média 12M",           198, 200, 210, 205, 180, 190),
    ("MoM",                 "-2,4%", "-1,8%", "+0,6%", "-3,1%", "-4,0%", "-2,0%"),
    ("YoY",                 "+8,9%", "+7,2%", "+5,1%", "+6,0%", "+10,0%", "+7,0%"),
    ("Retenção",            "91,3%", "90,9%", "88,4%", "90,1%", "92,0%", "93,0%"),
    ("Run-rate",            260, 245, 220, 240, 300, 280),
]

cols = st.columns(6)
for col, card in zip(cols, cards_data):
    with col:
        render_card(*card)


