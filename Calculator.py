import streamlit as st
st.title("CALCULATOR APP 😎")
st.set_page_config(page_title="Calculator", layout="centered", page_icon="🧮")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
html, body, [data-testid="stAppViewContainer"] {
    background: #111 !important;
}
[data-testid="stHeader"], footer, #MainMenu { visibility: hidden; }
.block-container { max-width: 340px !important; padding-top: 3rem !important; }
.screen {
    background: #1a1a1a;
    border: 1px solid #333;
    border-radius: 14px;
    padding: 10px 10px 14px;
    margin-bottom: 16px;
    text-align: right;
    font-family: 'Share Tech Mono', monospace;
}
.screen-expr { color: #666; font-size: 14px; min-height: 20px; }
.screen-num  { color: #fff; font-weight: bold; line-height: 1.1; word-break: break-all; }
button[kind="secondary"] {
    width: 95%;
    height: 40px;
    border-radius: 12px;
    font-size: 22px;
    font-family: 'Share Tech Mono', monospace;
    font-weight: bold;
    border: none;
}
</style>
""", unsafe_allow_html=True)
for k, v in {"num1": None, "op": None, "display": "0", "expr": "", "fresh": False}.items():
    if k not in st.session_state:
        st.session_state[k] = v
S = st.session_state

def _fmt(v):
    return str(int(v)) if float(v) == int(float(v)) else f"{float(v):.6g}"
def press_digit(d):
    if S.fresh:
        S.display = d; S.fresh = False
    else:
        S.display = d if S.display == "0" else S.display + d
def press_op(op):
    S.num1 = float(S.display)
    S.op = op
    S.expr = f"{_fmt(S.num1)} {op}"
    S.fresh = True
def press_eq():
    if S.op is None or S.num1 is None: return
    a, b = S.num1, float(S.display)
    if S.op == "+": result = a + b
    elif S.op == "-": result = a - b
    elif S.op == "x": result = a * b
    elif S.op == "/":
        result = None if b == 0 else a / b
    S.expr = f"{_fmt(a)} {S.op} {_fmt(b)} ="
    S.display = "Error" if result is None else _fmt(result)
    S.num1 = None; S.op = None; S.fresh = True
def press_clear():
    S.display = "0"; S.expr = ""
    S.num1 = None; S.op = None; S.fresh = False
size = "52px" if len(S.display) <= 7 else "36px" if len(S.display) <= 11 else "26px"
st.markdown(f"""
<div class="screen">
  <div class="screen-expr">{S.expr or "&nbsp;"}</div>
  <div class="screen-num" style="font-size:{size}">{S.display}</div>
</div>
""", unsafe_allow_html=True)
# Row 1
c1,c2,c3,c4 = st.columns(4)
if c1.button("7"): press_digit("7")
if c2.button("8"): press_digit("8")
if c3.button("9"): press_digit("9")
if c4.button("DIV /"): press_op("/")
# Row 2
c1,c2,c3,c4 = st.columns(4)
if c1.button("4"): press_digit("4")
if c2.button("5"): press_digit("5")
if c3.button("6"): press_digit("6")
if c4.button("MUL *"): press_op("x")
# Row 3
c1,c2,c3,c4 = st.columns(4)
if c1.button("1"): press_digit("1")
if c2.button("2"): press_digit("2")
if c3.button("3"): press_digit("3")
if c4.button("SUB -"): press_op("-")
# Row 4
c1,c2,c3,c4 = st.columns(4)
if c1.button("C"):  press_clear()
if c2.button("0"):  press_digit("0")
if c3.button("="):  press_eq()
if c4.button("ADD+"): press_op("+")