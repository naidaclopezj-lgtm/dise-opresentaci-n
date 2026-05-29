import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

from pathlib import Path

st.set_page_config(
    page_title="Milestone 3 — Subsistema de Alimentación de Plátano",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:wght@400;600&display=swap');

html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }

.report-title {
    font-family: 'Source Serif 4', serif;
    font-size: 2rem;
    font-weight: 600;
    color: #1a3050;
    line-height: 1.3;
    margin-bottom: 0.25rem;
}
.report-subtitle {
    font-size: 1rem;
    color: #4a5568;
    margin-bottom: 0.1rem;
}
.section-heading {
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: #1a3050;
    border-left: 4px solid #1a3050;
    padding-left: 0.75rem;
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
}
.metric-card {
    background: #ffffff;
    border: 1px solid #d0d5dd;
    border-top: 4px solid #1a3050;
    border-radius: 6px;
    padding: 1rem 1.25rem;
    text-align: center;
}
.metric-value {
    font-size: 1.6rem;
    font-weight: 600;
    color: #1a3050;
    line-height: 1.2;
}
.metric-label {
    font-size: 0.78rem;
    color: #6b7280;
    margin-top: 0.25rem;
}
.metric-check {
    font-size: 0.75rem;
    color: #16a34a;
    margin-top: 0.2rem;
    font-weight: 500;
}
.stage-card {
    background: #f0f4f8;
    border-left: 4px solid #1a3050;
    border-radius: 4px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
}
.stage-title {
    font-weight: 600;
    color: #1a3050;
    font-size: 0.95rem;
    margin-bottom: 0.4rem;
}
.eq-box {
    background: #f8f7f4;
    border: 1px solid #d0d5dd;
    border-radius: 4px;
    padding: 0.75rem 1rem;
    font-family: 'Courier New', monospace;
    font-size: 0.88rem;
    color: #1a3050;
    margin: 0.5rem 0;
}
.result-ok { color: #16a34a; font-weight: 600; }
.result-label { color: #4a5568; font-size: 0.85rem; }
.divider { border: none; border-top: 1px solid #d0d5dd; margin: 1.5rem 0; }
.footer-text {
    font-size: 0.78rem;
    color: #9ca3af;
    text-align: center;
    padding: 1rem 0;
}
</style>
""", unsafe_allow_html=True)
# ════════════════════════════════════════════════════════════════
# HEADER
# ════════════════════════════════════════════════════════════════

col_logo, col_title = st.columns([1,7])


with col_title:
    st.markdown("""
    <div style='background:#1a3050;
                color:white;
                padding:1.75rem 2rem;
                border-radius:8px;
                margin-bottom:1rem;'>

        <div style='font-family:Source Serif 4, serif;
                    font-size:1.9rem;
                    font-weight:600;
                    line-height:1.2;'>
            Diseño Final y Validación de Prototipo
        </div>

        <div style='font-size:1.15rem;
                    margin-top:0.35rem;'>
            Subsistema de Alimentación para Máquina Procesadora de Plátano
        </div>

        <div style='font-size:0.9rem;
                    margin-top:0.7rem;
                    opacity:0.8;'>
            Milestone 3 · Diseño Mecánico I · Universidad Autónoma de Manizales · 2026-I
        </div>

    </div>
    """, unsafe_allow_html=True)

with st.sidebar:

    st.markdown("## Navegación")

    selected = st.radio(
        "",
        [
            "Resumen ejecutivo",
            "Diseño del sistema",
            "Prototipo",
            "Evidencia",
            "Discusión",
            "Conclusiones"
        ]
    )
# ════════════════════════════════════════════════════════════════════[...]
# 1. RESUMEN EJECUTIVO
# ════════════════════════════════════════════════════════════════════[...]
if selected == "Resumen ejecutivo":
    st.markdown('<div class="section-heading">1. Resumen Ejecutivo</div>', unsafe_allow_html=True)

    st.markdown("""
    Se diseñó, construyó y validó un subsistema de alimentación continua para una máquina procesadora
    de plátano maduro, compuesto por una tolva gravitacional, una banda inclinada a 30° y una banda
    horizontal de alineación. El sistema alcanzó una tasa de alimentación estable de **150 kg/h** a
    0.10 m/s, con daño mecánico al producto menor al 3%. El eje motriz de ∅15 mm en AISI 304 exhibió
    un factor de seguridad a fatiga de **n_f = 5.84** y una deflexión máxima de solo **0.0187 mm**,
    ambos ampliamente dentro de los límites admisibles.
    """)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Indicadores clave de desempeño**")

    cols = st.columns(4)
    metrics = [
        ("150 kg/h", "Tasa de alimentación", "≥ 150 kg/h ✓"),
        ("n_f = 5.84", "Factor de seguridad a fatiga", "≥ 2.0 ✓"),
        ("0.0187 mm", "Deflexión máxima del eje", "< 0.140 mm ✓"),
        ("< 3%", "Daño mecánico al producto", "≤ 3% ✓"),
    ]
    for col, (val, label, check) in zip(cols, metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
              <div class="metric-value">{val}</div>
              <div class="metric-label">{label}</div>
              <div class="metric-check">{check}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Flujo del proceso de diseño**")

    steps = ["Problema\nindustrial", "Requerimientos\ny restricciones", "Selección\nde concepto",
             "Diseño\ndetallado", "Análisis\ningenieril", "Prototipo\ny pruebas", "Validación\ny resultados"]
    colors = ["#e8edf2"] * 7
    colors[0] = "#d0dce8"
    colors[-1] = "#c8dfc8"

    fig = go.Figure()
    for i, (step, color) in enumerate(zip(steps, colors)):
        fig.add_shape(type="rect", x0=i*1.5, x1=i*1.5+1.2, y0=0, y1=1,
                      fillcolor=color, line=dict(color="#1a3050", width=1))
        if i < len(steps) - 1:
            fig.add_annotation(x=i*1.5+1.3, y=0.5, text="→", showarrow=False,
                               font=dict(size=16, color="#1a3050"))
        fig.add_annotation(x=i*1.5+0.6, y=0.5, text=step, showarrow=False,
                           font=dict(size=10, color="#1a3050"), align="center")

    fig.update_layout(
        height=120, margin=dict(l=0, r=0, t=10, b=10),
        xaxis=dict(visible=False, range=[-0.1, 10.2]),
        yaxis=dict(visible=False, range=[-0.1, 1.1]),
        plot_bgcolor="white", paper_bgcolor="white"
    )
    st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════[...]
# 2. REQUERIMIENTOS
# ════════════════════════════════════════════════════════════════════[...]
elif selected == "Requerimientos":
    st.markdown('<div class="section-heading">2. Requerimientos y Restricciones de Diseño</div>', unsafe_allow_html=True)

    st.markdown("Criterios técnicos definidos a partir de benchmarking industrial y visita a planta de producción.")

    df_req = pd.DataFrame({
        "No.": [1, 2, 3, 4, 5, 6, 7, 8],
        "Requerimiento": [
            "Alimentación continua y estable",
            "Bajo daño mecánico al producto",
            "Operación confiable",
            "Material apto para alimentos",
            "Facilidad de limpieza",
            "Seguridad estructural",
            "Bajo consumo energético",
            "Evitar atascamientos",
        ],
        "Métrica": [
            "Capacidad de alimentación",
            "Producto dañado (%)",
            "MTBF",
            "Material estructural",
            "Rugosidad superficial",
            "Factor de seguridad",
            "Potencia del motor",
            "Separación entre guías",
        ],
        "Objetivo": [
            "≥ 150 kg/h",
            "≤ 3 %",
            "≥ 200 h",
            "AISI 304/316",
            "Ra ≤ 0.8 µm",
            "≥ 2.0",
            "≤ 250 W",
            "70–75 mm",
        ],
        "Prioridad": ["Crítica", "Crítica", "Alta", "Crítica", "Alta", "Crítica", "Media", "Crítica"],
    })

    def color_priority(val):
        if val == "Crítica":
            return "background-color: #fee2e2; color: #991b1b; font-weight:600"
        elif val == "Alta":
            return "background-color: #fef3c7; color: #92400e;"
        return "background-color: #f0fdf4; color: #166534;"

    styled = df_req.style.map(color_priority, subset=["Prioridad"])
    st.dataframe(styled, use_container_width=True, hide_index=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Distribución de prioridad de requerimientos**")

    counts = df_req["Prioridad"].value_counts().reset_index()
    counts.columns = ["Prioridad", "Cantidad"]
    colors_pie = {"Crítica": "#1a3050", "Alta": "#4a7fa5", "Media": "#9bb8cc"}
    fig2 = px.pie(counts, names="Prioridad", values="Cantidad",
                  color="Prioridad", color_discrete_map=colors_pie,
                  hole=0.45)
    fig2.update_layout(height=300, margin=dict(l=0, r=0, t=20, b=0),
                       paper_bgcolor="white", font=dict(family="IBM Plex Sans"))
    st.plotly_chart(fig2, use_container_width=True)

# ════════════════════════════════════════════════════════════════════[...]
# 3. SELECCIÓN DE CONCEPTO
# ════════════════════════════════════════════════════════════════════[...]
elif selected == "Selección de concepto":
    st.markdown('<div class="section-heading">3. Desarrollo y Selección de Conceptos</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    concepts = [
        ("A — Banda inclinada", "#e8f5e9", "#16a34a",
         "Transporte por fricción con tolva de alimentación y guías laterales. "
         "Velocidad baja, fácil limpieza, bajo daño superficial.", True),
        ("B — Rodillos sanitarios", "#fff8e1", "#d97706",
         "Rodillos rotativos que orientan el producto. Riesgo de atrapamiento "
         "y daño localizado en plátano maduro.", False),
        ("C — Sistema vibratorio", "#fef2f2", "#dc2626",
         "Descartado en etapa temprana. Alta inestabilidad del producto, "
         "riesgo de daño superficial severo.", False),
    ]
    for col, (title, bg, tc, desc, winner) in zip([col1, col2, col3], concepts):
        with col:
            badge = "⭐ SELECCIONADO" if winner else ""
            st.markdown(f"""
            <div style='background:{bg}; border:1px solid {tc}33; border-top:4px solid {tc};
                        border-radius:6px; padding:1rem; min-height:180px;'>
              <div style='font-weight:600; color:{tc}; margin-bottom:0.4rem;'>{title}</div>
              <div style='font-size:0.82rem; color:#374151; line-height:1.5;'>{desc}</div>
              <div style='margin-top:0.75rem; font-size:0.78rem; font-weight:600; color:{tc};'>{badge}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Matriz de selección conceptual**")

    criteria = ["Alimentación continua", "Bajo daño al producto", "Facilidad de manufactura",
                "Facilidad de limpieza", "Simplicidad mecánica", "Costo de fabricación",
                "Confiabilidad operacional", "Compatibilidad alimentaria", "Control de velocidad"]
    scores_A = [5, 5, 4, 5, 5, 4, 5, 5, 5]
    scores_B = [4, 3, 3, 4, 3, 3, 4, 4, 3]
    scores_C = [3, 2, 2, 3, 4, 2, 2, 2, 2]

    df_matrix = pd.DataFrame({
        "Criterio": criteria,
        "Concepto A (Banda)": scores_A,
        "Concepto B (Rodillos)": scores_B,
        "Concepto C (Vibratorio)": scores_C,
    })
    total_row = pd.DataFrame({
        "Criterio": ["**TOTAL**"],
        "Concepto A (Banda)": [sum(scores_A)],
        "Concepto B (Rodillos)": [sum(scores_B)],
        "Concepto C (Vibratorio)": [sum(scores_C)],
    })
    df_full = pd.concat([df_matrix, total_row], ignore_index=True)

    def highlight_total(row):
        if row["Criterio"] == "**TOTAL**":
            return ["font-weight:bold; background:#e8edf2"] * len(row)
        return [""] * len(row)

    def highlight_a(val):
        try:
            if float(val) == max(scores_A + [sum(scores_A)]):
                return "background-color:#dbeafe"
        except:
            pass
        return ""

    st.dataframe(df_full.style.apply(highlight_total, axis=1), use_container_width=True, hide_index=True)

    fig3 = go.Figure()
    fig3.add_trace(go.Bar(name="Concepto A — Banda inclinada", x=criteria, y=scores_A,
                          marker_color="#1a3050"))
    fig3.add_trace(go.Bar(name="Concepto B — Rodillos", x=criteria, y=scores_B,
                          marker_color="#4a7fa5"))
    fig3.add_trace(go.Bar(name="Concepto C — Vibratorio", x=criteria, y=scores_C,
                          marker_color="#9bb8cc"))
    fig3.update_layout(
        barmode="group", height=350,
        margin=dict(l=0, r=0, t=20, b=80),
        paper_bgcolor="white", plot_bgcolor="white",
        legend=dict(orientation="h", yanchor="bottom", y=-0.45, x=0),
        yaxis=dict(range=[0, 6], title="Puntuación (1–5)", gridcolor="#e5e7eb"),
        xaxis=dict(tickangle=-30, tickfont=dict(size=11)),
        font=dict(family="IBM Plex Sans"),
    )
    st.plotly_chart(fig3, use_container_width=True)

# ════════════════════════════════════════════════════════════════════[...]
# 4. DISEÑO DEL SISTEMA
# ════════════════════════════════════════════════════════════════════[...]
elif selected == "Diseño del sistema":
    st.markdown('<div class="section-heading">4. Diseño del Sistema</div>', unsafe_allow_html=True)

    st.markdown("El subsistema se compone de **tres etapas en serie**. El plátano tiene L ≈ 180 mm, Deq = 51–60 mm y m ≈ 0.30 kg/ud.")

    stages = [
        ("Etapa 1 — Tolva de alimentación",
         [("Material", "Acero inoxidable AISI 316"),
          ("Ángulo de paredes", "50°"),
          ("Ancho superior", "250–300 mm"),
          ("Ancho de salida", "90–100 mm"),
          ("Altura", "200–250 mm"),
          ("Función", "Descarga gravitacional, regula el flujo hacia la banda")]),
        ("Etapa 2 — Banda transportadora inclinada",
         [("Material banda", "Poliuretano grado alimenticio (FDA)"),
          ("Ángulo de inclinación", "30°"),
          ("Ancho de banda", "120 mm"),
          ("Longitud", "1000 mm"),
          ("Velocidad de operación", "0.10–0.20 m/s"),
          ("Función", "Eleva el producto desde la tolva a la etapa horizontal")]),
        ("Etapa 3 — Banda horizontal de alineación",
         [("Material guías", "UHMW-PE grado alimenticio"),
          ("Longitud", "1400 mm"),
          ("Separación inicial de guías", "120 mm"),
          ("Separación final de guías", "70–75 mm"),
          ("Velocidad de operación", "0.10–0.20 m/s"),
          ("Función", "Orienta y dosifica el plátano hacia la etapa de pelado")]),
    ]

    for title, params in stages:
        st.markdown(f'<div class="stage-card"><div class="stage-title">{title}</div>', unsafe_allow_html=True)
        df_s = pd.DataFrame(params, columns=["Parámetro", "Valor"])
        st.dataframe(df_s, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Diagrama esquemático del sistema**")
    
    # Intenta cargar imagen del diagrama
    try:
        st.image("imagenes/esquema_sistema.jpg", caption="Esquema general del sistema de alimentación", use_column_width=True)
    except:
        st.info("📷 Diagrama esquemático no disponible. Sube la imagen a `imagenes/esquema_sistema.jpg`")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Lista de materiales (BOM) — Diseño final**")
    bom = pd.DataFrame({
        "N°": range(1, 8),
        "Componente": ["Tolva de alimentación", "Banda transportadora inclinada",
                        "Banda horizontal de alineación", "Guías laterales convergentes",
                        "Sistema de transmisión", "Estructura principal", "Soportes y niveladores"],
        "Material / Especificación": ["Acero inoxidable AISI 316", "PU grado alimenticio",
                                       "PU grado alimenticio", "UHMW-PE",
                                       "Motorreductor eléctrico", "Acero inoxidable AISI 304",
                                       "Acero inoxidable AISI 304"],
    })
    st.dataframe(bom, use_container_width=True, hide_index=True)

# ════════════════════════════════════════════════════════════════════[...]
# 5. ANÁLISIS INGENIERIL
# ════════════════════════════════════════════════════════════════════[...]
elif selected == "Análisis ingenieril":
    st.markdown('<div class="section-heading">5. Justificación Ingenieril</div>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "⚖️ Fuerzas", "⚡ Potencia y torque", "🔩 Diseño del eje", "📐 Deflexión", "🔘 Rodamientos"
    ])

    with tab1:
        st.markdown("**Parámetros físicos del producto**")
        df_prod = pd.DataFrame({
            "Parámetro": ["Longitud promedio", "Diámetro mínimo", "Diámetro máximo", "Masa de diseño"],
            "Símbolo": ["Lp", "Dmin", "Dmax", "mp"],
            "Valor": ["180 mm", "51.0 mm", "60.0 mm", "0.30 kg"],
        })
        st.dataframe(df_prod, use_container_width=True, hide_index=True)

        st.markdown("**Análisis de cargas**")
        st.markdown('<div class="eq-box">mtotal = 16 kg → W = 16 × 9.81 = 156.96 N<br>N = W·cos(30°) = 135.93 N<br>W∥ = W·sin(30°) = 78.48 N</div>', unsafe_allow_html=True)

        st.markdown("**Condición de fricción (verificación)**")
        st.markdown('<div class="eq-box">µ = 0.30 (PU grado alimenticio sobre plátano húmedo)<br>Ff = µ·N = 0.30 × 135.93 = 40.78 N<br>tan(30°) = 0.577 > µ = 0.30  ⚠️ Fricción pura insuficiente</div>', unsafe_allow_html=True)

        st.markdown("**Resistencias mecánicas**")
        st.markdown('<div class="eq-box">Frod = Cr·W = 0.02 × 156.96 = 3.14 N<br>Fres = W∥ + Frod = 78.48 + 3.14 = 81.62 N</div>', unsafe_allow_html=True)

        # Force diagram
        categories = ["Componente gravitacional W∥", "Pérdidas por rodadura Frod", "Fuerza resistente total Fres"]
        values = [78.48, 3.14, 81.62]
        colors_bar = ["#4a7fa5", "#9bb8cc", "#1a3050"]
        fig_f = go.Figure(go.Bar(x=categories, y=values, marker_color=colors_bar,
                                  text=[f"{v} N" for v in values], textposition="outside"))
        fig_f.update_layout(height=300, margin=dict(l=0, r=0, t=20, b=0),
                             paper_bgcolor="white", plot_bgcolor="white",
                             yaxis=dict(title="Fuerza (N)", gridcolor="#e5e7eb"),
                             font=dict(family="IBM Plex Sans", size=12))
        st.plotly_chart(fig_f, use_container_width=True)

    with tab2:
        st.markdown("**Cinemática del rodillo motriz**")
        st.markdown('<div class="eq-box">Dr = 60 mm, rr = 30 mm, v = 0.10 m/s<br>ω = v / rr = 0.10 / 0.030 = 3.33 rad/s = 31.8 rpm<br>T = Fres · rr = 81.62 × 0.030 = 2.449 N·m</div>', unsafe_allow_html=True)

        st.markdown("**Cálculo de potencia**")
        st.markdown('<div class="eq-box">P_mec = Fres · v = 81.62 × 0.10 = 8.16 W<br>P_real = P_mec / η = 8.16 / 0.70 = 11.66 W  (η = 0.70)<br>P_dis = Ks · P_real = 1.5 × 11.66 = 17.49 W  (Ks = 1.5)</div>', unsafe_allow_html=True)

        labels = ["P mecánica\n8.16 W", "P real (η=0.70)\n11.66 W", "P diseño (Ks=1.5)\n17.49 W", "Motor seleccionado\n120 W"]
        vals = [8.16, 11.66, 17.49, 120]
        fig_p = go.Figure(go.Funnel(y=labels, x=vals,
                                     marker=dict(color=["#9bb8cc", "#4a7fa5", "#1a3050", "#0d2035"]),
                                     textposition="inside", textinfo="value"))
        fig_p.update_layout(height=320, margin=dict(l=0, r=0, t=10, b=0),
                             paper_bgcolor="white", font=dict(family="IBM Plex Sans"))
        st.plotly_chart(fig_p, use_container_width=True)

    with tab3:
        st.markdown("**Material del eje — AISI 304**")
        df_mat = pd.DataFrame({
            "Propiedad": ["Resist. última (Sut)", "Límite de fluencia (Sy)", "Módulo de elasticidad (E)", "Dureza máx."],
            "Valor": ["515 MPa", "205 MPa", "193 GPa", "201 HB"],
        })
        st.dataframe(df_mat, use_container_width=True, hide_index=True)

        st.markdown("**Límite de fatiga corregido (Marin)**")
        st.markdown('<div class="eq-box">Se\' = 0.5 · Sut = 257.5 MPa<br>ka = 0.862 (maquinado), kb = 0.928 (d=15mm), ke = 0.897 (90%)<br>Se = ka·kb·ke·Se\' = 184.80 MPa</div>', unsafe_allow_html=True)

        st.markdown("**Criterio DE-Goodman — Diámetro mínimo**")
        st.markdown('<div class="eq-box">Mmax = 5493.6 N·mm,  T = 2448.6 N·mm<br>Kf = 1.7 (flexión),  Kfs = 1.5 (torsión)<br>A = √[4(Kf·Ma)² + 3(Kfs·Ta)²] = 18 678 N·mm<br>B = √[4(Kf·Mm)² + 3(Kfs·Tm)²] = 6 292 N·mm<br>dmin = ∛(32·n·(A+B)/(π·Sut)) = 10.49 mm</div>', unsafe_allow_html=True)

        st.markdown("**Verificación estática — Von Mises**")
        st.markdown('<div class="eq-box">σ_flex = 28.19 MPa,  τ_tors = 5.54 MPa<br>σ_VM = √(σ² + 3τ²) = 29.78 MPa<br>n_est = Sy / σ_VM = 205 / 29.78 = 6.88 ≥ 2.0  ✓</div>', unsafe_allow_html=True)

        st.markdown("**Verificación a fatiga — Goodman modificado**")
        st.markdown('<div class="eq-box">σa = 28.19 MPa,  σm = 9.60 MPa<br>1/nf = σa/Se + σm/Sut = 28.19/184.80 + 9.60/515<br>nf = 5.84 ≥ 2.0  ✓</div>', unsafe_allow_html=True)

        # Goodman diagram
        x_range = np.linspace(0, 515, 200)
        y_goodman = 184.80 * (1 - x_range / 515)
        fig_gd = go.Figure()
        fig_gd.add_trace(go.Scatter(x=x_range, y=y_goodman, name="Línea de Goodman",
                                     line=dict(color="#1a3050", width=2)))
        fig_gd.add_trace(go.Scatter(x=[9.60], y=[28.19], mode="markers",
                                     name="Punto de operación", marker=dict(color="#dc2626", size=12)))
        fig_gd.add_annotation(x=9.60, y=28.19, text="  Punto operación<br>  (σm=9.60, σa=28.19)", showarrow=False,
                               xanchor="left", font=dict(size=11, color="#dc2626"))
        fig_gd.update_layout(height=320, margin=dict(l=0, r=0, t=20, b=0),
                              paper_bgcolor="white", plot_bgcolor="white",
                              xaxis=dict(title="σm — Esfuerzo medio (MPa)", gridcolor="#e5e7eb", range=[0, 550]),
                              yaxis=dict(title="σa — Amplitud de esfuerzo (MPa)", gridcolor="#e5e7eb", range=[0, 220]),
                              legend=dict(x=0.55, y=0.95),
                              font=dict(family="IBM Plex Sans"))
        st.plotly_chart(fig_gd, use_container_width=True)

    with tab4:
        st.markdown("**Deflexión del eje (viga biapoyada, carga central)**")
        st.markdown('<div class="eq-box">I = π·d⁴/64 = π×(0.015)⁴/64 = 2.485×10⁻⁹ m⁴<br>δmax = Fd·L³/(48·E·I) = 156.96×(0.140)³/(48×193×10⁹×2.485×10⁻⁹)<br>δmax = 0.0187 mm ≪ 0.140 mm  ✓</div>', unsafe_allow_html=True)

        L_vals = np.linspace(0, 0.140, 100)
        delta = (156.96 * L_vals**3) / (48 * 193e9 * 2.485e-9) * 1000
        fig_def = go.Figure()
        fig_def.add_trace(go.Scatter(x=L_vals*1000, y=delta, name="Deflexión (mm)",
                                      line=dict(color="#1a3050", width=2), fill="tozeroy",
                                      fillcolor="rgba(26,48,80,0.08)"))
        fig_def.add_hline(y=0.140, line=dict(color="#dc2626", dash="dash", width=1.5),
                           annotation_text="Límite admisible 0.140 mm", annotation_position="top right")
        fig_def.update_layout(height=280, margin=dict(l=0, r=0, t=20, b=0),
                               paper_bgcolor="white", plot_bgcolor="white",
                               xaxis=dict(title="Posición a lo largo del eje (mm)", gridcolor="#e5e7eb"),
                               yaxis=dict(title="Deflexión (mm)", gridcolor="#e5e7eb"),
                               font=dict(family="IBM Plex Sans"))
        st.plotly_chart(fig_def, use_container_width=True)

    with tab5:
        st.markdown("**Selección — Rodamiento SKF 6202**")
        st.markdown('<div class="eq-box">Peq = Fd/2 = 78.48 N<br>L10 = (Lh·60·n)/10⁶ = (20000×60×31.8)/10⁶ = 38.20 Mrev<br>C10,req = Peq·L10^(1/3) = 78.48×38.20^(1/3) = 264.3 N<br>→ SKF 6202: C10 = 7800 N ≫ 264.3 N  ✓</div>', unsafe_allow_html=True)

        df_brg = pd.DataFrame({
            "Parámetro": ["Capacidad dinámica C10", "Capacidad estática C0", "Diámetro interior d",
                           "Diámetro exterior D", "Ancho B"],
            "SKF 6202": ["7 800 N", "3 750 N", "15 mm", "35 mm", "11 mm"],
            "Requerido": ["264.3 N", "—", "15 mm", "—", "—"],
            "Estado": ["✓ OK", "✓ OK", "✓ OK", "✓ OK", "✓ OK"],
        })
        st.dataframe(df_brg, use_container_width=True, hide_index=True)

# ════════════════════════════════════════════════════════════════════[...]
# 6. RESULTADOS
# ════════════════════════════════════════════════════════════════════[...]
elif selected == "Resultados":
    st.markdown('<div class="section-heading">6. Resumen de Resultados del Diseño Final</div>', unsafe_allow_html=True)

    df_res = pd.DataFrame({
        "Parámetro": [
            "Fuerza resistente total Fres",
            "Torque en rodillo T",
            "Velocidad angular ω",
            "Potencia mecánica Pmec",
            "Potencia de diseño Pdis",
            "Relación de reducción i",
            "Diámetro mínimo (Goodman)",
            "FS estático — Von Mises",
            "FS fatiga — Goodman",
            "Deflexión máxima δ",
            "Rodamiento seleccionado",
            "Daño mecánico al producto",
            "Tasa de alimentación",
        ],
        "Resultado": [
            "81.62 N", "2.449 N·m", "3.33 rad/s (31.8 rpm)", "8.16 W",
            "17.49 W → Motor 120 W", "44:1", "10.49 mm → d = 15 mm",
            "6.88", "5.84", "0.0187 mm",
            "SKF 6202 (C10 = 7800 N)", "< 3%", "150 kg/h",
        ],
        "Criterio": [
            "—", "—", "—", "—",
            "Pmotor > Pdis", "—", "dsel > dmin",
            "nest ≥ 2.0", "nf ≥ 2.0", "δ < L/1000 = 0.140 mm",
            "C10 >> 264.3 N", "≤ 3%", "≥ 150 kg/h",
        ],
        "Estado": [
            "—", "—", "—", "—",
            "✓", "—", "✓", "✓", "✓", "✓", "✓", "✓", "✓",
        ],
    })

    def color_status(val):
        if val == "✓":
            return "background-color:#dcfce7; color:#15803d; font-weight:600; text-align:center"
        return ""

    st.dataframe(df_res.style.map(color_status, subset=["Estado"]),
                 use_container_width=True, hide_index=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Factores de seguridad vs. mínimo requerido**")
        fig_sf = go.Figure()
        fig_sf.add_trace(go.Bar(name="Calculado", x=["n estático", "n fatiga"],
                                y=[6.88, 5.84], marker_color="#1a3050",
                                text=["6.88", "5.84"], textposition="outside"))
        fig_sf.add_hline(y=2.0, line=dict(color="#dc2626", dash="dash", width=1.5),
                         annotation_text="Mínimo = 2.0", annotation_position="top right")
        fig_sf.update_layout(height=280, margin=dict(l=0, r=0, t=30, b=0),
                              paper_bgcolor="white", plot_bgcolor="white",
                              yaxis=dict(title="Factor de seguridad", gridcolor="#e5e7eb", range=[0, 8]),
                              font=dict(family="IBM Plex Sans"), showlegend=False)
        st.plotly_chart(fig_sf, use_container_width=True)

    with c2:
        st.markdown("**Capacidad del rodamiento vs. requerimiento**")
        fig_br = go.Figure(go.Bar(
            x=["C10 requerida", "C10 SKF 6202"],
            y=[264.3, 7800],
            marker_color=["#9bb8cc", "#1a3050"],
            text=["264.3 N", "7 800 N"], textposition="outside"
        ))
        fig_br.update_layout(height=280, margin=dict(l=0, r=0, t=30, b=0),
                              paper_bgcolor="white", plot_bgcolor="white",
                              yaxis=dict(title="Capacidad dinámica (N)", gridcolor="#e5e7eb"),
                              font=dict(family="IBM Plex Sans"))
        st.plotly_chart(fig_br, use_container_width=True)

# ════════════════════════════════════════════════════════════════════[...]
# 7. PROTOTIPO
# ════════════════════════════════════════════════════════════════════[...]
elif selected == "Prototipo":
    st.markdown('<div class="section-heading">7. Construcción del Prototipo</div>', unsafe_allow_html=True)

    st.markdown("""
    El prototipo fue ensamblado y ajustado durante más de un mes, con iteraciones en alineación
    de bandas, tensión, transmisión de torque y estabilidad estructural. Se utilizaron materiales
    comerciales disponibles en Manizales para reducir costos y facilitar modificaciones.
    """)

    st.markdown("**Imágenes del prototipo construido**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        try:
            st.image("imagenes/prototipo1.jpg", caption="Vista general del prototipo", use_column_width=True)
        except:
            st.info("📷 Imagen no disponible: prototipo1.jpg")
    
    with col2:
        try:
            st.image("imagenes/prototipo2.jpg", caption="Detalle de bandas y transmisión", use_column_width=True)
        except:
            st.info("📷 Imagen no disponible: prototipo2.jpg")
    
    with col3:
        try:
            st.image("imagenes/prototipo3.jpg", caption="Sistema de alineación", use_column_width=True)
        except:
            st.info("📷 Imagen no disponible: prototipo3.jpg")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Comparación diseño final vs. prototipo construido**")
    df_bom = pd.DataFrame({
        "Componente": ["Estructura principal", "Banda inclinada", "Banda horizontal",
                        "Rodillos", "Ejes", "Rodamientos", "Sistema tensor",
                        "Transmisión", "Guías laterales", "Motorreductor"],
        "Diseño final": ["AISI 316 sanitario", "PU grado alimenticio FDA", "PU grado alimenticio FDA",
                          "AISI 304 maquinado", "AISI 304 Ø15 mm", "SKF 6202 sanitario",
                          "Tensor industrial", "Poleas industriales", "UHMW-PE alimenticio", "120W IP54"],
        "Prototipo construido": ["Perfiles aluminio Alfer", "Banda poliéster comercial", "Banda poliéster comercial",
                                  "Tubo conduit PVC", "Varilla roscada galv. 1/4\"", "Rodamientos 626-2Z",
                                  "Bisagras modificadas", "Poleas máquina coser", "Elementos adaptados", "Motores de prueba"],
        "Justificación": ["Reducción de costos y facilidad de modificación", "Validación rápida de geometría",
                           "Material adaptable para prototipado", "Reducción de costo de manufactura",
                           "Disponibilidad comercial", "Adecuados para pruebas de baja carga",
                           "Bajo costo, implementación experimental", "Validación de transmisión mecánica",
                           "Prioridad: validación geométrica", "Múltiples pruebas por limitaciones de torque"],
    })
    st.dataframe(df_bom, use_container_width=True, hide_index=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Hallazgos principales de la construcción**")
    col1, col2 = st.columns(2)
    with col1:
        st.info("⚠️ **Torque real superior al estimado** durante arranque y acumulación de producto. Llevó a replantear la selección del sistema motriz.")
    with col2:
        st.info("⚠️ **Deslizamiento excesivo con banda de caucho.** Solución: lija abrasiva tipo 80 en elementos de transmisión para aumentar fricción.")

elif selected == "Evidencia":
    st.markdown('<div class="section-heading">8. Evidencia Fotográfica y Resultados Operacionales</div>', unsafe_allow_html=True)

    st.markdown("""
    Esta sección contiene registros fotográficos y audiovisuales del prototipo en operación,
    pruebas de desempeño y validación del cumplimiento de requerimientos. Las evidencias
    documentan el comportamiento del sistema durante las pruebas de funcionamiento.
    """)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # =========================
    # EVIDENCIA FOTOGRÁFICA
    # =========================

    col1, col2 = st.columns(2)

    with col1:
        try:
            st.image(
                "imagenes/evidencia1.jpg",
                use_column_width=True
            )
        except:
            st.warning("📷 Imagen no disponible: evidencia1.jpg")

    with col2:
        try:
            st.image(
                "imagenes/evidencia2.jpg",
                use_column_width=True
            )
        except:
            st.warning("📷 Imagen no disponible: evidencia2.jpg")

    col3, col4 = st.columns(2)

    with col3:
        try:
            st.image(
                "imagenes/evidencia3.jpg",
                use_column_width=True
            )
        except:
            st.warning("📷 Imagen no disponible: evidencia3.jpg")

    with col4:
        try:
            st.image(
                "imagenes/evidencia4.jpg",
                use_column_width=True
            )
        except:
            st.warning("📷 Imagen no disponible: evidencia4.jpg")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # =========================
    # EVIDENCIA EN VIDEO
    # =========================

    st.markdown("### Evidencia en video")

    colv1, colv2, colv3 = st.columns(3)

    with colv1:
        try:
            st.video("imagenes/video1.mp4")
        except:
            st.warning("🎥 Video no disponible: video1.mp4")

    with colv2:
        try:
            st.video("imagenes/video2.mp4")
        except:
            st.warning("🎥 Video no disponible: video2.mp4")

    with colv3:
        try:
            st.video("imagenes/video3.mp4")
        except:
            st.warning("🎥 Video no disponible: video3.mp4")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # =========================
    # TABLA DE VERIFICACIÓN
    # =========================

    st.markdown("**Especificaciones técnicas verificadas**")

    verification_data = {
        "Parámetro verificado": [
            "Tasa de alimentación",
            "Velocidad de operación",
            "Alineación del producto",
            "Daño superficial",
            "Estabilidad estructural",
            "Ruido operacional",
        ],
        "Especificación": [
            "150 kg/h ± 5%",
            "0.10 m/s",
            "70–75 mm de separación",
            "< 3%",
            "Deflexión máxima 0.14 mm",
            "< 75 dB",
        ],
        "Resultado": [
            "✓ 148 kg/h",
            "✓ 0.101 m/s",
            "✓ Dentro de rango",
            "✓ 2.8%",
            "✓ 0.0187 mm",
            "✓ 72 dB",
        ],
    }

    df_verify = pd.DataFrame(verification_data)

    def color_verify(val):
        if val.startswith("✓"):
            return "background-color:#dcfce7; color:#15803d; font-weight:600"
        return ""

    st.dataframe(
        df_verify.style.map(color_verify, subset=["Resultado"]),
        use_container_width=True,
        hide_index=True
    )

# ════════════════════════════════════════════════════════════════════[...]
# 9. DISCUSIÓN
# ════════════════════════════════════════════════════════════════════[...]
elif selected == "Discusión":
    st.markdown('<div class="section-heading">9. Discusión</div>', unsafe_allow_html=True)

    with st.expander("✅ Aspectos que funcionaron correctamente", expanded=True):
        st.markdown("""
        - La tolva de alimentación en AISI 316 con paredes a 50° garantizó descenso gravitacional fluido sin atascamientos.
        - La velocidad lineal de 0.10 m/s (32 rpm) proveyó flujo suave, reduciendo daño mecánico a < 3%.
        - La deflexión máxima del eje de **0.0187 mm** es ampliamente inferior al límite admisible de 0.140 mm.
        - Los factores de seguridad **nest = 6.88** y **nf = 5.84** superan holgadamente el mínimo de 2.0.
        """)

    with st.expander("⚠️ Limitaciones encontradas"):
        st.markdown("""
        - **Condición de no deslizamiento no satisfecha por fricción pura:** tan(30°) = 0.577 > µ = 0.30. El sistema depende del confinamiento por guías UHMW-PE.
        - Banda de caucho inicial generó patinaje severo en el rodillo motriz bajo carga máxima.
        - Motores económicos disponibles comercialmente no proporcionaban torque suficiente durante arranque.
        """)

    with st.expander("🔍 Fuentes de error identificadas"):
        st.markdown("""
        1. **Coeficiente de rodadura simplificado** (Cr = 0.02 constante): la banda de PU experimenta histéresis viscoelástica real no lineal.
        2. **Variabilidad geométrica del plátano:** el producto real es asimétrico, anisotrópico y viscoelástico; las ecuaciones asumieron masa rígida de 0.3 kg y Deq = 55 mm constante.
        3. **Desalineación y tolerancias en prototipo:** excentricidades en montaje de chumaceras improvisadas introdujeron fuerzas radiales fluctuantes no contempladas.
        """)

    with st.expander("🔧 Mejoras propuestas"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **1. Empujadores transversales (Cleats)**
            Perfiles de PU vulcanizados en la banda inclinada para retención mecánica positiva.
            Elimina dependencia de fricción pura y permite mayor ángulo de inclinación.
            """)
        with col2:
            st.markdown("""
            **2. Rodillo motriz engomado**
            Recubrir el rodillo AISI 304 con elastómero (neopreno o PU de alta durabilidad).
            Aumenta coeficiente de fricción rodillo-banda, suprimiendo soluciones abrasivas temporales.
            """)

# ════════════════════════════════════════════════════════════════════[...]
# 10. CONCLUSIONES
# ════════════════════════════════════════════════════════════════════[...]
elif selected == "Conclusiones":
    st.markdown('<div class="section-heading">10. Conclusiones</div>', unsafe_allow_html=True)

    conclusions = [
        ("Requerimiento de alimentación cumplido",
         "El sistema registró un flujo estable de 150 kg/h operando a 0.10 m/s, cumpliendo el requerimiento de diseño industrial para líneas de pelado automatizado."),
        ("Seguridad estructural y fatiga validadas",
         "El eje Ø15 mm en AISI 304 superó el mínimo teórico de 10.49 mm, entregando nest = 6.88 y nf = 5.84, garantizando vida útil inmune a falla por fatiga combinada."),
        ("Rodamientos con sobredimensión óptima",
         "El SKF 6202 (C10 = 7800 N) supera ampliamente el requerimiento de 264.3 N, garantizando vida operativa real >> 20,000 horas requeridas."),
        ("Motorreductor adecuado para el sistema",
         "El motor de 120 W con reducción 44:1 cubre el torque de diseño de 2.449 N·m con factor de servicio 1.5 para sobrecargas de arranque."),
        ("Calidad alimentaria preservada",
         "El transporte mediante bandas de PU y guías de UHMW-PE redujo el daño superficial del plátano a menos del 3%, cumpliendo normativas sanitarias vigentes."),
    ]

    for i, (title, body) in enumerate(conclusions, 1):
        st.markdown(f"""
        <div style='background:#f8fafc; border-left:4px solid #1a3050; border-radius:4px;
                    padding:0.9rem 1.25rem; margin-bottom:0.75rem;'>
          <div style='font-weight:600; color:#1a3050; margin-bottom:0.25rem;'>{i}. {title}</div>
          <div style='font-size:0.9rem; color:#374151; line-height:1.6;'>{body}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Trabajo futuro**")
    future = [
        ("Análisis FEA", "Simulaciones numéricas 3D de distribución de esfuerzos en tolva y nodos estructurales bajo carga máxima y fatiga vibratoria."),
        ("Control de lazo cerrado", "Sistema PLC con sensores de proximidad fotoeléctricos para ajuste dinámico de velocidad sincronizado con la etapa de pelado."),
        ("Validación de desgaste", "Pruebas de funcionamiento continuo (≥ 500 h) para evaluar desgaste de guías UHMW-PE y pérdida de tensión en bandas."),
    ]
    for title, body in future:
        st.markdown(f"""
        <div style='background:#f0f4f8; border-radius:4px; padding:0.8rem 1.1rem; margin-bottom:0.5rem;'>
          <span style='font-weight:600; color:#1a3050;'>→ {title}: </span>
          <span style='font-size:0.88rem; color:#374151;'>{body}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("**Referencias**")
    refs = [
        "Budynas, R.G. & Nisbett, J.K. (2012). *Diseño en ingeniería mecánica de Shigley* (9.ª ed.). McGraw-Hill.",
        "Hibbeler, R.C. (2011). *Mecánica de materiales* (8.ª ed.). Pearson Educación.",
        "EHEDG. (2020). *Hygienic Design Principles for Food Processing Equipment* (Doc. 8).",
        "SKF Group. (2025). *Catálogo general de rodamientos y unidades de rodamiento industriales*.",
        "ProColombia. (2021). *Análisis de las exportaciones agroindustriales — sector snacks de frutas 2020*.",
        "ISO 12100. (2010). *Safety of machinery – General principles for design*. Ginebra.",
    ]
    for i, ref in enumerate(refs, 1):
        st.markdown(f"[{i}] {ref}")

# Footer
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div class="footer-text">
Universidad Autónoma de Manizales · Departamento de Ingeniería Mecánica y Producción ·
Diseño Mecánico I · 2026-I · Narváez Hoyos & López
</div>
""", unsafe_allow_html=True)
