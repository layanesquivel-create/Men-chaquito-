import streamlit as st

# Configuración de página con la identidad corporativa de El Chaquito
st.set_page_config(
    page_title="Menú - El Chaquito de Felipe",
    page_icon="🔥",
    layout="centered"
)

# Estilos CSS inyectados para forzar la paleta de colores oficial:
# Carbón Absoluto (#1C1917), Fuego Vivo (#C2410C), Crema Hueso (#FEFACC)
st.markdown("""
    <style>
    .stApp {
        background-color: #1C1917;
        color: #FEFACC;
    }
    h1, h2, h3 {
        color: #C2410C !important;
        font-family: 'Sans-Serif', sans-serif;
    }
    .stTabs [data-baseweb="tab"] {
        color: #FEFACC;
        font-size: 16px;
    }
    .stTabs [aria-selected="true"] {
        color: #C2410C !important;
        font-weight: bold;
        border-bottom-color: #C2410C !important;
    }
    .price-tag {
        color: #C2410C;
        font-weight: bold;
        font-size: 18px;
        float: right;
    }
    .item-box {
        border-bottom: 1px solid #78350F;
        padding-bottom: 12px;
        margin-bottom: 15px;
    }
    .footer-text {
        text-align: center;
        color: #78350F;
        font-size: 14px;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.title("🔥 EL CHAQUITO DE FELIPE")
st.subheader("Menú Oficial 2026")

# Sistema de navegación interactivo por Pestañas (Tabs)
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🥩 Parrillas", 
    "🍽️ Especialidades y Cortes", 
    "🍢 Platos y Piqueos", 
    "🥤 Bebidas y Refrescos",
    "🍷 Selección de Vinos"
])

with tab1:
    st.header("Parrillas Personalizadas")
    st.caption("*Todas las parrillas incluyen: Arroz con queso o graneado, papas fritas y ensalada.")
    
    parrillas = [
        {"nombre": "Parrilla Personal", "precio": "150 Bs.", "desc": "1 Chorizo, 150g de Vacío, 100g de Chuleta de Cerdo, 50g de Asado de Tira, 50g de Filete de Pollo, Ubre, Tripas."},
        {"nombre": "Parrilla Bi Personal", "precio": "190 Bs.", "desc": "2 Chorizos, 300g de Vacío, 150g de Chuleta de Cerdo, 100g de Asado de Tira, 100g de Filete de Pollo, Ubre, Tripas."},
        {"nombre": "Parrilla Tri Personal", "precio": "230 Bs.", "desc": "3 Chorizos, 500g de Vacío, 300g de Chuleta de Cerdo, 200g de Asado de Tira, 200g de Filete de Pollo, Ubre, Tripas."}
    ]
    for p in parrillas:
        st.markdown(f"<div class='item-box'><b>{p['nombre']}</b> <span class='price-tag'>{p['precio']}</span><br><small style='color:#b5b094;'>{p['desc']}</small></div>", unsafe_allow_html=True)

with tab2:
    st.header("Especialidades de la Casa")
    espe = [
        {"nombre": "Bife Chorizo", "precio": "90 Bs.", "desc": "150g de Bife Chorizo, arroz con queso o graneado, papas fritas, ensalada."},
        {"nombre": "BrochetaChaquito", "precio": "90 Bs.", "desc": "80g de Churrasco, tripitas, ubre, pollo, cebolla, morrón, arroz con queso o graneado, papas fritas, ensalada."},
        {"nombre": "Filete de Res", "precio": "100 Bs.", "desc": "150g de Filete de Cerdo, arroz con queso o graneado, papas fritas, ensalada."}
    ]
    for e in espe:
        st.markdown(f"<div class='item-box'><b>{e['nombre']}</b> <span class='price-tag'>{e['precio']}</span><br><small style='color:#b5b094;'>{e['desc']}</small></div>", unsafe_allow_html=True)

    st.header("Cortes Chaquito")
    cortes = [
        {"nombre": "Corte Chaquito Vacío", "precio": "60 Bs.", "desc": "230g de Vacío, arroz con queso o graneado, papas fritas, ensalada."},
        {"nombre": "Corte Chaquito Pollo", "precio": "60 Bs.", "desc": "200g de filete de pollo, arroz con queso o graneado, papas fritas, ensalada."},
        {"nombre": "Corte Chaquito Cerdo", "precio": "60 Bs.", "desc": "200g de Chuleta de cerdo, arroz con queso o graneado, papas fritas, ensalada."},
        {"nombre": "Corte Chaquito Medio Churrasco", "precio": "50 Bs.", "desc": "110g de Churrasco, arroz con queso o graneado, papas fritas, ensalada."}
    ]
    for c in cortes:
        st.markdown(f"<div class='item-box'><b>{c['nombre']}</b> <span class='price-tag'>{c['precio']}</span><br><small style='color:#b5b094;'>{c['desc']}</small></div>", unsafe_allow_html=True)

with tab3:
    st.header("Platos Tradicionales y Piqueos")
    platos = [
        {"nombre": "Chorizo al Plato", "precio": "60 Bs.", "desc": "3 Unidades de chorizo criollo + arroz con queso o graneado + papas fritas/yuca + ensalada."},
        {"nombre": "Pacumuto Entero", "precio": "60 Bs.", "desc": "100g de churrasco + chorizo + tripitas + ubre + arroz con queso o graneado + papas fritas + ensalada."},
        {"nombre": "Asado de Tira", "precio": "60 Bs.", "desc": "200g tira delgada + arroz con queso o graneado + papas fritas/yuca + ensalada."},
        {"nombre": "Antojito", "precio": "40 Bs.", "desc": "1 Chorizo picado + 1 vacío picado + pan a la parrilla + salsa chimichurri."},
        {"nombre": "Capricho", "precio": "60 Bs.", "desc": "1.5 chorizos picados + 2 vacíos picados + 1 pollo picado + papas fritas + pan a la parrilla + salsa chimichurri."},
        {"nombre": "Al límite", "precio": "80 Bs.", "desc": "2 chorizos picados + 3 vacíos picados + 2 pollos picados + papas fritas + pan a la parrilla + salsa chimichurri."}
    ]
    for pl in platos:
        st.markdown(f"<div class='item-box'><b>{pl['nombre']}</b> <span class='price-tag'>{pl['precio']}</span><br><small style='color:#b5b094;'>{pl['desc']}</small></div>", unsafe_allow_html=True)
        
    st.header("Express y Extras")
    st.markdown("<div class='item-box'><b>Choripan</b> <span class='price-tag'>15 Bs.</span><br><small style='color:#b5b094;'>Chorizo criollo + lechuga + tomate + papas fritas + pan + chimichurri.</small></div>", unsafe_allow_html=True)
    st.markdown("<div class='item-box'><b>Extras Acompañamientos</b> <span class='price-tag'>15 Bs.</span><br><small style='color:#b5b094;'>Papas fritas, Arroz con queso o graneado, Pollo, Chuleta, Chorizo.</small></div>", unsafe_allow_html=True)
    st.markdown("<div class='item-box'><b>Ensalada Extra</b> <span class='price-tag'>12 Bs.</span></div>", unsafe_allow_html=True)

with tab4:
    st.header("Refrescos y Bebidas")
    st.subheader("Jugos Naturales")
    st.write("• Vaso personal: 5 Bs.  \n• Jarra Mediana: 15 Bs.  \n• Jarra Grande: 20 Bs.")
    st.subheader("Gaseosas")
    st.write("• Personales 330 ml: 3 Bs.  \n• Botella de 500 ml: 10 Bs.  \n• Botella de 1L: 12 Bs.  \n• Botella de 2L: 20 Bs.")
    st.subheader("Cervezas Locales")
    st.write("• Paceña 620 ml: 24 Bs.  \n• Huari 620 ml: 25 Bs.")

with tab5:
    st.header("Nuestra Selección de Vinos")
    st.caption("Maridaje sugerido para potenciar los sabores de nuestras carnes.")
    st.markdown("<div class='item-box'><b>Vinos Clásicos (620ml)</b> <span class='price-tag'>55 Bs.</span><br><small style='color:#b5b094;'>Kohlberg Clásico, Campos de Solana Clásico, Stirpe (Vino tinto / Vino blanco / Oporto).</small></div>", unsafe_allow_html=True)

# Pie de página con Ficha Técnica Comercial Inmutable
st.markdown("---")
st.markdown(f"""
    <div class='footer-text'>
        <b>📍 Dirección:</b> Calle Panamá, casi esquina Plaza Uyuni (Miraflores), La Paz<br>
        <b>📱 Pedidos WhatsApp:</b> +591 68133991 | 🛵 <b>Delivery:</b> Pedidos Ya<br>
        <b>📸 Redes Sociales:</b> @Chaquito de Felipe<br>
        <p style='color: #C2410C; margin-top:15px; font-weight:bold;'>La mejor parrilla de la ciudad</p>
    </div>
""", unsafe_allow_html=True)
  
