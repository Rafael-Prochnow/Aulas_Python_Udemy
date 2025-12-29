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





# ===============================

# Injeta o CSS apenas uma vez
if "css_cards_injected" not in st.session_state:
    st.markdown("""
    <style>
    .card {
        background: #ffffff;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        border: 1px solid #eaeaea;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    /* Título 20px centralizado */
    .card .title {
        font-size: 20px;
        color: #333;
        font-weight: 700;
        text-align: center;
        line-height: 1.1;
    }

    /* Valor 28px centralizado */
    .card .value {
        font-size: 28px;
        font-weight: 800;
        color: #111;
        text-align: center;
        line-height: 1.2;
        white-space: nowrap;
    }

    /* Linha do delta alinhada à esquerda */
    .card .delta-row {
        display: flex;
        align-items: center;   /* alinha verticalmente no centro */
        justify-content: flex-start;
        gap: 0px;              /* sem gap entre label e content; o recuo será no content */
        font-size: 14px;
    }

    .delta-label {
        color: #666;
        font-weight: 600;
        /* largura mínima opcional; se preferir livre, remova */
        min-width: 110px;
    }

    /* Conteúdo (volume, diff e seta) com recuo de 2 cm */
    .delta-content {
        display: flex;
        align-items: center;
        gap: 8px;             /* espaço interno entre volume, diff e seta */
        margin-left: -25px;      /* >>> recuo solicitado titulo e delta <<< */
    }

    .delta-volume {
        color: #444;
        font-weight: 600;
    }

    /* Diferença com cor por sinal */
    .diff-badge {
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 12px;
        border: 1px solid transparent;
        white-space: nowrap;
    }
    .diff-up { 
        color: #0f9d58; 
        background: rgba(15, 157, 88, 0.10);
        border-color: rgba(15, 157, 88, 0.25);
    }
    .diff-down { 
        color: #d93025; 
        background: rgba(217, 48, 37, 0.10);
        border-color: rgba(217, 48, 37, 0.25);
    }
    .diff-flat { 
        color: #b8860b; /* amarelo escuro */
        background: rgba(255, 193, 7, 0.15);
        border-color: rgba(255, 193, 7, 0.35);
    }

    .delta-arrow {
        font-size: 16px;
        font-weight: 700;
        min-width: 18px;
        text-align: center;
    }

    /* Responsividade opcional: reduz recuo em telas muito estreitas */
    @media (max-width: 900px) {
        .delta-content { margin-left: 1cm; }
    }
    @media (max-width: 600px) {
        .delta-content { margin-left: 0.5cm; }
    }
    </style>
    """, unsafe_allow_html=True)
    st.session_state["css_cards_injected"] = True


# --- Utilitários de formatação/parse ---
def fmt_int_br(x):
    """Formata inteiros no padrão pt-BR (milhares com ponto)."""
    try:
        return f"{int(round(float(x))):,}".replace(",", ".")
    except Exception:
        return str(x)


def fmt_pct_br(p, casas=1):
    """Formata percentual (0-100) com vírgula e sinal %, ex.: 91,3%."""
    try:
        return (f"{float(p):.{casas}f}").replace(".", ",") + "%"
    except Exception:
        return str(p)


def parse_num_or_pct(value):
    """
    Recebe número ou string (ex.: '91,3%', '260', '+8,9%').
    Retorna (tipo, numero), onde tipo ∈ {'number','percent'} e numero é float.
    Para 'percent', interpreta a parte numérica (ex.: '91,3%' -> 91.3).
    """
    if isinstance(value, (int, float)):
        return "number", float(value)
    if isinstance(value, str):
        v = value.strip().lower()
        is_percent = "%" in v or "pp" in v
        import re
        num_str = re.sub(r"[^0-9,.\-+]", "", v)
        if "," in num_str and "." in num_str:
            num_str = num_str.replace(".", "").replace(",", ".")
        elif "," in num_str and "." not in num_str:
            num_str = num_str.replace(",", ".")
        try:
            num = float(num_str)
            return ("percent" if is_percent else "number"), num
        except Exception:
            return "number", 0.0
    return "number", 0.0


def render_card(title, value, prev_value):
    """
    title: str
    value: número ou string (ex.: '260', '91,3%')
    prev_value: número ou string (ex.: '245', '90,9%')
    """
    tipo_atual, num_atual = parse_num_or_pct(value)
    tipo_prev, num_prev = parse_num_or_pct(prev_value)

    # string exibida para o valor principal
    value_str = fmt_pct_br(
        num_atual) if tipo_atual == "percent" else fmt_int_br(num_atual)
    # string exibida para o mês anterior
    prev_str = fmt_pct_br(
        num_prev) if tipo_prev == "percent" else fmt_int_br(num_prev)

    # calcula diferença (valor atual - mês anterior)
    diff = num_atual - num_prev if tipo_atual == tipo_prev else 0.0

    # decide classe e seta
    if diff > 0:
        diff_class = "diff-up"
        arrow = "↑"
        sign_prefix = "+"
    elif diff < 0:
        diff_class = "diff-down"
        arrow = "↓"
        sign_prefix = "−"
    else:
        diff_class = "diff-flat"
        arrow = "↔"
        sign_prefix = ""

    # formata diferença
    if tipo_atual == "percent" and tipo_prev == "percent":
        diff_abs = abs(diff)  # em pontos percentuais (0-100)
        diff_str = (f"{diff_abs:.1f} pp").replace(".", ",")
    else:
        diff_str = fmt_int_br(abs(diff))

    html = f"""
    <div class="card">
        <div class="title">{title}</div>
        <div class="value">{value_str}</div>
        <div class="delta-row">
            <div class="delta-label">Mês anterior</div>
            <div class="delta-content">
                <div class="delta-volume">{prev_str}</div>
                <div class="diff-badge {diff_class}">{sign_prefix}{diff_str}</div>
                <div class="delta-arrow">{arrow}</div>
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


# --- Exemplo com 6 cards lado a lado ---
cards_data = [
    ("Cancelamentos (Mês)", 245, 237),
    ("Média 12M",           198, 200),
    ("MoM",                 "-2,4%", "-1,8%"),  # diferença mostrada em pp
    ("YoY",                 "+8,9%", "+7,2%"),
    ("Retenção",            "91,3%", "90,9%"),
    ("Run-rate",            260, 245),
]

cols = st.columns(6)
for col, (title, value, prev) in zip(cols, cards_data):
    with col:
        render_card(title, value, prev)


