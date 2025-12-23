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
# CONFIGURAÇÃO
# ===============================
st.set_page_config(
    page_title="Cancelamento",
    layout="wide"
)

# ===============================
# CSS (APENAS TÍTULO E LINHA)
# ===============================
st.markdown("""
<style>
.titulo {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-top: 15px;
}

.linha-vermelha {
    height: 4px;
    background-color: #ef4444;
    width: 100%;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# CONTEÚDO PRINCIPAL
# ===============================
with col_main:
    st.markdown('<div class="titulo">Cancelamento</div>', unsafe_allow_html=True)
    st.markdown('<div class="linha-vermelha"></div>', unsafe_allow_html=True)

    st.dataframe(df_filtrado, width="stretch")

    st.metric(
        "Total de gastos",
        f"R$ {abs(df_filtrado['Valor'].sum()):,.2f}"
    )





